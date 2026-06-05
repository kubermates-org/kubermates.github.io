---
title: Mastering Infrastructure Policies in VMware Cloud Foundation Automation 9.1
date: '2026-05-28T16:51:23+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/05/28/vcf-automation-infrastructure-policies/
post_kind: link
draft: false
tldr: 'Table of contents Bridging the Gap: VCF Automation Infrastructure Policies
  and vSphere Compute Policies Provider Administrator Optional vs. Mandatory Policies
  Using the Criteria Builder Apply Policies to the Region Quota Organization Administrator:
  Adding Infrastructure Policies to Namespaces Organization User: Consuming Infrastructure
  Policies in Deployments Complete Example Workflow Try It Out in VMware Hands-on
  Labs Discover more from VMware Cloud Foundation (VCF) Blog Related Articles VCF
  Breakroom Chats Episode 85 – Cloning Success at Scale: Inside VCF 9.1’s App Stack
  Formation Unlocking the Full Potential of Programmable Infrastructure with VMware
  Cloud Foundation 9.1 - New Features and Capabilities Modernizing Your Infrastructure:
  Introducing VMware Cloud Foundation 9.1 to VCSPs With the release of VMware Cloud
  Foundation (VCF) 9.1, VMware has introduced a modernized management architecture
  designed to streamline private cloud operations.'
summary: 'Table of contents Bridging the Gap: VCF Automation Infrastructure Policies
  and vSphere Compute Policies Provider Administrator Optional vs. Mandatory Policies
  Using the Criteria Builder Apply Policies to the Region Quota Organization Administrator:
  Adding Infrastructure Policies to Namespaces Organization User: Consuming Infrastructure
  Policies in Deployments Complete Example Workflow Try It Out in VMware Hands-on
  Labs Discover more from VMware Cloud Foundation (VCF) Blog Related Articles VCF
  Breakroom Chats Episode 85 – Cloning Success at Scale: Inside VCF 9.1’s App Stack
  Formation Unlocking the Full Potential of Programmable Infrastructure with VMware
  Cloud Foundation 9.1 - New Features and Capabilities Modernizing Your Infrastructure:
  Introducing VMware Cloud Foundation 9.1 to VCSPs With the release of VMware Cloud
  Foundation (VCF) 9.1, VMware has introduced a modernized management architecture
  designed to streamline private cloud operations. Among the most exciting features
  are the new Infrastructure Policies. Let’s look at the benefits of integrating Infrastructure
  Policies into your environments to ensure optimal workload placement, license compliance,
  and governance. The new VCF Automation Infrastructure Policies provide the ability
  for administrators to dynamically govern VM placement across various zones. Whether
  you are aiming for license optimization by pinning Windows workloads to specific
  hosts, or ensuring regulatory compliance by strictly controlling where specific
  apps reside, Infrastructure Policies allow you to enforce these rules systematically
  without manual toil. Bridging the Gap: VCF Automation Infrastructure Policies and
  vSphere Compute Policies Provider Administrator Optional vs. Mandatory Policies
  Using the Criteria Builder Apply Policies to the Region Quota Optional vs. Mandatory
  Policies Using the Criteria Builder Apply Policies to the Region Quota Organization
  Administrator: Adding Infrastructure Policies to Namespaces Organization User: Consuming
  Infrastructure Policies in Deployments Complete Example Workflow Try It Out in VMware
  Hands-on Labs Try It Out in VMware Hands-on Labs Historically, Infrastructure Administrators
  have created Compute Policies to ensure workloads are placed on compatible hosts.
  These policies are based on key value pairs like category and tag, where administrators
  can create categories and tags for host and VMs to ensure the host tags running
  the VM are compatible with the tags applied to the VM. Now, let’s review how VCF
  Automation interacts with your underlying infrastructure. An Infrastructure Policy
  in VCF Automation acts as a bridge to your vCenter configurations.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/05/28/vcf-automation-infrastructure-policies/
