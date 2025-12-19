---
title: 'Kubernetes v1.35: Job Managed By Goes GA'
date: '2025-12-18T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/12/18/kubernetes-v1-35-job-managedby-for-jobs-goes-ga/
post_kind: link
draft: false
tldr: 'Kubernetes v1.35: Job Managed By Goes GA Why delegate Job reconciliation? How.
  spec.'
summary: 'Kubernetes v1.35: Job Managed By Goes GA Why delegate Job reconciliation?
  How. spec. managedBy works Ecosystem Adoption How can you learn more? Acknowledgments
  Get involved In Kubernetes v1.35, the ability to specify an external Job controller
  (through. spec. managedBy ) graduates to General Availability. spec. managedBy This
  feature allows external controllers to take full responsibility for Job reconciliation,
  unlocking powerful scheduling patterns like multi-cluster dispatching with MultiKueue.
  The primary motivation for this feature is to support multi-cluster batch scheduling
  architectures, such as MultiKueue. The MultiKueue architecture distinguishes between
  a Management Cluster and a pool of Worker Clusters: The Management Cluster is responsible
  for dispatching Jobs but not executing them. It needs to accept Job objects to track
  status, but it skips the creation and execution of Pods. The Worker Clusters receive
  the dispatched Jobs and execute the actual Pods. Users usually interact with the
  Management Cluster.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/12/18/kubernetes-v1-35-job-managedby-for-jobs-goes-ga/
