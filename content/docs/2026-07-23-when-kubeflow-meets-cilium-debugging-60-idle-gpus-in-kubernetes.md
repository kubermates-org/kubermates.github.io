---
title: 'When Kubeflow meets Cilium: Debugging 60% idle GPUs in Kubernetes'
date: '2026-07-23T11:33:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/07/23/when-kubeflow-meets-cilium-debugging-60-idle-gpus-in-kubernetes/
post_kind: link
draft: false
tldr: Posted on July 23, 2026 by Ramkumar Nagaraj (Golden Kubestronaut, Adobe) and
  Bingi Narasimha Karthik (Golden Kubestronaut, Adobe) The symptom that made no sense
  The first time we saw it, we didn’t trust the dashboard. A distributed training
  job was scheduled and healthy — every pod was running, no crashes, no OOMKills,
  nothing in the logs.
summary: Posted on July 23, 2026 by Ramkumar Nagaraj (Golden Kubestronaut, Adobe)
  and Bingi Narasimha Karthik (Golden Kubestronaut, Adobe) The symptom that made no
  sense The first time we saw it, we didn’t trust the dashboard. A distributed training
  job was scheduled and healthy — every pod was running, no crashes, no OOMKills,
  nothing in the logs. And yet more than half the GPUs we were paying for sat idle,
  and training never actually started. Every health check was green, and nothing was
  computing. A metaphor that finally made it click We kept reaching for a way to explain
  it, and this is the one that stuck. Imagine a sold-out concert hall. Every musician
  is in their seat, instruments tuned, the hall lit. But the conductor was shown to
  the wrong wing of the building — and the fire-safety doors, doing exactly their
  job, sealed that wing off. The result is a full, expensive hall and complete silence.
  That is a GPU cluster in this failure mode. The conductor is the training coordinator.
  The musicians are the GPU workers, who can only play in sync, through the conductor
  — the same way distributed training synchronizes gradients through a coordinator.
---
Open the original post ↗ https://www.cncf.io/blog/2026/07/23/when-kubeflow-meets-cilium-debugging-60-idle-gpus-in-kubernetes/
