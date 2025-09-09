---
title: 'Kubernetes v1.34: VolumeAttributesClass for Volume Modification GA'
date: '2025-09-08T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/09/08/kubernetes-v1-34-volume-attributes-class/
post_kind: link
draft: false
tldr: 'Kubernetes v1.34: VolumeAttributesClass for Volume Modification GA What is
  VolumeAttributesClass? What is new from Beta to GA Cancel support from infeasible
  errors Quota support based on scope Drivers support VolumeAttributesClass Contact
  The VolumeAttributesClass API, which empowers users to dynamically modify volume
  attributes, has officially graduated to General Availability (GA) in Kubernetes
  v1.34. This marks a significant milestone, providing a robust and stable way to
  tune your persistent storage directly within Kubernetes.'
summary: 'Kubernetes v1.34: VolumeAttributesClass for Volume Modification GA What
  is VolumeAttributesClass? What is new from Beta to GA Cancel support from infeasible
  errors Quota support based on scope Drivers support VolumeAttributesClass Contact
  The VolumeAttributesClass API, which empowers users to dynamically modify volume
  attributes, has officially graduated to General Availability (GA) in Kubernetes
  v1.34. This marks a significant milestone, providing a robust and stable way to
  tune your persistent storage directly within Kubernetes. At its core, VolumeAttributesClass
  is a cluster-scoped resource that defines a set of mutable parameters for a volume.
  Think of it as a "profile" for your storage, allowing cluster administrators to
  expose different quality-of-service (QoS) levels or performance tiers. Users can
  then specify a volumeAttributesClassName in their PersistentVolumeClaim (PVC) to
  indicate which class of attributes they desire. The magic happens through the Container
  Storage Interface (CSI): when a PVC referencing a VolumeAttributesClass is updated,
  the associated CSI driver interacts with the underlying storage system to apply
  the specified changes to the volume. volumeAttributesClassName This means you can
  now: Dynamically scale performance: Increase IOPS or throughput for a busy database,
  or reduce it for a less critical application. Optimize costs: Adjust attributes
  on the fly to match your current needs, avoiding over-provisioning. Simplify operations:
  Manage volume modifications directly within the Kubernetes API, rather than relying
  on external tools or manual processes. There are two major enhancements from beta.
  To improve resilience and user experience, the GA release introduces explicit cancel
  support when a requested volume modification becomes infeasible. If the underlying
  storage system or CSI driver indicates that the requested changes cannot be applied
  (e.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/09/08/kubernetes-v1-34-volume-attributes-class/
