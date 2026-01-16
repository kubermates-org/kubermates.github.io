---
title: 'NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation 9.0 Part
  6: End-to-End Configuration'
date: '2026-01-13T13:00:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/01/13/nvme-memory-tiering-design-and-sizing-on-vmware-cloud-foundation-9-0-part-6/
post_kind: link
draft: false
tldr: 'Configuration Steps Pre-Checks Partition Creation Enabling Memory Tiering Final
  Step Discover more from VMware Cloud Foundation (VCF) Blog Related Articles NVMe
  Memory Tiering Design and Sizing on VMware Cloud Foundation 9.0 Part 6: End-to-End
  Configuration NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation 9
  Part 5: Deployment Scenarios (Greenfield, Brownfield, Nested Lab) NVMe Memory Tiering
  Design and Sizing on VMware Cloud Foundation 9 Part 4: vSAN Compatibility and Storage
  Considerations Throughout this blog series, we’ve explored important aspects to
  consider before configuring Memory Tiering such as design, sizing, interoperability,
  redundancy, security, and much more. Now, it is time to apply what you’ve learned
  and optimize this feature for your environment, budget, and strategy.'
summary: 'Configuration Steps Pre-Checks Partition Creation Enabling Memory Tiering
  Final Step Discover more from VMware Cloud Foundation (VCF) Blog Related Articles
  NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation 9.0 Part 6: End-to-End
  Configuration NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation 9
  Part 5: Deployment Scenarios (Greenfield, Brownfield, Nested Lab) NVMe Memory Tiering
  Design and Sizing on VMware Cloud Foundation 9 Part 4: vSAN Compatibility and Storage
  Considerations Throughout this blog series, we’ve explored important aspects to
  consider before configuring Memory Tiering such as design, sizing, interoperability,
  redundancy, security, and much more. Now, it is time to apply what you’ve learned
  and optimize this feature for your environment, budget, and strategy. Since many
  existing documents and blogs cover the configuration steps in detail, this blog
  post will focus on a high-level approach and reference previous blog posts for specific
  sections. Always rely on the official Broadcom documentation for exact configuration
  steps, you can find the official guide here. I’ve also highlighted the steps in
  this blog post. Technically there are only two steps needed to configure Memory
  Tiering in your environment, but I’ve added pre- and post-configuration tasks to
  ensure due diligence and to verify the implementation. Many carpenters live by the
  rule “measure twice, cut once”, because you can’t add material back after the cut.
  To avoid critical errors during configuration, we must first verify that we have
  made the correct architectural decisions for our environment. Please ensure you
  have reviewed the following: PART 1 : NVMe endurance and performance classes PART
  2 : Redundancy and RAID controllers PART 3 : NVMe device sizing PART 4 : Interoperability
  with vSAN Once you’ve made all these important decisions, the pre-check step involves
  verifying that the devices show up properly on all ESX hosts. You will need the
  UID of each device to create the partition to be used by Memory Tiering. The first
  step is creating a partition for each NVMe device. Whether you are deploying a single
  device per host or leveraging hardware-based RAID, a partition is required on each
  logical NVMe device.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/01/13/nvme-memory-tiering-design-and-sizing-on-vmware-cloud-foundation-9-0-part-6/
