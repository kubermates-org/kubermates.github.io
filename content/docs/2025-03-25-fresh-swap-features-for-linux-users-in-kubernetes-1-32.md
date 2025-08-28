---
title: Fresh Swap Features for Linux Users in Kubernetes 1.32
date: '2025-03-25T10:00:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/03/25/swap-linux-improvements/
post_kind: link
draft: false
tldr: Fresh Swap Features for Linux Users in Kubernetes 1.32 How do I use it? Install
  a swap-enabled cluster with kubeadm Before you begin Create a swap file and turn
  swap on Set up a Kubernetes cluster that uses swap-enabled nodes How is the swap
  limit being determined with LimitedSwap? How does it work? How can I monitor swap?
  Node and container level metric statistics Node Feature Discovery (NFD) Caveats
  Memory-backed volumes Good practice for using swap in a Kubernetes cluster Disable
  swap for system-critical daemons Protect system-critical daemons for I/O latency
  Swap and control plane nodes Use of a dedicated disk for swap Looking ahead How
  can I learn more? How do I get involved? Swap is a fundamental and an invaluable
  Linux feature. It offers numerous benefits, such as effectively increasing a node’s
  memory by swapping out unused data, shielding nodes from system-level memory spikes,
  preventing Pods from crashing when they hit their memory limits, and much more.
summary: Fresh Swap Features for Linux Users in Kubernetes 1.32 How do I use it? Install
  a swap-enabled cluster with kubeadm Before you begin Create a swap file and turn
  swap on Set up a Kubernetes cluster that uses swap-enabled nodes How is the swap
  limit being determined with LimitedSwap? How does it work? How can I monitor swap?
  Node and container level metric statistics Node Feature Discovery (NFD) Caveats
  Memory-backed volumes Good practice for using swap in a Kubernetes cluster Disable
  swap for system-critical daemons Protect system-critical daemons for I/O latency
  Swap and control plane nodes Use of a dedicated disk for swap Looking ahead How
  can I learn more? How do I get involved? Swap is a fundamental and an invaluable
  Linux feature. It offers numerous benefits, such as effectively increasing a node’s
  memory by swapping out unused data, shielding nodes from system-level memory spikes,
  preventing Pods from crashing when they hit their memory limits, and much more.
  As a result, the node special interest group within the Kubernetes project has invested
  significant effort into supporting swap on Linux nodes. The 1.22 release introduced
  Alpha support for configuring swap memory usage for Kubernetes workloads running
  on Linux on a per-node basis. Later, in release 1.28, support for swap on Linux
  nodes has graduated to Beta, along with many new improvements. In the following
  Kubernetes releases more improvements were made, paving the way to GA in the near
  future. Prior to version 1.22, Kubernetes did not provide support for swap memory
  on Linux systems. This was due to the inherent difficulty in guaranteeing and accounting
  for pod memory utilization when swap memory was involved. As a result, swap support
  was deemed out of scope in the initial design of Kubernetes, and the default behavior
  of a kubelet was to fail to start if swap memory was detected on a node. In version
  1.22, the swap feature for Linux was initially introduced in its Alpha stage. This
  provided Linux users the opportunity to experiment with the swap feature for the
  first time. However, as an Alpha version, it was not fully developed and only partially
  worked on limited environments.
---
Open the original post ↗ https://kubernetes.io/blog/2025/03/25/swap-linux-improvements/
