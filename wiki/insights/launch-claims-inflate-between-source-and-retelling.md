---
type: Insight
title: "Scope words and multipliers inflate between a vendor's text and its retellings"
description: "In three checked cases, a retelling claimed more than the primary source: Duet's scope, xerj's 40x, and a 1/83 cost claim. Check scope words and multipliers against the first-hand text before quoting."
tags: [verification, vendor-claims, fact-check]
status: draft
confidence: medium-low
issues: [62, 49, 10, 7]
generated: { by: reference_agent/claude-sonnet-5-5, at: 2026-10-24T08:40:57+08:00 }
sources:
  - { id: duet, resource: https://claude.com/blog/claude-duet, title: "Introducing Claude Duet", author: "team:anthropic" }
  - { id: xerj, resource: https://xerj.org/case-studies/reference-coding.html, title: "xerj reference-coding case study" }
---

# Claim

When a product claim is retold, it grows in a predictable direction: wider platform, more continuous, more enterprise, bigger multiplier. Three cases in this tracker show it, and each was caught only by reading the first-hand text.

# Evidence

| Case | Retelling said | First-hand text said | Strength |
| --- | --- | --- | --- |
| [#62](../issues/62-add-a-verified-scope-table-for-claude-duet-to-the-wiki.md) Claude Duet | "cloud and desktop agent", "continuously monitors", "enterprise tools" | iOS, Android and web; a morning brief plus checks every few hours; US Pro and Max waitlist, Team and Enterprise excluded.[^duet] | Three of five claims wrong. The VentureBeat source was not found. |
| [#10](../issues/10-xerj-local-retrieval-layer-test-whether-it-saves-coding.md) xerj | "40x fewer tokens than grep" | The project's own case study reports 2.7x.[^xerj] | Both numbers sit in the same README, so the gap is checkable. |
| [#7](../issues/07-deepseek-flash-1017-deepseek-harness-minimal-comparison.md) DeepSeek Flash | "1/83 the cost for Opus 5-level" (second-hand post) | Not in the official changelog; marked unverified in the issue. | Single second-hand claim, no first-hand number. |

[#49](../issues/49-deep-read-anthropic-claude-duet-the-approval-gates-and-s.md) holds the corrected Duet facts, and the concept page [Claude Duet verified scope](../concepts/claude-duet-verified-scope.md) holds the table and image.

# So what

- Treat these as tell words: *continuous, always-on, enterprise, desktop, 10x, 40x*. When one appears in a retelling, find the sentence in the first-hand text that supports it before quoting.
- Cost of the check in the Duet case: one search plus the vendor post, about 15 minutes.
- Mark any number you could not trace as "unverified" in the issue. Issues #7 and #10 already do this.
- Added to the intake doc as a triage step (see below).

# What would change my mind

- A base rate: if a sample of retellings from other vendors matches their sources, the three cases are a coincidence of what I chose to check.
- A retelling that understates a vendor's claim. I have not seen one here, but I also did not look for them.

# Gaps

- Sample is three cases that I picked because they looked off. There is no base rate.
- The Duet check used launch coverage, not a full read of the Anthropic post. Which outlet states each fact was not recorded.

[^duet]: Introducing Claude Duet, Anthropic, 2026-10-21; launch coverage agrees (MacRumors, Thurrott, iPhone in Canada).
[^xerj]: xerj README and case study as read in issue [#10](../issues/10-xerj-local-retrieval-layer-test-whether-it-saves-coding.md).
