---
title: 'The platform under the model: How cloud native powers AI engineering in production'
date: '2026-03-26T09:07:14+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/03/26/the-platform-under-the-model-how-cloud-native-powers-ai-engineering-in-production/
post_kind: link
draft: false
tldr: From model to systems The cloud native stack for (Gen) AI Bridging the gap Why
  open source matters here Getting started Looking ahead Posted on March 26, 2026
  by Max Körbächer, CNCF Ambassador CNCF projects highlighted in this post AI workloads
  are increasingly running on Kubernetes in production, but for many teams, the path
  from a working model to a reliable system remains unclear. The cloud native ecosystem
  – its projects, patterns, and community – offers a growing set of building blocks
  that help teams bridge these two worlds.
summary: 'From model to systems The cloud native stack for (Gen) AI Bridging the gap
  Why open source matters here Getting started Looking ahead Posted on March 26, 2026
  by Max Körbächer, CNCF Ambassador CNCF projects highlighted in this post AI workloads
  are increasingly running on Kubernetes in production, but for many teams, the path
  from a working model to a reliable system remains unclear. The cloud native ecosystem
  – its projects, patterns, and community – offers a growing set of building blocks
  that help teams bridge these two worlds. AI Engineering is the discipline of building
  reliable, production-grade systems that use AI models as components. It goes beyond
  model training and prompt design into the operational challenges that teams running
  inference at scale will recognize: serving models with low latency and high availability,
  efficiently scheduling GPU and accelerator resources, observing token throughput
  and cost alongside traditional infrastructure metrics, managing model versions and
  rollouts safely, and enforcing governance and access policies across multi-tenant
  environments. These are infrastructure problems, and they map closely to capabilities
  the cloud native ecosystem has been developing for years. If you’re a platform engineer
  or SRE being asked to support AI workloads, the good news is that much of what you
  need already exists in the CNCF landscape. Orchestration and scheduling: Kubernetes
  is the orchestration layer for AI inference and training. The 2025 CNCF Annual Survey
  found that 82% of container users run Kubernetes in production, and the platform
  has evolved well beyond stateless web services. A key development is Dynamic Resource
  Allocation (DRA) , which reached GA in Kubernetes 1.34. DRA replaces the limitations
  of device plugins with fine-grained, topology-aware GPU scheduling using CEL-based
  filtering and declarative ResourceClaims. For teams managing GPU clusters, DRA is
  a significant step forward. Inference routing and load balancing: The Gateway API
  Inference Extension (Inference Gateway), which has reached GA, provides Kubernetes-native
  APIs for routing inference traffic based on model names, LoRA adapters, and endpoint
  health.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/03/26/the-platform-under-the-model-how-cloud-native-powers-ai-engineering-in-production/
