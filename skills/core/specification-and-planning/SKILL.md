---
name: specification-and-planning
description: Turn a significant or unclear change into an evidence-aware specification and an ordered, verifiable implementation plan. Use when requirements are ambiguous, a change spans independently testable capabilities, dependencies or delivery order are unclear, or implementation needs explicit acceptance criteria and checkpoints. Do not use for a trivial, self-contained request with clear acceptance.
---

# Specification and Planning

Plan the requested outcome before implementation when a clear specification or delivery
order will materially reduce risk, rework, or ambiguity. This skill plans work; it
does not implement, create tracker items, or run validation commands.

## Establish scope

Identify:

- The requested outcome and intended user or system behavior.
- In-scope work and explicit non-goals.
- Constraints, dependencies, affected boundaries, and material risks.
- FACT, INFERENCE, ASSUMPTION, UNKNOWN, and UNVERIFIED claims.
- Decisions that need user authority before work can proceed.

Use the smallest reasonable interpretation for safe, reversible details. Ask for
direction only when an ambiguity changes safety, cost, confidentiality, irreversible
scope, or externally visible behavior.

## Write the specification

State:

1. Objective and desired outcome.
2. In-scope behavior and non-goals.
3. Observable acceptance criteria.
4. Constraints, risks, dependencies, and evidence needs.
5. Open questions that genuinely block a material choice.

Do not claim that a design, test, integration, or operational result already exists
unless it was directly established.

## Map capabilities only when useful

Create a compact capability map only when the request contains independently testable
capabilities with meaningful dependency relationships. Give each capability a stable
identifier, a concise outcome, direct prerequisites, and a proposed build order.

Do not force a capability map for a self-contained change. Avoid circular
dependencies; flag them as a design issue rather than hiding them in task order.

## Build an implementation plan

Prefer small vertical slices that produce an observable result where the architecture
permits it. Use a limited horizontal change only when a shared primitive, migration,
or mechanically safe refactor is a real prerequisite.

For each task, state:

- Purpose and expected outcome.
- Prerequisites and safe parallelization opportunities.
- Acceptance criteria and proportionate verification.
- Likely affected paths only when evidenced; otherwise mark them proposed.
- Risks, dependencies, and any checkpoint or authority requirement.

Return a dependency-aware sequence and identify work that must remain sequential.
Treat numerical file-count or time estimates as advisory signals, not rigid gates.

## Output and write boundary

Return the specification and plan in the requested medium by default. Do not create
tasks directories, plan files, todo files, tickets, issues, or external tracker
records unless the user explicitly authorizes the destination and mutation.

Route durable architectural choices to adr. Route current external, framework, SDK,
or standard claims to source-grounding. Apply engineering-evidence-policy to scope,
assumptions, validation, and completion claims.
