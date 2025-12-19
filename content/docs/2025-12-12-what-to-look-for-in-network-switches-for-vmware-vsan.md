---
title: What to Look for in Network Switches for VMware vSAN
date: '2025-12-12T13:00:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/12/12/what-to-look-for-in-network-switches-for-vmware-vsan/
post_kind: link
draft: false
tldr: 'Why Network Switches Are so Important for vSAN Recommendations for ToR Switches
  Used with vSAN Downlink Port Count and Speed Uplink Port Count and Speed Switch
  Capacity Packets Per Second Port Buffers Summary Discover more from VMware Cloud
  Foundation (VCF) Blog Related Articles NVMe Memory Tiering Design and Sizing on
  VMware Cloud Foundation 9 Part 4: vSAN Compatibility and Storage Considerations
  Using Harbor as a Proxy Cache for Cloud-Based Registries What to Look for in Network
  Switches for VMware vSAN Since the recent series of blog posts on VMware vSAN networking
  came out earlier this year, one of the more common questions received has been “
  What should I use as a Top of Rack (ToR) network switch in my vSAN environment?”
  Our Broadcom Compatibility Guide (BCG) for vSAN details compatibility and requirements
  for the hosts that make up a vSAN cluster, but it does not address network switches.
  Almost any network switch will work with vSAN, but that does not mean they all meet
  your data center requirements.'
summary: 'Why Network Switches Are so Important for vSAN Recommendations for ToR Switches
  Used with vSAN Downlink Port Count and Speed Uplink Port Count and Speed Switch
  Capacity Packets Per Second Port Buffers Summary Discover more from VMware Cloud
  Foundation (VCF) Blog Related Articles NVMe Memory Tiering Design and Sizing on
  VMware Cloud Foundation 9 Part 4: vSAN Compatibility and Storage Considerations
  Using Harbor as a Proxy Cache for Cloud-Based Registries What to Look for in Network
  Switches for VMware vSAN Since the recent series of blog posts on VMware vSAN networking
  came out earlier this year, one of the more common questions received has been “
  What should I use as a Top of Rack (ToR) network switch in my vSAN environment?”
  Our Broadcom Compatibility Guide (BCG) for vSAN details compatibility and requirements
  for the hosts that make up a vSAN cluster, but it does not address network switches.
  Almost any network switch will work with vSAN, but that does not mean they all meet
  your data center requirements. There are characteristics of modern network switches
  that you should consider when moving forward with your latest hardware refresh,
  or new cluster build. Let’s look at what warrants attention, and why these specifications
  are so important. vSAN is a distributed storage solution. It stores data across
  hosts in a cluster to ensure data resilience and availability. The hosts that make
  up a vSAN cluster depend on fast, reliable networking to provide consistent, low
  latency storage. Figure 1. vSAN’s distributed storage model and its reliance on
  networking. The dramatic increase in hardware capabilities found in servers over
  the past two decades is stunning. CPU cores have increased anywhere between 32-128
  times of what they were 20 years ago. The same goes for RAM.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/12/12/what-to-look-for-in-network-switches-for-vmware-vsan/
