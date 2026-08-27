---
name: atlas-resource-zoning
description: Recommend a proportionate available model, reasoning effort, and agentic execution mode before substantive work; use for model choice, reasoning choice, compute budgeting, or escalation and de-escalation decisions. Do not use for simple requests that do not require a model-selection gate.
---

# Atlas Resource Zoning

Choose the minimum sufficient capability for a reliable result. Optimize expected total cost of successful completion, including retries and verification, rather than minimizing the cost of the first attempt. Preserve the user's explicit model choice and approval boundaries.

## Decision dimensions

Keep these dimensions independent:

- **Surface and entitlement:** Chat, Work, Codex, API; Plus, Pro, Business, Enterprise, or unknown.
- **Base capability:** Luna, Terra, Sol, or a future equivalent.
- **Reasoning effort:** none/low/medium/high/xhigh/max or the labels actually exposed by the surface.
- **Quality mode:** standard or Pro-quality when the surface supports it.
- **Agentic execution:** single-agent or parallel/multi-agent when available and authorized.

Never infer an available combination from a plan name alone. `ChatGPT Pro`, the ChatGPT `Pro` selection, and API `reasoning.mode: pro` are different concepts. Treat `ultra` as a surface-dependent label; inspect current runtime metadata before deciding whether it adds reasoning, delegation, or both. Never assume a fixed number of agents.

## Route the task

Assess the task qualitatively. Consider ambiguity, intellectual difficulty, failure cost, reversibility, novelty, interdependencies, verifiability, context burden, security/correctness sensitivity, and meaningful parallelizability. Do not create a numeric score.

Choose the base capability independently from reasoning:

- **Luna:** deterministic extraction, formatting, classification, repetitive edits, routine inspection, mechanical validation, and other low-risk work with cheap verification.
- **Terra:** normal serious-work default for implementation, debugging, research, planning, multi-file changes, integrations, refactoring, and standard review.
- **Sol:** use when frontier capability has meaningful expected value: difficult architecture, high ambiguity, conflicting evidence, cross-system reasoning, novel root-cause analysis, security-sensitive decisions, high blast radius, or failed competent cheaper attempts.

Do not choose Sol because a task is important, urgent, long, or touches many files. A large deterministic task can remain Luna or Terra; a tiny irreversible decision can justify Sol.

Choose reasoning independently:

- **Low/none:** deterministic, reversible work with negligible ambiguity and cheap verification.
- **Medium:** ordinary analysis or implementation with several dependencies.
- **High:** material ambiguity, several plausible approaches, non-trivial debugging, or meaningful failure cost.
- **XHigh:** unusually difficult single-agent reasoning with a clear expected benefit.
- **Max:** exceptional quality-first work involving difficult system synthesis, hidden interactions, failed competent attempts, very high failure cost, or hard-to-reverse decisions. Every Max recommendation needs a concrete justification.

Use Pro-quality only for difficult work where a marginal reliability gain materially affects the outcome. Use parallel/multi-agent execution only when the work is difficult **and** divides into genuinely independent workstreams. Do not use it when one sequential reasoning chain dominates or coordination overhead exceeds the benefit.

## Availability gate

Use this precedence:

1. capabilities exposed by the active runtime or selector;
2. current authoritative product documentation or configuration;
3. the dated capability registry;
4. a conservative fallback explicitly marked uncertain.

If plan, surface, or availability is unknown, do not guess. Recommend the logical target and the closest safe fallback, for example: `Sol XHigh if available; otherwise Sol High`.

Read [references/capability-registry.md](references/capability-registry.md) when plan/surface differences or current availability affect the recommendation. For advanced or disputed routing decisions, read [references/routing-policy.md](references/routing-policy.md). Read [references/eval-cases.md](references/eval-cases.md) only when testing or maintaining this skill.

## Recommendation contract

For a substantive task, keep the pre-task recommendation compact:

```text
Recomand: 5.6 Terra — High.
Motiv: [one sentence tied to the task's actual difficulty, risk, and verifiability].

Aștept: GO
```

If availability is uncertain, add one short fallback line. Do not print a large schema unless the user asks for an audit.

When the host environment has a user-confirmation rule, that rule controls the pause. For a workflow that uses `GO`, a `GO` counts only after the recommendation for the current task. Do not claim to have changed or verified the user's selector. Simple translations, links, short explanations, and other trivial requests proceed without this gate.

## During execution

- Escalate only when new evidence shows the chosen capability is insufficient; change the dimension that matches the failure.
- De-escalate after the difficult phase when the remaining work is routine.
- Do not interrupt the user for every internal phase. Request a new manual selector change only when it materially affects reliability or resource use.
- Use cheaper configurations more readily when deterministic verification is strong; route conservatively when correctness is hard to verify.
- A recommendation does not authorize tools, external writes, deployment, purchases, publication, or broader project scope.
