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
tldr: 'Kubernetes v1. 33: Storage Capacity Scoring of Nodes for Dynamic Provisioning
  (alpha) About this feature How to use Enabling the feature Configuration changes
  Further reading Additional note: Relationship with VolumeCapacityPriority Kubernetes
  v1.'
summary: 'Kubernetes v1. 33: Storage Capacity Scoring of Nodes for Dynamic Provisioning
  (alpha) About this feature How to use Enabling the feature Configuration changes
  Further reading Additional note: Relationship with VolumeCapacityPriority Kubernetes
  v1. 33 introduces a new alpha feature called StorageCapacityScoring. This feature
  adds a scoring method for pod scheduling with the topology-aware volume provisioning.
  This feature eases to schedule pods on nodes with either the most or least available
  storage capacity. StorageCapacityScoring This feature extends the kube-scheduler''s
  VolumeBinding plugin to perform scoring using node storage capacity information
  obtained from Storage Capacity. Currently, you can only filter out nodes with insufficient
  storage capacity. So, you have to use a scheduler extender to achieve storage-capacity-based
  pod scheduling. This feature is useful for provisioning node-local PVs, which have
  size limits based on the node''s storage capacity. By using this feature, you can
  assign the PVs to the nodes with the most available storage space so that you can
  expand the PVs later as much as possible. In another use case, you might want to
  reduce the number of nodes as much as possible for low operation costs in cloud
  environments by choosing the least storage capacity node. This feature helps maximize
  resource utilization by filling up nodes more sequentially, starting with the most
  utilized nodes first that still have enough storage capacity for the requested volume
  size.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/04/30/kubernetes-v1-33-storage-capacity-scoring-feature/
