---
title: 'Kubernetes v1.34: Introducing CPU Manager Static Policy Option for Uncore
  Cache Alignment'
date: '2025-09-02T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/09/02/kubernetes-v1-34-prefer-align-by-uncore-cache-cpumanager-static-policy-optimization/
post_kind: link
draft: false
tldr: 'Kubernetes v1.34: Introducing CPU Manager Static Policy Option for Uncore Cache
  Alignment Understanding the feature What is uncore cache? Cache-aware workload placement
  Use cases Enabling the feature Further reading Getting involved A new CPU Manager
  Static Policy Option called prefer-align-cpus-by-uncorecache was introduced in Kubernetes
  v1.32 as an alpha feature, and has graduated to beta in Kubernetes v1.34. This CPU
  Manager Policy Option is designed to optimize performance for specific workloads
  running on processors with a split uncore cache architecture.'
summary: 'Kubernetes v1.34: Introducing CPU Manager Static Policy Option for Uncore
  Cache Alignment Understanding the feature What is uncore cache? Cache-aware workload
  placement Use cases Enabling the feature Further reading Getting involved A new
  CPU Manager Static Policy Option called prefer-align-cpus-by-uncorecache was introduced
  in Kubernetes v1.32 as an alpha feature, and has graduated to beta in Kubernetes
  v1.34. This CPU Manager Policy Option is designed to optimize performance for specific
  workloads running on processors with a split uncore cache architecture. In this
  article, I''ll explain what that means and why it''s useful. prefer-align-cpus-by-uncorecache
  Until relatively recently, nearly all mainstream computer processors had a monolithic
  last-level-cache cache that was shared across every core in a multiple CPU package.
  This monolithic cache is also referred to as uncore cache (because it is not linked
  to a specific core), or as Level 3 cache. As well as the Level 3 cache, there is
  other cache, commonly called Level 1 and Level 2 cache, that is associated with
  a specific CPU core. In order to reduce access latency between the CPU cores and
  their cache, recent AMD64 and ARM architecture based processors have introduced
  a split uncore cache architecture, where the last-level-cache is divided into multiple
  physical caches, that are aligned to specific CPU groupings within the physical
  package. The shorter distances within the CPU package help to reduce latency. Kubernetes
  is able to place workloads in a way that accounts for the cache topology within
  the CPU package(s). The matrix below shows the CPU-to-CPU latency measured in nanoseconds
  (lower is better) when passing a packet between CPUs, via its cache coherence protocol
  on a processor that uses split uncore cache. In this example, the processor package
  consists of 2 uncore caches. Each uncore cache serves 8 CPU cores.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/09/02/kubernetes-v1-34-prefer-align-by-uncore-cache-cpumanager-static-policy-optimization/
