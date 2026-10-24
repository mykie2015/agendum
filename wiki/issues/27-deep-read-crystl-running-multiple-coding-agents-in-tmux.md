---
type: Agendum Action
title: "Deep read: crystl, running multiple coding agents in tmux, methods and ceiling"
description: "Worth a close read this week, pulling out a reusable operations checklist."
resource: https://github.com/mykie2015/agendum/issues/27
tags: [read, p1, ai, agent, harness]
status: draft
issue: 27
action_type: read
priority: p1
state: open
created: 2026-10-19
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:47:18+08:00 }
sources:
  - { id: s1, resource: https://crystl.dev/guides/tmux-for-ai-agents/ }
  - { id: s2, resource: https://news.ycombinator.com/item?id=50148855 }
---

# Decision

Worth a close read this week, pulling out a reusable operations checklist. This is a methods article that puts "multiple Claude Code / coding-agent sessions" onto tmux primitives: the built-in `--worktree --tmux` path, session/window naming, scripted `send-keys`/`capture-pane`, status-bar polling for monitoring, and it states the limits of tmux plainly (no agent state, brittle screen scraping, no cross-session sharing). It directly serves multi-session operation for Agent Harness / Coding Agent and is not just another hot post.

# Summary

Not chasing HN scores, but spending under two hours to get an operating boundary for "how to keep multiple coding agents running." After reading you should be able to say when `claude --tmux` is enough and when to stop using the screen-scraping hack.

# Limits

The author also sells crystl (a macOS multi-agent terminal); the methods section can be verified independently, while the product conclusions need your own judgment; the status-bar script was not reproduced locally

# Next steps

- [ ] Read the full text and put 8–12 commands into personal notes (including `--tmux=classic`, `send-keys -l`, `capture-pane -J`)
- [ ] If Claude Code is installed locally: run `claude --worktree demo --tmux=classic` once and record the differences from a hand-written session
- [ ] A three-line comparison: against #14 minimal harness / #16 Browser trio, does this article add the "human-machine parallel scene" or can it be ignored

# Sources

- https://crystl.dev/guides/tmux-for-ai-agents/
- https://news.ycombinator.com/item?id=50148855

# Tracking

[Issue #27](https://github.com/mykie2015/agendum/issues/27) · READ · P1 · S · 45–90 minutes · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
