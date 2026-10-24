---
type: Agendum Action
title: "Deep read: Anthropic OSS Scanner, 29K candidate vulnerabilities with only 6,000 human-reviewed, unreviewed reports sent straight to maintainers + threat_model.md"
description: "Worth reading."
resource: https://github.com/mykie2015/agendum/issues/41
tags: [read, p1, ai, agent, opensource]
status: draft
issue: 41
action_type: read
priority: p1
state: open
created: 2026-10-20
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:41:17+08:00 }
sources:
  - { id: s1, resource: https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source }
  - { id: s2, resource: https://red.anthropic.com/oss-scanner/ }
  - { id: s3, resource: https://github.com/anthropics/oss-scanner }
  - { id: s4, resource: https://x.com/ClaudeDevs/status/2112299602510749992 }
---

# Decision

Worth reading. Anthropic's Frontier Red Team published a set of numbers: in six months models found over 29,000 candidate vulnerabilities, and humans finished reviewing only about 6,000. Their answer is to let qualifying open-source projects opt in to a fast path of "take model reports directly without human review," and let maintainers use a `threat_model.md` file to tell the scanning agent what to test and what counts as severe. The bottleneck moved from "can we find them" to "can humans review them all," the security version of the same thing as #20 (AI agents push the bottleneck to code review) and a continuation of the model-company first-hand disclosures like #37.

# Summary

Models find vulnerabilities accurately enough that Anthropic is stuck on human review, so it lets maintainers choose to take unreviewed reports directly and steers the scanning agent with threat_model.md. What is worth reading is the numbers and the governance design; what is worth borrowing is the threat_model.md format; it can also be combined with #20 into one piece on "the bottleneck in the AI era is verification."

# Used in insights

* [Verification, not generation, is now the bottleneck, and vendors answer by moving the review](../insights/verification-is-the-bottleneck-not-generation.md)

# Limits

The 88% qualifying rate comes only from 97 high/critical findings across 48 projects, a sample Anthropic chose itself; maintainer feedback mentions severity sometimes being too high and the scanner sometimes misreading a project's threat model; fast-path reports are not human-reviewed and Anthropic says plainly there may be false positives; eligibility follows OSS-Fuzz and new projects are usually not accepted, and…

# Next steps

- [ ] Read the full blog and FAQ (links in the evidence chain), focusing on the numbers and the threat model sections
- [ ] Decide whether it is worth writing a threat_model.md for md2wechat-skill or another repo of mine and then having a coding agent run an offline security review; if so, open a separate EXPERIMENT
- [ ] If writing content, merge it with #20 into one topic and leave a one-line viewpoint in this issue

# Updates

- Imported comment from the upstream issue (2026-10-21), translated into English.
- Imported comment from the upstream issue (2026-10-22), translated into English.

# Sources

- https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source
- https://red.anthropic.com/oss-scanner/
- https://github.com/anthropics/oss-scanner
- https://x.com/ClaudeDevs/status/2112299602510749992

# Tracking

[Issue #41](https://github.com/mykie2015/agendum/issues/41) · READ · P1 · XS · 30–45 minutes · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [opensource](../topics/opensource.md)
