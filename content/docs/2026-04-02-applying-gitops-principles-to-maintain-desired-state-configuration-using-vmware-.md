---
title: Applying GitOps Principles to Maintain Desired State Configuration using VMware
  vSphere Configuration Profile – Part 3
date: '2026-04-02T09:12:12+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/04/02/applying-gitops-principles-to-maintain-desired-state-configuration-using-vmware-vsphere-configuration-profile-part-3/
post_kind: link
draft: false
tldr: 'What is Infrastructure as Code (IaC)? The Scenario The Solution: GitOps Powered
  by VCP APIs Understanding Github Repository Global Intent File (vcp_managed_clusters.
  yaml) Managed Folders (vc-*/) Config JSON (*.'
summary: 'What is Infrastructure as Code (IaC)? The Scenario The Solution: GitOps
  Powered by VCP APIs Understanding Github Repository Global Intent File (vcp_managed_clusters.
  yaml) Managed Folders (vc-*/) Config JSON (*. json) Under the Hood: How Automation
  Works Smart Change Detection Asynchronous Lifecycle Management Safety First: Run
  Draft Validation Sample Run: End-to-End Workflow Onboarding a Cluster Day-2 Operations
  – Update/Modify Cluster Configuration Implementation Note Conclusion Demo Important
  Links Discover more from VMware Cloud Foundation (VCF) Blog Related Articles Applying
  GitOps Principles to Maintain Desired State Configuration using VMware vSphere Configuration
  Profile - Part 3 Accelerate Database as a Service with new VMware Data Services
  Manager Proof of Value Service from AxelCore Announcing the i7i. metal-24xl Instance
  for VMware Cloud on AWS Welcome back to the third blog post in the Automating vSphere
  Configuration Profile (VCP) workflows series. In the first post, we explored the
  VCP APIs and the set of APIs required to work with vSphere Configuration Profiles.
  The second post focused on consuming these APIs using PowerCLI and the Unified SDK
  for Python, demonstrating how they can be integrated into your Python and PowerCLI
  scripts. I highly recommend going through both of these posts to build the foundational
  understanding of VCP and its real-world use cases. Maintaining infrastructure configuration
  is a top priority for cloud architects and administrators. While the vSphere Client
  gives you a great high-level view of your environment, it becomes difficult to maintain
  consistency when managing configurations at scale, especially across multiple locations
  and clusters. Infrastructure as Code (IaC) solves this problem by allowing you to
  define and document infrastructure using code instead of manual UI operations. With
  IaC, you can: Version your configurations Apply consistent configurations across
  the entire SDDC Track configuration drifts In short, your infrastructure becomes
  repeatable, auditable, and automated. As a cloud administrator, you likely manage
  multiple VMware Cloud Foundation (VCF) instances, each with several workload domains
  and clusters.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/04/02/applying-gitops-principles-to-maintain-desired-state-configuration-using-vmware-vsphere-configuration-profile-part-3/
