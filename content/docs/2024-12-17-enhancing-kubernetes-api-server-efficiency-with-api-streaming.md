---
title: Enhancing Kubernetes API Server Efficiency with API Streaming
date: '2024-12-17T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2024/12/17/kube-apiserver-api-streaming/
post_kind: link
draft: false
tldr: Managing Kubernetes clusters efficiently is critical, especially as their size
  is growing.
summary: Managing Kubernetes clusters efficiently is critical, especially as their
  size is growing. A significant challenge with large clusters is the memory overhead
  caused by list requests. In the existing implementation, the kube-apiserver processes
  list requests by assembling the entire response in-memory before transmitting any
  data to the client. But what if the response body is substantial, say hundreds of
  megabytes? Additionally, imagine a scenario where multiple list requests flood in
  simultaneously, perhaps after a brief network outage. While API Priority and Fairness
  has proven to reasonably protect kube-apiserver from CPU overload, its impact is
  visibly smaller for memory protection. T...
---
Open the original post ↗ https://kubernetes.io/blog/2024/12/17/kube-apiserver-api-streaming/
