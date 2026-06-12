---
title: Announcing etcd 3.7.0-beta.0
date: '2026-05-20T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/05/20/etcd-370-beta/
post_kind: link
draft: false
tldr: Announcing etcd 3.7.0-beta. 0 RangeStream Removal of v2store 3.4 EOL Feedback
  and Future Betas SIG-Etcd announces the availability of the first beta release of
  etcd v3.7.0.
summary: 'Announcing etcd 3.7.0-beta. 0 RangeStream Removal of v2store 3.4 EOL Feedback
  and Future Betas SIG-Etcd announces the availability of the first beta release of
  etcd v3.7.0. This new version of the popular distributed database and key Kubernetes
  component includes the long-requested RangeStream feature, as well as a refactoring
  and cleanup of multiple legacy components and interfaces. v3.7 will deliver improved
  security, better operational reliability, and an improved experience for working
  with large resultsets. First, however, the project needs users to test the beta.
  You can find v3.7.0-beta. 0 here: Source code Binaries Official container images
  Please try it out and report issues in the etcd repo. This beta also determines
  the EOL of version 3.4. In etcd v3.6 and earlier, it is challenging to work with
  requests that return large resultsets. The client or requesting application is forced
  to wait for the full result set, leading to unpredictable latency and memory usage.
  The RangeStream RPC lets calling applications accept result sets in chunks, reducing
  latency and making buffering memory usage more predictable. Much of the work on
  RangeStream was done by a relatively new contributor to etcd, Jeffrey Ying , a software
  engineer at Google.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/05/20/etcd-370-beta/
