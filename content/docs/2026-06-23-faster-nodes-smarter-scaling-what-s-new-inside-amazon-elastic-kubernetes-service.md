---
title: 'Faster nodes, smarter scaling: What’s new inside Amazon Elastic Kubernetes
  Service (Amazon EKS) Auto Mode'
date: '2026-06-23T15:39:02+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode/
post_kind: link
draft: false
tldr: 'Faster nodes, smarter scaling: What’s new inside Amazon Elastic Kubernetes
  Service (Amazon EKS) Auto Mode Runtime: Faster nodes, fewer surprises 39 percent
  faster node startup Memory stability with zram Faster container image pulls Automatic
  security hardening Compute: Scaling faster and smarter with Karpenter What changed
  Results Customer impact Storage: Smoother EBS integration Topology-aware volume
  scheduling Migration tooling Networking: Local-first, zero-configuration Node-local
  DNS Separate pod subnets and security groups IPv4 egress in IPv6 clusters DNS-based
  network policies Network Flow Monitor EFA support for ML/HPC on Auto Mode See it
  in your cluster Conclusion Getting started About the authors When you’re running
  production Kubernetes workloads, every second matters. The time a node takes to
  become ready, how quickly your cluster scales in response to a traffic spike, or
  how fast DNS resolves from a new pod—these non-functional characteristics aren’t
  flashy feature announcements, but they determine whether your applications feel
  responsive or sluggish under real-world conditions.'
summary: 'Faster nodes, smarter scaling: What’s new inside Amazon Elastic Kubernetes
  Service (Amazon EKS) Auto Mode Runtime: Faster nodes, fewer surprises 39 percent
  faster node startup Memory stability with zram Faster container image pulls Automatic
  security hardening Compute: Scaling faster and smarter with Karpenter What changed
  Results Customer impact Storage: Smoother EBS integration Topology-aware volume
  scheduling Migration tooling Networking: Local-first, zero-configuration Node-local
  DNS Separate pod subnets and security groups IPv4 egress in IPv6 clusters DNS-based
  network policies Network Flow Monitor EFA support for ML/HPC on Auto Mode See it
  in your cluster Conclusion Getting started About the authors When you’re running
  production Kubernetes workloads, every second matters. The time a node takes to
  become ready, how quickly your cluster scales in response to a traffic spike, or
  how fast DNS resolves from a new pod—these non-functional characteristics aren’t
  flashy feature announcements, but they determine whether your applications feel
  responsive or sluggish under real-world conditions. Since launching Amazon Elastic
  Kubernetes Service (Amazon EKS) Auto Mode , we’ve been focused on making the infrastructure
  beneath your workloads faster, more efficient, and more resilient—without requiring
  changes on your part. In this post, we walk through the performance and scalability
  improvements we shipped across the four pillars of EKS Auto Mode: runtime, compute,
  storage, and networking. Key takeaways: Node boot time reduced 39 percent (13 seconds
  faster) through startup detection optimization. Karpenter, the node lifecycle manager
  in EKS Auto Mode, delivers 43 percent faster scale-out. Consolidation is up to 69
  percent faster, with 30 percent more cluster capacity. Node-local DNS delivers sub-millisecond
  resolution without cluster-wide bottlenecks. Separate pod subnets and security groups
  bring enterprise networking to Auto Mode. All improvements ship automatically. No
  configuration changes are required for clusters already running EKS Auto Mode. EKS
  Auto Mode manages the node operating system, bootstrap process, and system daemons
  on your behalf.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode/
