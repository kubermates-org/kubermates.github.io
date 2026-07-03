---
title: 'Kepler, re-architected: Improved power accuracy and a community call to action!'
date: '2026-06-30T11:38:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/06/30/kepler-re-architected-improved-power-accuracy-and-a-community-call-to-action/
post_kind: link
draft: false
tldr: 'Re-architecting Kepler Validating Accuracy Improvements Experiment 1: Comparing
  pre- and post-rewrite versions Experiment 2: Negligible attribution gap What’s Next?
  A Call to Action Posted on June 30, 2026 by Niki Manoledaki (Grafana Labs), Sunyanan
  Choochotkaew (IBM) | CNCF Ambassadors CNCF projects highlighted in this post Thank
  you to Laura Llinares, Mary Baldwin Hughes, Vimal Kumar, and Sunil Thaha for their
  significant contributions to this blog post and the Kepler project. Data centers
  accounted for 1.5% of global electricity demand in 2024, which is projected to double
  to around 945 TWh by 2030, driven in part by rapid growth in AI workloads according
  to the International Energy Agency’s “Energy and AI” report published in 2025.'
summary: 'Re-architecting Kepler Validating Accuracy Improvements Experiment 1: Comparing
  pre- and post-rewrite versions Experiment 2: Negligible attribution gap What’s Next?
  A Call to Action Posted on June 30, 2026 by Niki Manoledaki (Grafana Labs), Sunyanan
  Choochotkaew (IBM) | CNCF Ambassadors CNCF projects highlighted in this post Thank
  you to Laura Llinares, Mary Baldwin Hughes, Vimal Kumar, and Sunil Thaha for their
  significant contributions to this blog post and the Kepler project. Data centers
  accounted for 1.5% of global electricity demand in 2024, which is projected to double
  to around 945 TWh by 2030, driven in part by rapid growth in AI workloads according
  to the International Energy Agency’s “Energy and AI” report published in 2025. In
  Kubernetes clusters, there is no easy built-in method to allocate power per workload.
  Kepler solves this: it reads from hardware power meters, attributes this power consumption
  to Linux processes, associates that to Pods running in your Kubernetes cluster,
  and exports Prometheus metrics. Since joining the CNCF as a sandbox project in 2023,
  Kepler adoption has grown. However, the original architecture relied on eBPF, and
  while that added granularity, it also created problems. First, it required CAP_BPF
  and CAP_SYSADMIN privileges, which is a blocker for many production environments.
  Secondly, eBPF proved to be error-prone when it comes to tracking fine-grained,
  kernel-level processes at this level of accuracy. Data inaccuracy at this level
  creates a bottleneck for the power estimation models that we need to train in order
  to deploy Kepler on virtual machines (VMs). Beyond the elevated privileges and accuracy
  issues, the eBPF integration made the learning curve steeper. It added complex abstractions
  that made it difficult to extend and maintain the codebase. CAP_BPF CAP_SYSADMIN
  The team decided to tackle these challenges head on.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/06/30/kepler-re-architected-improved-power-accuracy-and-a-community-call-to-action/
