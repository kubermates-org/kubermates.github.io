---
title: Announcing etcd v3.7.0
date: '2026-07-08T20:00:00+08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/07/08/announcing-etcd-3.7/
post_kind: link
draft: false
tldr: Announcing etcd v3.7.0 Major features Features RangeStream Performance improvements
  Other features Upgrading Experimental flags removed Legacy V2 API packages and code
  cleanup Non-blocking client creation Multiarch container images only API changes
  bbolt v1.5.1 raft v3.7.0 Dependency updates Contributors Leads Other contributors
  New contributors This article is a mirror of the original announcement Today, SIG
  etcd is releasing etcd v3.7.0 , the latest minor release of the popular distributed
  key-value store and core Kubernetes component. v3.7 ships the long-requested RangeStream
  feature, delivers several other performance improvements, removes the last remnants
  of the legacy v2store, and completes a major protobuf overhaul.
summary: 'Announcing etcd v3.7.0 Major features Features RangeStream Performance improvements
  Other features Upgrading Experimental flags removed Legacy V2 API packages and code
  cleanup Non-blocking client creation Multiarch container images only API changes
  bbolt v1.5.1 raft v3.7.0 Dependency updates Contributors Leads Other contributors
  New contributors This article is a mirror of the original announcement Today, SIG
  etcd is releasing etcd v3.7.0 , the latest minor release of the popular distributed
  key-value store and core Kubernetes component. v3.7 ships the long-requested RangeStream
  feature, delivers several other performance improvements, removes the last remnants
  of the legacy v2store, and completes a major protobuf overhaul. You can download
  etcd v3.7.0 here: Source code Binaries Official container images This release also
  includes new versions of the two core etcd dependencies, bbolt v1.5.0 and raft v3.7.0.
  For instructions on installing etcd, see the install documentation. For the full
  list of changes, see the etcd v3.7 changelog. A heartfelt thank you to all the contributors
  who made this release possible! The most significant changes in v3.7.0 include:
  RangeStream — stream large result sets in chunks instead of buffering the whole
  response. Keys-only range requests, faster and more reliable leases, and several
  other performance improvements. etcd now boots entirely from v3store , eliminating
  a long-standing dependency on the legacy v2 store A completed protobuf overhaul
  , replacing outdated protobuf libraries with fully supported ones. etcd v3.7 ships
  with bbolt v1.5.1 and raft v3.7.0. In etcd v3.6 and earlier, it is challenging to
  work with requests that return large result sets. The database would buffer the
  full result set before sending, leading to unpredictable latency and memory usage,
  both on the server and the client. The RangeStream RPC lets calling applications
  accept result sets in chunks, reducing latency and making buffering memory usage
  more predictable.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/07/08/announcing-etcd-3.7/
