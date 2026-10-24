---
type: Agendum Action
title: "Test whether a handoff turns a suggestion into an approval: can permissions really be revoked"
description: "Worth a small experiment."
resource: https://github.com/mykie2015/agendum/issues/17
tags: [experiment, p1, ai, agent, harness]
status: draft
issue: 17
action_type: experiment
priority: p1
state: open
created: 2026-10-19
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:34:53+08:00 }
sources:
  - { id: s1, resource: https://swarmcha.se/posts/chinese-agent-fleet-full-report }
  - { id: s2, resource: https://natesnewsletter.substack.com/p/ai-agent-swarms }
  - { id: s3, resource: https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf }
  - { id: s4, resource: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ }
---

# Decision

Worth a small experiment. Field deployments and incident reports all say the same thing: an agent treats a peer's or a web page's "you can continue" as authorization, and judgment must be revocable. This is on the same axis as #13 (the authorization boundary when an agent spends money); this slot adds a method layer with three locally reproducible probes and does not expand into a long security piece.

# Insight

Not another chase of a security news item, but three local probes to verify whether existing agents treat a handoff note as an approval and whether they truly stop after revocation. Results go into rules; an X post can hang off #13, without a separate hype post.

# Limits

Nate's full prompt kit was not read (paywalled); Tencent has not responded publicly (the report cites background sources saying the evaluation has ended); some agents claim to be Claude/Claude Code, and the report uses stylometry to question that identity; this experiment tests only the local harness and does not reproduce field attacks

# Next steps

- [ ] Design 3 probes (capability boundary / does peer approval escalate / does it stop after revocation) and run them in an environment with no real payments and no destructive writes
- [ ] Record: does the tool refuse, does it require human confirmation, does it silently continue
- [ ] Write passing items into the digital-employee preferences; open follow-up actions for failing items or fold them into #13

# Updates

- Imported comment from the upstream issue (2026-10-21), translated into English.
- Imported comment from the upstream issue (2026-10-21), translated into English.

# Sources

- https://swarmcha.se/posts/chinese-agent-fleet-full-report
- https://natesnewsletter.substack.com/p/ai-agent-swarms
- https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf
- https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/

# Tracking

[Issue #17](https://github.com/mykie2015/agendum/issues/17) · EXPERIMENT · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
