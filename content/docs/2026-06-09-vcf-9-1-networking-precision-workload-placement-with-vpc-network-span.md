---
title: 'VCF 9.1 Networking: Precision Workload Placement with VPC Network Span'
date: '2026-06-09T18:25:53+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/06/09/vcf-9-1-networking-precision-workload-placement-with-vpc-network-span/
post_kind: link
draft: false
tldr: 'Related VCF 9.1 Networking Posts: What is VPC Network Span? The Evolution:
  VCF 9.0 vs. VCF 9.1 Key Benefits of VPC Network Span Summary VCF 9.1 VPC Network
  Span Demo Discover more from VMware Cloud Foundation (VCF) Blog Related Articles
  Improving VMware Cloud Foundation Performance with Enhanced Data Path (EDP) VCF
  9.1 Networking: Precision Workload Placement with VPC Network Span Achieve Speed,
  Scale, and Reliability of Virtual Machine Deployments with ‘cloud-init’ Network
  Services Simpler VPC Connectivity Control Precision Workload Placement with VPC
  Network Span Transit Gateway Connectivity Options Integration with Infoblox VMware
  Cloud Foundation (VCF) continues to evolve its self-service networking capabilities
  (as we explored in our post VCF Networking 9.1: Exploring Network Services for Virtual
  Private Clouds ).'
summary: 'Related VCF 9.1 Networking Posts: What is VPC Network Span? The Evolution:
  VCF 9.0 vs. VCF 9.1 Key Benefits of VPC Network Span Summary VCF 9.1 VPC Network
  Span Demo Discover more from VMware Cloud Foundation (VCF) Blog Related Articles
  Improving VMware Cloud Foundation Performance with Enhanced Data Path (EDP) VCF
  9.1 Networking: Precision Workload Placement with VPC Network Span Achieve Speed,
  Scale, and Reliability of Virtual Machine Deployments with ‘cloud-init’ Network
  Services Simpler VPC Connectivity Control Precision Workload Placement with VPC
  Network Span Transit Gateway Connectivity Options Integration with Infoblox VMware
  Cloud Foundation (VCF) continues to evolve its self-service networking capabilities
  (as we explored in our post VCF Networking 9.1: Exploring Network Services for Virtual
  Private Clouds ). With the release of VCF 9.1, we are seeing a major enhancement
  in how subnets are presented to your infrastructure: VPC Network Span. In short,
  Network Span defines visibility. It allows administrators to specify exactly which
  vCenter clusters can “see” and host the subnets associated with a specific Virtual
  Private Cloud (VPC). Think of it as a way to map your virtual network boundaries
  directly onto your physical cluster boundaries with total precision. To understand
  why this is a game-changer, we have to look at how VPC subnets were handled previously:
  VCF 9.0 (The Global Model): In version 9.0, VPC subnets were available across all
  vCenter clusters by default. While this provided maximum flexibility for workload
  mobility, it didn’t allow for much architectural isolation at the cluster level.
  VCF 9.1 (The Targeted Model): You now have the option to limit VPC subnets to specific
  vCenter clusters. This control is managed at the Transit Gateway (TGW) level, ensuring
  that workloads only live exactly where you want them. Why should you move away from
  the “global” model? This new granular control offers several strategic advantages:
  Granular Application Placement: You can now ensure that specific applications are
  only deployed within a designated subset of your vCenter clusters, rather than being
  spread across the entire environment. Dedicated Security Zones (DMZ): This is perfect
  for architectures requiring isolation.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/06/09/vcf-9-1-networking-precision-workload-placement-with-vpc-network-span/
