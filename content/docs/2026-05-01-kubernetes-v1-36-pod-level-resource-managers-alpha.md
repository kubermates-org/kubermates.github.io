---
title: 'Kubernetes v1.36: Pod-Level Resource Managers (Alpha)'
date: '2026-05-01T10:35:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/05/01/kubernetes-v1-36-feature-pod-level-resource-managers-alpha/
post_kind: link
draft: false
tldr: 'Kubernetes v1.36: Pod-Level Resource Managers (Alpha) Why do we need pod-level
  resource managers? Introducing pod-level resource managers Real-world use cases
  CPU quotas (CFS) and isolation How to enable Pod-Level Resource Managers Observability
  Current limitations and caveats Getting started and providing feedback Kubernetes
  v1.36 introduces Pod-Level Resource Managers as an alpha feature, bringing a more
  flexible and powerful resource management model to performance-sensitive workloads.
  This enhancement extends the kubelet''s Topology, CPU, and Memory Managers to support
  pod-level resource specifications (.'
summary: 'Kubernetes v1.36: Pod-Level Resource Managers (Alpha) Why do we need pod-level
  resource managers? Introducing pod-level resource managers Real-world use cases
  CPU quotas (CFS) and isolation How to enable Pod-Level Resource Managers Observability
  Current limitations and caveats Getting started and providing feedback Kubernetes
  v1.36 introduces Pod-Level Resource Managers as an alpha feature, bringing a more
  flexible and powerful resource management model to performance-sensitive workloads.
  This enhancement extends the kubelet''s Topology, CPU, and Memory Managers to support
  pod-level resource specifications (. spec. resources ), evolving them from a strictly
  per-container allocation model to a pod-centric one. spec. resources When running
  performance-critical workloads such as machine learning (ML) training, high-frequency
  trading applications, or low-latency databases, you often need exclusive, NUMA-aligned
  resources for your primary application containers to ensure predictable performance.
  However, modern Kubernetes pods rarely consist of just one container. They frequently
  include sidecar containers for logging, monitoring, service meshes, or data ingestion.
  Before this feature, this created a trade-off, to get NUMA-aligned, exclusive resources
  for your main application, you had to allocate exclusive, integer-based CPU resources
  to every container in the pod. This might be wasteful for lightweight sidecars.
  If you didn''t do this, you forfeited the pod''s Guaranteed Quality of Service (QoS)
  class entirely, losing the performance benefits. Enabling pod-level resources support
  for the resource managers (via the PodLevelResourceManagers and PodLevelResources
  feature gates) allows the kubelet to create hybrid resource allocation models.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/05/01/kubernetes-v1-36-feature-pod-level-resource-managers-alpha/
