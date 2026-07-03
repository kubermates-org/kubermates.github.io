---
title: Understanding dynamic resource allocation in Kubernetes
date: '2026-07-01T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/07/01/understanding-dynamic-resource-allocation-in-kubernetes/
post_kind: link
draft: false
tldr: 'CNTUG Infra Labs: Lab environment overview Lab Environment Installing NVIDIA
  GPU Operator Installing NVIDIA DRA Driver GPU A first look at DRA ResourceSlice
  ResourceClaim & ResourceClaimTemplate Hands-On with DRA Scenario I: Two Containers
  Sharing One GPU Scenario II: ResourceClaimTemplate — Prefer A5000 in a Deployment
  Scenario III: GPUs With at Least 20 GiB of Memory Scenario IV: GPU Time Slicing
  in DRA Posted on July 1, 2026 by ChengHao Yang, CNCF Ambassador CNCF projects highlighted
  in this post Dynamic Resource Allocation (DRA) recently reached GA in Kubernetes
  v1.35, and I believe many of us are eager to give it a try. Adding to the momentum,
  NVIDIA has moved dra-driver-nvidia-gpu into Kubernetes SIGs, with the documentation
  dropping the Beta label — a sign that the technology and its standards are gradually
  maturing.'
summary: 'CNTUG Infra Labs: Lab environment overview Lab Environment Installing NVIDIA
  GPU Operator Installing NVIDIA DRA Driver GPU A first look at DRA ResourceSlice
  ResourceClaim & ResourceClaimTemplate Hands-On with DRA Scenario I: Two Containers
  Sharing One GPU Scenario II: ResourceClaimTemplate — Prefer A5000 in a Deployment
  Scenario III: GPUs With at Least 20 GiB of Memory Scenario IV: GPU Time Slicing
  in DRA Posted on July 1, 2026 by ChengHao Yang, CNCF Ambassador CNCF projects highlighted
  in this post Dynamic Resource Allocation (DRA) recently reached GA in Kubernetes
  v1.35, and I believe many of us are eager to give it a try. Adding to the momentum,
  NVIDIA has moved dra-driver-nvidia-gpu into Kubernetes SIGs, with the documentation
  dropping the Beta label — a sign that the technology and its standards are gradually
  maturing. For this post, I borrowed all the NVIDIA GPUs currently available at CNTUG
  Infra Labs to learn how to elegantly allocate devices and resources with DRA. CNTUG
  Infra Labs was founded to nurture the next generation of students and engineers
  in Taiwan’s software infrastructure field. The lab is hosted in Equinix’s Tokyo
  data center and is jointly funded by several CNTUG community members. Building the
  environment leverages a stack of open source projects, including OpenStack, Ceph,
  and Ansible. Since infrastructure software has a steep learning curve and requires
  substantial compute, storage, and network resources, CNTUG Infra Labs aims to provide
  a cloud platform where students and community members can experiment with and host
  related services. Spare capacity is also offered to the open source community for
  hosting services such as websites, Mattermost, and Jitsi Meet, or for workshop events.
  You can review the use cases for more details. We’ll use a Kubernetes cluster built
  with Cluster API + OpenStack. For brevity, the setup process is omitted here — feel
  free to refer to other blog posts for the details, or wait for a future post once
  I finish writing it up. OS: Ubuntu 24.04 Kubernetes v1.35.3 Containerd 2.2.2 Node:
  1 Control Plane + etcd 3 Workers No GPU T10 * 2 A5000 * 1 NVIDIA GPU Operator v26.3.1
  NVIDIA DRA Driver GPU v25.12.0 Running kubectl get node should return something
  like: NAME STATUS ROLES AGE VERSION capi-dralabs-control-plane-xtcth Ready control-plane
  8m7s v1.35.3 capi-dralabs-md-0-p4xkh-rpfxc Ready <none> 6m55s v1.35.3 capi-dralabs-md-gpua5000-jw4mx-d64jz
  Ready <none> 2m37s v1.35.3 capi-dralabs-md-gput10-gzl84-f2m2d Ready <none> 6m49s
  v1.35.3 NAME STATUS ROLES AGE VERSION capi-dralabs-control-plane-xtcth Ready control-plane
  8m7s v1.35.3 capi-dralabs-md-0-p4xkh-rpfxc Ready <none> 6m55s v1.35.3 capi-dralabs-md-gpua5000-jw4mx-d64jz
  Ready <none> 2m37s v1.35.3 capi-dralabs-md-gput10-gzl84-f2m2d Ready <none> 6m49s
  v1.35.3 Before installing the GPU Operator, label the Nodes that have GPUs.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/07/01/understanding-dynamic-resource-allocation-in-kubernetes/
