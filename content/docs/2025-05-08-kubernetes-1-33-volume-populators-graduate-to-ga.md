---
title: 'Kubernetes 1.33: Volume Populators Graduate to GA'
date: '2025-05-08T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/05/08/kubernetes-v1-33-volume-populators-ga/
post_kind: link
draft: false
tldr: 'Kubernetes 1. 33: Volume Populators Graduate to GA What is new Populator Pod
  is optional Mutator functions to modify the Kubernetes resources Flexible metric
  handling for providers Clean up for temporary resources How to use it Future directions
  and potential feature requests Kubernetes volume populators are now generally available
  (GA)! The AnyVolumeDataSource feature gate is treated as always enabled for Kubernetes
  v1.'
summary: 'Kubernetes 1. 33: Volume Populators Graduate to GA What is new Populator
  Pod is optional Mutator functions to modify the Kubernetes resources Flexible metric
  handling for providers Clean up for temporary resources How to use it Future directions
  and potential feature requests Kubernetes volume populators are now generally available
  (GA)! The AnyVolumeDataSource feature gate is treated as always enabled for Kubernetes
  v1. 33, which means that users can specify any appropriate custom resource as the
  data source of a PersistentVolumeClaim (PVC). AnyVolumeDataSource An example of
  how to use dataSourceRef in PVC: apiVersion : v1 kind : PersistentVolumeClaim metadata
  : name : pvc1 spec :. dataSourceRef : apiGroup : provider. example. com kind : Provider
  name : provider1 apiVersion : v1 kind : PersistentVolumeClaim metadata : name :
  pvc1 spec :. dataSourceRef : apiGroup : provider. example. com kind : Provider name
  : provider1 There are four major enhancements from beta. During the beta phase,
  contributors to Kubernetes identified potential resource leaks with PersistentVolumeClaim
  (PVC) deletion while volume population was in progress; these leaks happened due
  to limitations in finalizer handling. Ahead of the graduation to general availability,
  the Kubernetes project added support to delete temporary resources (PVC prime, etc.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/08/kubernetes-v1-33-volume-populators-ga/
