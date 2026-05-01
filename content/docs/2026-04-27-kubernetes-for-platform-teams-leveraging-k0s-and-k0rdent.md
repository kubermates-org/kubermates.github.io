---
title: 'Kubernetes for platform teams: Leveraging k0s and k0rdent'
date: '2026-04-27T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/04/27/kubernetes-for-platform-teams-leveraging-k0s-and-k0rdent/
post_kind: link
draft: false
tldr: 'The scale problem nobody talks about enough What are we solving? A centralized
  control plane architecture A declarative cluster provisioning system A multi-cluster
  platform foundation The core shift: From cluster-centric to platform-centric Feel
  free to check out more on the k0s and k0rdent community Posted on April 27, 2026
  by Prithvi Raj (CNCF Ambassador) & Shivani Rathod (Bacancy Technology) CNCF projects
  highlighted in this post In our previous blog , we explored a GitOps use case for
  on-premises infrastructure, managing multiple clusters hosted on the k3s Kubernetes
  distribution using k0rdent. But the platform engineering ecosystem is vast, and
  one blog barely scratches the surface of what it takes to manage multi-cluster environments
  at ease, or to make the most of different Kubernetes distributions.'
summary: 'The scale problem nobody talks about enough What are we solving? A centralized
  control plane architecture A declarative cluster provisioning system A multi-cluster
  platform foundation The core shift: From cluster-centric to platform-centric Feel
  free to check out more on the k0s and k0rdent community Posted on April 27, 2026
  by Prithvi Raj (CNCF Ambassador) & Shivani Rathod (Bacancy Technology) CNCF projects
  highlighted in this post In our previous blog , we explored a GitOps use case for
  on-premises infrastructure, managing multiple clusters hosted on the k3s Kubernetes
  distribution using k0rdent. But the platform engineering ecosystem is vast, and
  one blog barely scratches the surface of what it takes to manage multi-cluster environments
  at ease, or to make the most of different Kubernetes distributions. Ultimately,
  success isn’t about running Kubernetes, it’s about running it at scale, efficiently,
  and consistently. That’s exactly what hosted control planes are designed to achieve.
  How do you manage dozens or hundreds of clusters without costs and complexity spiralling
  out of control? Open infrastructure is neither small nor shrinking. In fact, most
  practitioners I encounter day-to-day are running their workloads on OpenStack. And
  if you’re on OpenStack, the challenge of managing multi-cluster applications doesn’t
  just exist, it compounds. Every new cluster adds overhead, and that overhead adds
  up fast. This blog explores how combining k0s, k0rdent, and Hosted Control Planes
  (HCP) can give you a scalable, cost-efficient, and production-ready Kubernetes platform
  on OpenStack. In a typical Kubernetes setup, every cluster ships with its own dedicated
  control plane — meaning at least 3 nodes per cluster just for the control plane
  itself. Multiply that across dev, staging, and production environments, and you’re
  burning through resources before your first workload even lands. This is the problem
  Hosted Control Planes were built to solve.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/04/27/kubernetes-for-platform-teams-leveraging-k0s-and-k0rdent/
