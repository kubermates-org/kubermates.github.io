---
title: Automating vSphere Configuration Profile APIs – Part 2 – PowerCLI and Python
  Sample Code
date: '2026-02-18T08:42:17+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/02/18/automating-vsphere-configuration-profile-apis-part-2-powercli-and-python-sample-code/
post_kind: link
draft: false
tldr: 'Consuming VCP APIs Using PowerCLI SDK Getting Started Finding Your Command
  Consuming VCP APIs Using Unified VCF SDK for Python​​ Core Enhancements in VCF SDK
  9.0 How are VCP APIs Structured in VCF SDK? Python Key Takeaway Resources Next Steps
  Discover more from VMware Cloud Foundation (VCF) Blog Related Articles Case Study:
  Navigating VKS Upgrades – Balancing Infrastructure Constraints and Application Reality
  Platform Engineering Needs a Cloud Engine Unlocking the Power of AI: A Journey with
  VMware Private AI Foundation and NVIDIA Welcome back to our series on Automating
  vSphere Configuration Profile (VCP). In Part 1 , we broke down the core VCP APIs
  and how they maintain the “desired state” of vSphere clusters.'
summary: 'Consuming VCP APIs Using PowerCLI SDK Getting Started Finding Your Command
  Consuming VCP APIs Using Unified VCF SDK for Python​​ Core Enhancements in VCF SDK
  9.0 How are VCP APIs Structured in VCF SDK? Python Key Takeaway Resources Next Steps
  Discover more from VMware Cloud Foundation (VCF) Blog Related Articles Case Study:
  Navigating VKS Upgrades – Balancing Infrastructure Constraints and Application Reality
  Platform Engineering Needs a Cloud Engine Unlocking the Power of AI: A Journey with
  VMware Private AI Foundation and NVIDIA Welcome back to our series on Automating
  vSphere Configuration Profile (VCP). In Part 1 , we broke down the core VCP APIs
  and how they maintain the “desired state” of vSphere clusters. Now, it’s time to
  get hands-on with the code. This blog post explains how to consume these APIs using
  the tools most familiar to VI admins and developers: PowerCLI and Python. If you
  are already living in a PowerShell world, the PowerCLI SDK is your best friend.
  It provides direct, low-level access to the VMware Cloud Foundation (VCF) and vSphere
  Automation APIs, making it a natural fit for existing automation pipelines. Pro
  Tip: If you’re new to the latest SDK architecture, check out my recent blog post,
  Demystifying VCF PowerCLI 9.0 SDK , to understand how the new bindings work. To
  begin, ensure you have VCF PowerCLI 9.0 (or later) installed. The magic of this
  SDK lies in its discoverability; you don’t have to guess the command names if you
  already know the REST URI. The Get-vSphereOperation cmdlet is the “Rosetta Stone”
  for mapping REST APIs to PowerCLI. Let’s look at a common VCP task: checking a cluster’s
  enablement status. The Discovery Command: PowerShell Running this will return a
  CommandInfo object.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/02/18/automating-vsphere-configuration-profile-apis-part-2-powercli-and-python-sample-code/
