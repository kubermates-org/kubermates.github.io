---
title: 'Kubernetes v1.36: Moving Volume Group Snapshots to GA'
date: '2026-05-08T10:35:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/05/08/kubernetes-v1-36-volume-group-snapshot-ga/
post_kind: link
draft: false
tldr: 'Kubernetes v1.36: Moving Volume Group Snapshots to GA An overview of volume
  group snapshots Why add volume group snapshots to Kubernetes? Kubernetes APIs for
  volume group snapshots What''s new in GA? How do I use Kubernetes volume group snapshots
  Creating a new group snapshot with Kubernetes How to use group snapshot for restore
  As a storage vendor, how do I add support for group snapshots? How do I get involved?
  Volume group snapshots were introduced as an Alpha feature with the Kubernetes v1.27
  release, moved to Beta in v1.32, and to a second Beta in v1.34. We are excited to
  announce that in the Kubernetes v1.36 release, support for volume group snapshots
  has reached General Availability (GA).'
summary: 'Kubernetes v1.36: Moving Volume Group Snapshots to GA An overview of volume
  group snapshots Why add volume group snapshots to Kubernetes? Kubernetes APIs for
  volume group snapshots What''s new in GA? How do I use Kubernetes volume group snapshots
  Creating a new group snapshot with Kubernetes How to use group snapshot for restore
  As a storage vendor, how do I add support for group snapshots? How do I get involved?
  Volume group snapshots were introduced as an Alpha feature with the Kubernetes v1.27
  release, moved to Beta in v1.32, and to a second Beta in v1.34. We are excited to
  announce that in the Kubernetes v1.36 release, support for volume group snapshots
  has reached General Availability (GA). The support for volume group snapshots relies
  on a set of extension APIs for group snapshots. These APIs allow users to take crash-consistent
  snapshots for a set of volumes. Behind the scenes, Kubernetes uses a label selector
  to group multiple PersistentVolumeClaim objects for snapshotting. A key aim is to
  allow you to restore that set of snapshots to new volumes and recover your workload
  based on a crash-consistent recovery point. PersistentVolumeClaim This feature is
  only supported for CSI volume drivers. Some storage systems provide the ability
  to create a crash-consistent snapshot of multiple volumes. A group snapshot represents
  copies made from multiple volumes that are taken at the same point-in-time. A group
  snapshot can be used either to rehydrate new volumes (pre-populated with the snapshot
  data) or to restore existing volumes to a previous state (represented by the snapshots).
  The Kubernetes volume plugin system already provides a powerful abstraction that
  automates the provisioning, attaching, mounting, resizing, and snapshotting of block
  and file storage. Underpinning all these features is the Kubernetes goal of workload
  portability.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/05/08/kubernetes-v1-36-volume-group-snapshot-ga/
