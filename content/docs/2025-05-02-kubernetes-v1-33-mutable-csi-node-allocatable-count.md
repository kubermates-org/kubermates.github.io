---
title: 'Kubernetes v1.33: Mutable CSI Node Allocatable Count'
date: '2025-05-02T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/05/02/kubernetes-1-33-mutable-csi-node-allocatable-count/
post_kind: link
draft: false
tldr: 'Kubernetes v1.33: Mutable CSI Node Allocatable Count Background Dynamically
  adapting CSI volume limits How it works Enabling the feature Example CSI driver
  configuration Immediate updates on attachment failures Getting started Next steps
  Scheduling stateful applications reliably depends heavily on accurate information
  about resource availability on nodes. Kubernetes v1.33 introduces an alpha feature
  called mutable CSI node allocatable count , allowing Container Storage Interface
  (CSI) drivers to dynamically update the reported maximum number of volumes that
  a node can handle.'
summary: 'Kubernetes v1.33: Mutable CSI Node Allocatable Count Background Dynamically
  adapting CSI volume limits How it works Enabling the feature Example CSI driver
  configuration Immediate updates on attachment failures Getting started Next steps
  Scheduling stateful applications reliably depends heavily on accurate information
  about resource availability on nodes. Kubernetes v1.33 introduces an alpha feature
  called mutable CSI node allocatable count , allowing Container Storage Interface
  (CSI) drivers to dynamically update the reported maximum number of volumes that
  a node can handle. This capability significantly enhances the accuracy of pod scheduling
  decisions and reduces scheduling failures caused by outdated volume capacity information.
  Traditionally, Kubernetes CSI drivers report a static maximum volume attachment
  limit when initializing. However, actual attachment capacities can change during
  a node''s lifecycle for various reasons, such as: Manual or external operations
  attaching/detaching volumes outside of Kubernetes control. Dynamically attached
  network interfaces or specialized hardware (GPUs, NICs, etc. ) consuming available
  slots. Multi-driver scenarios, where one CSI driver’s operations affect available
  capacity reported by another. Static reporting can cause Kubernetes to schedule
  pods onto nodes that appear to have capacity but don''t, leading to pods stuck in
  a ContainerCreating state. ContainerCreating With the new feature gate MutableCSINodeAllocatableCount
  , Kubernetes enables CSI drivers to dynamically adjust and report node attachment
  capacities at runtime. This ensures that the scheduler has the most accurate, up-to-date
  view of node capacity. MutableCSINodeAllocatableCount When this feature is enabled,
  Kubernetes supports two mechanisms for updating the reported node volume limits:
  Periodic Updates: CSI drivers specify an interval to periodically refresh the node''s
  allocatable capacity.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/02/kubernetes-1-33-mutable-csi-node-allocatable-count/
