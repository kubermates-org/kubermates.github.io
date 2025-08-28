---
title: Enhancing Kubernetes API Server Efficiency with API Streaming
date: '2024-12-17T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2024/12/17/kube-apiserver-api-streaming/
post_kind: link
draft: false
tldr: Enhancing Kubernetes API Server Efficiency with API Streaming Why does kube-apiserver
  allocate so much memory for list requests? Streaming list requests Enabling API
  Streaming for your component What's next? The synthetic test Kubernetes 1. 33 update
  Managing Kubernetes clusters efficiently is critical, especially as their size is
  growing.
summary: Enhancing Kubernetes API Server Efficiency with API Streaming Why does kube-apiserver
  allocate so much memory for list requests? Streaming list requests Enabling API
  Streaming for your component What's next? The synthetic test Kubernetes 1. 33 update
  Managing Kubernetes clusters efficiently is critical, especially as their size is
  growing. A significant challenge with large clusters is the memory overhead caused
  by list requests. In the existing implementation, the kube-apiserver processes list
  requests by assembling the entire response in-memory before transmitting any data
  to the client. But what if the response body is substantial, say hundreds of megabytes?
  Additionally, imagine a scenario where multiple list requests flood in simultaneously,
  perhaps after a brief network outage. While API Priority and Fairness has proven
  to reasonably protect kube-apiserver from CPU overload, its impact is visibly smaller
  for memory protection. This can be explained by the differing nature of resource
  consumption by a single API request - the CPU usage at any given time is capped
  by a constant, whereas memory, being uncompressible, can grow proportionally with
  the number of processed objects and is unbounded. This situation poses a genuine
  risk, potentially overwhelming and crashing any kube-apiserver within seconds due
  to out-of-memory (OOM) conditions. To better visualize the issue, let's consider
  the below graph. The graph shows the memory usage of a kube-apiserver during a synthetic
  test. (see the synthetic test section for more details). The results clearly show
  that increasing the number of informers significantly boosts the server's memory
  consumption.
---
Open the original post ↗ https://kubernetes.io/blog/2024/12/17/kube-apiserver-api-streaming/
