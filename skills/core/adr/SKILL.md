---
name: adr
description: Record and maintain architecture decisions with context, alternatives, consequences, non-goals, implementation implications, and verifiable outcomes. Use when a decision is hard to reverse, establishes a reusable technical pattern, changes a dependency or system boundary, or conflicts with an accepted decision. Do not use for routine local implementation choices.
---

# ADR

Create a durable decision record only when the decision will help future work avoid
reopening the same material trade-off.

## Decide whether an ADR is warranted

Use an ADR when one or more of these are true:

- Reversing the decision would be costly or disruptive.
- The decision changes a system boundary, interface, data contract, dependency,
  security posture, operational model, or reusable technical pattern.
- More than one viable option has material trade-offs.
- The decision supersedes or conflicts with an accepted prior decision.

For a routine local choice, explain the rationale in the relevant plan, review, or
code discussion instead of creating an ADR.

## Gather bounded evidence

Inspect only the relevant existing ADRs, project rules, design material, and affected
code or configuration. Separate:

- FACT: directly observed material.
- INFERENCE: conclusion supported by the available material.
- ASSUMPTION: a disclosed working premise.
- UNKNOWN or UNVERIFIED: a gap that cannot be established from the allowed scope.

Do not invent paths, versions, owners, test results, performance figures, or prior
decisions. If a material alternative cannot be evaluated safely, say so and request
the missing decision or evidence.

## Draft before mutating

Draft the ADR in the response by default. Use assets/adr-simple.md for a
straightforward decision and assets/adr-options.md when alternatives need a direct
comparison.

Include:

1. A concise title and Proposed, Accepted, Superseded, or Rejected status.
2. The decision trigger, context, constraints, and non-goals.
3. The decision drivers and genuine alternatives considered.
4. The selected decision and its consequences, including downsides.
5. Implementation implications only where evidence supports them.
6. Verification evidence, limitations, and conditions that should cause review.

Run references/review-checklist.md against the draft before presenting it as ready
for acceptance.

## Preserve decision history

Never rewrite an accepted ADR merely to make old reasoning look current. When a new
decision replaces one, create a new ADR that identifies the prior record and explains
the supersession. Keep the former rationale intact.

## Write boundary

Do not create, rename, overwrite, index, commit, or update an ADR file unless the
user has explicitly authorized the target location and mutation. Confirm that the
target is an approved working location before writing. This skill drafts and reviews
decision records; it does not authorize filesystem changes or run helper scripts.

## Handoffs

Use specification-and-planning for delivery sequencing and acceptance work. Use
source-grounding when an external or version-sensitive claim needs evidence. Apply
engineering-evidence-policy to every claim of completion or verification.
