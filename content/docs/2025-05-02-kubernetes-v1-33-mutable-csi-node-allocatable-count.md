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
  about resource availability on nodes.
summary: Scheduling stateful applications reliably depends heavily on accurate information
  about resource availability on nodes. Kubernetes v1. 33 introduces an alpha feature
  called mutable CSI node allocatable count , allowing Container Storage Interface
  (CSI) drivers to dynamically update the reported maximum number of volumes that
  a node can handle. This capability significantly enhances the accuracy of pod scheduling
  decisions and reduces scheduling failures caused by outdated volume capacity information.
  Traditionally, Kubernetes CSI drivers report a static maximum volume attachment
  limit when initializing. However, actual attachment capacities can change during
  a node's lifecycle for various...
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/02/kubernetes-1-33-mutable-csi-node-allocatable-count/
