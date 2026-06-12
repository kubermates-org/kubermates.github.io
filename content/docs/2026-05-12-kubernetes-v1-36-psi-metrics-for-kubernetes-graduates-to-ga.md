---
title: 'Kubernetes v1.36: PSI Metrics for Kubernetes Graduates to GA'
date: '2026-05-12T10:35:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/05/12/kubernetes-v1-36-psi-metrics-ga/
post_kind: link
draft: false
tldr: 'Kubernetes v1.36: PSI Metrics for Kubernetes Graduates to GA Beyond utilization:
  why PSI? Proving stability: performance testing at scale Improvements between beta
  (1.34) and stable (1.36) Getting started Further reading Acknowledgements Feedback
  Since its original implementation in the Linux kernel in 2018, Pressure Stall Information
  (PSI) has provided users with the high-fidelity signals needed to identify resource
  saturation before it becomes an outage. Unlike traditional utilization metrics,
  PSI tells the story of tasks stalled and time lost, all in nicely-packaged percentages
  of time across the CPU, memory, and I/O.'
summary: 'Kubernetes v1.36: PSI Metrics for Kubernetes Graduates to GA Beyond utilization:
  why PSI? Proving stability: performance testing at scale Improvements between beta
  (1.34) and stable (1.36) Getting started Further reading Acknowledgements Feedback
  Since its original implementation in the Linux kernel in 2018, Pressure Stall Information
  (PSI) has provided users with the high-fidelity signals needed to identify resource
  saturation before it becomes an outage. Unlike traditional utilization metrics,
  PSI tells the story of tasks stalled and time lost, all in nicely-packaged percentages
  of time across the CPU, memory, and I/O. With the recent release of Kubernetes v1.36,
  users across the ecosystem have a stable, reliable interface to observe resource
  contention at the node, pod, and container levels. In this post, we will dive into
  the improvements and performance testing that proved its readiness for production.
  Monitoring CPU or memory usage alone can be misleading. A node may report XX% (below
  100%) CPU utilization while certain tasks are experiencing severe latency due to
  scheduling delays. PSI fills this gap by providing: Cumulative Totals : Absolute
  time spent in a stalled state. Moving Averages : 10s, 60s, and 300s windows that
  allow operators to distinguish between transient spikes and sustained resource tension.
  A common concern when graduating telemetry features is the resource overhead required
  to collect and serve the metrics. To address this, SIG Node conducted extensive
  performance validation on high-density workloads (80+ pods) across various machine
  types. Our testing focused on two primary scenarios to isolate the impact of the
  Kubelet and kernel-level collection respectively: Kernel PSI ON / Kubelet Feature
  OFF vs Kernel PSI ON / Kubelet Feature ON (Kubelet overhead) Kernel PSI OFF / Kubelet
  Feature ON vs Kernel PSI ON / Kubelet Feature ON (Kernel overhead) First, we looked
  at the kubelet usage on 4 core machines (Case 1). For these, the Linux kernel was
  already tracking pressure on both clusters by default( psi=1 ), but we toggled the
  KubeletPSI feature gate to see if the Kubelet actively querying and exposing these
  metrics impacted the resource usage.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/05/12/kubernetes-v1-36-psi-metrics-ga/
