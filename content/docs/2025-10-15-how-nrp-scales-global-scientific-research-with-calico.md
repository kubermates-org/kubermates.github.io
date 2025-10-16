---
title: How NRP Scales Global Scientific Research with Calico
date: '2025-10-15T15:53:20+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/how-nrp-scales-global-scientific-research-with-calico/
post_kind: link
draft: false
tldr: Challenges Complex Network Visibility and Debugging Balancing Performance with
  Granular Security at Scale Managing Advanced Heterogeneous Networking Solutions
  Enhanced Observability with Calico Telemetry Performant Network Policy Enforcement
  Flexible Kubernetes Networking Results Customer Perspective What’s Next The National
  Research Platform (NRP) operates a globally distributed, high-performance computing
  and networking environment, with an average of 15,000 pods across 450 nodes supporting
  more than 3,000 scientific project namespaces. With its head node in San Diego,
  NRP connects research institutions and data centers worldwide via links ranging
  from 10 to 400 Gbps, serving more than 5,000 users in 70+ locations.
summary: Challenges Complex Network Visibility and Debugging Balancing Performance
  with Granular Security at Scale Managing Advanced Heterogeneous Networking Solutions
  Enhanced Observability with Calico Telemetry Performant Network Policy Enforcement
  Flexible Kubernetes Networking Results Customer Perspective What’s Next The National
  Research Platform (NRP) operates a globally distributed, high-performance computing
  and networking environment, with an average of 15,000 pods across 450 nodes supporting
  more than 3,000 scientific project namespaces. With its head node in San Diego,
  NRP connects research institutions and data centers worldwide via links ranging
  from 10 to 400 Gbps, serving more than 5,000 users in 70+ locations. Non-profit
  company Uses Calico Open Source NRP is a partnership of more than 50 institutions,
  led by researchers at UC San Diego, University of Nebraska-Lincoln, and Massachusetts
  Green High Performance Computing Center and includes contributions by the National
  Science Foundation, the Department of Energy, the Department of Defense, and many
  research universities and R&E networking organizations in the US and around the
  world. NRP needed a way to diagnose connectivity problems across globally distributed
  storage nodes. Frequent changes to edge network configurations, ACLs, firewalls,
  and static routes caused blocked ports, forcing manual troubleshooting with tools
  such as nmap and iperf. This process slowed down root-cause analysis and problem
  resolution. Scientific workflows demanded maximum throughput over 100/400 Gbps links
  and jumbo frames. Traditional host firewalls introduced unacceptable performance
  penalties, preventing researchers from mounting data and forcing the team to disable
  them. NRP required a centralized, high-performance network security solution that
  could enforce fine-grained policies at scale without degrading throughput. NRP’s
  workflows relied on advanced capabilities such as Layer 2 paths over WAN using ESnet
  Sense and AutoGOLE, dual-stack IPv4/IPv6 support, and experiments with multipath
  BGP. They also needed integration with specialized hardware such as FPGAs and smartNICs
  for P4 packet processing. Managing this mix of protocols, services, and hardware
  required a flexible CNI that could support complex, multi-layer orchestration.
---
Open the original post ↗ https://www.tigera.io/blog/how-nrp-scales-global-scientific-research-with-calico/
