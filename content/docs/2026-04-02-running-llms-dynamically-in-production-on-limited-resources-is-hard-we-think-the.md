---
title: Running LLMs dynamically, in production, on limited resources, is hard. We
  think there’s room for another approach…
date: '2026-04-02T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/running-llms-dynamically-production-limited-resources-hard-we-think-theres-room-another-approach
post_kind: link
draft: false
tldr: 'Running LLMs dynamically, in production, on limited resources, is hard. We
  think there’s room for another approach… The production scale challenges Inference
  cost is the real bill The hardware math can be challenging Static partitioning might
  not fit every use case Exploring a different approach Another approach Meeting kvcached…
  … and its companion project, Sardeenz How it works in practice A few things worth
  highlighting Deployment: one container, one port What it isn''t Where this fits
  and where to go from here Scenarios we had in mind When to look elsewhere Getting
  started What''s next Red Hat AI Inference Server | Product Trial About the authors
  Guillaume Moutier Xingqi Cui Jiarong Xing Yifan Qiao More like this Red Hat and
  NVIDIA: Setting standards for high-performance AI inference Red Hat AI tops MLPerf
  Inference v6.0 with vLLM on Qwen3-VL, Whisper, and GPT-OSS-120B Technically Speaking
  | Build a production-ready AI toolbox Technically Speaking | Platform engineering
  for AI agents Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share The promise of large language models (LLMs) is clear.'
summary: 'Running LLMs dynamically, in production, on limited resources, is hard.
  We think there’s room for another approach… The production scale challenges Inference
  cost is the real bill The hardware math can be challenging Static partitioning might
  not fit every use case Exploring a different approach Another approach Meeting kvcached…
  … and its companion project, Sardeenz How it works in practice A few things worth
  highlighting Deployment: one container, one port What it isn''t Where this fits
  and where to go from here Scenarios we had in mind When to look elsewhere Getting
  started What''s next Red Hat AI Inference Server | Product Trial About the authors
  Guillaume Moutier Xingqi Cui Jiarong Xing Yifan Qiao More like this Red Hat and
  NVIDIA: Setting standards for high-performance AI inference Red Hat AI tops MLPerf
  Inference v6.0 with vLLM on Qwen3-VL, Whisper, and GPT-OSS-120B Technically Speaking
  | Build a production-ready AI toolbox Technically Speaking | Platform engineering
  for AI agents Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share The promise of large language models (LLMs) is clear. From code generation
  to customer support, from document analysis to creative workflows, organizations
  everywhere are racing to integrate LLMs into their products and operations. The
  enterprise LLM market is projected to grow from $6 billion in 2025 to over $50 billion
  by 2035. But behind the excitement lies a practical challenge—serving LLMs in production
  can be expensive, inefficient, and operationally complex. There''s a common misconception
  that training is where most of the money goes. In many production deployments we
  see, however, inference costs dominate infrastructure budgets. Training happens
  once (or occasionally); inference happens millions of times a day. Every inefficiency
  in the serving stack—idle GPU cycle, cold-start delay, over-provisioned instance—can
  compound into real dollars. A single enterprise-grade GPU can be astonishingly expensive.
  A more modest setup with consumer GPUs can also represent a significant investment.
  And most organizations don’t rely on just one model.'
---
Open the original post ↗ https://www.redhat.com/en/blog/running-llms-dynamically-production-limited-resources-hard-we-think-theres-room-another-approach
