---
title: The Cloud Controller Manager Chicken and Egg Problem
date: '2025-02-14T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/02/14/cloud-controller-manager-chicken-egg-problem/
post_kind: link
draft: false
tldr: Kubernetes 1. 31 completed the largest migration in Kubernetes history , removing
  the in-tree cloud provider.
summary: Kubernetes 1. 31 completed the largest migration in Kubernetes history ,
  removing the in-tree cloud provider. While the component migration is now done,
  this leaves some additional complexity for users and installer projects (for example,
  kOps or Cluster API). We will go over those additional steps and failure points
  and make recommendations for cluster owners. This migration was complex and some
  logic had to be extracted from the core components, building four new subsystems.
  The cloud controller manager is part of the control plane. It is a critical component
  that replaces some functionality that existed previously in the kube-controller-manager
  and the kubelet. Components of Kubernetes One of the most critical functionalities
  of the cloud controller manager is the node controller, which is responsible for
  the initialization of the nodes. As you can see in the following diagram, when the
  kubelet starts, it registers the Node object with the apiserver, Tainting the node
  so it can be processed first by the cloud-controller-manager. The initial Node is
  missing the cloud-provider specific information, like the Node Addresses and the
  Labels with the cloud provider specific information like the Node, Region and Instance
  type information. Chicken and egg problem sequence diagram This new initialization
  process adds some latency to the node readiness. Previously, the kubelet was able
  to initialize the node at the same time it created the node.
---
Open the original post ↗ https://kubernetes.io/blog/2025/02/14/cloud-controller-manager-chicken-egg-problem/
