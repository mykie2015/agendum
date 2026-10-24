---
type: Agendum Action
title: "Try Archify in 1–2h: render a project/plan into an inspectable interactive diagram"
description: "Worth a real 1–2 hour test."
resource: https://github.com/mykie2015/agendum/issues/60
tags: [experiment, p1, ai, agent, opensource]
status: draft
issue: 60
action_type: experiment
priority: p1
state: open
created: 2026-10-23
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:41:17+08:00 }
sources:
  - { id: s1, resource: https://github.com/tt-a1i/archify }
  - { id: s2, resource: https://archify.si }
  - { id: s3, resource: https://github.com/ruanyf/weekly/blob/master/docs/issue-416.md }
---

# Decision

Worth a real 1–2 hour test. Archify (tt-a1i/archify) is an Agent Skill for Claude Code / Codex / Cursor and others: from natural language or repo evidence it generates a self-contained interactive HTML diagram (architecture/sequence/workflow, etc.) or a "conclusion-first" one-page answer, with validate→deliver→check. About 87K★ (checked via the GitHub API on 2026-10-23), so it is not a <200★ shell. It links back to md2wechat / content visualization / Agent Skills (#58); under Experiment before Build, get one run working first and then decide whether to bring it into daily use.

# Summary

A high-star Agent Skill built for inspectable diagrams and one-page answers. Run it for 1–2 hours on a real plan or repo of mine, then decide whether it stays in the toolbox.

# Limits

Not actually run on this machine; the site's example numbers carry an "illustrative" disclaimer; requires my own Node and agent file permissions

# Next steps

- [ ] Install it into my usual agent (Claude Code or Codex) using the site's command
- [ ] Output A: draw an architecture/workflow diagram for md2wechat or Agendum
- [ ] Output B: use the "one-page answer" to answer a real question (such as a release risk)
- [ ] Record: install friction, whether validation catches a bad diagram, and whether it is worth weekly use

# Sources

- https://github.com/tt-a1i/archify
- https://archify.si
- https://github.com/ruanyf/weekly/blob/master/docs/issue-416.md

# Tracking

[Issue #60](https://github.com/mykie2015/agendum/issues/60) · EXPERIMENT · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [opensource](../topics/opensource.md)
