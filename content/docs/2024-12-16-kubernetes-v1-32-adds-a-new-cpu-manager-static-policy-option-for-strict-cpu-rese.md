---
title: Kubernetes v1.32 Adds A New CPU Manager Static Policy Option For Strict CPU
  Reservation
date: '2024-12-16T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2024/12/16/cpumanager-strict-cpu-reservation/
post_kind: link
draft: false
tldr: In Kubernetes v1. 32, after years of community discussion, we are excited to
  introduce a strict-cpu-reservation option for the CPU Manager static policy.
summary: In Kubernetes v1. 32, after years of community discussion, we are excited
  to introduce a strict-cpu-reservation option for the CPU Manager static policy.
  This feature is currently in alpha, with the associated policy hidden by default.
  You can only use the policy if you explicitly enable the alpha behavior in your
  cluster. The CPU Manager static policy is used to reduce latency or improve performance.
  The reservedSystemCPUs defines an explicit CPU set for OS system daemons and kubernetes
  system daemons. This option is designed for Telco/NFV type use cases where uncontrolled
  interrupts/timers may impact the workload performance. you can use this option to
  define the explicit cpuset for the system/kubernetes daemons as well as the interrupts/timers,
  so the rest CPUs on the system can be used exclusively for workloads, with less
  impact from uncontrolled interrupts/timers. More details of this parameter can be
  found on the Explicitly Reserved CPU List page. If you want to protect your system
  daemons and interrupt processing, the obvious way is to use the reservedSystemCPUs
  option. However, until the Kubernetes v1. 32 release, this isolation was only implemented
  for guaranteed pods that made requests for a whole number of CPUs.
---
Open the original post ↗ https://kubernetes.io/blog/2024/12/16/cpumanager-strict-cpu-reservation/
