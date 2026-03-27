---
title: 5 Things You Didn’t Know You Can Do With Traceflow
date: '2026-03-26T18:03:05+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/03/26/5-things-you-didnt-know-you-can-do-with-traceflow/
post_kind: link
draft: false
tldr: 1. Test Inbound Network Connectivity (Ingress Through the Tier-0) Inbound Traceflow
  Example and Output 2.
summary: '1. Test Inbound Network Connectivity (Ingress Through the Tier-0) Inbound
  Traceflow Example and Output 2. Identify the Firewall Rule Dropping Packets FW Rule
  Identification Example and Output 3. Isolating the Fault Domain (Pinpointing the
  Physical Exit Point) Outbound Traceflow Example and Output 4. Finding the Exact
  NAT Translation In the Path NAT Use Case Example and Output 5. Automating Troubleshooting
  (Integrating Traceflow via API) Final Thoughts Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles Unlocking VMware Cloud Foundation Enterprise Value:
  Cloud Field Day 25 5 Things You Didn’t Know You Can Do With Traceflow Looking at
  Technology from a Different Perspective: Francesca Palazzo’s Approach to Customer
  Strategy with VMware Cloud Foundation Managing a modern software-defined network
  means navigating a multi-layered architecture. When network traffic goes missing
  between overlays, distributed firewalls, and physical handoffs, many engineers still
  default to traditional troubleshooting methods – SSHing into ESXi hosts and Edge
  Nodes, running pktcap-uw, or digging through esxcli outputs. While those tools are
  vital, they are also time-consuming. NSX Traceflow has been a native feature in
  your VCF virtual networking stack for a while, but it remains an underutilized tool
  in the arsenal. Traceflow isn’t just a graphical traceroute. Unlike a traditional
  traceroute that relies on the guest OS to generate a packet and waits for ICMP “Time
  Exceeded” messages from physical routers, Traceflow injects a specially tagged,
  synthetic packet directly into the hypervisor’s data plane at the relevant NSX observation
  points. It doesn’t rely on ICMP features.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/03/26/5-things-you-didnt-know-you-can-do-with-traceflow/
