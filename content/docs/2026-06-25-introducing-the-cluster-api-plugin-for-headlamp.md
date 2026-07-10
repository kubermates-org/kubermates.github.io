---
title: Introducing the Cluster API plugin for Headlamp
date: '2026-06-25T14:00:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/06/25/headlamp-cluster-api-plugin/
post_kind: link
draft: false
tldr: Introducing the Cluster API plugin for Headlamp What this plugin provides A
  tour of the plugin Cluster API dashboard Bring full Cluster API visibility into
  Headlamp Explore Cluster API resources in a visual interface Scale workloads directly
  from Headlamp Inspect bootstrap configuration without raw YAML Visualize cluster
  relationships with map view Prometheus metrics integration How to use Developed
  during LFX Mentorship Feedback and questions Headlamp is an open-source, extensible
  Kubernetes SIG UI project designed to let you explore, manage, and debug cluster
  resources directly from a browser. Cluster API (CAPI) is a Kubernetes sub-project
  that brings declarative, Kubernetes-style APIs to cluster lifecycle management.
summary: Introducing the Cluster API plugin for Headlamp What this plugin provides
  A tour of the plugin Cluster API dashboard Bring full Cluster API visibility into
  Headlamp Explore Cluster API resources in a visual interface Scale workloads directly
  from Headlamp Inspect bootstrap configuration without raw YAML Visualize cluster
  relationships with map view Prometheus metrics integration How to use Developed
  during LFX Mentorship Feedback and questions Headlamp is an open-source, extensible
  Kubernetes SIG UI project designed to let you explore, manage, and debug cluster
  resources directly from a browser. Cluster API (CAPI) is a Kubernetes sub-project
  that brings declarative, Kubernetes-style APIs to cluster lifecycle management.
  It lets platform teams provision, upgrade, and manage the lifecycle of Kubernetes
  clusters using standard Kubernetes objects stored and reconciled in a management
  cluster. Managing Cluster API resources has historically required raw kubectl commands
  and deep familiarity with ownership hierarchies. The Headlamp Cluster API plugin
  brings visual clarity, faster debugging, and simplified operations for platform
  teams, directly inside Headlamp. kubectl The Cluster API plugin adds a dedicated
  Cluster API section to Headlamp and brings full visibility into core CAPI resources
  through consistent list and detail views. The Headlamp Cluster API plugin brings
  core Cluster API resources into a consistent, visual interface inside Headlamp.
  Here are some of the key views included in the first release. The dashboard provides
  a centralized view of Cluster API resources and their health across a management
  cluster. The overview summarizes the status of clusters, Machines, MachineDeployments,
  MachinePools, MachineSets, and control planes. It also highlights active condition
  issues, provider information, and configuration template counts to help operators
  quickly identify degraded or unhealthy resources. Selecting a cluster opens a detailed
  health view showing control plane and worker status, machine information, infrastructure
  details, and resource conditions.
---
Open the original post ↗ https://kubernetes.io/blog/2026/06/25/headlamp-cluster-api-plugin/
