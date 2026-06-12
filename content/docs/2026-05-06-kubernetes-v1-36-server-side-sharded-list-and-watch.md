---
title: 'Kubernetes v1.36: Server-Side Sharded List and Watch'
date: '2026-05-06T10:35:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/05/06/kubernetes-v1-36-server-side-sharded-list-and-watch/
post_kind: link
draft: false
tldr: 'Kubernetes v1.36: Server-Side Sharded List and Watch The problem with client-side
  sharding How it works Using sharded watches in controllers Verifying server support
  Getting involved As Kubernetes clusters grow to tens of thousands of nodes, controllers
  that watch high-cardinality resources like Pods face a scaling wall. Every replica
  of a horizontally scaled controller receives the full stream of events from the
  API server, paying the CPU, memory, and network cost to deserialize everything,
  only to discard the objects it is not responsible for.'
summary: 'Kubernetes v1.36: Server-Side Sharded List and Watch The problem with client-side
  sharding How it works Using sharded watches in controllers Verifying server support
  Getting involved As Kubernetes clusters grow to tens of thousands of nodes, controllers
  that watch high-cardinality resources like Pods face a scaling wall. Every replica
  of a horizontally scaled controller receives the full stream of events from the
  API server, paying the CPU, memory, and network cost to deserialize everything,
  only to discard the objects it is not responsible for. Scaling out the controller
  does not reduce per-replica cost; it multiplies it. Kubernetes v1.36 introduces
  server-side sharded list and watch as an alpha feature ( KEP-5866 ). With this feature
  enabled, the API server filters events at the source so that each controller replica
  receives only the slice of the resource collection it owns. Some controllers, such
  as kube-state-metrics , already support horizontal sharding. Each replica is assigned
  a portion of the keyspace and discards objects that do not belong to it. While this
  works functionally, it does not reduce the volume of data flowing from the API server:
  N replicas x full event stream : every replica deserializes and processes every
  event, then throws away what it does not need. Network bandwidth scales with replicas
  , not with shard size. CPU spent on deserialization is wasted for the discarded
  fraction. Server-side sharded list and watch solves this by moving the filtering
  upstream into the API server. Each replica tells the API server which hash range
  it owns, and the API server only sends matching events.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/05/06/kubernetes-v1-36-server-side-sharded-list-and-watch/
