# Victor Buret — Agent Skills Collection

A curated, reviewed collection of 14 reusable Agent Skills for disciplined engineering work, evidence-based review, and bounded media-intelligence workflows.

These skills are designed to be installed selectively. **Fourteen available skills do not mean fourteen skills active at once.** Permanent core skills establish baseline reasoning discipline; on-demand skills are used only when their specialised capability is relevant.

## Skill catalogue

| Skill | Category | Invocation | Purpose | License / provenance |
| --- | --- | --- | --- | --- |
| [adr](skills/core/adr/) | Permanent core | When a durable technical decision is needed | Record consequential architecture decisions | Apache-2.0; adapted from Vercel |
| [specification-and-planning](skills/core/specification-and-planning/) | Permanent core | For significant or unclear change | Create an evidence-aware specification and plan | MIT; merged from Addy Osmani sources |
| [source-grounding](skills/core/source-grounding/) | Permanent core | For version-sensitive external facts | Ground decisions in authoritative sources | MIT; adapted from Addy Osmani |
| [engineering-evidence-policy](skills/core/engineering-evidence-policy/) | Permanent core | For substantive engineering work | Apply truth, scope, authority, and verification discipline | Apache-2.0; locally authored |
| [code-review](skills/core/code-review/) | On-demand core | Before accepting a code change | Review correctness, maintainability, and evidence | MIT; adapted from Addy Osmani |
| [security-review](skills/core/security-review/) | On-demand core | For a scoped security review | Perform a focused read-only security assessment | Apache-2.0 / CC BY-SA 4.0 components |
| [doubt-driven-review](skills/core/doubt-driven-review/) | On-demand core | For consequential uncertainty | Run a bounded adversarial challenge | MIT; adapted from Addy Osmani |
| [skill-intake-review](skills/core/skill-intake-review/) | On-demand core | Before deciding whether to install a skill | Perform a read-only static intake review | Apache-2.0; locally authored |
| [trend-opportunity-analysis](skills/media-intelligence/trend-opportunity-analysis/) | On-demand Media Intelligence | For supplied trend evidence | Interpret bounded trend signals | Apache-2.0; locally authored |
| [media-discovery-provenance](skills/media-intelligence/media-discovery-provenance/) | On-demand Media Intelligence | For media-source evidence | Evaluate media provenance and rights records | Apache-2.0; locally authored |
| [visual-media-evidence](skills/media-intelligence/visual-media-evidence/) | On-demand Media Intelligence | For identified media or renders | Record descriptive visual evidence | Apache-2.0; locally authored |
| [edit-decision-planning](skills/media-intelligence/edit-decision-planning/) | On-demand Media Intelligence | For approved story and asset packages | Create a declarative edit plan | Apache-2.0; locally authored |
| [video-qa-gate](skills/media-intelligence/video-qa-gate/) | On-demand Media Intelligence | For an immutable render | Issue an independent QA gate verdict | Apache-2.0; locally authored |
| [performance-learning-evaluation](skills/media-intelligence/performance-learning-evaluation/) | On-demand Media Intelligence | For supplied performance data | Evaluate hypotheses and learning evidence | Apache-2.0; locally authored |

## Choose the smallest useful skill

- Architecture decision → `adr`
- Specification or implementation plan → `specification-and-planning`
- Current vendor, framework, or standards fact → `source-grounding`
- Engineering evidence and authority boundary → `engineering-evidence-policy`
- Code change review → `code-review`
- Security review → `security-review`
- Fresh adversarial challenge → `doubt-driven-review`
- Third-party skill intake → `skill-intake-review`
- Trend, media, edit, video QA, or learning evaluation → choose the matching Media Intelligence skill

## Install and reuse

See [INSTALLATION.md](INSTALLATION.md) for selective installation and [SKILLS_INDEX.md](SKILLS_INDEX.md) for concise usage guidance.

## Licensing and provenance

This is a component-aware collection. The root [LICENSE](LICENSE) applies to Victor-authored repository content; it does **not** override component licenses. Read [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and the complete [provenance manifest](manifests/provenance-manifest.md) before redistributing or modifying a third-party-derived component.

## Scope

The repository contains reusable skills and their required supporting materials only. It does not include private project architecture, workflows, credentials, client data, logs, or internal audit packs.
