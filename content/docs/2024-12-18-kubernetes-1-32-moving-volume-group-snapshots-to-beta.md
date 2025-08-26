---
title: 'Kubernetes 1.32: Moving Volume Group Snapshots to Beta'
date: '2024-12-18T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2024/12/18/kubernetes-1-32-volume-group-snapshot-beta/
post_kind: link
draft: false
tldr: Volume group snapshots were introduced as an Alpha feature with the Kubernetes
  1. 27 release.
summary: Volume group snapshots were introduced as an Alpha feature with the Kubernetes
  1. 27 release. The recent release of Kubernetes v1. 32 moved that support to beta.
  The support for volume group snapshots relies on a set of extension APIs for group
  snapshots. These APIs allow users to take crash consistent snapshots for a set of
  volumes. Behind the scenes, Kubernetes uses a label selector to group multiple PersistentVolumeClaims
  for snapshotting. A key aim is to allow you restore that set of snapshots to new
  volumes and recover your workload based on a crash consistent recovery point. This
  new feature is only supported for CSI volume drivers. Some storage systems provide
  the ability to create a crash consistent snapshot of multiple volumes. A group snapshot
  represents copies made from multiple volumes, that are taken at the same point-in-time.
  A group snapshot can be used either to rehydrate new volumes (pre-populated with
  the snapshot data) or to restore existing volumes to a previous state (represented
  by the snapshots).
---
Open the original post ↗ https://kubernetes.io/blog/2024/12/18/kubernetes-1-32-volume-group-snapshot-beta/
