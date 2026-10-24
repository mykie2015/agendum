---
type: Agendum Action
title: "Deep read: Anthropic Frontier Red Team on reducing attack surface with Claude (three methods + the OpenSSH case)"
description: "Deep read: Anthropic Frontier Red Team on reducing attack surface with Claude (three methods + the OpenSSH case)"
resource: https://github.com/mykie2015/agendum/issues/45
tags: [read, p1, ai, agent, opensource]
status: draft
issue: 45
action_type: read
priority: p1
state: open
created: 2026-10-21
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:47:18+08:00 }
sources:
  - { id: s1, resource: https://www.anthropic.com/research/attack-surface-reduction }
---

# Decision

Deep read: Anthropic Frontier Red Team on reducing attack surface with Claude (three methods + the OpenSSH case)

# Summary

Anthropic demonstrated three attack-surface-reduction methods with Claude on 25 projects (493 findings), and used OpenSSH 10.4→10.6 to show it can be merged upstream. How to read it: extract the "default/interaction/early reachability" checklist and compare it with your own agent permissions and default tool surface; cross-reference details with #41, and do not open a parallel Scanner experiment.

# Limits

Anthropic's own narrative; the 493 findings do not have a fully public reproduction package; the engineering cost of applying the skill directly to a personal repo is not given.

# Next steps

- [ ] Read the three methods + OpenSSH and extract three check items that carry over to the default tool surface of a personal agent
- [ ] Compare with #41 and annotate the intersection points (do not expand a Scanner experiment in this one)

# Sources

- https://www.anthropic.com/research/attack-surface-reduction

# Tracking

[Issue #45](https://github.com/mykie2015/agendum/issues/45) · READ · P1 · S · 40–55 minutes · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [opensource](../topics/opensource.md)
