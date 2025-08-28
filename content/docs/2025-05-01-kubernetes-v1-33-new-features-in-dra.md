---
title: 'Kubernetes v1.33: New features in DRA'
date: '2025-05-01T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/05/01/kubernetes-v1-33-dra-updates/
post_kind: link
draft: false
tldr: 'Kubernetes v1.33: New features in DRA Features promoted to beta New alpha features
  Preparing for general availability What’s next? Getting involved Acknowledgments
  Kubernetes Dynamic Resource Allocation (DRA) was originally introduced as an alpha
  feature in the v1.26 release, and then went through a significant redesign for Kubernetes
  v1.31. The main DRA feature went to beta in v1.32, and the project hopes it will
  be generally available in Kubernetes v1.34.'
summary: 'Kubernetes v1.33: New features in DRA Features promoted to beta New alpha
  features Preparing for general availability What’s next? Getting involved Acknowledgments
  Kubernetes Dynamic Resource Allocation (DRA) was originally introduced as an alpha
  feature in the v1.26 release, and then went through a significant redesign for Kubernetes
  v1.31. The main DRA feature went to beta in v1.32, and the project hopes it will
  be generally available in Kubernetes v1.34. The basic feature set of DRA provides
  a far more powerful and flexible API for requesting devices than Device Plugin.
  And while DRA remains a beta feature for v1.33, the DRA team has been hard at work
  implementing a number of new features and UX improvements. One feature has been
  promoted to beta, while a number of new features have been added in alpha. The team
  has also made progress towards getting DRA ready for GA. Driver-owned Resource Claim
  Status was promoted to beta. This allows the driver to report driver-specific device
  status data for each allocated device in a resource claim, which is particularly
  useful for supporting network devices. Partitionable Devices lets a driver advertise
  several overlapping logical devices (“partitions”), and the driver can reconfigure
  the physical device dynamically based on the actual devices allocated. This makes
  it possible to partition devices on-demand to meet the needs of the workloads and
  therefore increase the utilization. Device Taints and Tolerations allow devices
  to be tainted and for workloads to tolerate those taints. This makes it possible
  for drivers or cluster administrators to mark devices as unavailable.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/01/kubernetes-v1-33-dra-updates/
