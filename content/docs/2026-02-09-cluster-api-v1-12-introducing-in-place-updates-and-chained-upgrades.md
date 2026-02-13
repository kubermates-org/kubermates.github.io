---
title: 'Cluster API v1.12: Introducing in-place updates and chained upgrades'
date: '2026-02-09T12:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/02/09/cluster-api-v1-12-introducing-in-place-updates-and-chained-upgrades/
post_kind: link
draft: false
tldr: Emphasis on simplicity and usability In-place Updates Chained Upgrades Release
  team What’s next? Posted on February 9, 2026 by Fabrizio Pandini, Broadcom CNCF
  projects highlighted in this post Cluster API brings declarative management to Kubernetes
  cluster lifecycle, allowing users and platform teams to define the desired state
  of clusters and rely on controllers to continuously reconcile toward it. Similar
  to how you can use StatefulSets or Deployments in Kubernetes to manage a group of
  Pods, in Cluster API you can use KubeadmControlPlane to manage a set of control
  plane Machines, or you can use MachineDeployments to manage a group of worker Nodes.
summary: 'Emphasis on simplicity and usability In-place Updates Chained Upgrades Release
  team What’s next? Posted on February 9, 2026 by Fabrizio Pandini, Broadcom CNCF
  projects highlighted in this post Cluster API brings declarative management to Kubernetes
  cluster lifecycle, allowing users and platform teams to define the desired state
  of clusters and rely on controllers to continuously reconcile toward it. Similar
  to how you can use StatefulSets or Deployments in Kubernetes to manage a group of
  Pods, in Cluster API you can use KubeadmControlPlane to manage a set of control
  plane Machines, or you can use MachineDeployments to manage a group of worker Nodes.
  The Cluster API v1.12.0 release expands what is possible in Cluster API, reducing
  friction in common lifecycle operations by introducing in-place updates and chained
  upgrades. With v1.12.0, the Cluster API project demonstrates once again that this
  community is capable of delivering a great amount of innovation, while at the same
  time minimizing impact for Cluster API users. Users simply have to change the Cluster
  or the Machine spec (just as with previous Cluster API releases), and Cluster API
  will automatically trigger in-place updates or chained upgrades when possible and
  advisable. Like Kubernetes does for Pods in Deployments, when the Machine spec changes
  also Cluster API performs rollouts by creating a new Machine and deleting the old
  one. This approach, inspired by the principle of immutable infrastructure, has a
  set of considerable advantages: It is simple to explain, predictable, consistent
  and easy to reason about with users and engineers. It is simple to implement, because
  it relies only on two core primitives, create and delete. Implementation does not
  depend on Machine-specific choices, like OS, bootstrap mechanism etc. As a result,
  Machine rollouts drastically reduce the number of variables to be considered when
  managing the lifecycle of a host server that is hosting Nodes. However, while advantages
  of immutability are not under discussion, both Kubernetes and Cluster API are undergoing
  a similar journey, introducing changes that allow users to minimize workload disruption
  whenever possible. Over time, also Cluster API has introduced several improvements
  to immutable rollouts, including: Support for in-place propagation of changes affecting
  Kubernetes resources only , thus avoiding unnecessary rollouts A way to Taint outdated
  nodes with PreferNoSchedule , thus reducing Pod churn by optimizing how Pods are
  rescheduled during rollouts.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/02/09/cluster-api-v1-12-introducing-in-place-updates-and-chained-upgrades/
