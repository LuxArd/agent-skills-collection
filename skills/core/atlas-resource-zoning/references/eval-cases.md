# Evaluation Cases

Use these cases when creating or materially changing the skill. Evaluate decisions, not exact wording.

## Pass criteria

A result passes when it:

- separates base model from reasoning effort;
- does not recommend an unavailable combination as confirmed;
- avoids both over-routing and under-routing;
- justifies Max, Pro-quality, or Ultra specifically;
- treats Ultra as surface-dependent and never assumes a fixed number of agents;
- preserves the `Aștept: GO` gate for substantive work and skips it for trivial requests;
- gives a compact recommendation and one fallback when availability is uncertain.

## Cases

| ID | Scenario | Expected route | Must avoid |
|---|---|---|---|
| E01 | Translate a two-sentence email | Direct answer; no zoning gate | Any `Aștept: GO` interruption |
| E02 | Rename one deterministic key in 50 files with tests | Luna Medium or Terra Low/Medium | Sol based only on file count |
| E03 | Extract fields from 200 uniform records | Luna Low/Medium | Terra/Sol prestige routing |
| E04 | Implement a normal multi-file feature with clear tests | Terra Medium | Sol Max by default |
| E05 | Debug a reproducible ordinary bug | Terra Medium/High | Ultra or Pro without evidence |
| E06 | Diagnose an intermittent cross-system bug after competent attempts failed | Sol High/XHigh | Luna loop; Max without additional justification |
| E07 | Choose an irreversible architecture with conflicting evidence | Sol XHigh or Max with explicit reason | Terra Low; vague "task is important" justification |
| E08 | Make a tiny security-sensitive production setting decision | Sol High/XHigh | Routing low because the diff is one line |
| E09 | Sol solved the root cause; remaining work is repetitive implementation and tests | De-escalate to Terra/Luna when practical | Sticky Sol Max |
| E10 | Difficult investigation with three independent hypotheses | Ultra/multi-agent only if runtime supports it | Fixed agent count; Ultra when work is sequential |
| E11 | Plus standard Chat request ideally needing Extra High | Recommend closest confirmed option, normally High, and state limitation | Claim Extra High is available |
| E12 | Pro account doing routine formatting | Direct answer or the lightest ordinary option exposed by the surface | Pro-quality merely because subscription is Pro |

## Release check

Before releasing a material routing change, run the cases above against the active runtime and record the result in that release's own notes. Do not present an internal smoke run, a local account observation, or a historical pass as proof that another account or future runtime exposes the same capabilities.

Release threshold: all availability and safety cases pass, with no material over-routing or under-routing.
