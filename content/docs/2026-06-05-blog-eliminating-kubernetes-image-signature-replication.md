---
title: 'Blog: Eliminating Kubernetes Image Signature Replication'
date: '2026-06-05T00:00:00+00:00'
tags:
- kubernetes
- community
source: Kubernetes.dev Blog
external_url: https://www.kubernetes.dev/blog/2026/06/05/image-signature-routing/
post_kind: link
draft: false
tldr: Eliminating Kubernetes Image Signature Replication The problem The insight The
  solution What changed Impact Trade-offs What’s next Getting involved The image promoter
  rewrite laid the groundwork for simplifying how Kubernetes delivers container image
  signatures. One of the rewrite phases (Phase 6) separated image signing from signature
  replication into distinct pipeline stages.
summary: 'Eliminating Kubernetes Image Signature Replication The problem The insight
  The solution What changed Impact Trade-offs What’s next Getting involved The image
  promoter rewrite laid the groundwork for simplifying how Kubernetes delivers container
  image signatures. One of the rewrite phases (Phase 6) separated image signing from
  signature replication into distinct pipeline stages. This follow-up covers the next
  step: eliminating signature replication entirely. After promoting container images
  to registry. k8s. io , the promoter signs them using cosign with keyless (OIDC)
  signatures. These signatures are stored as OCI artifacts alongside the images, tagged
  with the convention sha256-<digest>. sig and sha256-<digest>. att. registry. k8s.
  io sha256-<digest>.'
---
Open the original post ↗ https://www.kubernetes.dev/blog/2026/06/05/image-signature-routing/
