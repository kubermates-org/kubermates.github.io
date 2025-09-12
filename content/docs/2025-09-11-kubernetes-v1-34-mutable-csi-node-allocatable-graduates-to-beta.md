---
title: 'Kubernetes v1.34: Mutable CSI Node Allocatable Graduates to Beta'
date: '2025-09-11T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/09/11/kubernetes-v1-34-mutable-csi-node-allocatable-count/
post_kind: link
draft: false
tldr: 'Kubernetes v1.34: Mutable CSI Node Allocatable Graduates to Beta Background
  Dynamically adapting CSI volume limits How it works Enabling the feature Example
  CSI driver configuration Immediate updates on attachment failures Getting started
  Next steps The functionality for CSI drivers to update information about attachable
  volume count on the nodes , first introduced as Alpha in Kubernetes v1.33, has graduated
  to Beta in the Kubernetes v1.34 release! This marks a significant milestone in enhancing
  the accuracy of stateful pod scheduling by reducing failures due to outdated attachable
  volume capacity information. Traditionally, Kubernetes CSI drivers report a static
  maximum volume attachment limit when initializing.'
summary: 'Kubernetes v1.34: Mutable CSI Node Allocatable Graduates to Beta Background
  Dynamically adapting CSI volume limits How it works Enabling the feature Example
  CSI driver configuration Immediate updates on attachment failures Getting started
  Next steps The functionality for CSI drivers to update information about attachable
  volume count on the nodes , first introduced as Alpha in Kubernetes v1.33, has graduated
  to Beta in the Kubernetes v1.34 release! This marks a significant milestone in enhancing
  the accuracy of stateful pod scheduling by reducing failures due to outdated attachable
  volume capacity information. Traditionally, Kubernetes CSI drivers report a static
  maximum volume attachment limit when initializing. However, actual attachment capacities
  can change during a node''s lifecycle for various reasons, such as: Manual or external
  operations attaching/detaching volumes outside of Kubernetes control. Dynamically
  attached network interfaces or specialized hardware (GPUs, NICs, etc. ) consuming
  available slots. Multi-driver scenarios, where one CSI driver’s operations affect
  available capacity reported by another. Static reporting can cause Kubernetes to
  schedule pods onto nodes that appear to have capacity but don''t, leading to pods
  stuck in a ContainerCreating state. ContainerCreating With this new feature, Kubernetes
  enables CSI drivers to dynamically adjust and report node attachment capacities
  at runtime. This ensures that the scheduler, as well as other components relying
  on this information, have the most accurate, up-to-date view of node capacity. Kubernetes
  supports two mechanisms for updating the reported node volume limits: Periodic Updates:
  CSI drivers specify an interval to periodically refresh the node''s allocatable
  capacity. Reactive Updates: An immediate update triggered when a volume attachment
  fails due to exhausted resources ( ResourceExhausted error). ResourceExhausted To
  use this beta feature, the MutableCSINodeAllocatableCount feature gate must be enabled
  in these components: MutableCSINodeAllocatableCount kube-apiserver kube-apiserver
  kubelet kubelet Below is an example of configuring a CSI driver to enable periodic
  updates every 60 seconds: apiVersion: storage.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/09/11/kubernetes-v1-34-mutable-csi-node-allocatable-count/
