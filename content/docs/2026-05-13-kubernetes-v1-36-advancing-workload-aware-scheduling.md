---
title: 'Kubernetes v1.36: Advancing Workload-Aware Scheduling'
date: '2026-05-13T10:35:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/05/13/kubernetes-v1-36-advancing-workload-aware-scheduling/
post_kind: link
draft: false
tldr: 'Kubernetes v1.36: Advancing Workload-Aware Scheduling Workload and PodGroup
  API updates PodGroup scheduling cycle and gang scheduling Limitations Topology-aware
  scheduling Workload-aware preemption DRA ResourceClaim support for workloads Integration
  with the Job controller When does the integration kick in? What''s not covered yet
  What''s next? Getting started Learn more AI/ML and batch workloads introduce unique
  scheduling challenges that go beyond simple Pod-by-Pod scheduling. In Kubernetes
  v1.35, we introduced the first tranche of workload-aware scheduling improvements,
  featuring the foundational Workload API alongside basic gang scheduling support
  built on a Pod-based framework, and an opportunistic batching feature to efficiently
  process identical Pods.'
summary: 'Kubernetes v1.36: Advancing Workload-Aware Scheduling Workload and PodGroup
  API updates PodGroup scheduling cycle and gang scheduling Limitations Topology-aware
  scheduling Workload-aware preemption DRA ResourceClaim support for workloads Integration
  with the Job controller When does the integration kick in? What''s not covered yet
  What''s next? Getting started Learn more AI/ML and batch workloads introduce unique
  scheduling challenges that go beyond simple Pod-by-Pod scheduling. In Kubernetes
  v1.35, we introduced the first tranche of workload-aware scheduling improvements,
  featuring the foundational Workload API alongside basic gang scheduling support
  built on a Pod-based framework, and an opportunistic batching feature to efficiently
  process identical Pods. Kubernetes v1.36 introduces a significant architectural
  evolution by cleanly separating API concerns: the Workload API acts as a static
  template, while the new PodGroup API handles the runtime state. To support this,
  the kube-scheduler features a new PodGroup scheduling cycle that enables atomic
  workload processing and paves the way for future enhancements. This release also
  debuts the first iterations of topology-aware scheduling and workload-aware preemption
  to advance scheduling capabilities. Additionally, ResourceClaim support for workloads
  unlocks Dynamic Resource Allocation ( DRA ) for PodGroups. Finally, to demonstrate
  real-world readiness, v1.36 delivers the first phase of integration between the
  Job controller and the new API. kube-scheduler The Workload API now serves as a
  static template, while the new PodGroup API describes the runtime object. Kubernetes
  v1.36 introduces the Workload and PodGroup APIs as part of the scheduling. k8s.
  io/v1alpha2 API group , completely replacing the previous v1alpha1 API version.
  scheduling.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/05/13/kubernetes-v1-36-advancing-workload-aware-scheduling/
