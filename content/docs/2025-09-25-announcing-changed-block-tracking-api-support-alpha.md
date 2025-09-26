---
title: Announcing Changed Block Tracking API support (alpha)
date: '2025-09-25T05:00:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/
post_kind: link
draft: false
tldr: Announcing Changed Block Tracking API support (alpha) What is changed block
  tracking? Benefits of changed block tracking support in Kubernetes Key components
  Implementation requirements Storage provider responsibilities Backup solution responsibilities
  Getting started What’s next? How do I get involved? We're excited to announce the
  alpha support for a changed block tracking mechanism. This enhances the Kubernetes
  storage ecosystem by providing an efficient way for CSI storage drivers to identify
  changed blocks in PersistentVolume snapshots.
summary: 'Announcing Changed Block Tracking API support (alpha) What is changed block
  tracking? Benefits of changed block tracking support in Kubernetes Key components
  Implementation requirements Storage provider responsibilities Backup solution responsibilities
  Getting started What’s next? How do I get involved? We''re excited to announce the
  alpha support for a changed block tracking mechanism. This enhances the Kubernetes
  storage ecosystem by providing an efficient way for CSI storage drivers to identify
  changed blocks in PersistentVolume snapshots. With a driver that can use the feature,
  you could benefit from faster and more resource-efficient backup operations. If
  you''re eager to try this feature, you can skip to the Getting Started section.
  Changed block tracking enables storage systems to identify and track modifications
  at the block level between snapshots, eliminating the need to scan entire volumes
  during backup operations. The improvement is a change to the Container Storage Interface
  (CSI), and also to the storage support in Kubernetes itself. With the alpha feature
  enabled, your cluster can: Identify allocated blocks within a CSI volume snapshot
  Determine changed blocks between two snapshots of the same volume Streamline backup
  operations by focusing only on changed data blocks For Kubernetes users managing
  large datasets, this API enables significantly more efficient backup processes.
  Backup applications can now focus only on the blocks that have changed, rather than
  processing entire volumes. As Kubernetes adoption grows for stateful workloads managing
  critical data, the need for efficient backup solutions becomes increasingly important.
  Traditional full backup approaches face challenges with: Long backup windows : Full
  volume backups can take hours for large datasets, making it difficult to complete
  within maintenance windows. High resource utilization : Backup operations consume
  substantial network bandwidth and I/O resources, especially for large data volumes
  and data-intensive applications. Increased storage costs : Repetitive full backups
  store redundant data, causing storage requirements to grow linearly even when only
  a small percentage of data actually changes between backups.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/
