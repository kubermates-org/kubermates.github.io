---
title: 'Kubernetes 1.36: What Actually Changed for Enterprise Platforms'
date: '2026-04-29T15:05:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/04/29/kubernetes-1-36-what-actually-changed-for-enterprise-platforms/
post_kind: link
draft: false
tldr: 'Kubernetes Is Becoming the Control Plane for AI Infrastructure Security Is
  No Longer a Choice Release Velocity Is Becoming an Operational Problem Kubernetes
  Is Becoming a Platform What This Means in Practice Looking Ahead References Discover
  more from VMware Cloud Foundation (VCF) Blog Related Articles How Many Users Can
  Your LLM Server Really Handle? From Infrastructure to Agents: A Hands-On Guide to
  Secure Private AI with Broadcom - Part 2 The New Frontier: Leading the Cloud-Native
  Evolution The release of Kubernetes 1.36 includes dozens of enhancements, updates,
  and deprecations. But for most enterprise teams, the details of each individual
  feature aren’t the most important part.'
summary: 'Kubernetes Is Becoming the Control Plane for AI Infrastructure Security
  Is No Longer a Choice Release Velocity Is Becoming an Operational Problem Kubernetes
  Is Becoming a Platform What This Means in Practice Looking Ahead References Discover
  more from VMware Cloud Foundation (VCF) Blog Related Articles How Many Users Can
  Your LLM Server Really Handle? From Infrastructure to Agents: A Hands-On Guide to
  Secure Private AI with Broadcom - Part 2 The New Frontier: Leading the Cloud-Native
  Evolution The release of Kubernetes 1.36 includes dozens of enhancements, updates,
  and deprecations. But for most enterprise teams, the details of each individual
  feature aren’t the most important part. What matters more is the direction these
  changes point to and what that means for Kubernetes’s evolution as a platform. One
  of the clearest signals in 1.36 is the continued investment in how Kubernetes handles
  specialized hardware, particularly GPUs. Work like Dynamic Resource Allocation (DRA)
  is about more than improving scheduling; it reflects a broader shift toward standardizing
  how Kubernetes interacts with high-value, constrained resources. A key advancement
  in 1.36 is the introduction of Structured Parameters for DRA. Previously, requesting
  complex resources often required opaque, vendor-specific blobs that were difficult
  for the scheduler to optimize. By moving toward a more structured approach, Kubernetes
  is making it easier for the scheduler to “understand” the specific requirements
  of a GPU or AI accelerator—drastically reducing the complexity of multi-node AI
  deployments. This shift matters because AI workloads behave very differently from
  traditional applications. Unlike standard web services that follow predictable,
  request-response patterns, AI workloads are often probabilistic and computationally
  “bursty. ” They involve different sets of inputs and outputs that require massive,
  parallel infrastructure demands; failing to place a pod correctly doesn’t just cause
  a slow response; it can stall an entire multi-node training job. Furthermore, AI
  introduces a much higher dependency on data gravity.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/04/29/kubernetes-1-36-what-actually-changed-for-enterprise-platforms/
