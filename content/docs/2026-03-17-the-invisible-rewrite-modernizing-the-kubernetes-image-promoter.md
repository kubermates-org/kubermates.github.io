---
title: 'The Invisible Rewrite: Modernizing the Kubernetes Image Promoter'
date: '2026-03-17T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/03/17/image-promoter-rewrite/
post_kind: link
draft: false
tldr: 'The Invisible Rewrite: Modernizing the Kubernetes Image Promoter A bit of history
  The problems we needed to solve One issue to answer them all The new pipeline Making
  it fast By the numbers No user-facing changes What comes next Thank you Every container
  image you pull from registry. k8s.'
summary: 'The Invisible Rewrite: Modernizing the Kubernetes Image Promoter A bit of
  history The problems we needed to solve One issue to answer them all The new pipeline
  Making it fast By the numbers No user-facing changes What comes next Thank you Every
  container image you pull from registry. k8s. io got there through kpromo , the Kubernetes
  image promoter. It copies images from staging registries to production, signs them
  with cosign , replicates signatures across more than 20 regional mirrors, and generates
  SLSA provenance attestations. If this tool breaks, no Kubernetes release ships.
  Over the past few weeks, we rewrote its core from scratch, deleted 20% of the codebase,
  made it dramatically faster, and nobody noticed. That was the whole point. registry.
  k8s. io kpromo The image promoter started in late 2018 as an internal Google project
  by Linus Arver. The goal was simple: replace the manual, Googler-gated process of
  copying container images into k8s. gcr.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/03/17/image-promoter-rewrite/
