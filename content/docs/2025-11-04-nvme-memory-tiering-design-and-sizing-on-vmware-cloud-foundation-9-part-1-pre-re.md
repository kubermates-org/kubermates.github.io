---
title: 'NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation 9 – Part
  1: Pre-requisites and Hardware Compatibility'
date: '2025-11-04T14:00:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/11/04/nvme-memory-tiering-design-and-sizing-on-vmware-cloud-foundation-9-part-1/
post_kind: link
draft: false
tldr: 'PART 1: Prerequisites and Hardware Compatibility Workload Assessment Software
  Pre-requisites NVMe Compatibility Discover more from VMware Cloud Foundation (VCF)
  Blog Related Articles SAP HANA and SAP NetWeaver Support for vSphere in VMware Cloud
  Foundation 9.0 on Intel Xeon 6 CPUs with P-core Systems Scaling VMware Cloud Foundation
  9.0 Lab Environments using Holodeck 9.0 VMware Cloud Foundation Automation - All
  Apps Organization Configurations At VMware Explore 2025 in Las Vegas, a plethora
  of announcements were made as well as many deep dives into the new features and
  enhancements included in VMware Cloud Foundation (VCF) 9, including the popular
  NVMe Memory Tiering feature. Although this feature is available at the compute component
  of VCF (vSphere), we refer to it in the context of VCF given the deep integration
  with other components such as VCF Operations, which we will refer to in later blogs.'
summary: 'PART 1: Prerequisites and Hardware Compatibility Workload Assessment Software
  Pre-requisites NVMe Compatibility Discover more from VMware Cloud Foundation (VCF)
  Blog Related Articles SAP HANA and SAP NetWeaver Support for vSphere in VMware Cloud
  Foundation 9.0 on Intel Xeon 6 CPUs with P-core Systems Scaling VMware Cloud Foundation
  9.0 Lab Environments using Holodeck 9.0 VMware Cloud Foundation Automation - All
  Apps Organization Configurations At VMware Explore 2025 in Las Vegas, a plethora
  of announcements were made as well as many deep dives into the new features and
  enhancements included in VMware Cloud Foundation (VCF) 9, including the popular
  NVMe Memory Tiering feature. Although this feature is available at the compute component
  of VCF (vSphere), we refer to it in the context of VCF given the deep integration
  with other components such as VCF Operations, which we will refer to in later blogs.
  Memory Tiering is a new feature included with VMware Cloud Foundation and was one
  of the main topics of conversation for most of my sessions at VMware Explore 2025.
  I saw a lot of interest, and a lot of great questions came from our customers on
  adoption, use cases, etc. This is a multi-part blog series where I intend to help
  answer a lot of the common questions coming from our customers, partners, and internal
  staff. For a high level understanding of what Memory Tiering is, please refer to
  this blog. Before enabling Memory Tiering, a thorough assessment of your environment
  is crucial. Start by evaluating workloads in your datacenter and pay special attention
  to memory. One of the key measures we will look at is the active memory of the workload.
  For workloads to be an optimal candidate for Memory Tiering, we want the total active
  memory to be 50% or less of the DRAM capacity. Why 50% you ask? Well, the default
  configuration of Memory Tiering is to provide you with 100% more memory or 2x your
  memory. So, after enabling Memory Tiering, half of the memory will be coming from
  DRAM (Tier 0) and the other half comes from NVMe (Tier 1).'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/11/04/nvme-memory-tiering-design-and-sizing-on-vmware-cloud-foundation-9-part-1/
