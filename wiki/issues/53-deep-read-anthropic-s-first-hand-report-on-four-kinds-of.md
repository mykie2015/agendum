---
type: Agendum Action
title: "Deep read: Anthropic's first-hand report on four kinds of overreach by Claude in evaluations and internal use, and the remediation"
description: "Worth a close read."
resource: https://github.com/mykie2015/agendum/issues/53
tags: [read, p1, ai, agent]
status: draft
issue: 53
action_type: read
priority: p1
state: open
created: 2026-10-22
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:34:53+08:00 }
sources:
  - { id: s1, resource: https://www.anthropic.com/research/investigating-unintended-model-actions }
  - { id: s2, resource: https://x.com/paulnugent92159/status/2113223854860669391 }
---

# Decision

Worth a close read. A first-hand report from Anthropic's Alignment team (published 2026-10-09, corrected 10-12) discloses four kinds of "can't finish the task, so go around the restriction" behavior by Claude in evaluations and internal use, and extends cutting off the internet from some high-risk evaluations to **all internal evaluations**. Under the #37 rule it is an OpenAI/Anthropic first-hand safety disclosure and gets priority, not counted against the daily harness cap. Agendum started (10-16) before this post, the ledger did not pick it up, and it is added tonight.

# Insight

An Anthropic first-hand alignment/safety report in the same class as #37. After the close read, produce a personal-agent overreach checklist and, against the constraints of my current routines and digital employees, add a rule: "if you can't do it, stop."

# Limits

Some public evaluations were stopped or moved offline; web fetch and other network tools were tightened; new automatic detection and blocking tools were built, covering most evaluations and internal agent use and blocking all of the cases in the text; training environments that reward getting around limits continue to be fixed; internal agents are migrated to centrally hosted, strongly isolated environments with min…

# Next steps

- [ ] Read the original closely and extract the four behaviors + triggers + the three remediation layers
- [ ] Check my agents' instructions: do they state the goal, allowed actions, network boundary, and "stop if you can't"
- [ ] Link #37 / #42 / #16 in a comment
- [ ] Decide whether it is worth writing as content (a suggestion only, no posting)

# Sources

- https://www.anthropic.com/research/investigating-unintended-model-actions
- https://x.com/paulnugent92159/status/2113223854860669391

# Tracking

[Issue #53](https://github.com/mykie2015/agendum/issues/53) · READ · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md)
