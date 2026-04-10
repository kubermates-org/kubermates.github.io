---
title: 'VMware Cloud Foundation Edge 9.0: Two-Host Edge Site Deployment with Brownfield
  Import'
date: '2026-04-07T07:04:29+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/04/07/vcf-edge-brownfield-import-two-host-deployment/
post_kind: link
draft: false
tldr: 'Why Choose Two-Host VCF Edge Sites? VCF Edge Brownfield Import: Key Advantage
  s Two-Host VCF Edge Architecture Overview Prerequisites for VCF Edge Brownfield
  Import Part 1: Cluster Setup in vCenter Step 1: Deploy vSAN Witness VM in the management
  domain Step 2: Set up ESX Hosts, vCenter, and vSphere cluster at the edge site Part
  2: VCF Edge Brownfield Import Process Understanding Brownfield Import Initiate Brownfield
  Import Conclusion Discover more from VMware Cloud Foundation (VCF) Blog Related
  Articles VCF Edge 9.0: Single Host Edge Site Deployment VCF 9.0 for Edge: Automating
  App Deployment at Scale with GitOps using Argo CD Revolutionizing the Factory Floor:
  Introducing the Industrial vSwitch in VMware Cloud Foundation 9.0 In our previous
  blog post , we explored how VMware Cloud Foundation (VCF) Edge 9.0 enables organizations
  to deploy single-host edge sites that support both VM and container workloads, dramatically
  reducing edge footprint and capital expenditure. While single-host deployments excel
  in space-constrained environments, many organizations require additional resilience
  and capacity at their edge locations.'
summary: 'Why Choose Two-Host VCF Edge Sites? VCF Edge Brownfield Import: Key Advantage
  s Two-Host VCF Edge Architecture Overview Prerequisites for VCF Edge Brownfield
  Import Part 1: Cluster Setup in vCenter Step 1: Deploy vSAN Witness VM in the management
  domain Step 2: Set up ESX Hosts, vCenter, and vSphere cluster at the edge site Part
  2: VCF Edge Brownfield Import Process Understanding Brownfield Import Initiate Brownfield
  Import Conclusion Discover more from VMware Cloud Foundation (VCF) Blog Related
  Articles VCF Edge 9.0: Single Host Edge Site Deployment VCF 9.0 for Edge: Automating
  App Deployment at Scale with GitOps using Argo CD Revolutionizing the Factory Floor:
  Introducing the Industrial vSwitch in VMware Cloud Foundation 9.0 In our previous
  blog post , we explored how VMware Cloud Foundation (VCF) Edge 9.0 enables organizations
  to deploy single-host edge sites that support both VM and container workloads, dramatically
  reducing edge footprint and capital expenditure. While single-host deployments excel
  in space-constrained environments, many organizations require additional resilience
  and capacity at their edge locations. This post builds on that foundation by demonstrating
  a two-host edge site deployment pattern. We will also showcase how to leverage VCF’s
  brownfield import capability to bring in this two-host edge site under VCF management.
  This approach delivers significant operational benefits for organizations that need
  to standardize their edge infrastructure management while preserving their existing
  investments and configurations. A two-host deployment provides several advantages
  over single-host configurations: High Availability : With two hosts, vSphere HA
  can restart VMs on the surviving host during hardware failures, minimizing downtime
  for critical edge workloads Maintenance Flexibility : Perform rolling updates and
  maintenance without service interruption using vMotion to migrate workloads between
  hosts Enhanced Performance : Distribute workload demands across two physical hosts,
  reducing resource contention Growth Capacity : Start with two hosts and scale workloads
  without immediate hardware expansion Industries such as manufacturing facilities
  with 24/7 operations, retail locations requiring continuous point-of-sale availability,
  and healthcare facilities providing critical patient services benefit significantly
  from this deployment pattern. VCF’s brownfield import capability addresses a common
  enterprise challenge: integrating existing infrastructure into standardized management
  frameworks. Rather than requiring complete infrastructure rebuild, brownfield import:
  Preserves Existing Configurations : Maintains your current cluster setup and deployed
  workloads Reduces Migration Risk : Eliminates the need for workload migration and
  reconfiguration Accelerates VCF Adoption : Brings existing infrastructure under
  VCF management in hours, not weeks Enables Standardization : Applies consistent
  lifecycle management, security policies, and operational practices across all edge
  sites This approach proves particularly valuable for organizations with distributed
  edge locations where downtime for infrastructure conversion is not acceptable. The
  two-host edge site architecture builds upon the single-host design with enhanced
  resilience: Key Components: Two ESX Hosts : Provide HA capability and workload distribution
  at the edge site vSphere Distributed Switch (vDS) or NSX : Consistent network configuration
  across both hosts Shared Storage : We’ll make use of VMware vSAN in this example
  vSphere HA & DRS : Automated failover and resource optimization Supervisor Cluster
  : Optional Kubernetes control plane for container workloads VCF Management : Centralized
  lifecycle management, compliance, and operations Before beginning, ensure you have:
  VCF 9.0.2 Environment : VCF 9.0.2 Management Domain deployed in the primary data
  center Two ESX Hosts : VCF 9.0.2 compatible hardware meeting minimum specifications
  with ESX 9.0.2 installed Network Configuration : Appropriate VLANs and IP addressing
  for management, vMotion, and vSAN networks Storage : Either shared storage (SAN/NAS)
  or local disks for VMFS/vSAN configuration This section demonstrates creating a
  two-host vSAN cluster with witness VM in vCenter before importing it into VCF management.
  Download the vSAN Witness OVA from the Broadcom Support Portal for the specific
  version of VCF you are running (9.0.2 in this case) and deploy it on the management
  domain vCenter. Ensure that the network provided to the vSAN witness will be able
  to reach the edge site. Note: In this demo, we are deploying the vSAN witness VM
  in our central DC where the management domain is located to allow the same witness
  VM to be used by multiple edge sites to form the vSAN cluster.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/04/07/vcf-edge-brownfield-import-two-host-deployment/
