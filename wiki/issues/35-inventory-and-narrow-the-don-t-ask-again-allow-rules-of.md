---
type: Agendum Action
title: "Inventory and narrow the \"don't ask again\" allow-rules of Claude Code / Codex"
description: "Worth a self-check right away: list every \"don't ask again\" allow-rule already approved in my Claude Code and Codex, and narrow or delete the ones that are too broad."
resource: https://github.com/mykie2015/agendum/issues/35
tags: [experiment, p1, ai, agent, harness]
status: stable
issue: 35
action_type: experiment
priority: p1
state: closed
created: 2026-10-20
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:47:18+08:00 }
sources:
  - { id: s1, resource: https://arxiv.org/abs/2610.22987 }
  - { id: s2, resource: https://ctxsec.com/context }
  - { id: s3, resource: https://x.com/misselvexu/status/2112348907376373900 }
---

# Decision

Worth a self-check right away: list every "don't ask again" allow-rule already approved in my Claude Code and Codex, and narrow or delete the ones that are too broad. The new paper From Approval to Abuse shows that a poisoned repository can, during a normal task, induce a coding agent to ask you for a rule that sounds reasonable but has a very wide actual scope; approve it once and malicious commands matching that rule no longer prompt. This hits exactly the gate of "judgment stays in human hands": a human in the loop only works if the human knows what they are approving.

# Summary

A coding agent's "don't ask again" is a long-lived authorization that repo content can manipulate indirectly. The cheapest defense is to inventory the existing rules now and from here on approve only single commands in other people's repos.

# Used in insights

* [A proactive agent is defined by where its approval boundary sits and what happens when it fails](../insights/proactive-agents-are-defined-by-their-approval-boundary.md)

# Limits

Only the abstract and the second-hand summary were read, not the full text; three points mentioned in the X post were not checked against the original: "0/25 without an attack," "Claude Sonnet 5 hardest to break at 9/25, 3/9," and "Anthropic data says 49.5% of active Claude Code CLI users have set a Bash allow-rule"; the experiments were done in an isolated synthetic environment with fake credentials; whether the au…

# Next steps

- [ ] List the project-level and user-level permissions allow rules of Claude Code on this machine (read-only, nothing leaves the machine)
- [ ] List the approval rules / trust settings saved by Codex CLI (read-only)
- [ ] Mark rules that contain wildcards or whole classes of commands (such as all of Bash, curl, package managers), and narrow or delete each one
- [ ] Write a personal rule: in unfamiliar repos approve only a single command and never click "don't ask again"
- [ ] Append the results to the progress log of #17 or #8

# Sources

- https://arxiv.org/abs/2610.22987
- https://ctxsec.com/context
- https://x.com/misselvexu/status/2112348907376373900

# Tracking

[Issue #35](https://github.com/mykie2015/agendum/issues/35) · EXPERIMENT · P1 · XS · 30–60 minutes · closed

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
