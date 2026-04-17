---
title: Peer-to-Peer acceleration for AI model distribution with Dragonfly
date: '2026-04-06T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/04/06/peer-to-peer-acceleration-for-ai-model-distribution-with-dragonfly/
post_kind: link
draft: false
tldr: 'The problem: AI model distribution is broken at scale What Is Dragonfly? Introducing
  native model hub protocols in Dragonfly The hf:// Protocol — Hugging Face hub The
  modelscope:// Protocol — ModelScope hub Under the hood: Technical deep dive Real-world
  impact: Where this matters Comparison: Why not just use platform CLIs? Getting started
  What’s next Contributing Conclusion Posted on April 6, 2026 by Pavan Madduri, CNCF
  Kubestronaut CNCF projects highlighted in this post Large-scale AI model distribution
  presents challenges in performance, efficiency, and cost. Consider a typical scenario:
  an ML platform team manages a Kubernetes cluster with 200 GPU nodes.'
summary: 'The problem: AI model distribution is broken at scale What Is Dragonfly?
  Introducing native model hub protocols in Dragonfly The hf:// Protocol — Hugging
  Face hub The modelscope:// Protocol — ModelScope hub Under the hood: Technical deep
  dive Real-world impact: Where this matters Comparison: Why not just use platform
  CLIs? Getting started What’s next Contributing Conclusion Posted on April 6, 2026
  by Pavan Madduri, CNCF Kubestronaut CNCF projects highlighted in this post Large-scale
  AI model distribution presents challenges in performance, efficiency, and cost.
  Consider a typical scenario: an ML platform team manages a Kubernetes cluster with
  200 GPU nodes. A new version of a 70B parameter model becomes available — for example,
  DeepSeek-V3 at approximately 130 GB. Each node requires a local copy, resulting
  in 26 TB of data transferred from a single model hub, often through shared origin
  infrastructure, network bandwidth, and rate limits. The scale of modern model hubs
  highlights these challenges: Hugging Face Hub serves over 1 million models, with
  individual files regularly exceeding 10 GB (safetensors, GGUF quantizations). ModelScope
  Hub hosts over 10,000 models — including large models such as Qwen, Yi, and inclusionAI’s
  Ling series — supporting a rapidly growing global user base. These platforms have
  significantly improved access to open models, but distributing large artifacts across
  many nodes introduces system-level constraints: Git LFS, which underpins large file
  storage on these platforms, is optimized for versioning and access rather than large-scale
  fan-out distribution. Rate limits can affect both unauthenticated and authenticated
  requests under burst traffic. Network costs increase as the same data is transferred
  repeatedly across environments. Existing approaches — such as NFS mounts, pre-built
  container images, or object storage mirrors — can help mitigate these issues, but
  may introduce operational complexity, stale-model risk, or additional storage overhead.
  This raises an important question: how can infrastructure enable model distribution
  to scale efficiently, so that downloading to the 200th node is as fast as downloading
  to the first, regardless of the model hub? That’s exactly what the new hf:// and
  modelscope:// protocol support in Dragonfly delivers. Dragonfly is a CNCF Graduated
  project that provides a P2P-based file distribution system.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/04/06/peer-to-peer-acceleration-for-ai-model-distribution-with-dragonfly/
