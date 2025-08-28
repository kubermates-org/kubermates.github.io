---
title: 'Kubernetes 1.32: Moving Volume Group Snapshots to Beta'
date: '2024-12-18T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2024/12/18/kubernetes-1-32-volume-group-snapshot-beta/
post_kind: link
draft: false
tldr: 'Kubernetes 1. 32: Moving Volume Group Snapshots to Beta An overview of volume
  group snapshots Why add volume group snapshots to Kubernetes? Kubernetes APIs for
  volume group snapshots What components are needed to support volume group snapshots
  What''s new in Beta? How do I use Kubernetes volume group snapshots Creating a new
  group snapshot with Kubernetes How to use group snapshot for restore in Kubernetes
  As a storage vendor, how do I add support for group snapshots to my CSI driver?
  What are the limitations? What’s next? How do I get involved? Volume group snapshots
  were introduced as an Alpha feature with the Kubernetes 1.'
summary: 'Kubernetes 1. 32: Moving Volume Group Snapshots to Beta An overview of volume
  group snapshots Why add volume group snapshots to Kubernetes? Kubernetes APIs for
  volume group snapshots What components are needed to support volume group snapshots
  What''s new in Beta? How do I use Kubernetes volume group snapshots Creating a new
  group snapshot with Kubernetes How to use group snapshot for restore in Kubernetes
  As a storage vendor, how do I add support for group snapshots to my CSI driver?
  What are the limitations? What’s next? How do I get involved? Volume group snapshots
  were introduced as an Alpha feature with the Kubernetes 1. 27 release. The recent
  release of Kubernetes v1. 32 moved that support to beta. The support for volume
  group snapshots relies on a set of extension APIs for group snapshots. These APIs
  allow users to take crash consistent snapshots for a set of volumes. Behind the
  scenes, Kubernetes uses a label selector to group multiple PersistentVolumeClaims
  for snapshotting. A key aim is to allow you restore that set of snapshots to new
  volumes and recover your workload based on a crash consistent recovery point. This
  new feature is only supported for CSI volume drivers. Some storage systems provide
  the ability to create a crash consistent snapshot of multiple volumes. A group snapshot
  represents copies made from multiple volumes, that are taken at the same point-in-time.'
---
Open the original post ↗ https://kubernetes.io/blog/2024/12/18/kubernetes-1-32-volume-group-snapshot-beta/
