---
title: 'Kubernetes 1.33: Volume Populators Graduate to GA'
date: '2025-05-08T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/05/08/kubernetes-v1-33-volume-populators-ga/
post_kind: link
draft: false
tldr: Kubernetes volume populators are now generally available (GA)! The AnyVolumeDataSource
  feature gate is treated as always enabled for Kubernetes v1. 33, which means that
  users can specify any appropriate custom resource as the data source of a PersistentVolumeClaim
  (PVC).
summary: 'Kubernetes volume populators are now generally available (GA)! The AnyVolumeDataSource
  feature gate is treated as always enabled for Kubernetes v1. 33, which means that
  users can specify any appropriate custom resource as the data source of a PersistentVolumeClaim
  (PVC). An example of how to use dataSourceRef in PVC: There are four major enhancements
  from beta. During the beta phase, contributors to Kubernetes identified potential
  resource leaks with PersistentVolumeClaim (PVC) deletion while volume population
  was in progress; these leaks happened due to limitations in finalizer handling.
  Ahead of the graduation to general availability, the Kubernetes project added support
  to delete temporary resources (PVC prime, etc. ) if the original PVC is deleted.
  To accommodate this, we''ve introduced three new plugin-based functions: A provider
  example is added in lib-volume-populator/example. For GA, the CSI volume populator
  controller code gained a MutatorConfig , allowing the specification of mutator functions
  to modify Kubernetes resources. For example, if the PVC prime is not an exact copy
  of the PVC and you need provider-specific information for the driver, you can include
  this information in the optional MutatorConfig. This allows you to customize the
  Kubernetes objects in the volume populator. Our beta phase highlighted a new requirement:
  the need to aggregate metrics not just from lib-volume-populator, but also from
  other components within the provider''s codebase. To address this, SIG Storage introduced
  a provider metric manager.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/08/kubernetes-v1-33-volume-populators-ga/
