---
title: 'Kubernetes v1.33: Mutable CSI Node Allocatable Count'
date: '2025-05-02T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/05/02/kubernetes-1-33-mutable-csi-node-allocatable-count/
post_kind: link
draft: false
tldr: Scheduling stateful applications reliably depends heavily on accurate information
  about resource availability on nodes. Kubernetes v1.
summary: 'Scheduling stateful applications reliably depends heavily on accurate information
  about resource availability on nodes. Kubernetes v1. 33 introduces an alpha feature
  called mutable CSI node allocatable count , allowing Container Storage Interface
  (CSI) drivers to dynamically update the reported maximum number of volumes that
  a node can handle. This capability significantly enhances the accuracy of pod scheduling
  decisions and reduces scheduling failures caused by outdated volume capacity information.
  Traditionally, Kubernetes CSI drivers report a static maximum volume attachment
  limit when initializing. However, actual attachment capacities can change during
  a node''s lifecycle for various reasons, such as: Static reporting can cause Kubernetes
  to schedule pods onto nodes that appear to have capacity but don''t, leading to
  pods stuck in a ContainerCreating state. With the new feature gate MutableCSINodeAllocatableCount
  , Kubernetes enables CSI drivers to dynamically adjust and report node attachment
  capacities at runtime. This ensures that the scheduler has the most accurate, up-to-date
  view of node capacity. When this feature is enabled, Kubernetes supports two mechanisms
  for updating the reported node volume limits: To use this alpha feature, you must
  enable the MutableCSINodeAllocatableCount feature gate in these components: Below
  is an example of configuring a CSI driver to enable periodic updates every 60 seconds:
  This configuration directs Kubelet to periodically call the CSI driver''s NodeGetInfo
  method every 60 seconds, updating the node’s allocatable volume count. Kubernetes
  enforces a minimum update interval of 10 seconds to balance accuracy and resource
  usage. In addition to periodic updates, Kubernetes now reacts to attachment failures.
  Specifically, if a volume attachment fails with a ResourceExhausted error (gRPC
  code 8 ), an immediate update is triggered to correct the allocatable count promptly.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/02/kubernetes-1-33-mutable-csi-node-allocatable-count/
