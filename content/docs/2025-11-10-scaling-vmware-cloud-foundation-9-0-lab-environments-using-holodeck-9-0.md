---
title: Scaling VMware Cloud Foundation 9.0 Lab Environments using Holodeck 9.0
date: '2025-11-10T07:30:31+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/11/09/add-clusters-and-hosts-in-vcf-using-holodeck/
post_kind: link
draft: false
tldr: 'Adding Additional Hosts Adding Additional Clusters Conclusion References Discover
  more from VMware Cloud Foundation (VCF) Blog Related Articles VCF Breakroom Chats
  Episode 69 - Beyond vRA + NSX: Delivering Cloud-Native Networking with VCF 9 Virtual
  Private Clouds Scaling VMware Cloud Foundation 9.0 Lab Environments using Holodeck
  9.0 Enterprise customers can now deploy NVIDIA Run:ai on VMware Cloud Foundation
  When we started building Holodeck 9.0 , the goal was simple — to automate the provisioning
  of VMware Cloud Foundation (VCF) lab environments using nested ESXi hosts. What
  began as a development project soon became a tool we actively use for testing real-world
  VCF use cases.'
summary: 'Adding Additional Hosts Adding Additional Clusters Conclusion References
  Discover more from VMware Cloud Foundation (VCF) Blog Related Articles VCF Breakroom
  Chats Episode 69 - Beyond vRA + NSX: Delivering Cloud-Native Networking with VCF
  9 Virtual Private Clouds Scaling VMware Cloud Foundation 9.0 Lab Environments using
  Holodeck 9.0 Enterprise customers can now deploy NVIDIA Run:ai on VMware Cloud Foundation
  When we started building Holodeck 9.0 , the goal was simple — to automate the provisioning
  of VMware Cloud Foundation (VCF) lab environments using nested ESXi hosts. What
  began as a development project soon became a tool we actively use for testing real-world
  VCF use cases. One of Holodeck’s biggest strengths is its scalability and ease of
  use thus enabling you to easily expand your lab environment even after the initial
  deployment. If you’re setting up your lab for the first time, check out the official
  Holodeck 9.0 documentation for detailed guidance. In this post, I’ll walk you through
  how to add additional ESXi hosts or clusters to an existing Holodeck 9.0 environment.
  You can easily scale your environment by provisioning additional nested ESXi hosts
  using the New-HoloDeckESXiNodes cmdlet. This command automates the entire process
  of deploying nested ESX hosts, configures, powers on, and connects new hosts to
  the network based on your specified parameters such as CPU, memory, site (‘a’ or
  ‘b’), and vSAN mode (‘ESA’ or ‘OSA’). You can easily scale your environment by provisioning
  additional nested ESXi hosts using the New-HoloDeckESXiNodes cmdlet. This command
  automates the entire process of deploying nested ESX hosts, configures, powers on,
  and connects new hosts to the network based on your specified parameters such as
  CPU, memory, site (‘a’ or ‘b’), and vSAN mode (‘ESA’ or ‘OSA’). Start PowerShell:
  Run pwsh. Import the Holodeck configuration associated with your Holodeck instance.
  Run below command to add additional hosts With this flexibility, the new hosts are
  instantly ready for use.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/11/09/add-clusters-and-hosts-in-vcf-using-holodeck/
