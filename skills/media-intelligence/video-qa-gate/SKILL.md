---
name: video-qa-gate
description: Independently evaluate supplied technical and perceptual evidence for an immutable identified render. Use only when a Video QA task explicitly needs a PASS, REVISE, REJECT, or CRITICAL_FAIL gate verdict and publish recommendation; it never renders, edits, or publishes.
---

# Video QA Gate

Use this skill only for an explicit independent QA review of one immutable,
identified render and its supplied technical, perceptual, editorial, and
provenance-related evidence. It owns the QA verdict and publish recommendation,
not production execution.

## Activation boundary and independence

This package is explicit-only. Require a render ID, version/hash or other
immutable identifier, supplied delivery constraints, and timestamped evidence
or an explicit coverage gap. The editor's plan may be input context, but the
editor must not approve its own output through this skill.

Do not issue `PASS` when required evidence is absent, the render identity is
ambiguous, or a blocking gate cannot be evaluated. Use `REVISE`, `REJECT`, or
`CRITICAL_FAIL` with the missing-evidence reason as appropriate.

## Evidence and defect record

For every material result, record:

- Immutable render ID and supplied version/hash, delivery target, evidence
  locator/timestamp, and coverage limits.
- Defect class: technical, perceptual, editorial/multimodal, integrity,
  rights/provenance gate, or safety gate.
- Severity: informational, minor, major, or critical; include factual evidence,
  impact, and confidence.
- A bounded correction request that identifies the defect and acceptance evidence
  without dictating renderer commands or changing the edit plan.

Distinguish a measured technical fact from a perceptual observation or editorial
preference. Do not invent measurements, timestamps, render properties, rights,
or safety evidence.

## Gate method

1. Verify that the supplied evidence identifies one immutable render and the
   delivery constraints being assessed.
2. Evaluate technical QC, perceptual quality, and editorial/multimodal fit only
   within the supplied evidence and stated coverage.
3. Treat integrity, rights/provenance, and safety gates as hard constraints.
   Performance feedback may inform soft editorial guidance only; it may never
   weaken a hard gate.
4. Classify each defect and decide the single gate verdict:
   - `PASS`: sufficient evidence and no blocking defect.
   - `REVISE`: correctable defect or missing bounded evidence prevents pass.
   - `REJECT`: the current immutable render is not acceptable and needs a
     replacement or material rework.
   - `CRITICAL_FAIL`: a critical technical, integrity, rights/provenance, or
     safety gate fails; the render must not proceed.
5. State a publish recommendation separate from the verdict: `DO_NOT_PUBLISH`,
   `ESCALATE`, or `ELIGIBLE_FOR_SEPARATE_CONTROLLED_PUBLISHING`. Eligibility is
   not publication and creates no execution authority.

## Output contract

Return the render identity, scope/coverage statement, defect ledger, one allowed
verdict, publish recommendation, bounded correction requirements, and unresolved
evidence. Preserve defect timestamps and IDs across a subsequent review; do not
rewrite history to make a prior finding disappear.

## Non-authority and CORE boundary

This skill must not render, execute FFmpeg/Remotion/VLM tools, edit media,
change an Edit Decision Plan, download assets, approve rights, write files,
publish, or modify production state. It does not decide architecture, security,
or general evidence policy and cannot override a CORE skill.

Visual evidence may be supplied from the separate shared evidence skill, but it
is never invoked automatically. Security or rights concerns requiring a distinct
review must be escalated explicitly to the relevant authorized process; this
skill does not perform a hidden review or external validation.
