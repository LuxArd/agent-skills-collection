---
name: media-discovery-provenance
description: Define and evaluate evidence contracts for supplied media-source and asset records. Use only when a Media or Radar task explicitly needs provenance, source-admission, rights-evidence, or generated-media record reasoning; it never retrieves, downloads, generates, or approves assets.
---

# Media Discovery and Provenance

Use this skill for an explicit, bounded review of supplied media-source,
asset-identity, or provenance records. It structures evidence and decision
criteria; it does not retrieve media or grant rights.

## Activation boundary

This package is explicit-only. The task must identify the media need, source
records or candidate assets, the applicable source policy, and the decision
being prepared. Treat missing evidence as a result, not as permission to
assume a source, creator, license, or right.

## Visual Need Contract

For each request, record a Visual Need Contract with:

- Need ID, story or editorial purpose, target audience, and intended use.
- Required subject, action, setting, composition, orientation, duration, and
  accessibility constraints.
- Prohibited content, required attribution, sensitivity, and format limits.
- Retrieval-first criteria and the conditions under which generated media may
  be considered.
- Evidence required before the controlled process can use the asset.

The contract describes the need. It does not authorize collection, generation,
editing, publication, or a rights decision.

## Source and asset record

Use stable identifiers rather than ambiguous display names. A supplied source
or asset record should distinguish these fields where known:

- Source ID, publisher or provider, supplied locator, collection timestamp, and
  declared source policy.
- Asset ID, version or derivative relationship, content identity evidence,
  owner/publisher claim, and applicable restrictions.
- Rights evidence type, evidence locator, scope of the claimed permission,
  attribution requirement, expiry or uncertainty, and reviewer status.
- Provenance chain: source to acquisition record to derivative or render, with
  gaps explicitly marked `UNKNOWN`.
- Status: `CANDIDATE`, `PENDING_EVIDENCE`, `EVIDENCE_RECORDED`,
  `ESCALATE`, or `EXCLUDED`.

`EVIDENCE_RECORDED` means evidence was supplied and described; it never means
that this skill approved a license or legal right. Only a separately authorized
rights or publishing process can grant an approval status.

## Source-admission evaluation

Evaluate supplied records against the stated policy:

1. Match the source and asset identity to the Visual Need Contract.
2. Determine whether the source policy, rights evidence, provenance chain,
   restrictions, and attribution conditions are present and internally
   consistent.
3. Classify gaps as `PENDING_EVIDENCE`, `ESCALATE`, or `EXCLUDED`; explain the
   missing evidence without inventing legal conclusions.
4. Prefer an eligible supplied retrieval candidate before proposing generated
   media. If no candidate meets the contract, say so rather than generating or
   downloading an alternative.

For generated media, require a supplied record of process or provider identity,
model or system version when known, operator, generation date, output/asset ID,
derivative chain, applicable policy/rights evidence, and any attribution or use
restrictions. Do not infer those facts from a file name or visual appearance.

## Output contract

Return:

1. The Visual Need Contract and its evidence limits.
2. A source/asset registry assessment with status, evidence locators, gaps, and
   escalation reason.
3. A retrieval-first recommendation expressed as a conditional next step, not
   an automatic action.
4. A provenance chain summary that names every unresolved link.

## Non-authority and CORE boundary

This skill must not download assets, execute models, call media providers,
approve rights without evidence, modify a registry, generate media, edit an
asset, render, publish, or modify production state. It does not decide visual
quality, create an edit plan, or issue a QA verdict.

It does not replace CORE truth/evidence, security, architecture, or review
authority. Use source-grounding only for an explicitly requested external or
version-sensitive policy claim; use security review only when explicitly asked
for a security review. Neither is silently invoked here.
