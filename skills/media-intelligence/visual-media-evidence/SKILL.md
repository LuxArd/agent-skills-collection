---
name: visual-media-evidence
description: Structure descriptive evidence about already identified media assets or immutable renders. Use only when Media/Radar or Video QA explicitly needs scene, shot, segment, or defect evidence; it does not retrieve media, run analysis models, change plans, or make approval decisions.
---

# Visual Media Evidence

Use this shared skill only for an explicit Media/Radar or Video QA task that
needs descriptive, timestamped evidence about already identified assets or an
immutable render. It is evidentiary, not operational or decisional.

## Activation boundary

This package is explicit-only and shared only between the Media/Radar and Video
QA domains. Start from supplied asset/render identifiers and supplied visual,
technical, or human-observation evidence. State when an observation comes from
provided material, a supplied measurement, or an assessor statement.

Do not convert an observation into a provenance claim, a rights conclusion, a
QA verdict, an edit instruction, or a publication recommendation.

## Evidence record

Record each observation with:

- Asset or immutable render ID, version/hash when supplied, and evidence locator.
- Scene, shot, segment, page, frame range, or timestamp interval; use an
  `UNKNOWN` locator when it cannot be determined.
- Observation category: semantic relevance, subject visibility, crop risk,
  motion/composition, visual quality, technical defect, perceptual defect, or
  other clearly named category.
- Descriptive observation, supplied basis, confidence, and material ambiguity.
- Separation between direct observation, supplied measurement, and inference.

Use concise description. Do not reproduce sensitive source text, hidden metadata,
or private locators unnecessarily.

## Descriptive method

For every material observation:

1. Identify what specific supplied evidence supports it.
2. Describe what is visible or measured without inferring intent, ownership,
   rights, safety, or audience impact beyond the evidence.
3. State crop or framing risk in relation to the supplied target format.
4. Separate technical/perceptual defects from editorial preference.
5. State confidence and the reason for uncertainty, such as an incomplete
   timestamp, missing source frame, unclear subject, or conflicting record.

When the evidence is insufficient, return `UNKNOWN` or a request for a bounded
additional observation. Do not manufacture a scene boundary, timestamp,
quality score, or semantic conclusion.

## Output contract

Return an evidence ledger or table with identifier, locator, category,
description, basis, confidence, and limitation. Add a short coverage statement
that names unobserved intervals, missing supplied data, and any identity mismatch.

The result may be handed to the Media/Radar domain for provenance context or to
Video QA for independent gate reasoning. It never chooses their decision.

## Non-authority and CORE boundary

This skill must not run VLMs, CLIP, SAM, FFmpeg, or other analysis tooling;
download media; approve rights; approve publishing; change an edit plan; render;
write files; or modify production state. It does not issue a QA verdict or infer
that an asset is legally usable from its visual appearance.

It does not override CORE evidence, source-grounding, architecture, security, or
review authority. Request a separate, explicit CORE workflow only when its
distinct purpose is actually needed; do not invoke one silently.
