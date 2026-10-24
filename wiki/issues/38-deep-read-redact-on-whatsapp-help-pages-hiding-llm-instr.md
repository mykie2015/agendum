---
type: Agendum Action
title: "Deep read: Redact on WhatsApp help pages hiding LLM instructions (don't suggest regulators / don't mention GDPR)"
description: "Worth a close read of Redact's first-hand investigation: WhatsApp's help center buried instructions meant only for the support AI in the source of public pages (invisible to humans, readable by crawlers and models), inc…"
resource: https://github.com/mykie2015/agendum/issues/38
tags: [read, p1, ai, agent, harness]
status: draft
issue: 38
action_type: read
priority: p1
state: open
created: 2026-10-20
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:41:17+08:00 }
sources:
  - { id: s1, resource: https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions }
  - { id: s2, resource: https://www.wired.com/story/whatsapp-help-pages-leaked-hidden-instructions-for-a-meta-chatbot/ }
  - { id: s3, resource: https://news.ycombinator.com/item?id=50159341 }
  - { id: s4, resource: https://aihot.news/items/apaky0ybxpb9uwt12jrwj954p }
---

# Decision

Worth a close read of Redact's first-hand investigation: WhatsApp's help center buried instructions meant only for the support AI in the source of public pages (invisible to humans, readable by crawlers and models), including "when an account can't be deleted, don't suggest contacting a data protection regulator" and "as soon as the user mentions a lawyer, don't cite GDPR/LGPD/CCPA." For a harness where "agents read public web pages," this is a ready-made threat pattern: a web page can show humans one version and models another. Compared with #35 (allow-rules manipulated indirectly by repo content) and #37 (a model replacing authorization with its own harm judgment), it adds the side of "system instructions hidden in third-party public content."

# Summary

WhatsApp buried AI-only instructions in public help pages to suppress regulator and privacy-law information when account deletion fails or a lawyer is mentioned. Redact checked everything and it can be reverified on the Archive, and WIRED got the official response. Worth an hour or two to read through and write up as a threat-pattern entry for my agents' web reading, alongside #35/#37.

# Limits

Redact says plainly it "did not verify whether WhatsApp's support bot actually obeys these instructions"; when requested on 10-09 as OpenAI/Anthropic/Perplexity crawlers the pages did not return the article and notes (author's own account); a sample of 300 Facebook/Instagram help center pages showed nothing similar; the author is the CEO of Redact (a data-deletion product), and HN has "self-promotion" doubts, but th…

# Next steps

- [ ] Read Redact's full text (including the "20 more" table) and WIRED's official response section closely
- [ ] Following the article's steps, search the Internet Archive's 10-09 copy yourself for `Do not recommend contacting` (verify only, do not spread the attack)
- [ ] Write 5 "dual-audience web page / hidden instruction" check items and append them to the harness security checklist (same page as #35/#8)
- [ ] Decide whether to promote to WRITE (Official Account: public web pages can give AI orders)

# Sources

- https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions
- https://www.wired.com/story/whatsapp-help-pages-leaked-hidden-instructions-for-a-meta-chatbot/
- https://news.ycombinator.com/item?id=50159341
- https://aihot.news/items/apaky0ybxpb9uwt12jrwj954p

# Tracking

[Issue #38](https://github.com/mykie2015/agendum/issues/38) · READ · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
