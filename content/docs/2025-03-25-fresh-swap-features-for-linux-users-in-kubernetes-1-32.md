---
title: Fresh Swap Features for Linux Users in Kubernetes 1.32
date: '2025-03-25T10:00:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/03/25/swap-linux-improvements/
post_kind: link
draft: false
tldr: Swap is a fundamental and an invaluable Linux feature. It offers numerous benefits,
  such as effectively increasing a node’s memory by swapping out unused data, shielding
  nodes from system-level memory spikes, preventing Pods from crashing when they hit
  their memory limits, and much more.
summary: Swap is a fundamental and an invaluable Linux feature. It offers numerous
  benefits, such as effectively increasing a node’s memory by swapping out unused
  data, shielding nodes from system-level memory spikes, preventing Pods from crashing
  when they hit their memory limits, and much more. As a result, the node special
  interest group within the Kubernetes project has invested significant effort into
  supporting swap on Linux nodes. The 1. 22 release introduced Alpha support for configuring
  swap memory usage for Kubernetes workloads running on Linux on a per-node basis.
  Later, in release 1. 28, support for swap on Linux nodes has graduated to Beta,
  along with many new improvements. In the following Kubernetes releases more improvements
  were made, paving the way to GA in the near future. Prior to version 1. 22, Kubernetes
  did not provide support for swap memory on Linux systems. This was due to the inherent
  difficulty in guaranteeing and accounting for pod memory utilization when swap memory
  was involved. As a result, swap support was deemed out of scope in the initial design
  of Kubernetes, and the default behavior of a kubelet was to fail to start if swap
  memory was detected on a node.
---
Open the original post ↗ https://kubernetes.io/blog/2025/03/25/swap-linux-improvements/
