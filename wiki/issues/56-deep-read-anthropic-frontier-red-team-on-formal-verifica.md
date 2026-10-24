---
type: Agendum Action
title: "Deep read: Anthropic Frontier Red Team on formal verification of 123 OSS libraries at scale with LLMs"
description: "Worth a close read."
resource: https://github.com/mykie2015/agendum/issues/56
tags: [read, p1, ai, agent]
status: draft
issue: 56
action_type: read
priority: p1
state: open
created: 2026-10-23
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:34:53+08:00 }
sources:
  - { id: s1, resource: https://www.anthropic.com/research/formal-verification }
  - { id: s2, resource: https://x.com/AnthropicAI/status/2113390212911083894 }
  - { id: s3, resource: https://aihot.news/items/jsr18rtgxl0kvb0k7np7lpyou }
---

# Decision

Worth a close read. First-hand research from Anthropic's Frontier Red Team (2026-10-22): working with Theorem, Claude wrote Rocq proofs at the RISC-V assembly level for 239 entry points across 123 OSS-Fuzz libraries (about 180 million lines), proving that under the stated assumptions no input under 64MB crashes the program; along the way it found bugs that had escaped for years (including a large-input OOB and a rediscovery of a libexpat CVE). Under the #15/#37 rule it is an OpenAI/Anthropic first-hand security and engineering methods long post and gets priority, not counted against the daily harness cap.

# Insight

A first-hand Anthropic security/engineering long post. After the close read, produce a method-boundary note and decide whether to follow a single-entry-point trial run or only watch the skill.

# Limits

Most deployments are x86/ARM+glibc; ASan ≠ all memory bugs; entry points ≠ the whole library; caller misuse is not covered; reward-hacking risk (patch audit).

# Next steps

- [ ] Read the original and appendix closely and excerpt the "fuzz → spec → proof" steps and the limits
- [ ] Note the Theorem Claude skill / the entry for the public proof release
- [ ] Link #50 / #45 in a comment
- [ ] Decide whether it is worth turning into content (a suggestion only, no posting)

# Updates

- Imported comment from the upstream issue (2026-10-23), translated into English.

# Sources

- https://www.anthropic.com/research/formal-verification
- https://x.com/AnthropicAI/status/2113390212911083894
- https://aihot.news/items/jsr18rtgxl0kvb0k7np7lpyou

# Tracking

[Issue #56](https://github.com/mykie2015/agendum/issues/56) · READ · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md)
