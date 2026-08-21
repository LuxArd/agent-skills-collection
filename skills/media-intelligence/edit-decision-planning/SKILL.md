---
name: edit-decision-planning
description: Transform approved story and asset packages into a declarative Edit Decision Plan. Use only when an editing task explicitly needs a constrained, non-executing plan; it does not render, edit files, operate FFmpeg or Remotion, or approve QA or publication.
---

# Edit Decision Planning

Use this skill only when an explicit editing task supplies an approved story
package and asset package and needs a declarative Edit Decision Plan (EDP).
Return a plan, not executable commands, project files, or rendered media.

## Activation boundary

This package is explicit-only. Before planning, establish the story version,
asset IDs and supplied approval/status records, applicable format/accessibility
constraints, narration/caption inputs, and the target delivery constraints.

If an asset lacks a supplied status or its intended segment is ambiguous, retain
the gap in the plan. This skill may not use a plan to decide source rights or to
turn a candidate asset into an approved one.

## Edit Decision Plan contract

Use a declarative structure with no shell commands, renderer calls, package
names, file paths, or implementation-specific code. Include:

- `edp_id`, schema version, story version, source-package identifiers, and
  unresolved constraints.
- Output format constraints: aspect ratio, duration target/range, resolution
  class, audio/caption/accessibility constraints, and delivery assumptions.
- Ordered scenes with scene ID, intended duration, narrative purpose, asset IDs,
  segment IDs, narration anchors, caption intent, transition class, framing/crop
  intent, and editorial rationale.
- Explicit handoff notes for a separately controlled renderer, preserving asset
  IDs and constraints without prescribing execution commands.
- Validation questions that the independent QA gate should assess after a
  separately identified immutable render exists.

Use stable identifiers. Do not substitute an unverified human-readable title or
a local file name for an asset or segment ID.

## Planning method

1. Trace each scene to an approved story purpose and supplied asset/segment ID.
2. Preserve source restrictions, required attribution, aspect-ratio limits,
   accessibility constraints, and duration constraints as plan constraints.
3. Separate requested editorial preference from a hard constraint or unresolved
   risk.
4. Flag conflicts, missing assets, unknown narration anchors, and incompatible
   crop requirements rather than silently resolving them.
5. Keep transitions and effects as semantic classes and rationale; renderer
   selection and implementation remain outside this skill.

## Output contract

Return an EDP plus a compact assumptions and unresolved-items section. The EDP
can recommend a controlled render handoff only after its inputs are identified;
it cannot launch that handoff. Include no command line, dependency, or code.

## Non-authority and CORE boundary

This skill must not execute FFmpeg or Remotion; use shell, `npx`, or package
managers; write production files; install or upgrade dependencies; render;
approve QA; approve publishing; or modify production state. FFmpeg and Remotion
remain separately controlled production execution technologies.

This skill neither grants asset rights nor decides provenance. It does not own
truth/evidence policy, architecture decisions, security review, or independent
quality review; those remain CORE or dedicated-domain responsibilities. Do not
silently invoke another skill or service from this plan.
