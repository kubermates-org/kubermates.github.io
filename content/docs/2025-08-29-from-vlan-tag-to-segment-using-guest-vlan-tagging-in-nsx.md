---
title: 'From VLAN Tag to Segment: Using Guest VLAN Tagging in NSX'
date: '2025-08-29T18:16:13+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/08/29/from-vlan-tag-to-segment-using-guest-vlan-tagging-in-nsx/
post_kind: link
draft: false
tldr: 'Guest VLAN Tagging alone… not great with NSX Mapping VLAN Tags to NSX Segments
  Step 1 – Attach the VM to a segment Step 2 – Convert the VM’s port into a parent
  port Step 3 – Create child ports for each VLAN Notes Configuration steps VM Configuration
  Creation of a child port using API Step 1 – Retrieve the VM’s Port Step 2 – Convert
  the Port into a Parent Port Step 3 – Create a Child Port for VLAN 10 Creation of
  a Child Port for via UI Related Articles From VLAN Tag to Segment: Using Guest VLAN
  Tagging in NSX Save Costs and Scale Efficiently with vSAN Deduplication in VMware
  Cloud Foundation 9.0 How to Connect your VMware Private AI Services Agents to OpenWeb
  UI By default, a virtual machine sends traffic to its vNIC untagged. The virtual
  switch then receives that traffic into a single VLAN or NSX segment.'
summary: 'Guest VLAN Tagging alone… not great with NSX Mapping VLAN Tags to NSX Segments
  Step 1 – Attach the VM to a segment Step 2 – Convert the VM’s port into a parent
  port Step 3 – Create child ports for each VLAN Notes Configuration steps VM Configuration
  Creation of a child port using API Step 1 – Retrieve the VM’s Port Step 2 – Convert
  the Port into a Parent Port Step 3 – Create a Child Port for VLAN 10 Creation of
  a Child Port for via UI Related Articles From VLAN Tag to Segment: Using Guest VLAN
  Tagging in NSX Save Costs and Scale Efficiently with vSAN Deduplication in VMware
  Cloud Foundation 9.0 How to Connect your VMware Private AI Services Agents to OpenWeb
  UI By default, a virtual machine sends traffic to its vNIC untagged. The virtual
  switch then receives that traffic into a single VLAN or NSX segment. This model
  limits a VM to connecting to at most 10 networks directly. But what if we need to
  connect the VM to more than 10 networks? With VLAN-backed networking, this is where
  Guest VLAN Tagging (GVT) comes in. When Guest VLAN Tagging is enabled on a port
  group, the VM itself is responsible for inserting VLAN tags (802. 1Q C-TAGs) into
  the frames it transmits. The virtual switch then uses the tag to direct the frame
  to the correct VLAN. With this approach, a single vNIC can access up to 4,094 VLAN-backed
  networks , dramatically increasing connectivity without adding more virtual NICs.
  Guest VLAN Tagging is enabled by specifying a VLAN ID range on the port group. For
  example, if you configure a range of 10–20, the vNIC will accept traffic tagged
  with VLAN IDs from 10 to 20, while dropping traffic tagged with IDs outside that
  range. The VM’s operating system must, of course, be configured to generate the
  appropriate VLAN-tagged subinterfaces. Guest VLAN Tagging can also be configured
  on NSX segments in a similar way, but there is an important difference: NSX segments
  are not identified by VLAN IDs.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/08/29/from-vlan-tag-to-segment-using-guest-vlan-tagging-in-nsx/
