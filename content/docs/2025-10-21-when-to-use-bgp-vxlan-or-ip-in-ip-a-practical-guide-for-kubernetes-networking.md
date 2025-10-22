---
title: 'When to Use BGP, VXLAN, or IP-in-IP: A Practical Guide for Kubernetes Networking'
date: '2025-10-21T19:29:35+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/when-to-use-bgp-vxlan-or-ip-in-ip-a-practical-guide-for-kubernetes-networking/
post_kind: link
draft: false
tldr: 'The Cost of a Mismatched Network Mode A Technical Breakdown of Networking Modes
  VXLAN (Virtual Extensible LAN) IP-in-IP BGP (Border Gateway Protocol) Decision Matrix
  Simplifying Operations Across Network Modes Final Verdict: Selecting the Right Networking
  Mode for Your Workload Ready to Simplify Kubernetes Networking? When deploying a
  Kubernetes cluster, a critical architectural decision is how pods on different nodes
  communicate. The choice of networking mode directly impacts performance, scalability,
  and operational overhead.'
summary: 'The Cost of a Mismatched Network Mode A Technical Breakdown of Networking
  Modes VXLAN (Virtual Extensible LAN) IP-in-IP BGP (Border Gateway Protocol) Decision
  Matrix Simplifying Operations Across Network Modes Final Verdict: Selecting the
  Right Networking Mode for Your Workload Ready to Simplify Kubernetes Networking?
  When deploying a Kubernetes cluster, a critical architectural decision is how pods
  on different nodes communicate. The choice of networking mode directly impacts performance,
  scalability, and operational overhead. Selecting the wrong mode for your environment
  can lead to persistent performance issues, troubleshooting complexity, and scalability
  bottlenecks. The core problem is that pod IPs are virtual. The underlying physical
  or cloud network has no native awareness of how to route traffic to a pod’s IP address,
  like 10.244.1.5 It only knows how to route traffic between the nodes themselves.
  This gap is precisely what the Container Network Interface (CNI) must bridge. 10.244.1.5
  The CNI employs two primary methods to solve this problem: Overlay Networking (Encapsulation):
  This method wraps a pod’s packet inside another packet that the underlying network
  understands. The outer packet is addressed between nodes, effectively creating a
  tunnel. VXLAN and IP-in-IP are common encapsulation protocols. Underlay Networking
  (Routing): This method teaches the network fabric itself how to route traffic directly
  to pods. It uses a routing protocol like BGP to advertise pod IP routes to the physical
  network, making pods routable without encapsulation. This guide dives into the technical
  differences of these options to help you select the right mode for your environment.'
---
Open the original post ↗ https://www.tigera.io/blog/when-to-use-bgp-vxlan-or-ip-in-ip-a-practical-guide-for-kubernetes-networking/
