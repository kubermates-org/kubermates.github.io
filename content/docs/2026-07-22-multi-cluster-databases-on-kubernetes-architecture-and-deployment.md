---
title: 'Multi-Cluster databases on Kubernetes: Architecture and deployment'
date: '2026-07-22T11:42:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/07/22/multi-cluster-databases-on-kubernetes-architecture-and-deployment/
post_kind: link
draft: false
tldr: 'Introduction Single Point of Failure: The risk of a single-cluster setup. 1.'
summary: 'Introduction Single Point of Failure: The risk of a single-cluster setup.
  1. Defining Site Roles 2. Connecting Clusters with the MCS API How to Design for
  High Availability Deployment Workflow Failover Behavior: The Election Process Architecture
  After Failover Posted on July 22, 2026 by Edith Puclla (CNCF Ambassador) and Ivan
  Groenewold (Tech Lead, Percona for MongoDB) Running a database on Kubernetes is
  well understood. Running one that survives a complete regional failure, a corrupted
  control plane, or a severed network requires a fault-resistant architecture. This
  post walks through how to build a multi-cluster MongoDB deployment on Kubernetes
  that can withstand those failures. We will use the Percona Operator for MongoDB,
  an open-source Apache 2.0 Licensed Kubernetes Operator, as our example. For relational
  workloads, similar patterns are available through projects like Vitess and CloudNativePG.
  If you are new to multi-cluster MongoDB on Kubernetes, Ivan Groenewold’s post is
  a great place to start. It walks you through a complete multi-cluster setup you
  can follow hands-on. Standard Kubernetes excels at self-healing within a single
  cluster, automatically recovering from crashed Pods or failed Nodes. However, it
  has no built-in mechanism to handle failures at the cluster level itself: a regional
  outage, a corrupted control plane, or a network partition can take down your entire
  database with no automatic recovery path.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/07/22/multi-cluster-databases-on-kubernetes-architecture-and-deployment/
