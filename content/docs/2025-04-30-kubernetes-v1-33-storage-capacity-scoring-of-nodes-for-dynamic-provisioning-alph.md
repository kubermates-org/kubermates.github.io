---
title: 'Kubernetes v1.33: Storage Capacity Scoring of Nodes for Dynamic Provisioning
  (alpha)'
date: '2025-04-30T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/04/30/kubernetes-v1-33-storage-capacity-scoring-feature/
post_kind: link
draft: false
tldr: Kubernetes v1.
summary: Kubernetes v1. 33 introduces a new alpha feature called StorageCapacityScoring.
  This feature adds a scoring method for pod scheduling with the topology-aware volume
  provisioning. This feature eases to schedule pods on nodes with either the most
  or least available storage capacity. This feature extends the kube-scheduler's VolumeBinding
  plugin to perform scoring using node storage capacity information obtained from
  Storage Capacity. Currently, you can only filter out nodes with insufficient storage
  capacity.
---
Open the original post ↗ https://kubernetes.io/blog/2025/04/30/kubernetes-v1-33-storage-capacity-scoring-feature/
