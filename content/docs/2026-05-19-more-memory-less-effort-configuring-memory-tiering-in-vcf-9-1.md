---
title: 'More Memory, Less Effort: Configuring Memory Tiering in VCF 9.1'
date: '2026-05-19T13:00:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/05/19/more-memory-less-effort-configuring-memory-tiering-in-vcf-9-1/
post_kind: link
draft: false
tldr: 'Introduction Prerequisites Step-by-Step Configuration Step 1: Navigate to the
  Cluster Configuration Profile Step 2: Create a New Draft Step 3: Enable Memory Tiering
  (Minimum Configuration) Step 4 (Optional but Recommended): Enable Software Mirroring
  Step 5 (Optional): Enable Encryption Step 6 (Optional): Set the DRAM-to-NVMe Memory
  Ratio Step 7: Save and Review the Draft Step 8: Apply the Configuration Monitoring
  After Configuration Wrapping Up Discover more from VMware Cloud Foundation (VCF)
  Blog Related Articles Encrypted vMotion Offload to Intel QAT in VMware Cloud Foundation
  9.1 Increase Deployment Flexibility with VCF Edge Automation 1.0.3 More Memory,
  Less Effort: Configuring Memory Tiering in VCF 9.1 Memory Tiering in VCF 9.1 lets
  you extend your memory capacity by using high-speed NVMe devices as a Tier 1 layer
  alongside DRAM (Tier 0), and the business case is compelling. You can consolidate
  more VMs per host , lower your TCO by delaying costly DRAM upgrades, and consume
  existing resources far more efficiently.'
summary: 'Introduction Prerequisites Step-by-Step Configuration Step 1: Navigate to
  the Cluster Configuration Profile Step 2: Create a New Draft Step 3: Enable Memory
  Tiering (Minimum Configuration) Step 4 (Optional but Recommended): Enable Software
  Mirroring Step 5 (Optional): Enable Encryption Step 6 (Optional): Set the DRAM-to-NVMe
  Memory Ratio Step 7: Save and Review the Draft Step 8: Apply the Configuration Monitoring
  After Configuration Wrapping Up Discover more from VMware Cloud Foundation (VCF)
  Blog Related Articles Encrypted vMotion Offload to Intel QAT in VMware Cloud Foundation
  9.1 Increase Deployment Flexibility with VCF Edge Automation 1.0.3 More Memory,
  Less Effort: Configuring Memory Tiering in VCF 9.1 Memory Tiering in VCF 9.1 lets
  you extend your memory capacity by using high-speed NVMe devices as a Tier 1 layer
  alongside DRAM (Tier 0), and the business case is compelling. You can consolidate
  more VMs per host , lower your TCO by delaying costly DRAM upgrades, and consume
  existing resources far more efficiently. The hypervisor manages data placement automatically,
  so your workloads get more addressable memory without any major hardware changes.
  What makes VCF 9.1 a genuine leap forward is how dramatically simpler the configuration
  experience has become. The entire setup happens in one place ; vSphere Configuration
  Profiles, through a guided point-and-click workflow that applies consistently across
  every host in your cluster. No ESX CLI commands, no scripts, no manual host-by-host
  coordination. VCF 9.1 also introduces software mirroring as a brand-new feature,
  delivering enterprise-grade Tier 1 memory redundancy with no additional RAID controllers
  required. Before we dive in, let’s make sure you’ve got the right pieces in place.
  VMware Cloud Foundation 9.1 deployed and operational. A cluster with compatible
  NVMe devices — one per host for basic tiering, two per host if you want software
  mirroring. Administrative permissions to manage cluster configuration profiles.
  vMotion-compatible VMs so the automation can live-migrate workloads during each
  host’s maintenance window.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/05/19/more-memory-less-effort-configuring-memory-tiering-in-vcf-9-1/
