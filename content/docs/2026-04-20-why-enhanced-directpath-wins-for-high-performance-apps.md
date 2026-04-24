---
title: Why Enhanced DirectPath Wins for High-Performance Apps
date: '2026-04-20T19:11:14+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/04/20/why-enhanced-directpath-wins-for-high-performance-apps/
post_kind: link
draft: false
tldr: 'Navigating the Passthrough Maze: Why Enhanced DirectPath Wins Enhanced DirectPath
  Overview Comparing Passthrough Technologies Fixed DirectPath (PCI Passthrough) Dynamic
  DirectPath Overview of Technologies Use Cases for Enhanced DirectPath Supported
  Devices for Enhanced DirectPath Final Thoughts Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles How VMware Salt Automates Compliance Across Private
  Cloud Analyst Insight Series #2: Operational Scalability and Lifecycle Management
  Analyst Insight Series #1: Unified Self-Service Consumption for Modern Workloads
  If you take a quick look through the vCenter UI, you’ll encounter a wide array of
  passthrough technologies: Fixed DirectPath (formerly just DirectPath or PCI Passthrough),
  Dynamic DirectPath, and Enhanced DirectPath. It can get confusing fast, not just
  regarding the technical differences, but how to best leverage them in your environment.'
summary: 'Navigating the Passthrough Maze: Why Enhanced DirectPath Wins Enhanced DirectPath
  Overview Comparing Passthrough Technologies Fixed DirectPath (PCI Passthrough) Dynamic
  DirectPath Overview of Technologies Use Cases for Enhanced DirectPath Supported
  Devices for Enhanced DirectPath Final Thoughts Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles How VMware Salt Automates Compliance Across Private
  Cloud Analyst Insight Series #2: Operational Scalability and Lifecycle Management
  Analyst Insight Series #1: Unified Self-Service Consumption for Modern Workloads
  If you take a quick look through the vCenter UI, you’ll encounter a wide array of
  passthrough technologies: Fixed DirectPath (formerly just DirectPath or PCI Passthrough),
  Dynamic DirectPath, and Enhanced DirectPath. It can get confusing fast, not just
  regarding the technical differences, but how to best leverage them in your environment.
  Historically, choosing a passthrough technology meant making a massive trade-off.
  You were fundamentally giving up core virtualization features in exchange for raw
  performance. It was a tough question of what you valued more: performance or manageability?
  Because many core VMware vSphere features, including vMotion, Live Patch, and Suspend/Resume,
  were reserved for virtual devices, enabling a passthrough architecture created serious
  headaches for Day 2 operations. Maintenance windows meant downtime and limited workload
  residency. However, as GPUs, AI accelerators, high-performance NICs, and crypto/compression
  accelerators have become standard in the modern data center, we realized you shouldn’t
  have to choose between performance and manageability. We needed passthrough performance
  while retaining core virtualization features, bridging the gap between raw hardware
  speed and the VMware Cloud Foundation (VCF) features you rely on every day. In this
  blog, I’ll provide an overview of Enhanced DirectPath, compare it to existing passthrough
  models, and highlight why it’s the bridge between hardware performance and flexibility.
  Introduced in vSphere 8, Enhanced DirectPath builds upon the DirectPath I/O framework
  by introducing a new API for hardware-backed virtual devices. It provides near-native
  performance, but for the first time, it pairs them with essential vSphere features
  like vMotion, Live Patch, and Suspend/Resume. This isn’t just for one niche; multiple
  device classes can take advantage of it, including AI accelerators, high-performance
  NICs, FPGAs, and GPUs.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/04/20/why-enhanced-directpath-wins-for-high-performance-apps/
