#!/usr/bin/env python3
"""Bounded, read-only static inspection for one untrusted skill directory."""

import argparse
import hashlib
import json
import os
import re
import stat
import sys
import time
import unicodedata


SCHEMA = "skill-intake-review/v1"
MAX_ENTRIES = 500
MAX_DEPTH = 8
MAX_FILE_BYTES = 1024 * 1024
MAX_TOTAL_TEXT_BYTES = 8 * 1024 * 1024
MAX_SECONDS = 15
TEXT_SUFFIXES = {
    ".bat",
    ".cfg",
    ".cmd",
    ".go",
    ".html",
    ".ini",
    ".java",
    ".js",
    ".json",
    ".md",
    ".ps1",
    ".py",
    ".rs",
    ".sh",
    ".toml",
    ".ts",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}
TEXT_FILENAMES = {"copying", "license", "license.txt", "notice"}
SUSPICIOUS_FRONTMATTER = {
    "allowed-tools": "declared-permissions",
    "hooks": "frontmatter-hook",
    "model": "model-override",
    "disable-model-invocation": "invocation-policy",
    "permissions": "declared-permissions",
}
CODE_RULES = (
    ("process-execution-pattern", "high", re.compile(r"\b(subprocess|os\.system|child_process|powershell|cmd\.exe)\b", re.I)),
    ("dynamic-execution-pattern", "high", re.compile(r"\b(eval|exec|Function)\s*\(", re.I)),
    ("network-access-pattern", "high", re.compile(r"\b(requests|urllib|http\.client|socket|fetch)\b", re.I)),
    ("configuration-write-pattern", "medium", re.compile(r"\b(write_text|writeFile|open\s*\([^)]*['\"]w|os\.replace)\b", re.I)),
    ("prompt-override-pattern", "medium", re.compile(r"\b(ignore (all |any )?(previous|prior) instructions|system prompt|you are now)\b", re.I)),
    ("hidden-html-comment", "low", re.compile(r"<!--")),
)
SECRET_PATTERN = re.compile(
    r"\b(api[_-]?key|access[_-]?token|secret|password|private[_-]?key)\b\s*[:=]",
    re.I,
)
URL_PATTERN = re.compile(r"https?://([^/\s?#]+)", re.I)
MANIFEST_NAMES = {
    "package.json",
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "pyproject.toml",
    "requirements.txt",
    "setup.py",
    "setup.cfg",
    "dockerfile",
    "compose.yaml",
    "docker-compose.yml",
}
LIFECYCLE_NAMES = {
    ".husky",
    "pre-commit",
    "postinstall",
    "preinstall",
    "prepare",
}


class ScanFailure(Exception):
    def __init__(self, reason, exit_code=2):
        super().__init__(reason)
        self.reason = reason
        self.exit_code = exit_code


def is_reparse_point(file_stat):
    mask = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    attributes = getattr(file_stat, "st_file_attributes", 0)
    return bool(attributes & mask)


def is_link_or_reparse(file_stat):
    return stat.S_ISLNK(file_stat.st_mode) or is_reparse_point(file_stat)


def is_within(root, candidate):
    try:
        root_norm = os.path.normcase(os.path.abspath(root))
        candidate_norm = os.path.normcase(os.path.abspath(candidate))
        return os.path.commonpath((root_norm, candidate_norm)) == root_norm
    except ValueError:
        return False


def path_id(root, candidate):
    relative = os.path.relpath(candidate, root).replace(os.sep, "/")
    digest = hashlib.sha256(relative.encode("utf-8", "surrogatepass")).hexdigest()
    return "path-" + digest[:16]


def safe_hostname(value):
    host = value.split("@")[ -1 ].split(":")[0].lower()
    if re.fullmatch(r"[a-z0-9.-]{1,253}", host):
        return host
    return "[REDACTED]"


def ensure_deadline(deadline):
    if time.monotonic() > deadline:
        raise ScanFailure("scan_time_limit_exceeded")


def verify_ancestors(root, deadline):
    absolute = os.path.abspath(root)
    drive, tail = os.path.splitdrive(absolute)
    current = drive + os.sep if drive else os.sep
    for part in (item for item in tail.split(os.sep) if item):
        ensure_deadline(deadline)
        current = os.path.join(current, part)
        try:
            current_stat = os.lstat(current)
        except OSError:
            raise ScanFailure("ancestor_metadata_unavailable")
        if is_link_or_reparse(current_stat):
            raise ScanFailure("ancestor_link_or_reparse_point")
    return absolute


def recognized_text(path):
    return (
        os.path.basename(path).lower() in TEXT_FILENAMES
        or os.path.splitext(path)[1].lower() in TEXT_SUFFIXES
    )


