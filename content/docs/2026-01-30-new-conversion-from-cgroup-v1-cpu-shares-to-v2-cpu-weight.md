---
title: New Conversion from cgroup v1 CPU Shares to v2 CPU Weight
date: '2026-01-30T08:00:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/01/30/new-cgroup-v1-to-v2-cpu-conversion-formula/
post_kind: link
draft: false
tldr: New Conversion from cgroup v1 CPU Shares to v2 CPU Weight Background Problems
  with previous conversion formula 1. Reduced priority against non-Kubernetes workloads
  2.
summary: 'New Conversion from cgroup v1 CPU Shares to v2 CPU Weight Background Problems
  with previous conversion formula 1. Reduced priority against non-Kubernetes workloads
  2. Unmanageable granularity New conversion formula Description How it solves the
  problems Adoption and integration Impact on existing deployments Where can I learn
  more? How do I get involved? I''m excited to announce the implementation of an improved
  conversion formula from cgroup v1 CPU shares to cgroup v2 CPU weight. This enhancement
  addresses critical issues with CPU priority allocation for Kubernetes workloads
  when running on systems with cgroup v2. Kubernetes was originally designed with
  cgroup v1 in mind, where CPU shares were defined simply by assigning the container''s
  CPU requests in millicpu form. For example, a container requesting 1 CPU (1024m)
  would get (cpu. shares = 1024). After a while, cgroup v1 started being replaced
  by its successor, cgroup v2. In cgroup v2, the concept of CPU shares (which ranges
  from 2 to 262144, or from 2¹ to 2¹⁸) was replaced with CPU weight (which ranges
  from [1, 10000], or 10⁰ to 10⁴). With the transition to cgroup v2, KEP-2254 introduced
  a conversion formula to map cgroup v1 CPU shares to cgroup v2 CPU weight. The conversion
  formula was defined as: cpu. weight = (1 + ((cpu.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/01/30/new-cgroup-v1-to-v2-cpu-conversion-formula/
