---
title: 'Kubernetes v1.33: Streaming List responses'
date: '2025-05-09T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/05/09/kubernetes-v1-33-streaming-list-responses/
post_kind: link
draft: false
tldr: 'Kubernetes v1. 33: Streaming List responses The problem: unnecessary memory
  consumption with large resources Streaming encoder for List responses Performance
  gains you''ll notice Benchmark results Managing Kubernetes cluster stability becomes
  increasingly critical as your infrastructure grows.'
summary: 'Kubernetes v1. 33: Streaming List responses The problem: unnecessary memory
  consumption with large resources Streaming encoder for List responses Performance
  gains you''ll notice Benchmark results Managing Kubernetes cluster stability becomes
  increasingly critical as your infrastructure grows. One of the most challenging
  aspects of operating large-scale clusters has been handling List requests that fetch
  substantial datasets - a common operation that could unexpectedly impact your cluster''s
  stability. Today, the Kubernetes community is excited to announce a significant
  architectural improvement: streaming encoding for List responses. Current API response
  encoders just serialize an entire response into a single contiguous memory and perform
  one ResponseWriter. Write call to transmit data to the client. Despite HTTP/2''s
  capability to split responses into smaller frames for transmission, the underlying
  HTTP server continues to hold the complete response data as a single buffer. Even
  as individual frames are transmitted to the client, the memory associated with these
  frames cannot be freed incrementally. When cluster size grows, the single response
  body can be substantial - like hundreds of megabytes in size. At large scale, the
  current approach becomes particularly inefficient, as it prevents incremental memory
  release during transmission. Imagining that when network congestion occurs, that
  large response body’s memory block stays active for tens of seconds or even minutes.
  This limitation leads to unnecessarily high and prolonged memory consumption in
  the kube-apiserver process.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/09/kubernetes-v1-33-streaming-list-responses/