def preflight(target):
    deadline = time.monotonic() + MAX_SECONDS
    root = verify_ancestors(target, deadline)
    try:
        root_stat = os.lstat(root)
    except OSError:
        raise ScanFailure("target_metadata_unavailable")
    if is_link_or_reparse(root_stat):
        raise ScanFailure("target_link_or_reparse_point")
    if not stat.S_ISDIR(root_stat.st_mode):
        raise ScanFailure("target_not_directory")

    root_real = os.path.realpath(root)
    if not is_within(root, root_real):
        raise ScanFailure("target_canonicalization_unsafe")

    files = []
    entries_seen = 0
    total_text_bytes = 0
    stack = [(root, 0)]
    while stack:
        directory, depth = stack.pop()
        ensure_deadline(deadline)
        try:
            with os.scandir(directory) as iterator:
                listed = sorted(iterator, key=lambda item: item.name)
        except OSError:
            raise ScanFailure("directory_metadata_unavailable")

        for entry in listed:
            ensure_deadline(deadline)
            entries_seen += 1
            if entries_seen > MAX_ENTRIES:
                raise ScanFailure("entry_limit_exceeded")
            candidate = os.path.abspath(entry.path)
            if not is_within(root, candidate):
                raise ScanFailure("path_containment_failed")
            try:
                entry_stat = entry.stat(follow_symlinks=False)
            except OSError:
                raise ScanFailure("entry_metadata_unavailable")
            if is_link_or_reparse(entry_stat):
                raise ScanFailure("link_or_reparse_point_detected")
            if stat.S_ISDIR(entry_stat.st_mode):
                if depth + 1 > MAX_DEPTH:
                    raise ScanFailure("depth_limit_exceeded")
                stack.append((candidate, depth + 1))
                continue
            if not stat.S_ISREG(entry_stat.st_mode):
                raise ScanFailure("non_regular_file_detected")
            if recognized_text(candidate):
                if entry_stat.st_size > MAX_FILE_BYTES:
                    raise ScanFailure("per_file_text_limit_exceeded")
                total_text_bytes += entry_stat.st_size
                if total_text_bytes > MAX_TOTAL_TEXT_BYTES:
                    raise ScanFailure("total_text_limit_exceeded")
            files.append(
                {
                    "path": candidate,
                    "path_id": path_id(root, candidate),
                    "stat": entry_stat,
                    "text": recognized_text(candidate),
                }
            )

    direct_skill = os.path.join(root, "SKILL.md")
    matching = [item for item in files if os.path.normcase(item["path"]) == os.path.normcase(direct_skill)]
    if len(matching) != 1:
        raise ScanFailure("direct_root_skill_md_missing")
    return {
        "root": root,
        "root_real": root_real,
        "deadline": deadline,
        "files": sorted(files, key=lambda item: item["path"]),
        "entries_seen": entries_seen,
    }


def same_identity(before, after):
    if not stat.S_ISREG(after.st_mode):
        return False
    for attribute in ("st_dev", "st_ino", "st_size", "st_mtime_ns"):
        before_value = getattr(before, attribute, None)
        after_value = getattr(after, attribute, None)
        if (
            before_value is not None
            and after_value is not None
            and not (attribute in ("st_dev", "st_ino") and (before_value == 0 or after_value == 0))
            and before_value != after_value
        ):
            return False
    return True


def read_verified(item, root_real, deadline):
    ensure_deadline(deadline)
    resolved = os.path.realpath(item["path"])
    if not is_within(root_real, resolved):
        raise ScanFailure("resolved_path_containment_failed")

    flags = os.O_RDONLY
    if hasattr(os, "O_BINARY"):
        flags |= os.O_BINARY
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        descriptor = os.open(item["path"], flags)
    except OSError:
        raise ScanFailure("safe_open_failed")
    try:
        opened_stat = os.fstat(descriptor)
        if not same_identity(item["stat"], opened_stat):
            raise ScanFailure("file_changed_after_preflight")
        remaining = MAX_FILE_BYTES
        chunks = []
        while remaining:
            ensure_deadline(deadline)
            chunk = os.read(descriptor, min(65536, remaining))
            if not chunk:
                break
            chunks.append(chunk)
            remaining -= len(chunk)
        if os.read(descriptor, 1):
            raise ScanFailure("per_file_text_limit_exceeded")
        return b"".join(chunks).decode("utf-8")
    except UnicodeDecodeError:
        return None
    finally:
        os.close(descriptor)


