---
title: Announcing etcd v3.6.0
date: '2025-05-15T16:00:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/05/15/announcing-etcd-3.6/
post_kind: link
draft: false
tldr: Announcing etcd v3.6.0 Security Features Migration to v3store Downgrade Feature
  gates livez / readyz checks v3discovery Performance Memory Throughput Breaking changes
  Peer endpoints no longer serve client requests Clear boundary between etcdctl and
  etcdutl Critical bug fixes Upgrade issue Testing Platforms Dependencies Dependency
  bumping guide Core Dependency Updates grpc-gateway@v2 grpc-ecosystem/go-grpc-middleware/providers/prometheus
  Community etcd Becomes a Kubernetes SIG New contributors, maintainers, and reviewers
  Introducing the etcd Operator Working Group Future Development This announcement
  originally appeared on the etcd blog. Today, we are releasing etcd v3.6.0 , the
  first minor release since etcd v3.5.0 on June 15, 2021.
summary: Announcing etcd v3.6.0 Security Features Migration to v3store Downgrade Feature
  gates livez / readyz checks v3discovery Performance Memory Throughput Breaking changes
  Peer endpoints no longer serve client requests Clear boundary between etcdctl and
  etcdutl Critical bug fixes Upgrade issue Testing Platforms Dependencies Dependency
  bumping guide Core Dependency Updates grpc-gateway@v2 grpc-ecosystem/go-grpc-middleware/providers/prometheus
  Community etcd Becomes a Kubernetes SIG New contributors, maintainers, and reviewers
  Introducing the etcd Operator Working Group Future Development This announcement
  originally appeared on the etcd blog. Today, we are releasing etcd v3.6.0 , the
  first minor release since etcd v3.5.0 on June 15, 2021. This release introduces
  several new features, makes significant progress on long-standing efforts like downgrade
  support and migration to v3store, and addresses numerous critical & major issues.
  It also includes major optimizations in memory usage, improving efficiency and performance.
  In addition to the features of v3.6.0, etcd has joined Kubernetes as a SIG (sig-etcd),
  enabling us to improve project sustainability. We've introduced systematic robustness
  testing to ensure correctness and reliability. Through the etcd-operator Working
  Group, we plan to improve usability as well. What follows are the most significant
  changes introduced in etcd v3.6.0, along with the discussion of the roadmap for
  future development. For a detailed list of changes, please refer to the CHANGELOG-3.6.
  A heartfelt thank you to all the contributors who made this release possible! etcd
  takes security seriously. To enhance software security in v3.6.0, we have improved
  our workflow checks by integrating govulncheck to scan the source code and trivy
  to scan container images. These improvements have also been backported to supported
  stable releases.
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/15/announcing-etcd-3.6/
