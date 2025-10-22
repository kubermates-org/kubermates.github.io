---
title: 'Applying RBAC to databases on Kubernetes: Practical, real-world examples'
date: '2025-10-21T14:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/10/21/applying-rbac-to-databases-on-kubernetes-practical-real-world-examples/
post_kind: link
draft: false
tldr: Introduction Why RBAC is important for managing databases How RBAC works in
  Kubernetes-based platforms Enabling RBAC Why Everest implements its own RBAC layer?
  Inside RBAC policy (Everest Example) Common RBAC roles in practice Validating and
  testing policies Best practices for RBAC in stateful workloads Conclusion Posted
  on October 21, 2025 by Edith Puclla, Percona CNCF projects highlighted in this post
  Role-Based Access Control (RBAC) is one of the most important security features
  in any cloud native platform. It determines who can do what inside the Kubernetes
  Cluster , helping teams give the right access to the right people, keep systems
  safer, and make permissions easy to manage.
summary: 'Introduction Why RBAC is important for managing databases How RBAC works
  in Kubernetes-based platforms Enabling RBAC Why Everest implements its own RBAC
  layer? Inside RBAC policy (Everest Example) Common RBAC roles in practice Validating
  and testing policies Best practices for RBAC in stateful workloads Conclusion Posted
  on October 21, 2025 by Edith Puclla, Percona CNCF projects highlighted in this post
  Role-Based Access Control (RBAC) is one of the most important security features
  in any cloud native platform. It determines who can do what inside the Kubernetes
  Cluster , helping teams give the right access to the right people, keep systems
  safer, and make permissions easy to manage. Learn how to apply Role-Based Access
  Control (RBAC) to manage database workloads safely and effectively on Kubernetes.
  Using Percona Everest as an example, this post demonstrates how to implement roles
  for developers, DBAs, and operators — with step-by-step policies and best practices.
  In the Kubernetes ecosystem, RBAC is usually discussed in the context of pods, nodes,
  or cluster-level resources, and when it comes to stateful workloads, especially
  databases, RBAC becomes even more critical. Databases carry sensitive data, backups,
  and credentials, so you want developers, DBAs, and operators to have the right level
  of access, no more, no less. In this post, I’ll use a database management platform
  running on Kubernetes as a case study to walk through RBAC concepts. Specifically,
  I’ll use Percona Everest , an open-source platform for running and managing databases
  on Kubernetes. Everest provides a UI, CLI, and API to create and manage PostgreSQL
  , MongoDB , and MySQL clusters. I will show examples using Everest’s RBAC, but the
  principles apply to any Kubernetes database platform. Note: Kubernetes already includes
  RBAC to manage access to cluster resources like pods and nodes. Platform like Percona
  Everest build on top of this their own RBAC layer for database-specific actions
  (clusters, backups, restores), and this post focuses on that layer.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/10/21/applying-rbac-to-databases-on-kubernetes-practical-real-world-examples/
