---
type: Agendum Action
title: "Coding-agent credential self-check after the OpenCode Console leak"
description: "Worth an immediate XS self-check: do the coding agents on this machine or in the cloud (OpenCode Console, Claude Code, Codex, Cursor, etc.) still store plaintext API keys that a third-party console could reuse, and are…"
resource: https://github.com/mykie2015/agendum/issues/8
tags: [experiment, p1, ai, agent]
status: draft
issue: 8
action_type: experiment
priority: p1
state: open
created: 2026-10-18
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:34:53+08:00 }
sources:
  - { id: s1, resource: https://x.com/opencode/status/2111519637049319818 }
  - { id: s2, resource: https://x.com/lydiahallie/status/2111563956666110287 }
  - { id: s3, resource: https://aihot.news/story/c3562486-19f9-44c5-9544-c3af3e3d43c5 }
---

# Decision

Worth an immediate XS self-check: do the coding agents on this machine or in the cloud (OpenCode Console, Claude Code, Codex, Cursor, etc.) still store plaintext API keys that a third-party console could reuse, and are usage caps set? OpenCode officially admitted that a subset of Console leaked and is remediating with Anthropic/OpenAI/Google; Anthropic has said it revoked Claude keys believed affected. Details are not public, but the "credential boundary" is enough to make a closable small experiment.

# Insight

The incident details are not complete, but the credential boundary is enough for a 30-minute self-check experiment. When done it should leave a reusable checklist, not stop at forwarding the official post.

# Limits

The attack surface, whether it was distillation, and where the traffic went are all undisclosed; community bill figures such as "$1700 overnight" are unverified; no equivalent first-hand post was seen on whether OpenAI/Google revoked keys the same way (this issue does not claim it)

# Next steps

- [ ] Check your email for an OpenCode notification; if there is one, rotate the keys it lists
- [ ] List the coding agents in use on this machine and where their keys come from (OpenCode Console / environment variables / system keychain / each CLI's auth file)
- [ ] For any Anthropic/OpenAI/Google key ever written into a third-party Console: revoke and recreate; set a separate key per tool plus daily/monthly usage caps
- [ ] Write 5 "credential boundary" rules into the personal agent SOP (no production keys in third-party consoles, least privilege, alerts on abnormal bills, etc.)

# Updates

- Imported comment from the upstream issue (2026-10-19), translated into English.
- Imported comment from the upstream issue (2026-10-22), translated into English.

# Sources

- https://x.com/opencode/status/2111519637049319818
- https://x.com/lydiahallie/status/2111563956666110287
- https://aihot.news/story/c3562486-19f9-44c5-9544-c3af3e3d43c5

# Tracking

[Issue #8](https://github.com/mykie2015/agendum/issues/8) · EXPERIMENT · P1 · XS · under 30 minutes · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md)
