---
title: 'K3s on On-Prem Infrastructures the GitOps Way: Writing a Custom k0rdent Template
  from Scratch'
date: '2026-04-17T11:59:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/04/17/k3s-on-on-prem-infrastructures-the-gitops-way-writing-a-custom-k0rdent-template-from-scratch/
post_kind: link
draft: false
tldr: 'The Big Picture Why On-Prem + k0rdent Makes Sense Step 1: Infrastructure Provider
  (BYOT) Why Bring Your Own Template? What the Helm Chart Does Step 2: Control Plane
  Provider Step 3: Bootstrapping Kubernetes with K3s What the Bootstrap Provider Does
  How k0rdent Ties It All Together What You End Up With Posted on April 17, 2026 by
  Shivani Rathod (Improwised Tech) & Prithvi Raj (CNCF Ambassador) CNCF projects highlighted
  in this post Kubernetes turns 12 this year. In that time, it’s gone from a Google
  side project to the operating system of modern infrastructure running everywhere
  from mainframes to GPUs, across multi-cloud, hybrid, on-prem, and edge environments.'
summary: 'The Big Picture Why On-Prem + k0rdent Makes Sense Step 1: Infrastructure
  Provider (BYOT) Why Bring Your Own Template? What the Helm Chart Does Step 2: Control
  Plane Provider Step 3: Bootstrapping Kubernetes with K3s What the Bootstrap Provider
  Does How k0rdent Ties It All Together What You End Up With Posted on April 17, 2026
  by Shivani Rathod (Improwised Tech) & Prithvi Raj (CNCF Ambassador) CNCF projects
  highlighted in this post Kubernetes turns 12 this year. In that time, it’s gone
  from a Google side project to the operating system of modern infrastructure running
  everywhere from mainframes to GPUs, across multi-cloud, hybrid, on-prem, and edge
  environments. The CNCF landscape has grown alongside it, filling in the gaps that
  Kubernetes left open. This blog isn’t about all of those gaps. It’s about one specific
  intersection: lightweight Kubernetes with K3s on an on-premise infrastructure (in
  this case Proxmox) and declarative multi-cluster management with k0rdent. If you’ve
  run Kubernetes on on-prem infrastructure, you know the pain: Manual VM creation
  Bash scripts that only you understand Clusters that work once, and then become untouchable
  We wanted something declarative, repeatable, and clean, but still friendly to an
  on-prem setup. That’s where k0rdent, Proxmox, and K3s came together. In this blog,
  we’ll walk through how we curated a use case for provisioning and used k0rdent to
  provision a K3s cluster on an On-premise environment by writing our own Helm charts
  and using k0rdent’s Bring Your Own Template (BYOT) approach. This isn’t a theoretical
  post, this is exactly how our cluster gets created. Here’s what we set out to build:
  Many end-users host their infrastructure layer on-premise, let us build that for
  you. Existing VM templates instead of building images every time k0rdent managing
  the full cluster lifecycle K3s as the Kubernetes bootstrap At a high level, the
  flow looks like this: User → k0rdent ↓ Proxmox Infrastructure (BYOT VMs) ↓ Control
  Plane Provider ↓ Bootstrap Provider (K3s) ↓ Running Kubernetes Cluster Each layer
  does one job, and does it well. Proxmox is one of the examples of a self-hosted
  environment, but Kubernetes on-prem often ends up being hand-crafted, hard to scale,
  and harder to reproduce.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/04/17/k3s-on-on-prem-infrastructures-the-gitops-way-writing-a-custom-k0rdent-template-from-scratch/
