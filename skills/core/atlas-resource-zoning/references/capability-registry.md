# Capability Registry

This file is a durable routing aid, not a record of one account or one machine. Runtime capabilities, plan entitlements, and current authoritative product documentation always take precedence.

## Sources to verify when availability matters

- Active runtime selector or configuration
- Official model documentation: <https://developers.openai.com/api/docs/guides/latest-model>
- Official model catalog: <https://developers.openai.com/api/docs/models>
- Current ChatGPT plan/help documentation: <https://help.openai.com/>

Do not embed local cache paths, account-specific access, prices, usage limits, promotional allowances, or reset periods in this public registry.

## Durable capability roles

Use logical roles rather than assuming a stable product label:

| Logical tier | Intended role |
|---|---|
| Economy | Efficient, deterministic, high-volume work with strong verification |
| Balanced | Normal serious work: implementation, debugging, research, planning, and review |
| Frontier | High ambiguity, conflicting evidence, difficult synthesis, or high failure cost |

Map the currently exposed models to these roles only after checking the active surface. A product may expose different model names, reasoning labels, quality modes, or agentic controls over time.

## Availability protocol

When plan, surface, or selector availability matters:

1. inspect the active runtime first;
2. verify disputed or time-sensitive claims in current official documentation;
3. state the logical recommendation separately from what is confirmed available;
4. offer one conservative fallback when availability is uncertain;
5. never infer plan entitlement from account intention, past access, or another product surface.

## Terminology guardrails

- A **plan** is an account entitlement; it is not a model name.
- A **model selection** is surface-specific and can differ across Chat, Work, Codex, and API.
- A **reasoning effort** is independent from the base model and may be offered as different labels by different surfaces.
- **Quality** and **agentic** modes are optional surface capabilities; do not imply they exist when they are not visible or documented.
- Treat labels such as `Pro`, `Max`, or `Ultra` as product-surface-specific unless the active runtime or official documentation defines them for the current task.

No fixed worker count, reasoning ladder, or plan-to-model mapping belongs in this registry. Verify current product facts whenever they affect a recommendation.
