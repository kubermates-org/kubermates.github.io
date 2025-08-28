---
title: Introducing Gateway API Inference Extension
date: '2025-06-05T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/
post_kind: link
draft: false
tldr: Introducing Gateway API Inference Extension Gateway API Inference Extension
  How it works Request flow Benchmarks Key results Roadmap Summary Modern generative
  AI and large language model (LLM) services create unique traffic-routing challenges
  on Kubernetes. Unlike typical short-lived, stateless web requests, LLM inference
  sessions are often long-running, resource-intensive, and partially stateful.
summary: Introducing Gateway API Inference Extension Gateway API Inference Extension
  How it works Request flow Benchmarks Key results Roadmap Summary Modern generative
  AI and large language model (LLM) services create unique traffic-routing challenges
  on Kubernetes. Unlike typical short-lived, stateless web requests, LLM inference
  sessions are often long-running, resource-intensive, and partially stateful. For
  example, a single GPU-backed model server may keep multiple inference sessions active
  and maintain in-memory token caches. Traditional load balancers focused on HTTP
  path or round-robin lack the specialized capabilities needed for these workloads.
  They also don’t account for model identity or request criticality (e. g. , interactive
  chat vs. batch jobs). Gateway API Inference Extension was created to address this
  gap by building on the existing Gateway API , adding inference-specific routing
  capabilities while retaining the familiar model of Gateways and HTTPRoutes. By adding
  an inference extension to your existing gateway, you effectively transform it into
  an Inference Gateway , enabling you to self-host GenAI/LLMs with a “model-as-a-service”
  mindset. The project’s goal is to improve and standardize routing to inference workloads
  across the ecosystem. Key objectives include enabling model-aware routing, supporting
  per-request criticalities, facilitating safe model roll-outs, and optimizing load
  balancing based on real-time model metrics.
---
Open the original post ↗ https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/
