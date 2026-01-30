---
title: 'NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation 9 Part 7:
  Advanced Configuration'
date: '2026-01-27T14:00:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/01/27/nvme-memory-tiering-design-and-sizing-on-vmware-cloud-foundation-9-part-7/
post_kind: link
draft: false
tldr: 'Adjusting the DRAM:NVMe Ratio Securing the Tier: Encryption Option A: Host-Level
  Encryption Option B: Per-VM Encryption Opting Out: Disabling Memory Tiering for
  Critical VMs Summary of Advanced Parameters Final Thoughts Discover more from VMware
  Cloud Foundation (VCF) Blog Related Articles NVMe Memory Tiering Design and Sizing
  on VMware Cloud Foundation 9 Part 7: Advanced Configuration Automating Desired State
  Configuration using vSphere Configuration Profile APIs - Part 1 SAP HANA and SAP
  NetWeaver Support for vSphere in VMware Cloud Foundation 9.0 on Intel Xeon 6 CPUs
  with P-core and older CPUs This is the final installment of our series on Memory
  Tiering. In previous posts, we covered the architecture, design, sizing, and basic
  setup among other topics.'
summary: 'Adjusting the DRAM:NVMe Ratio Securing the Tier: Encryption Option A: Host-Level
  Encryption Option B: Per-VM Encryption Opting Out: Disabling Memory Tiering for
  Critical VMs Summary of Advanced Parameters Final Thoughts Discover more from VMware
  Cloud Foundation (VCF) Blog Related Articles NVMe Memory Tiering Design and Sizing
  on VMware Cloud Foundation 9 Part 7: Advanced Configuration Automating Desired State
  Configuration using vSphere Configuration Profile APIs - Part 1 SAP HANA and SAP
  NetWeaver Support for vSphere in VMware Cloud Foundation 9.0 on Intel Xeon 6 CPUs
  with P-core and older CPUs This is the final installment of our series on Memory
  Tiering. In previous posts, we covered the architecture, design, sizing, and basic
  setup among other topics. Now, we’re diving into the advanced configuration. These
  settings are not necessary for this feature to be operational, but rather provides
  options for data encryption, and memory ratios among others. While the defaults
  in vSphere in VMware Cloud Foundation 9.0 are designed to “just work” for most environments,
  true optimization requires fine-tuning. Whether you are running virtual desktop
  workloads or databases, you need to know which levers to pull. Here is how to master
  the advanced parameters for memory ratios, per host and per VM encryption, as well
  as disabling per-VM tiering. By default, when you enable Memory Tiering, ESX sets
  a DRAM to NVMe ratio of 1:1, or 100% more memory coming from NVMe. This means if
  you have 512GB of DRAM, the host will have an additional 512GB of NVMe capacity
  as Tier 1 memory, resulting in 1TB of total memory. However, depending on your workloads,
  you might want to change this density. For example, in a VDI environment where cost-per-desktop
  is king, you might want a higher ratio (more NVMe per GB of DRAM). Conversely, for
  performance-heavy clusters, you might want to limit the NVMe tier size.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/01/27/nvme-memory-tiering-design-and-sizing-on-vmware-cloud-foundation-9-part-7/
