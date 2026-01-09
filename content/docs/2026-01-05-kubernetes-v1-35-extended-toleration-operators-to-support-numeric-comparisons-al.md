---
title: 'Kubernetes v1.35: Extended Toleration Operators to Support Numeric Comparisons
  (Alpha)'
date: '2026-01-05T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/01/05/kubernetes-v1-35-numeric-toleration-operators/
post_kind: link
draft: false
tldr: 'Kubernetes v1.35: Extended Toleration Operators to Support Numeric Comparisons
  (Alpha) The evolution of tolerations Why extend tolerations instead of using NodeAffinity?
  Introducing Gt and Lt operators Use cases and examples Example 1: Spot instance
  protection with SLA thresholds Example 2: AI workload placement with GPU tiers Example
  3: Cost-optimized workload placement Example 4: Performance-based placement How
  to use this feature What''s next? Getting involved How can I learn more? Many production
  Kubernetes clusters blend on-demand (higher-SLA) and spot/preemptible (lower-SLA)
  nodes to optimize costs while maintaining reliability for critical workloads. Platform
  teams need a safe default that keeps most workloads away from risky capacity, while
  allowing specific workloads to opt-in with explicit thresholds like "I can tolerate
  nodes with failure probability up to 5%".'
summary: 'Kubernetes v1.35: Extended Toleration Operators to Support Numeric Comparisons
  (Alpha) The evolution of tolerations Why extend tolerations instead of using NodeAffinity?
  Introducing Gt and Lt operators Use cases and examples Example 1: Spot instance
  protection with SLA thresholds Example 2: AI workload placement with GPU tiers Example
  3: Cost-optimized workload placement Example 4: Performance-based placement How
  to use this feature What''s next? Getting involved How can I learn more? Many production
  Kubernetes clusters blend on-demand (higher-SLA) and spot/preemptible (lower-SLA)
  nodes to optimize costs while maintaining reliability for critical workloads. Platform
  teams need a safe default that keeps most workloads away from risky capacity, while
  allowing specific workloads to opt-in with explicit thresholds like "I can tolerate
  nodes with failure probability up to 5%". Today, Kubernetes taints and tolerations
  can match exact values or check for existence, but they can''t compare numeric thresholds.
  You''d need to create discrete taint categories, use external admission controllers,
  or accept less-than-optimal placement decisions. In Kubernetes v1.35, we''re introducing
  Extended Toleration Operators as an alpha feature. This enhancement adds Gt (Greater
  Than) and Lt (Less Than) operators to spec. tolerations , enabling threshold-based
  scheduling decisions that unlock new possibilities for SLA-based placement, cost
  optimization, and performance-aware workload distribution. Gt Lt spec. tolerations
  Historically, Kubernetes supported two primary toleration operators: Equal : The
  toleration matches a taint if the key and value are exactly equal Equal Exists :
  The toleration matches a taint if the key exists, regardless of value Exists While
  these worked well for categorical scenarios, they fell short for numeric comparisons.
  Starting with v1.35, we are closing this gap. Consider these real-world scenarios:
  SLA requirements : Schedule high-availability workloads only on nodes with failure
  probability below a certain threshold Cost optimization : Allow cost-sensitive batch
  jobs to run on cheaper nodes that exceed a specific cost-per-hour value Performance
  guarantees : Ensure latency-sensitive applications run only on nodes with disk IOPS
  or network bandwidth above minimum thresholds Without numeric comparison operators,
  cluster operators have had to resort to workarounds like creating multiple discrete
  taint values or using external admission controllers, neither of which scale well
  or provide the flexibility needed for dynamic threshold-based scheduling. You might
  wonder: NodeAffinity already supports numeric comparison operators, so why extend
  tolerations? While NodeAffinity is powerful for expressing pod preferences, taints
  and tolerations provide critical operational benefits: Policy orientation : NodeAffinity
  is per-pod, requiring every workload to explicitly opt-out of risky nodes.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/01/05/kubernetes-v1-35-numeric-toleration-operators/
