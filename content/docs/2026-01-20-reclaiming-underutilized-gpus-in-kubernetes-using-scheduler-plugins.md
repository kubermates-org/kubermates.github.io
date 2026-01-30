---
title: Reclaiming underutilized GPUs in Kubernetes using scheduler plugins
date: '2026-01-20T12:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/01/20/reclaiming-underutilized-gpus-in-kubernetes-using-scheduler-plugins/
post_kind: link
draft: false
tldr: 'The problem nobody talks about Kubernetes scheduling trade-offs for GPUs The
  core idea: Utilization-aware preemption Where ReclaimIdleResource fits in the scheduling
  cycle How it works Key design decisions What we learned Related Links Posted on
  January 20, 2026 by Lalit Somavarapha, Gernot Seidler and Srujana Reddy Attunuri,
  Principal Engineers at HPE CNCF projects highlighted in this post GPUs are expensive;
  and yours are probably sitting idle right now. High-end GPUs (for example, NVIDIA
  A100-class devices) can cost $10,000+, and in a Kubernetes cluster running AI workloads,
  you might have dozens of them.'
summary: 'The problem nobody talks about Kubernetes scheduling trade-offs for GPUs
  The core idea: Utilization-aware preemption Where ReclaimIdleResource fits in the
  scheduling cycle How it works Key design decisions What we learned Related Links
  Posted on January 20, 2026 by Lalit Somavarapha, Gernot Seidler and Srujana Reddy
  Attunuri, Principal Engineers at HPE CNCF projects highlighted in this post GPUs
  are expensive; and yours are probably sitting idle right now. High-end GPUs (for
  example, NVIDIA A100-class devices) can cost $10,000+, and in a Kubernetes cluster
  running AI workloads, you might have dozens of them. Here’s the uncomfortable truth:
  most of the time, they’re sitting idle. If you’re struggling with GPU scheduling
  in Kubernetes or looking for ways to reclaim idle GPUs, you’re not alone. A data
  scientist spins up a training job, requests 4 GPUs, runs for two hours, then leaves
  for lunch. The GPUs sit allocated but unused. Meanwhile, another team’s job is queued,
  waiting for resources that technically exist but aren’t available. Standard Kubernetes
  scheduling doesn’t help here. It sees allocated resources as unavailable — period.
  The scheduler does not currently take real-time GPU utilization into account. Kubernetes
  was built for CPUs. Its scheduling model assumes resources are either allocated
  or free, with nothing in between.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/01/20/reclaiming-underutilized-gpus-in-kubernetes-using-scheduler-plugins/
