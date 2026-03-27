---
title: Unlocking Database Performance on Kubernetes with TuneDProfile in VKS 3.6
date: '2026-03-20T19:51:17+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/03/20/tunedprofile-vks-3-6-os-level-tuning-kubernetes/
post_kind: link
draft: false
tldr: 'The Shift Down: Platform Engineering 2.0 Architecture Deep Dive Zero-Touch
  Reboot Orchestration Why not just use allowedUnsafeSysctls ? Walkthrough: Deploying
  a Database-Optimized Node Pool Step 1: Define the Profile Step 2: Apply it to a
  Node Pool Advanced Pattern: The Heterogeneous Cluster Production Ready Defaults:
  The builtin-vks Profile Frequently Asked Questions Conclusion Discover more from
  VMware Cloud Foundation (VCF) Blog Related Articles 5 Things You Didn’t Know You
  Can Do With Traceflow Looking at Technology from a Different Perspective: Francesca
  Palazzo’s Approach to Customer Strategy with VMware Cloud Foundation Accelerating
  Customer Success with Expanded Partnerships across the Kubernetes Ecosystem TL;DR:
  VKS 3.6 introduces TuneDProfile , a declarative API for Kubernetes OS tuning. It
  replaces imperative scripts and unsafe sysctls with a supported, Kubernetes-native
  approach.'
summary: 'The Shift Down: Platform Engineering 2.0 Architecture Deep Dive Zero-Touch
  Reboot Orchestration Why not just use allowedUnsafeSysctls ? Walkthrough: Deploying
  a Database-Optimized Node Pool Step 1: Define the Profile Step 2: Apply it to a
  Node Pool Advanced Pattern: The Heterogeneous Cluster Production Ready Defaults:
  The builtin-vks Profile Frequently Asked Questions Conclusion Discover more from
  VMware Cloud Foundation (VCF) Blog Related Articles 5 Things You Didn’t Know You
  Can Do With Traceflow Looking at Technology from a Different Perspective: Francesca
  Palazzo’s Approach to Customer Strategy with VMware Cloud Foundation Accelerating
  Customer Success with Expanded Partnerships across the Kubernetes Ecosystem TL;DR:
  VKS 3.6 introduces TuneDProfile , a declarative API for Kubernetes OS tuning. It
  replaces imperative scripts and unsafe sysctls with a supported, Kubernetes-native
  approach. Key features include per-pool granularity, automated drain-and-reboot
  handling for kernel changes, and a built-in “Production Ready” profile that fixes
  common Elasticsearch and database crashes out of the box. TuneDProfile Kubernetes
  is often described as a “leaky abstraction. ” While it does an incredible job of
  abstracting away underlying infrastructure, the reality is that containers are just
  processes sharing a kernel. When you deploy stateful, high-performance workloads—like
  Elasticsearch, Kafka, MongoDB, or Telco applications—that abstraction starts to
  leak. Suddenly, you aren’t just managing Pods; you’re debugging vm. max_map_count
  errors, tracing packet drops due to ring buffer exhaustion, or fighting latency
  jitter. vm. max_map_count In the past, solving these issues meant breaking the Kubernetes
  model. You might have baked custom OS images (creating a maintenance nightmare),
  run privileged DaemonSets to fundamentally alter the host (a security risk), or
  manually SSH-ed into nodes to tweak /proc/sys (creating “snowflake” servers). /proc/sys
  With vSphere Kubernetes Service (VKS) 3.6 , we are introducing a better way: TuneDProfile.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/03/20/tunedprofile-vks-3-6-os-level-tuning-kubernetes/
