---
title: 'Kubernetes v1.34: Moving Volume Group Snapshots to v1beta2'
date: '2025-09-16T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/09/16/kubernetes-v1-34-volume-group-snapshot-beta-2/
post_kind: link
draft: false
tldr: 'Kubernetes v1.34: Moving Volume Group Snapshots to v1beta2 What''s new in Beta
  2? What’s next? How do I get involved? Volume group snapshots were introduced as
  an Alpha feature with the Kubernetes 1.27 release and moved to Beta in the Kubernetes
  1.32 release. The recent release of Kubernetes v1.34 moved that support to a second
  beta.'
summary: 'Kubernetes v1.34: Moving Volume Group Snapshots to v1beta2 What''s new in
  Beta 2? What’s next? How do I get involved? Volume group snapshots were introduced
  as an Alpha feature with the Kubernetes 1.27 release and moved to Beta in the Kubernetes
  1.32 release. The recent release of Kubernetes v1.34 moved that support to a second
  beta. The support for volume group snapshots relies on a set of extension APIs for
  group snapshots. These APIs allow users to take crash consistent snapshots for a
  set of volumes. Behind the scenes, Kubernetes uses a label selector to group multiple
  PersistentVolumeClaims for snapshotting. A key aim is to allow you restore that
  set of snapshots to new volumes and recover your workload based on a crash consistent
  recovery point. This new feature is only supported for CSI volume drivers. While
  testing the beta version, we encountered an issue where the restoreSize field is
  not set for individual VolumeSnapshotContents and VolumeSnapshots if CSI driver
  does not implement the ListSnapshots RPC call. We evaluated various options here
  and decided to make this change releasing a new beta for the API. restoreSize Specifically,
  a VolumeSnapshotInfo struct is added in v1beta2, it contains information for an
  individual volume snapshot that is a member of a volume group snapshot. VolumeSnapshotInfoList,
  a list of VolumeSnapshotInfo, is added to VolumeGroupSnapshotContentStatus, replacing
  VolumeSnapshotHandlePairList. VolumeSnapshotInfoList is a list of snapshot information
  returned by the CSI driver to identify snapshots on the storage system.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/09/16/kubernetes-v1-34-volume-group-snapshot-beta-2/
