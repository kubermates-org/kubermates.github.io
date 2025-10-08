---
title: Karmada v1.15 Released! Enhanced Resource Awareness for Multi-Template Workloads
date: '2025-10-08T00:56:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/10/07/karmada-v1-15-released-enhanced-resource-awareness-for-multi-template-workloads/
post_kind: link
draft: false
tldr: Overview of New Features Precise Resource Awareness for Multi-Template Workloads
  Enhanced Cluster-Level Failover Functionality Structured Logging Significant Performance
  Improvements for Karmada Controllers and Schedulers Acknowledging Our Contributors
  References： Posted on October 7, 2025 by The Karmada Maintainers CNCF projects highlighted
  in this post Karmada is an open multi-cloud and multi-cluster container orchestration
  engine designed to help users deploy and operate business applications in a multi-cloud
  environment. With its compatibility with the native Kubernetes API, Karmada can
  smoothly migrate single-cluster workloads while still maintaining coordination with
  the surrounding Kubernetes ecosystem tools.
summary: 'Overview of New Features Precise Resource Awareness for Multi-Template Workloads
  Enhanced Cluster-Level Failover Functionality Structured Logging Significant Performance
  Improvements for Karmada Controllers and Schedulers Acknowledging Our Contributors
  References： Posted on October 7, 2025 by The Karmada Maintainers CNCF projects highlighted
  in this post Karmada is an open multi-cloud and multi-cluster container orchestration
  engine designed to help users deploy and operate business applications in a multi-cloud
  environment. With its compatibility with the native Kubernetes API, Karmada can
  smoothly migrate single-cluster workloads while still maintaining coordination with
  the surrounding Kubernetes ecosystem tools. Karmada v1.15 has been released, this
  version includes the following new features: Precise resource awareness for multi-template
  workloads Enhanced cluster-level failover functionality Structured logging Significant
  performance improvements for Karmada controllers and schedulers Karmada utilizes
  a resource interpreter to retrieve the replica count and resource requests of workloads.
  Based on this data, it calculates the total resource requirements of the workloads,
  thereby enabling advanced capabilities such as resource-aware scheduling and federated
  quota management. This mechanism works well for traditional single-template workloads.
  However, many AI and big data application workloads (e. g. , FlinkDeployments, PyTorchJobs,
  and RayJobs) consist of multiple Pod templates or components, each with unique resource
  demands. Since the resource interpreter can only process resource requests from
  a single template and fails to accurately reflect differences between multiple templates,
  the resource calculation for multi-template workloads is not precise enough. In
  this version, Karmada has strengthened its resource awareness for multi-template
  workloads. By extending the resource interpreter, Karmada can now obtain the replica
  count and resource requests of different templates within the same workload, ensuring
  data accuracy. This improvement also provides more reliable and granular data support
  for federated quota management of multi-template workloads.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/10/07/karmada-v1-15-released-enhanced-resource-awareness-for-multi-template-workloads/
