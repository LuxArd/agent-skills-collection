# Routing Policy

Use this reference only for complex, ambiguous, or disputed zoning decisions. Ordinary recommendations should follow `SKILL.md` directly.

## Durable objective

Select the minimum sufficient intelligence, reasoning depth, context, quality mode, and agentic execution required for a reliable result. Optimize the expected total resource cost of successful completion, including retries, context rereads, verification, and recovery from errors.

Correctness takes priority over economy when a failure would be expensive, difficult to reverse, security-sensitive, or hard to detect. Economy takes priority when the work is deterministic and verification is strong.

## Common routing errors

- **Tank for a rabbit:** frontier capability for routine deterministic work.
- **Cheap-model loop:** repeating weak attempts instead of selecting a sufficient model.
- **Prestige routing:** selecting the strongest configuration because a project feels important.
- **Complexity inflation:** confusing file count, prompt length, or urgency with intellectual difficulty.
- **Sticky escalation:** keeping an expensive configuration after the difficult part is solved.
- **Maximum by default:** recommending XHigh or Max without a task-specific reason.
- **Parallelism by prestige:** using agents that duplicate one another instead of dividing real workstreams.
- **Plan or surface blindness:** assuming Chat, Work, Codex, and API expose identical controls.
- **Availability invention:** recommending a model/effort combination not observed or documented.
- **Fuel panic:** reducing critical correctness merely because an allowance is low.

## Escalation

Escalation must address observed evidence:

| Evidence | Matching response |
|---|---|
| Reasoning is shallow but base capability is adequate | Increase reasoning effort |
| Task requires capabilities the current tier cannot provide reliably | Luna → Terra or Terra → Sol |
| Difficult single-answer quality remains inadequate | Consider Pro-quality if supported |
| Independent investigations dominate | Consider parallel/multi-agent execution |
| Context is missing or noisy | Narrow or improve context before adding compute |
| Verification fails | Diagnose the failed assumption; do not blindly repeat |

Do not follow a fixed ladder. `Terra High → Sol High` may be correct for insufficient capability; `Terra Medium → Terra High` may be correct when only deliberation is insufficient.

## De-escalation

After architecture, root cause, or critical synthesis is resolved, reconsider the remaining task. Mechanical implementation, repetitive changes, compilation, and routine checks often belong on Terra or Luna. Do not require a manual switch for tiny remaining work when the interruption would cost more than it saves.

## Verification and context

Strong deterministic verification permits a less expensive route. Weak verification, irreversible decisions, and latent failure modes justify more conservative routing.

Use bounded context:

- reuse validated checkpoints;
- inspect the relevant files and dependencies first;
- avoid rereading an entire repository without a direct reason;
- avoid giving parallel workers identical context and identical questions;
- expand scope only when evidence establishes a dependency.

## User control

The user owns the final model, reasoning, speed/cost preference, and risk tolerance. Warn concisely when a chosen configuration is clearly excessive or insufficient. Preserve an explicit selection unless it is unavailable; if it is likely insufficient for critical work, explain the risk and propose the smallest adequate alternative.
