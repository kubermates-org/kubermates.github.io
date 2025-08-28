---
title: 'Tuning Linux Swap for Kubernetes: A Deep Dive'
date: '2025-08-19T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/
post_kind: link
draft: false
tldr: 'Tuning Linux Swap for Kubernetes: A Deep Dive Introduction to Linux swap Anonymous
  vs File-backed memory Key kernel parameters for swap tuning Swap tests and results
  Test setup Test methodology Findings Risks and recommendations Kubernetes context
  Recommended starting point The Kubernetes NodeSwap feature , likely to graduate
  to stable in the upcoming Kubernetes v1. 34 release, allows swap usage: a significant
  shift from the conventional practice of disabling swap for performance predictability.'
summary: 'Tuning Linux Swap for Kubernetes: A Deep Dive Introduction to Linux swap
  Anonymous vs File-backed memory Key kernel parameters for swap tuning Swap tests
  and results Test setup Test methodology Findings Risks and recommendations Kubernetes
  context Recommended starting point The Kubernetes NodeSwap feature , likely to graduate
  to stable in the upcoming Kubernetes v1. 34 release, allows swap usage: a significant
  shift from the conventional practice of disabling swap for performance predictability.
  This article focuses exclusively on tuning swap on Linux nodes, where this feature
  is available. By allowing Linux nodes to use secondary storage for additional virtual
  memory when physical RAM is exhausted, node swap support aims to improve resource
  utilization and reduce out-of-memory (OOM) kills. However, enabling swap is not
  a "turn-key" solution. The performance and stability of your nodes under memory
  pressure are critically dependent on a set of Linux kernel parameters. Misconfiguration
  can lead to performance degradation and interfere with Kubelet''s eviction logic.
  In this blogpost, I''ll dive into critical Linux kernel parameters that govern swap
  behavior. I will explore how these parameters influence Kubernetes workload performance,
  swap utilization, and crucial eviction mechanisms. I will present various test results
  showcasing the impact of different configurations, and share my findings on achieving
  optimal settings for stable and high-performing Kubernetes clusters. At a high level,
  the Linux kernel manages memory through pages, typically 4KiB in size. When physical
  memory becomes constrained, the kernel''s page replacement algorithm decides which
  pages to move to swap space.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/
