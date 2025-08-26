---
title: NFTables mode for kube-proxy
date: '2025-02-28T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/02/28/nftables-kube-proxy/
post_kind: link
draft: false
tldr: A new nftables mode for kube-proxy was introduced as an alpha feature in Kubernetes
  1.
summary: A new nftables mode for kube-proxy was introduced as an alpha feature in
  Kubernetes 1. 29. Currently in beta, it is expected to be GA as of 1. 33. The new
  mode fixes long-standing performance problems with the iptables mode and all users
  running on systems with reasonably-recent kernels are encouraged to try it out.
  (For compatibility reasons, even once nftables becomes GA, iptables will still be
  the default.
---
Open the original post ↗ https://kubernetes.io/blog/2025/02/28/nftables-kube-proxy/
