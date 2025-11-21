---
title: Mapping VLAN Tags to Virtual Private Cloud Subnets
date: '2025-11-20T15:49:06+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/11/20/mapping-vlan-tags-to-virtual-private-cloud-subnets/
post_kind: link
draft: false
tldr: 'Traditional Guest VLAN Tagging (Trunking) Guest VLAN Tagging on NSX Overlay
  Segments Implementing VLAN-to-Subnet Mapping in a VPC Key Benefits of Subnet-Level
  Mapping Discover more from VMware Cloud Foundation (VCF) Blog Related Articles Mapping
  VLAN Tags to Virtual Private Cloud Subnets Unified Authentication in VMware Cloud
  Foundation SDK 9.0: Seamless authentication across vSphere and vSAN APIs NVMe Memory
  Tiering Design and Sizing on VMware Cloud Foundation 9 Part 2: Design for Security,
  Redundancy, and Scalability In a typical virtualized environment, a VM sends untagged
  traffic from its virtual NIC (vNIC). By default, the virtual switch drops any traffic
  that carries an 802.'
summary: 'Traditional Guest VLAN Tagging (Trunking) Guest VLAN Tagging on NSX Overlay
  Segments Implementing VLAN-to-Subnet Mapping in a VPC Key Benefits of Subnet-Level
  Mapping Discover more from VMware Cloud Foundation (VCF) Blog Related Articles Mapping
  VLAN Tags to Virtual Private Cloud Subnets Unified Authentication in VMware Cloud
  Foundation SDK 9.0: Seamless authentication across vSphere and vSAN APIs NVMe Memory
  Tiering Design and Sizing on VMware Cloud Foundation 9 Part 2: Design for Security,
  Redundancy, and Scalability In a typical virtualized environment, a VM sends untagged
  traffic from its virtual NIC (vNIC). By default, the virtual switch drops any traffic
  that carries an 802. 1Q VLAN tag. To allow this traffic, a feature known as Guest
  VLAN Tagging (GVT) must be explicitly enabled on the vNIC’s port connection. Let’s
  review how this is traditionally handled before diving into the simple and powerful
  method available in Virtual Private Cloud (VPC) subnets. On a vSphere Distributed
  Port Group (dvPortGroup) or a VLAN-backed NSX segment, GVT is enabled by configuring
  the port as a trunk. This involves specifying a range of allowed VLAN IDs instead
  of just one. In this trunking model, traffic sent by a VM with VLAN tag X is forwarded
  onto the physical network, still tagged with VLAN X. The physical network infrastructure
  is then responsible for handling that tagged traffic. Enabling GVT on an NSX overlay
  segment (configuring a VLAN range) works similarly at first. Traffic from a VM with
  a VLAN tag is injected into the overlay segment while retaining its tag. Because
  NSX sees tagged frames, it treats this as simple Layer 2 traffic.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/11/20/mapping-vlan-tags-to-virtual-private-cloud-subnets/
