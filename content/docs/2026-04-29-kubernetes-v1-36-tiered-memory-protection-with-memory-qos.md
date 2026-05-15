---
title: 'Kubernetes v1.36: Tiered Memory Protection with Memory QoS'
date: '2026-04-29T10:35:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/04/29/kubernetes-v1-36-memory-qos-tiered-protection/
post_kind: link
draft: false
tldr: 'Kubernetes v1.36: Tiered Memory Protection with Memory QoS What''s new in v1.36
  Opt-in memory reservation with memoryReservationPolicy Observability metrics Kernel
  version check How Kubernetes maps Memory QoS to cgroup v2 Cgroup hierarchy How do
  I use it? Prerequisites Configuration How can I learn more? Getting involved On
  behalf of SIG Node, we are pleased to announce updates to the Memory QoS feature
  (alpha) in Kubernetes v1.36. Memory QoS uses the cgroup v2 memory controller to
  give the kernel better guidance on how to treat container memory.'
summary: 'Kubernetes v1.36: Tiered Memory Protection with Memory QoS What''s new in
  v1.36 Opt-in memory reservation with memoryReservationPolicy Observability metrics
  Kernel version check How Kubernetes maps Memory QoS to cgroup v2 Cgroup hierarchy
  How do I use it? Prerequisites Configuration How can I learn more? Getting involved
  On behalf of SIG Node, we are pleased to announce updates to the Memory QoS feature
  (alpha) in Kubernetes v1.36. Memory QoS uses the cgroup v2 memory controller to
  give the kernel better guidance on how to treat container memory. It was first introduced
  in v1.22 and updated in v1.27. In Kubernetes v1.36, we''re introducing: opt-in memory
  reservation, tiered protection by QoS class, observability metrics, and kernel-version
  warning for memory. high. memory. high memoryReservationPolicy v1.36 separates throttling
  from reservation. Enabling the feature gate turns on memory. high throttling (the
  kubelet sets memory. high based on memoryThrottlingFactor , default 0.9), but memory
  reservation is now controlled by a separate kubelet configuration field: memory.
  high memory. high memoryThrottlingFactor None (default): no memory.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/04/29/kubernetes-v1-36-memory-qos-tiered-protection/
