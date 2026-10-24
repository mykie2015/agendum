---
type: Agendum Action
title: "Deep read: Anthropic Claude Duet, the approval gates and safety stack of a proactive agent"
description: "Worth a close read."
resource: https://github.com/mykie2015/agendum/issues/49
tags: [read, p1, ai, agent, product]
status: draft
issue: 49
action_type: read
priority: p1
state: open
created: 2026-10-22
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:34:53+08:00 }
sources:
  - { id: s1, resource: https://claude.com/blog/claude-duet }
  - { id: s2, resource: https://aihot.news/items/jgg0i29t3o1eycc24c3wev0fx }
---

# Decision

Worth a close read. Anthropic's first-hand research preview of a proactive personal agent: it reaches out to you and keeps working in the background, but must wait for a human to approve before sending, paying, signing, or deleting. The safety stack is spelled out (trustworthy agents, Managed Agents credentials, the auto mode classifier, browser-use injection defense, a sensitive-information classifier). It ties directly to "judgment stays in human hands" and the personal AI / agent + computer-use main line; it is not a pure model drop.

# Insight

Not another chat shell, but a first-hand design post where Anthropic ships "act proactively + wait for human approval on key actions" as a research preview. Read it closely this week, extract the gate checklist, and compare with #44/#16/#17; don't rush to join the waitlist for a BUILD.

# Limits

Early research preview; the text says it may misread threads or misjudge urgency; it cannot yet show its browser; it is separate from the main Claude app; waitlist only, and this machine has not joined it; specific model names such as Opus 5.5 go by the page's wording at the time

# Next steps

- [ ] Read the Duet blog closely and list a three-column comparison table of "autonomous / needs approval / forbidden"
- [ ] Compare with the #44 shared-agent permission model and the #16 browser-use failure modes, and mark 5 rules that carry over to the digital employees
- [ ] Decide: whether to open a separate EXPERIMENT (default no, wait for more public safety detail)

# Updates

- Imported comment from the upstream issue (2026-10-22), translated into English.
- Imported comment from the upstream issue (2026-10-22), translated into English.
- Imported comment from the upstream issue (2026-10-22), translated into English.
- Imported comment from the upstream issue (2026-10-23), translated into English.
- Imported comment from the upstream issue (2026-10-23), translated into English.
- Fact check of a pasted Duet summary (2026-10-24)

# Sources

- https://claude.com/blog/claude-duet
- https://aihot.news/items/jgg0i29t3o1eycc24c3wev0fx

# Tracking

[Issue #49](https://github.com/mykie2015/agendum/issues/49) · READ · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [product](../topics/product.md)
