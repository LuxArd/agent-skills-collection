# Installation

Install only the skills you need. These packages follow the common Agent Skills directory convention: each installed skill is a folder containing a root `SKILL.md` file.

## Install one skill

Copy one complete directory, preserving every nested file.

```text
skills/core/adr
→ ~/.agents/skills/adr
```

On Windows, the equivalent common location is:

```text
C:\\Users\\<your-user>\\.agents\\skills\\adr
```

## Install selected skills

For example, an engineering baseline may use:

```text
skills/core/adr
skills/core/specification-and-planning
skills/core/source-grounding
skills/core/engineering-evidence-policy
```

Add an on-demand skill only when its scope is needed.

## Install all skills

Copy the contents of both `skills/core/` and `skills/media-intelligence/` into your Agent Skills discovery directory. Do not flatten folders and do not copy only `SKILL.md`; supporting references, templates, and safe scripts belong with their skill.

## Verify discovery

Use the discovery mechanism of your AI-agent environment and confirm that each intended folder is detected as one skill. A valid package has a direct-root `SKILL.md`.

## Upgrade safely

1. Review the release diff and component license notices.
2. Back up or version-control your existing installed skill folder.
3. Replace the complete skill directory as one unit.
4. Re-run discovery and inspect the root `SKILL.md`.

Never place credentials, environment files, or project-specific configuration inside a skill directory.
