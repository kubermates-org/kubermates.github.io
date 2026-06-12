---
title: 'Modern Automation with VMware Cloud Foundation Part 2: Modern Infrastructure
  as Code with VCF'
date: '2026-06-11T11:54:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/06/11/modern-automation-with-vmware-cloud-foundation-part-2-modern-infrastructure-as-code-with-vcf/
post_kind: link
draft: false
tldr: 'Dispatches from the Field: A Word on Automation Platforms Let’s Do Something
  on VCF, Shall We! Part 1: Formatting the Output with bash Part 2: The main. tf File
  Part 3: Running Terraform Apply Additional Resources Discover more from VMware Cloud
  Foundation (VCF) Blog Related Articles VCF Breakroom Chats Episode 87 – Governing
  the AI Private Cloud: Deep Dive into VCF 9.1 Infrastructure Placement Policies Deploying
  VMware Cloud Foundation Private AI Services: Navigating Supervisor Architectures
  With and Without NSX Modern Automation with VMware Cloud Foundation Part 2: Modern
  Infrastructure as Code with VCF In my last post , we learned about push-button automation
  with the UI provided by the SDDC Manager.'
summary: 'Dispatches from the Field: A Word on Automation Platforms Let’s Do Something
  on VCF, Shall We! Part 1: Formatting the Output with bash Part 2: The main. tf File
  Part 3: Running Terraform Apply Additional Resources Discover more from VMware Cloud
  Foundation (VCF) Blog Related Articles VCF Breakroom Chats Episode 87 – Governing
  the AI Private Cloud: Deep Dive into VCF 9.1 Infrastructure Placement Policies Deploying
  VMware Cloud Foundation Private AI Services: Navigating Supervisor Architectures
  With and Without NSX Modern Automation with VMware Cloud Foundation Part 2: Modern
  Infrastructure as Code with VCF In my last post , we learned about push-button automation
  with the UI provided by the SDDC Manager. We learned that the SDDC Manager allows
  us to manage the automation of new clusters, add new hosts into existing clusters,
  and that it can manage infrastructure across multiple vCenters Fleet -wide. Here,
  we are going to take a look at the infrastructure as code (IaC) approach and detail
  how we can leverage the VCF APIs to achieve a more automated way of provisioning
  and life-cycling VCF infrastructure. Talking to VMware engineers on the daily, I
  commonly get the question whether or not we “support Terraform” or if we “support
  Ansible”. Those are the wrong questions. We don’t care what tool you use: The advantage
  of using VCF is that we provide a standard and unified REST API endpoint that provides
  flexibility in automation platform choice. Here are some more details on that with
  VCF 9.1. Since a VCF Fleet allows you to have one single API endpoint to easily
  manage your entire VMware infrastructure, you won’t need to make multiple calls
  across multiple vCenters, ESX hosts, etc. Additionally, with unified policies and
  guardrails, they are all enforced/accessible through the set of VCF APIs. We have
  API reference docs for every VCF component. You can also access the local swagger
  documentation for all VCF components, like here is how to access that for VCF Operations.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/06/11/modern-automation-with-vmware-cloud-foundation-part-2-modern-infrastructure-as-code-with-vcf/
