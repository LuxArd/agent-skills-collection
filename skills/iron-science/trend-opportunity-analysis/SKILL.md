---
name: trend-opportunity-analysis
description: Interpret already-collected trend signals into an explainable opportunity analysis. Use only for an explicitly requested trend-analysis task with supplied observations, metric definitions, time windows, and channel context; it does not collect data or operate platforms.
---

# Trend Opportunity Analysis

Use this skill only when the task explicitly asks for a bounded interpretation
of supplied trend observations. It reasons about evidence; it does not collect,
alter, publish, or act on trend data.

## Activation boundary

This package is explicit-only. Begin only with a stated question, a bounded
observation window, supplied source/provenance context, metric definitions, and
a channel or audience context. If these are incomplete, identify the gap rather
than fabricating a baseline or confidence level.

## Required input contract

Establish, when applicable:

- The decision question and the affected channel, audience, or content format.
- Observation window, time zone, granularity, comparison baseline, and outcome
  horizon.
- Supplied source identifiers, collection dates, completeness limits, and known
  changes in measurement or ranking rules.
- Metric definitions, denominator, aggregation method, and material missing or
  censored data.
- The candidate topic, related topics, and an explicit comparator set.

Do not treat a platform metric, search result, ranking, or anecdote as a fact
outside the evidence supplied in the task.

## Evidence states

Label every material claim with exactly one appropriate state:

- `OBSERVED` — directly present in the supplied data or source record.
- `CORRELATED` — an association appears in the supplied observations without a
  causal identification claim.
- `HYPOTHESIS` — a testable explanation, forecast, or decision premise.
- `VALIDATED` — supported by a stated evaluation design, frozen cutoff, and
  reported result within its defined scope.
- `UNKNOWN` — not established by the supplied evidence.

`VALIDATED` is not a synonym for true, permanent, or causal. Do not upgrade a
claim solely because it has a plausible narrative.

## Interpret signals consistently

Explain the evidence and comparison used for each applicable signal:

- **Baseline:** the stated normal level for a comparable period or cohort.
- **Velocity:** change over a stated, comparable interval.
- **Acceleration:** change in velocity across equal or explicitly normalized
  intervals.
- **Burst:** a transient deviation relative to the stated baseline and window.
- **Weak signal:** a low-volume or early pattern whose reliability remains
  uncertain; state corroboration and selection bias risks.
- **Lifecycle:** the evidence for emergence, growth, maturity, decline, or an
  `UNKNOWN` stage.
- **Novelty and saturation:** distinguish new attention from an under-served
  need; explain the comparator and evidence limitations.
- **Remaining opportunity and content gap:** frame as a hypothesis unless the
  supplied evidence supports the relevant audience, supply, and outcome link.
- **Channel fit:** connect the stated audience and format evidence to the
  channel; do not infer fit from topic popularity alone.

State confidence separately from desirability. Confidence reflects evidence
quality, completeness, comparator quality, agreement across supplied sources,
and sensitivity to reasonable alternatives—not expected upside.

## Backtesting and leakage controls

When interpreting a past decision rule, record the historical cutoff, what was
known by that cutoff, the selection rule, the outcome window, and the relevant
comparator. Do not use later information to describe what a decision-maker
could have known. Report selection bias, survivorship bias, sparse samples,
unavailable counterfactuals, and metric-definition changes.

## Output contract

Return an explainable analysis containing:

1. Decision question, scope, supplied inputs, and material data limits.
2. Signal table: signal, evidence state, observation/comparator, interpretation,
   confidence, and caveat.
3. Opportunity hypotheses ranked only by stated criteria; do not present a rank
   as an instruction to publish or invest.
4. Backtesting interpretation when evidence supports it, including leakage and
   selection limitations.
5. Recommended next evidence or experiment, if any, with no automatic action.

## Non-authority and CORE boundary

This skill must not scrape, call YouTube, Google Trends, social, or other APIs;
authenticate; install dependencies; execute statistical software; publish; or
modify production state. It does not decide source rights, create edit plans,
run QA, render media, activate policies, or override any CORE skill.

Use the supplied evidence discipline for truth labels. Request source-grounding
only when an external, version-sensitive claim is necessary and explicitly in
scope. Architecture, security, and independent review remain the authority of
the relevant CORE skills and are never invoked silently by this package.
