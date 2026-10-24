---
type: Agendum Action
title: "Deep read: METR × Redwood embedded red team of OpenAI's internal agent monitoring"
description: "Worth a close read."
resource: https://github.com/mykie2015/agendum/issues/57
tags: [read, p1, ai, agent]
status: draft
issue: 57
action_type: read
priority: p1
state: open
created: 2026-10-23
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:47:18+08:00 }
sources:
  - { id: s1, resource: https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/ }
  - { id: s2, resource: https://blog.redwoodresearch.org/p/red-teaming-openais-internal-agent }
  - { id: s3, resource: https://www.redwoodresearch.org/blog/red-teaming-openais-internal-agent }
  - { id: s4, resource: https://x.com/METR_Evals/status/2113290966933389390 }
  - { id: s5, resource: https://aihot.news/items/fcw2s1pdclkgm5kmg2qwginp7 }
---

# Decision

Worth a close read. METR and Redwood Research ran a three-week, high-access embedded red team (2026-07-21→08-11) on OpenAI's internal misalignment monitoring system and published a high-level summary on 2026-10-22. It evaluates the system as of ≤2026-07-21, not today's production state. In the same cluster as #42 (the incident of OpenAI's own monitoring being suppressed) but from a different view: this is an external deep-access audit; it is the same type as #43 (METR reviewing Anthropic's risk report). Under the security-disclosure priority rule it gets its own READ and does not count against the daily harness cap.

# Summary

A first-hand external red-team summary by METR/Redwood, independent of #42. After the close read, produce a monitoring design checklist and attach comments to #42/#33/#26.

# Used in insights

* [A proactive agent is defined by where its approval boundary sits and what happens when it fails](../insights/proactive-agents-are-defined-by-their-approval-boundary.md)

# Limits

A snapshot of a historical system; public information is heavily compressed; some exploit details are redacted; it does not include all internal agent traffic sources.

# Next steps

- [ ] Read the METR post closely and extract the coverage numbers, the gaps, and the five design ideals
- [ ] Compare whether my agents' approval/observability meet "hard to bypass + books match reality"
- [ ] Link #42 / #33 / #26 in a comment
- [ ] Decide whether it is worth turning into content (a suggestion only, no posting)

# Sources

- https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/
- https://blog.redwoodresearch.org/p/red-teaming-openais-internal-agent
- https://www.redwoodresearch.org/blog/red-teaming-openais-internal-agent
- https://x.com/METR_Evals/status/2113290966933389390
- https://aihot.news/items/fcw2s1pdclkgm5kmg2qwginp7

# Tracking

[Issue #57](https://github.com/mykie2015/agendum/issues/57) · READ · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md)
