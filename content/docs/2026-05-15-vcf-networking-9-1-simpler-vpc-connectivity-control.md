---
title: 'VCF Networking 9.1: Simpler VPC Connectivity Control'
date: '2026-05-15T22:45:58+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/05/15/vcf-networking-9-1-simpler-vpc-connectivity-control/
post_kind: link
draft: false
tldr: 'Related VCF Networking 9.1 Posts: Taking Control of Cross-VPC Communication
  The Three Connectivity Policies Real-World Use Case: Shared Services Summary VCF
  9.1 VPC Connectivity Demo Discover more from VMware Cloud Foundation (VCF) Blog
  Related Articles Encrypted vMotion Offload to Intel QAT in VMware Cloud Foundation
  9.1 More Memory, Less Effort: Configuring Memory Tiering in VCF 9.1 Why APJ Networking
  Professionals Need Private Cloud Expertise Network Services Simpler VPC Connectivity
  Control Transit Gateway Connectivity Options Integration with Infoblox VMware Cloud
  Foundation (VCF) provides a robust suite of self-service networking capabilities
  (as covered in our previous post: [Link to: VCF 9.1 – Network Services]) In this
  blog, we zoom in on a powerful new feature introduced in VCF 9.1: Connectivity Policy
  for Virtual Private Clouds (VPCs). By default, applications in a VPC can communicate
  freely with other applications in other VPCs.'
summary: 'Related VCF Networking 9.1 Posts: Taking Control of Cross-VPC Communication
  The Three Connectivity Policies Real-World Use Case: Shared Services Summary VCF
  9.1 VPC Connectivity Demo Discover more from VMware Cloud Foundation (VCF) Blog
  Related Articles Encrypted vMotion Offload to Intel QAT in VMware Cloud Foundation
  9.1 More Memory, Less Effort: Configuring Memory Tiering in VCF 9.1 Why APJ Networking
  Professionals Need Private Cloud Expertise Network Services Simpler VPC Connectivity
  Control Transit Gateway Connectivity Options Integration with Infoblox VMware Cloud
  Foundation (VCF) provides a robust suite of self-service networking capabilities
  (as covered in our previous post: [Link to: VCF 9.1 – Network Services]) In this
  blog, we zoom in on a powerful new feature introduced in VCF 9.1: Connectivity Policy
  for Virtual Private Clouds (VPCs). By default, applications in a VPC can communicate
  freely with other applications in other VPCs. Restricting this traffic used to mean
  relying on the vDefend Firewall Add-on. Starting with VCF 9.1, you can natively
  manage cross-VPC communication using Connectivity Policy to your VPCs , and dictate
  their routing boundaries without any firewall. VCF 9.1 introduces three distinct
  policy types to govern how your VPCs interact within a project: Community : Group
  specific VPCs together under a shared community policy. Applications within these
  VPCs can communicate seamlessly with others in the exact same community, but are
  strictly isolated from any VPCs outside of it. Promiscuous : VPCs assigned this
  policy act as open VPC. A promiscuous VPC is allowed to communicate with any other
  VPC in the project. Isolated : VPCs in this group are highly restricted. An isolated
  VPC cannot communicate with other community VPCs; it can only communicate with VPCs
  designated as Promiscuous. These connectivity policies provide a remarkably simple
  way to architect project environments. For example, imagine you need a Shared Services
  VPC (housing DNS, Active Directory, or logging tools) that every application in
  their VPC needs to access, while keeping those isolated from one another.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/05/15/vcf-networking-9-1-simpler-vpc-connectivity-control/