def add_finding(findings, item, line, rule, severity, detail=None):
    finding = {
        "id": "finding-" + hashlib.sha256(
            (item["path_id"] + rule + str(line)).encode("utf-8")
        ).hexdigest()[:16],
        "severity": severity,
        "rule": rule,
        "location": item["path_id"],
        "line": line,
        "evidence": "[REDACTED]",
    }
    if detail:
        finding["detail"] = detail
    findings.append(finding)


def inspect_frontmatter(lines, item, findings):
    if not lines or lines[0].strip() != "---":
        add_finding(findings, item, 1, "missing_frontmatter", "medium")
        return
    closing = None
    for index, line in enumerate(lines[1:121], start=2):
        if line.strip() == "---":
            closing = index
            break
    if closing is None:
        add_finding(findings, item, 1, "unterminated_frontmatter", "medium")
        return

    fields = set()
    for index in range(2, closing):
        line = lines[index - 1]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith(("!", "&", "*", "<<")) or ": |" in stripped or ": >" in stripped:
            add_finding(findings, item, index, "manual_frontmatter_review_required", "medium")
            continue
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        key = key.strip().lower()
        fields.add(key)
        if key in SUSPICIOUS_FRONTMATTER:
            add_finding(findings, item, index, SUSPICIOUS_FRONTMATTER[key], "medium")
        if key == "name" and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value.strip()):
            add_finding(findings, item, index, "noncanonical_skill_name", "medium")
    if "name" not in fields:
        add_finding(findings, item, 1, "missing_name", "high")
    if "description" not in fields:
        add_finding(findings, item, 1, "missing_description", "high")


def inspect_text(lines, item, findings):
    filename = os.path.basename(item["path"]).lower()
    if filename == "skill.md":
        inspect_frontmatter(lines, item, findings)
    if filename in MANIFEST_NAMES:
        add_finding(findings, item, 1, "package_or_dependency_manifest", "medium")
    if filename in LIFECYCLE_NAMES:
        add_finding(findings, item, 1, "lifecycle_hook_name", "high")

    for line_number, line in enumerate(lines, start=1):
        if any(unicodedata.category(character) == "Cf" for character in line):
            add_finding(findings, item, line_number, "invisible_unicode", "medium")
        if SECRET_PATTERN.search(line):
            add_finding(findings, item, line_number, "possible_secret_assignment", "high")
        for rule, severity, pattern in CODE_RULES:
            if pattern.search(line):
                add_finding(findings, item, line_number, rule, severity)
        for match in URL_PATTERN.finditer(line):
            add_finding(
                findings,
                item,
                line_number,
                "external_url",
                "low",
                {"hostname": safe_hostname(match.group(1))},
            )


def result(status, findings, scope, error=None):
    payload = {
        "schema": SCHEMA,
        "status": status,
        "requires_human_review": True,
        "disposition": "manual_review_required",
        "scope": scope,
        "findings": sorted(
            findings,
            key=lambda item: (item["location"], item["line"], item["rule"], item["id"]),
        ),
        "limitations": [
            "Static analysis only",
            "No provenance verification",
            "No code execution",
            "No installation decision",
        ],
    }
    if error:
        payload["error"] = error
    return payload


def scan(target):
    preflight_result = preflight(target)
    findings = []
    text_files_scanned = 0
    unscanned_files = 0
    for item in preflight_result["files"]:
        ensure_deadline(preflight_result["deadline"])
        if not item["text"]:
            unscanned_files += 1
            continue
        content = read_verified(item, preflight_result["root_real"], preflight_result["deadline"])
        if content is None:
            unscanned_files += 1
            add_finding(findings, item, 1, "text_decode_incomplete", "low")
            continue
        inspect_text(content.splitlines(), item, findings)
        text_files_scanned += 1

    scope = {
        "entries_seen": preflight_result["entries_seen"],
        "text_files_scanned": text_files_scanned,
        "unscanned_files": unscanned_files,
    }
    status = "incomplete" if unscanned_files else "completed"
    return result(status, findings, scope), 0 if status == "completed" else 2


def main():
    parser = argparse.ArgumentParser(
        description="Perform a bounded read-only static inspection of one skill directory."
    )
    parser.add_argument("target", help="One directory to inspect; archives are not accepted.")
    arguments = parser.parse_args()
    try:
        payload, exit_code = scan(arguments.target)
    except ScanFailure as error:
        payload = result(
            "blocked",
            [],
            {"entries_seen": 0, "text_files_scanned": 0, "unscanned_files": 0},
            error.reason,
        )
        exit_code = error.exit_code
    except Exception:
        payload = result(
            "incomplete",
            [],
            {"entries_seen": 0, "text_files_scanned": 0, "unscanned_files": 0},
            "scanner_internal_error",
        )
        exit_code = 3
    sys.stdout.write(json.dumps(payload, ensure_ascii=True, sort_keys=True) + "\n")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
