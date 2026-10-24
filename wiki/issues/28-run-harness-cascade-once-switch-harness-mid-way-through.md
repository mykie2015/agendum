---
type: Agendum Action
title: "Run Harness Cascade once: switch harness mid-way through the same bug, compare cost and result"
description: "Worth a small experiment."
resource: https://github.com/mykie2015/agendum/issues/28
tags: [experiment, p1, ai, agent, harness]
status: draft
issue: 28
action_type: experiment
priority: p1
state: open
created: 2026-10-20
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:47:18+08:00 }
sources:
  - { id: s1, resource: https://ykwon0407.github.io/posts/harness-cascade/ }
  - { id: s2, resource: https://github.com/ykwon0407/harness-cascade }
  - { id: s3, resource: https://x.com/ykwon_0407/status/2112258805149147293 }
  - { id: s4, resource: https://x.com/james_y_zou/status/2112316421053268035 }
---

# Decision

Worth a small experiment. James Zou's Stanford group open-sourced Harness Cascade: on the same task, one harness runs the first N turns, writes a handoff summary, and another harness continues in the same workspace. Paper-level data shows that switching harnesses can cut cost and raise accuracy at the same time, using exactly the DeepSeek V4.1 Flash from #7. Running "solo vs handoff" once on a small bug of your own answers "should my daily coding agent be fixed to one?" better than reading more harness articles.

# Summary

Switching harnesses is not mysticism: a short summary replacing a long history saves money, and a second pair of eyes checking against the files catches errors. Treat the accuracy gain with care; the cost gain is steadier. Running solo vs handoff once on a real small bug is enough to decide whether to write "periodic handoff / restart" into your own coding-agent habits.

# Used in insights

* [Where harness changes do raise accuracy, the mechanism is an independent check against real state](../insights/accuracy-gains-come-from-an-independent-second-look.md)
* [At a strong base model, the harness is mostly a cost lever, not an accuracy lever](../insights/harness-is-a-cost-lever-at-a-strong-base.md)

# Limits

The authors themselves caution that accuracy gains should be treated carefully: on DeepSeek, 16 handoff pairs averaged 2.4 points above running the ending harness alone (p=0.007), while on GLM and DeepSWE accuracy is within noise; cost differences are mostly significant. Claude Code uses --bare mode. Only Terminal-Bench 2.1 and DeepSWE 1.1 were tested, with the switch fixed at turn 5.

# Next steps

- [ ] Install per the README (uv tool install), look at the plan with --dry-run first; prepare a small bug in your own repo or a public small Terminal-Bench task
- [ ] Run 3 configurations: solo A, solo B, A → B (--switch-after 5), with DeepSeek V4.1 Flash (shared with #7)
- [ ] Record per configuration: whether it was fixed, total tokens, cost, time, whether the handoff note had errors, whether the second harness corrected them
- [ ] Write the conclusion into a #7 comment and decide whether to make "restart at turn N + handoff note" a personal rule

# Updates

- Imported comment from the upstream issue (2026-10-22), translated into English.
- Imported comment from the upstream issue (2026-10-23), translated into English.

# Sources

- https://ykwon0407.github.io/posts/harness-cascade/
- https://github.com/ykwon0407/harness-cascade
- https://x.com/ykwon_0407/status/2112258805149147293
- https://x.com/james_y_zou/status/2112316421053268035

# Tracking

[Issue #28](https://github.com/mykie2015/agendum/issues/28) · EXPERIMENT · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
