---
title: 'Kubernetes v1.33: Prevent PersistentVolume Leaks When Deleting out of Order
  graduates to GA'
date: '2025-05-05T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/05/05/kubernetes-v1-33-prevent-persistentvolume-leaks-when-deleting-out-of-order-graduate-to-ga/
post_kind: link
draft: false
tldr: I am thrilled to announce that the feature to prevent PersistentVolume (or PVs
  for short) leaks when deleting out of order has graduated to General Availability
  (GA) in Kubernetes v1. 33! This improvement, initially introduced as a beta feature
  in Kubernetes v1.
summary: I am thrilled to announce that the feature to prevent PersistentVolume (or
  PVs for short) leaks when deleting out of order has graduated to General Availability
  (GA) in Kubernetes v1. 33! This improvement, initially introduced as a beta feature
  in Kubernetes v1. 31, ensures that your storage resources are properly reclaimed,
  preventing unwanted leaks. PersistentVolumeClaim (or PVC for short) is a user's
  request for storage. A PV and PVC are considered Bound if a newly created PV or
  a matching PV is found. The PVs themselves are backed by volumes allocated by the
  storage backend. Normally, if the volume is to be deleted, then the expectation
  is to delete the PVC for a bound PV-PVC pair. However, there are no restrictions
  on deleting a PV before deleting a PVC. For a Bound PV-PVC pair, the ordering of
  PV-PVC deletion determines whether the PV reclaim policy is honored. The reclaim
  policy is honored if the PVC is deleted first; however, if the PV is deleted prior
  to deleting the PVC, then the reclaim policy is not exercised. As a result of this
  behavior, the associated storage asset in the external infrastructure is not removed.
  With the graduation to GA in Kubernetes v1.
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/05/kubernetes-v1-33-prevent-persistentvolume-leaks-when-deleting-out-of-order-graduate-to-ga/
