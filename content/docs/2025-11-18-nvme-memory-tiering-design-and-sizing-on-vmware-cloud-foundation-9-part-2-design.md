---
title: 'NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation 9 Part 2:
  Design for Security, Redundancy, and Scalability'
date: '2025-11-18T12:00:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/11/18/nvme-memory-tiering-design-and-sizing-on-vmware-cloud-foundation-9-part-2/
post_kind: link
draft: false
tldr: 'Security Redundancy Scalability Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles Mapping VLAN Tags to Virtual Private Cloud Subnets Unified
  Authentication in VMware Cloud Foundation SDK 9.0: Seamless authentication across
  vSphere and vSAN APIs NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation
  9 Part 2: Design for Security, Redundancy, and Scalability In Part 1 of this series,
  we explored some of the pre-requisites for NVMe Memory Tiering such as workload
  assessment, memory activeness percentage, VM profile limitations, software pre-requisites,
  and compatibility of NVMe devices. In addition, we highlighted the importance of
  adopting VMware Cloud Foundation (VCF) 9, which could provide a significant cost
  reduction in memory, better CPU utilization and greater VM consolidation.'
summary: 'Security Redundancy Scalability Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles Mapping VLAN Tags to Virtual Private Cloud Subnets Unified
  Authentication in VMware Cloud Foundation SDK 9.0: Seamless authentication across
  vSphere and vSAN APIs NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation
  9 Part 2: Design for Security, Redundancy, and Scalability In Part 1 of this series,
  we explored some of the pre-requisites for NVMe Memory Tiering such as workload
  assessment, memory activeness percentage, VM profile limitations, software pre-requisites,
  and compatibility of NVMe devices. In addition, we highlighted the importance of
  adopting VMware Cloud Foundation (VCF) 9, which could provide a significant cost
  reduction in memory, better CPU utilization and greater VM consolidation. But before
  we can fully deploy this solution it is important we design with security, redundancy,
  and scalability in mind, and that is what this section is all about. Memory security
  is not necessarily a super popular topic for admins, and this is because memory
  is volatile. However attackers can leverage memory to store malicious information
  on non-volatile media to evade detection, but I digress – this is more a forensics
  topic (which I enjoy). Once power is no longer present the information on DRAM (volatile)
  disappears within minutes. So, with NVMe Memory Tiering we are moving pages from
  volatile (DRAM) to non-volatile media (NVMe). In order to address any security concerns
  with memory pages being stored on NVMe devices, we have come up with a couple of
  solutions that our customers can easily implement after initial configuration. With
  this first release of the Memory Tiering feature, encryption is already part of
  the package, and ready to be implemented out of the box. In fact, you have the option
  to encrypt at the VM level (per VM) or at the host level (all VMs in the host).
  By default, this option is not enabled but can easily be added to your configuration
  within the vCenter UI. For NVMe Memory Tiering encryption we do not require a Key
  Management System (KMS) or Native Key Provider (NKP), instead, the key will be randomly
  generated at the kernel level by each host using AES-XTS encryption.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/11/18/nvme-memory-tiering-design-and-sizing-on-vmware-cloud-foundation-9-part-2/
