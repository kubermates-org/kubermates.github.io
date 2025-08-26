---
title: The Cloud Controller Manager Chicken and Egg Problem
date: '2025-02-14T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/02/14/cloud-controller-manager-chicken-egg-problem/
post_kind: link
draft: false
tldr: Kubernetes 1.
summary: Kubernetes 1. 31 completed the largest migration in Kubernetes history ,
  removing the in-tree cloud provider. While the component migration is now done,
  this leaves some additional complexity for users and installer projects (for example,
  kOps or Cluster API). We will go over those additional steps and failure points
  and make recommendations for cluster owners. This migration was complex and some
  logic had to be extracted from the core components, building four new subsystems.
  The cloud controller manager is part of the control plane.
---
Open the original post ↗ https://kubernetes.io/blog/2025/02/14/cloud-controller-manager-chicken-egg-problem/
