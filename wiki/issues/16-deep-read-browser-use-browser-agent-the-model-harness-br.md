---
type: Agendum Action
title: "Deep read: Browser Use \"Browser Agent\": the Model / Harness / Browser trio and failure modes"
description: "Worth reading."
resource: https://github.com/mykie2015/agendum/issues/16
tags: [read, p1, ai, agent, harness]
status: draft
issue: 16
action_type: read
priority: p1
state: open
created: 2026-10-19
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:47:18+08:00 }
sources:
  - { id: s1, resource: https://browser-use.com/posts/browser-agents }
  - { id: s2, resource: https://aihot.news/items/w3vpc68lufgj57zcy1hd38a60 }
---

# Decision

Worth reading. Browser Use uses first-hand cloud usage data to split a browser agent into three parts, model, harness, and browser, and gives selection boundaries among API / script / agent. It forms an "application layer" counterpart to the minimal harness (#14) and Harness² (#12), and directly serves the Agent + Computer Use main line.

# Summary

Browser Use turns computer use from a slogan into a comparable trio plus a failure list. After reading, produce a one-page guardrail rather than rushing to hook up a cloud agent. Compared with #12/#14: those edit harness files; this one defines where the browser session sits in the harness.

# Limits

Usage data is a vendor-reported snapshot, not an independent audit; success rates and cost distributions are not given; "Browser Harness gives a coding agent a browser" is a product path and needs comparison with a self-built Playwright/MCP setup before any experiment

# Next steps

- [ ] Read the full text and excerpt the "trio / selection triangle / five failure types / starter checklist" into a one-page note
- [ ] Compare with #14 (minimal coding agent) and #12 Harness²: does the browser session count as a ninth knob?
- [ ] Decide whether to run a read-only price-extraction experiment on Grok Bot (open a separate EXPERIMENT; this issue does not expand scope)

# Updates

- Imported comment from the upstream issue (2026-10-21), translated into English.
- Imported comment from the upstream issue (2026-10-21), translated into English.

# Sources

- https://browser-use.com/posts/browser-agents
- https://aihot.news/items/w3vpc68lufgj57zcy1hd38a60

# Tracking

[Issue #16](https://github.com/mykie2015/agendum/issues/16) · READ · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
