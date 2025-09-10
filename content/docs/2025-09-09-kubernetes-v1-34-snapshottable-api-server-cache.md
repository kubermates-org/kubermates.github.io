---
title: 'Kubernetes v1.34: Snapshottable API server cache'
date: '2025-09-09T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/09/09/kubernetes-v1-34-snapshottable-api-server-cache/
post_kind: link
draft: false
tldr: 'Kubernetes v1.34: Snapshottable API server cache Evolving the cache for performance
  and stability Consistent reads from cache (Beta in v1.31) Taming large responses
  with streaming (Beta in v1.33) The missing piece Kubernetes 1.34: snapshots complete
  the picture A new era of API Server performance 🚀 How to get started Acknowledgements
  For years, the Kubernetes community has been on a mission to improve the stability
  and performance predictability of the API server. A major focus of this effort has
  been taming list requests, which have historically been a primary source of high
  memory usage and heavy load on the etcd datastore.'
summary: 'Kubernetes v1.34: Snapshottable API server cache Evolving the cache for
  performance and stability Consistent reads from cache (Beta in v1.31) Taming large
  responses with streaming (Beta in v1.33) The missing piece Kubernetes 1.34: snapshots
  complete the picture A new era of API Server performance 🚀 How to get started Acknowledgements
  For years, the Kubernetes community has been on a mission to improve the stability
  and performance predictability of the API server. A major focus of this effort has
  been taming list requests, which have historically been a primary source of high
  memory usage and heavy load on the etcd datastore. With each release, we''ve chipped
  away at the problem, and today, we''re thrilled to announce the final major piece
  of this puzzle. etcd The snapshottable API server cache feature has graduated to
  Beta in Kubernetes v1.34, culminating a multi-release effort to allow virtually
  all read requests to be served directly from the API server''s cache. The path to
  the current state involved several key enhancements over recent releases that paved
  the way for today''s announcement. While the API server has long used a cache for
  performance, a key milestone was guaranteeing consistent reads of the latest data
  from it. This v1.31 enhancement allowed the watch cache to be used for strongly-consistent
  read requests for the first time, a huge win as it enabled filtered collections
  (e. g. "a list of pods bound to this node") to be safely served from the cache instead
  of etcd, dramatically reducing its load for common workloads. Another key improvement
  was tackling the problem of memory spikes when transmitting large responses. The
  streaming encoder, introduced in v1.33, allowed the API server to send list items
  one by one, rather than buffering the entire multi-gigabyte response in memory.
  This made the memory cost of sending a response predictable and minimal, regardless
  of its size.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/09/09/kubernetes-v1-34-snapshottable-api-server-cache/
