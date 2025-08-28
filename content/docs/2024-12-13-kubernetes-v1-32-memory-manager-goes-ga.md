---
title: 'Kubernetes v1.32: Memory Manager Goes GA'
date: '2024-12-13T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2024/12/13/memory-manager-goes-ga/
post_kind: link
draft: false
tldr: 'Kubernetes v1. 32: Memory Manager Goes GA Observability improvements Improving
  memory manager reliability and consistency Future development Getting involved With
  Kubernetes 1.'
summary: 'Kubernetes v1. 32: Memory Manager Goes GA Observability improvements Improving
  memory manager reliability and consistency Future development Getting involved With
  Kubernetes 1. 32, the memory manager has officially graduated to General Availability
  (GA), marking a significant milestone in the journey toward efficient and predictable
  memory allocation for containerized applications. Since Kubernetes v1. 22, where
  it graduated to beta, the memory manager has proved itself reliable, stable and
  a good complementary feature for the CPU Manager. As part of kubelet''s workload
  admission process, the memory manager provides topology hints to optimize memory
  allocation and alignment. This enables users to allocate exclusive memory for Pods
  in the Guaranteed QoS class. More details about the process can be found in the
  memory manager goes to beta blog. Most of the changes introduced since the Beta
  are bug fixes, internal refactoring and observability improvements, such as metrics
  and better logging. As part of the effort to increase the observability of memory
  manager, new metrics have been added to provide some statistics on memory allocation
  patterns. memory_manager_pinning_requests_total - tracks the number of times the
  pod spec required the memory manager to pin memory pages. memory_manager_pinning_errors_total
  - tracks the number of times the pod spec required the memory manager to pin memory
  pages, but the allocation failed.'
---
Open the original post ↗ https://kubernetes.io/blog/2024/12/13/memory-manager-goes-ga/
