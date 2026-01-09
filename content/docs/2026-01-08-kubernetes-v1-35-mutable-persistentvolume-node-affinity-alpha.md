---
title: 'Kubernetes v1.35: Mutable PersistentVolume Node Affinity (alpha)'
date: '2026-01-08T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/01/08/kubernetes-v1-35-mutable-pv-nodeaffinity/
post_kind: link
draft: false
tldr: 'Kubernetes v1.35: Mutable PersistentVolume Node Affinity (alpha) Why make node
  affinity mutable? Try it out Race condition between updating and scheduling Future
  integration with CSI (Container Storage Interface) We welcome your feedback from
  users and storage driver developers The PersistentVolume node affinity API dates
  back to Kubernetes v1.10. It is widely used to express that volumes may not be equally
  accessible by all nodes in the cluster.'
summary: 'Kubernetes v1.35: Mutable PersistentVolume Node Affinity (alpha) Why make
  node affinity mutable? Try it out Race condition between updating and scheduling
  Future integration with CSI (Container Storage Interface) We welcome your feedback
  from users and storage driver developers The PersistentVolume node affinity API
  dates back to Kubernetes v1.10. It is widely used to express that volumes may not
  be equally accessible by all nodes in the cluster. This field was previously immutable,
  and it is now mutable in Kubernetes v1.35 (alpha). This change opens a door to more
  flexible online volume management. This raises an obvious question: why make node
  affinity mutable now? While stateless workloads like Deployments can be changed
  freely and the changes will be rolled out automatically by re-creating every Pod,
  PersistentVolumes (PVs) are stateful and cannot be re-created easily without losing
  data. However, Storage providers evolve and storage requirements change. Most notably,
  multiple providers are offering regional disks now. Some of them even support live
  migration from zonal to regional disks, without disrupting the workloads. This change
  can be expressed through the VolumeAttributesClass API, which recently graduated
  to GA in 1.34. However, even if the volume is migrated to regional storage, Kubernetes
  still prevents scheduling Pods to other zones because of the node affinity recorded
  in the PV object. In this case, you may want to change the PV node affinity from:
  spec : nodeAffinity : required : nodeSelectorTerms : - matchExpressions : - key
  : topology. kubernetes.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/01/08/kubernetes-v1-35-mutable-pv-nodeaffinity/
