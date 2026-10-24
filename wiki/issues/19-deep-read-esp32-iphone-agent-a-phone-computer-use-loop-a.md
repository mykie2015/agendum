---
type: Agendum Action
title: "Deep read: ESP32 iPhone Agent, a phone computer-use loop and run export, compared with #16"
description: "Worth a close read this week."
resource: https://github.com/mykie2015/agendum/issues/19
tags: [read, p1, ai, agent, harness]
status: draft
issue: 19
action_type: read
priority: p1
state: open
created: 2026-10-19
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:47:18+08:00 }
sources:
  - { id: s1, resource: https://github.com/onehumanbeing/esp32-iphone-agent }
  - { id: s2, resource: https://github.com/onehumanbeing/esp32-iphone-agent/blob/main/README.md }
  - { id: s3, resource: https://github.com/onehumanbeing/esp32-iphone-agent/blob/main/README.zh-CN.md }
  - { id: s4, resource: https://github.com/onehumanbeing/esp32-iphone-agent/blob/main/docs/run-data-export.md }
  - { id: s5, resource: http://www.ruanyifeng.com/blog/2026/10/weekly-issue-415.html }
  - { id: s6, resource: https://x.com/iamhenryyuan }
  - { id: s7, resource: https://www.youtube.com/watch?v=Ly4im-P4jYg }
  - { id: s8, resource: https://github.com/boboabw/phone-agent }
---

# Decision

Worth a close read this week. A $7 ESP32-S3 acts as the AirPlay eyes and the USB HID hands, and the agent runs on the same iPhone, with no Mac, jailbreak, or developer account needed; the repo already has a run export so another agent can review the run. It fills the "phone computer use beyond Browser Agent (#16)" comparison directly, without buying the board first and without a BUILD.

# Summary

Not chasing the weekly's hot tool list, but adding a computer-use harness sample on a physical device. First read the loop and limits clearly, then decide whether to spend about seven dollars on one minimal real-device task.

# Limits

Needs iOS 18+, cellular data, and a one-time Mac + Xcode to flash the board and sign the app; BLE about 300–500 kbps, mirroring about 480×1040 at ≤5 fps; lock screen / passcode / Apple Pay / DRM are not visible; non-ASCII input and landscape are unsupported; not reproduced locally; WebFetch once showed 0 stars, so go by the API

# Next steps

- [ ] Read the README / Limitations / Related projects closely and write a 5-row comparison table with #16
- [ ] Skim the run-data-export doc: note whether the exported fields are enough to design an "another agent reviews the run" experiment
- [ ] Decide: just close this READ, or open an EXPERIMENT for "buy the board + flash + one alarm-type task" (state the cellular and iOS 18 prerequisites)

# Updates

- Imported comment from the upstream issue (2026-10-21), translated into English.

# Sources

- https://github.com/onehumanbeing/esp32-iphone-agent
- https://github.com/onehumanbeing/esp32-iphone-agent/blob/main/README.md
- https://github.com/onehumanbeing/esp32-iphone-agent/blob/main/README.zh-CN.md
- https://github.com/onehumanbeing/esp32-iphone-agent/blob/main/docs/run-data-export.md
- http://www.ruanyifeng.com/blog/2026/10/weekly-issue-415.html
- https://x.com/iamhenryyuan
- https://www.youtube.com/watch?v=Ly4im-P4jYg
- https://github.com/boboabw/phone-agent

# Tracking

[Issue #19](https://github.com/mykie2015/agendum/issues/19) · READ · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
