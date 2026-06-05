---
title: VCF 9.1 Brings Multi-Network Support to VMware vSphere Kubernetes Service
date: '2026-06-02T16:12:04+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/06/02/vcf-9-1-brings-multi-network-support-to-vsphere-kubernetes-service/
post_kind: link
draft: false
tldr: 'The Network Separation Challenge in Kubernetes How VKS Multi-Network Works:
  Primary and Secondary NICs Step-by-Step: Configuring VKS Multi-Network Support (NSX
  VPC) Step 1: Supervisor Admin – Prepare the VPC Network Step 2: Supervisor Admin
  – Create the VKS Cluster Step 3: Verify the Configuration VDS Variant: VKS Multi-Network
  Support without NSX What’s Not Supported (Yet) Gotchas When Configuring VKS Multi-Network
  Support Frequently Asked Questions Up Next: The VKS Multi-Network Series Related
  Resources Discover more from VMware Cloud Foundation (VCF) Blog Related Articles
  Explore What’s New: VMware vSphere Foundation 9.1 Resources Now Available VCF 9.1
  Tag Management: Elevating Operational Governance VCF 9.1 Brings Multi-Network Support
  to VMware vSphere Kubernetes Service Part 1 of a series on VKS Multiple Networks
  in VCF 9.1 TL;DR: VMware Cloud Foundation (VCF) 9.1 and vSphere Kubernetes Service
  (VKS) 3.6 introduce declarative multi-NIC support for Kubernetes nodes, making VKS
  multi-network support a first-class platform capability. This first post covers
  the foundation: provisioning a secondary NIC on every node.'
summary: 'The Network Separation Challenge in Kubernetes How VKS Multi-Network Works:
  Primary and Secondary NICs Step-by-Step: Configuring VKS Multi-Network Support (NSX
  VPC) Step 1: Supervisor Admin – Prepare the VPC Network Step 2: Supervisor Admin
  – Create the VKS Cluster Step 3: Verify the Configuration VDS Variant: VKS Multi-Network
  Support without NSX What’s Not Supported (Yet) Gotchas When Configuring VKS Multi-Network
  Support Frequently Asked Questions Up Next: The VKS Multi-Network Series Related
  Resources Discover more from VMware Cloud Foundation (VCF) Blog Related Articles
  Explore What’s New: VMware vSphere Foundation 9.1 Resources Now Available VCF 9.1
  Tag Management: Elevating Operational Governance VCF 9.1 Brings Multi-Network Support
  to VMware vSphere Kubernetes Service Part 1 of a series on VKS Multiple Networks
  in VCF 9.1 TL;DR: VMware Cloud Foundation (VCF) 9.1 and vSphere Kubernetes Service
  (VKS) 3.6 introduce declarative multi-NIC support for Kubernetes nodes, making VKS
  multi-network support a first-class platform capability. This first post covers
  the foundation: provisioning a secondary NIC on every node. By itself this does
  not reroute application traffic; it creates the network topology that makes VKS
  network isolation possible and unlocks further capabilities covered in subsequent
  posts. Supported on NSX Virtual Private Cloud (VPC) and Virtual Distributed Switch
  (VDS). This diagram shows the VKS multi-network architecture this series builds
  toward. Part 1 covers the node-level vNIC separation at the foundation. With that
  in place, subsequent posts cover the use cases this unlocks: NFS storage isolation,
  pod-level multi-NIC with Antrea, multicast traffic separation, and SR-IOV (Single
  Root I/O Virtualization). In most Kubernetes deployments, a single network interface
  carries all traffic: communications to the Kubernetes API server, application traffic,
  storage I/O, and cluster management all share eth0. That creates a potential structural
  compliance gap. Frameworks including CIS Kubernetes Benchmark, NIST SP 800-190,
  and PCI-DSS require network segmentation. NetworkPolicies provide Layer 4 controls
  within the cluster, but cannot enforce separation at the node NIC level or govern
  traffic originating outside the cluster. The boundary needs to exist at the infrastructure
  layer.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/06/02/vcf-9-1-brings-multi-network-support-to-vsphere-kubernetes-service/
