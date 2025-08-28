---
title: How 1&1 Mail & Media Scaled Kubernetes Networking with eBPF and Calico
date: '2025-08-05T16:12:16+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/how-11-mail-media-scaled-kubernetes-networking-with-ebpf-and-calico/
post_kind: link
draft: false
tldr: Challenge Solution Results What’s Next “We started in 2017 with Calico and never
  regretted it!” —Stephan Fudeus, Product Owner/Lead Architect, 1&1 Mail & Media 1&1
  Mail & Media, part of the United Internet, powers popular European internet brands
  including GMX and Web. de, serving more than 50% of Germany’s population with critical
  identity and email infrastructure.
summary: 'Challenge Solution Results What’s Next “We started in 2017 with Calico and
  never regretted it!” —Stephan Fudeus, Product Owner/Lead Architect, 1&1 Mail & Media
  1&1 Mail & Media, part of the United Internet, powers popular European internet
  brands including GMX and Web. de, serving more than 50% of Germany’s population
  with critical identity and email infrastructure. With roughly 45 to 50 million users,
  network reliability is non-negotiable. Any downtime could affect millions. By 2022,
  the company had containerized 80% of its workloads on Kubernetes across three self-managed
  data centers. While the platform, backed by bare metal nodes and custom network
  layers, was highly scalable, network throughput bottlenecks began to emerge. Pods
  were limited to 2. 5 Gbps of bandwidth due to IP encapsulation overhead, despite
  10 Gbps network interfaces. The team needed a solution that: Improved pod-to-pod
  network performance Maintained strong network policy isolation across up to 40 tenants
  per cluster Scaled to millions of network connections and 1. 4 million HTTP requests
  per second 1&1 Mail & Media had adopted Calico back in 2017, largely for its unique
  Kubernetes NetworkPolicy standard support. As their Kubernetes platform evolved,
  with clusters scaling to 300 bare metal nodes, 16,000 pods, and over 4 million conntrack
  entries, the team turned to Calico’s eBPF data plane to unlock performance gains.
  Following successful initial trials of eBPF in development and integration environments,
  the team moved forward with production migrations in 2023.'
---
Open the original post ↗ https://www.tigera.io/blog/how-11-mail-media-scaled-kubernetes-networking-with-ebpf-and-calico/
