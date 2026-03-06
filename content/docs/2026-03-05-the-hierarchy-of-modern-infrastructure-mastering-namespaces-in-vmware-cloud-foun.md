---
title: 'The Hierarchy of Modern Infrastructure: Mastering Namespaces in VMware Cloud
  Foundation, vSphere Kubernetes Service, and VCF Automation'
date: '2026-03-05T22:02:45+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/03/05/the-hierarchy-of-modern-infrastructure-mastering-namespaces-in-vmware-cloud-foundation-vsphere-kubernetes-service-and-vcf-automation/
post_kind: link
draft: false
tldr: 'Layer 1: The VCF Automation Project (the Governance Layer) Layer 2: The vSphere
  Namespace (The Resource Boundary) Layer 3: The VKS Namespace (the Workload Layer)
  Operational Reality: Putting it All Together The Architecture Advantage: Why Structure
  (and Deletion) Matters Step 1: The Governance Layer – Business and Policy Tier (VCF
  Automation) Step 2: The Infrastructure Layer – Resource and Security Tier (vSphere
  Namespace) Step 3: The Workload Layer – Platform Tier (VKS Cluster) Step 4: The
  Application Layer (Kubernetes Namespace) Operationalizing the Design: How Broadcom
  Professional Services Assists Discover more from VMware Cloud Foundation (VCF) Blog
  Related Articles The Hierarchy of Modern Infrastructure: Mastering Namespaces in
  VMware Cloud Foundation, vSphere Kubernetes Service, and VCF Automation Mastering
  Application Migration to VKS: Patterns and Best Practices Case Study: Navigating
  VKS Upgrades – Balancing Infrastructure Constraints and Application Reality In the
  traditional vSphere environment, we functioned within a hierarchy of folders and
  resource pools. With the adoption of VMware Cloud Foundation (VCF) and especially
  VCF 9, the “Namespace” has emerged as the fundamental building block.'
summary: 'Layer 1: The VCF Automation Project (the Governance Layer) Layer 2: The
  vSphere Namespace (The Resource Boundary) Layer 3: The VKS Namespace (the Workload
  Layer) Operational Reality: Putting it All Together The Architecture Advantage:
  Why Structure (and Deletion) Matters Step 1: The Governance Layer – Business and
  Policy Tier (VCF Automation) Step 2: The Infrastructure Layer – Resource and Security
  Tier (vSphere Namespace) Step 3: The Workload Layer – Platform Tier (VKS Cluster)
  Step 4: The Application Layer (Kubernetes Namespace) Operationalizing the Design:
  How Broadcom Professional Services Assists Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles The Hierarchy of Modern Infrastructure: Mastering Namespaces
  in VMware Cloud Foundation, vSphere Kubernetes Service, and VCF Automation Mastering
  Application Migration to VKS: Patterns and Best Practices Case Study: Navigating
  VKS Upgrades – Balancing Infrastructure Constraints and Application Reality In the
  traditional vSphere environment, we functioned within a hierarchy of folders and
  resource pools. With the adoption of VMware Cloud Foundation (VCF) and especially
  VCF 9, the “Namespace” has emerged as the fundamental building block. However, as
  many architects discover, a namespace in VCF is not a single entity – it is a layered
  construct that spans from the physical ESX host up to the application’s runtime
  environment. To successfully scale modern applications, you must understand the
  three critical layers: the VCF Automation Project , the vSphere Namespace , and
  the VKS Namespace. At the top of the stack sits VCF Automation. In this layer, the
  “Namespace” is abstracted into a Project. VCF Automation serves as the primary tenancy
  boundary. While vCenter allows you to create namespaces directly, VCF Automation
  adds the necessary “guardrails” for an enterprise environment. The Abstraction of
  Regions: VCF Automation uses Regions to hide the underlying complexity of the SDDC.
  A Region maps to a Supervisor Cluster, but to the developer, it is simply a location
  where resources live. The Project as a Container: A Project in VCF Automation is
  where you tie together users (via SSO), cloud zones, and shared resources. When
  you entitle a Project to a specific “Namespace Class,” you are defining exactly
  what kind of footprint a developer can claim.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/03/05/the-hierarchy-of-modern-infrastructure-mastering-namespaces-in-vmware-cloud-foundation-vsphere-kubernetes-service-and-vcf-automation/
