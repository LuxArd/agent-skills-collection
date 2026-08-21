---
name: performance-learning-evaluation
description: Evaluate supplied performance facts, hypotheses, experiments, and learning state with causal and leakage discipline. Use only when an explicit performance-learning task needs interpretation of already-collected data; it does not ingest data, run models, launch experiments, or activate policies.
---

# Performance Learning Evaluation

Use this skill only when an explicit task supplies already-collected performance
data, experiment records, or a learning ledger and asks for bounded evaluation.
It helps distinguish observed outcomes from increasingly supported lessons; it
does not operate analytics or policy systems.

## Activation boundary

This package is explicit-only. Require the decision question, metric
definitions, observation and outcome windows, supplied data provenance,
completeness limits, population/cohort definition, and relevant change history.
If these are not available, record the limitation and avoid a causal or policy
claim.

## Learning ledger

For each fact, hypothesis, experiment, or lesson, retain a stable ID and record:

- The claim, decision context, owner/process context, and current state.
- Evidence locators, collection cutoff, population/cohort, metric definition,
  sample size or sample-size concern, and data-completeness caveat.
- Causal assumptions, known confounders, treatment/exposure definition, and
  alternatives that could explain the observation.
- Validation method, outcome horizon, no-future-leakage controls, and links to
  superseded or contradictory lessons.

Use only these lesson states:

- `OBSERVED` — a bounded recorded fact.
- `CORRELATED` — an observed association without causal identification.
- `HYPOTHESIS` — a testable proposed explanation or policy premise.
- `TESTING` — an evaluation has a defined design and measurement window.
- `SUPPORTED` — supplied evidence is consistent with the claim in its scope,
  while material alternatives or replication limits remain.
- `CONFIRMED` — the program's stated confirmation criteria and evidence are met;
  state the criteria and scope rather than treating the claim as universal.
- `REJECTED` — supplied evidence materially contradicts the stated claim.
- `STALE` — the evidence may no longer represent the current population,
  measurement method, or operating conditions.
- `SUPERSEDED` — a newer identified lesson replaces it; preserve the link and
  reason.

## Evaluation method

1. Separate raw facts from derived metrics, correlations, causal hypotheses,
   experiment results, and proposed policy implications.
2. Check metric definitions, missingness, sample-size concerns, selection,
   censoring, seasonality, channel changes, change points, and known confounders.
3. Enforce no-future-leakage: a historical decision may use only information
   available before its stated cutoff. State the cutoff, forecast/decision rule,
   and outcome horizon.
4. Interpret trajectory and change points as evidence within the supplied data,
   not as proof of cause.
5. Express policy validation as a recommendation for a separately controlled
   decision process. Never activate, modify, or tune a policy from this skill.

## Output contract

Return a ledger update or review with the decision question, input coverage,
facts, hypotheses, state transitions with evidence, causal/confounding limits,
leakage checks, trajectory interpretation, and conditional next measurement or
experiment. State whether a lesson is unusable, stale, or superseded rather than
silently carrying it into a recommendation.

## Non-authority and CORE boundary

This skill must not activate policies automatically; call YouTube APIs; execute
DoWhy, PyWhy, MABWiser, River, ruptures, MLflow, Evidently, Grafana, or other
analytics technologies; modify dashboards; write production state; or launch
experiments. These remain separately controlled production technologies and
processes.

It cannot weaken QA, integrity, rights/provenance, or safety gates. It does not
replace CORE evidence policy, source grounding, architecture decisions, security
review, or independent challenge. Those skills/processes are used only through
their explicit activation boundaries.
