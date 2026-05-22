---
title: 'Kubernetes v1.36: More Drivers, New Features, and the Next Era of DRA'
date: '2026-05-07T10:35:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/05/07/kubernetes-v1-36-dra-136-updates/
post_kind: link
draft: false
tldr: 'Kubernetes v1.36: More Drivers, New Features, and the Next Era of DRA Feature
  graduations Prioritized list (stable) Extended resource support (beta) Partitionable
  devices (beta) Device taints (beta) Device binding conditions (beta) Resource health
  status (beta) New Features ResourceClaim support for workloads Node allocatable
  resources DRA resource availability visibility List types for attributes Deterministic
  device selection Discoverable device metadata in containers What’s next? Getting
  involved Dynamic Resource Allocation (DRA) has fundamentally changed how platform
  administrators handle hardware accelerators and specialized resources in Kubernetes.
  In the v1.36 release, DRA continues to mature, bringing a wave of feature graduations,
  critical usability improvements, and new capabilities that extend the flexibility
  of DRA to native resources like memory and CPU, and support for ResourceClaims in
  PodGroups.'
summary: 'Kubernetes v1.36: More Drivers, New Features, and the Next Era of DRA Feature
  graduations Prioritized list (stable) Extended resource support (beta) Partitionable
  devices (beta) Device taints (beta) Device binding conditions (beta) Resource health
  status (beta) New Features ResourceClaim support for workloads Node allocatable
  resources DRA resource availability visibility List types for attributes Deterministic
  device selection Discoverable device metadata in containers What’s next? Getting
  involved Dynamic Resource Allocation (DRA) has fundamentally changed how platform
  administrators handle hardware accelerators and specialized resources in Kubernetes.
  In the v1.36 release, DRA continues to mature, bringing a wave of feature graduations,
  critical usability improvements, and new capabilities that extend the flexibility
  of DRA to native resources like memory and CPU, and support for ResourceClaims in
  PodGroups. Driver availability continues to expand. Beyond specialized compute accelerators,
  the ecosystem includes support for networking and other hardware types, reflecting
  a move toward a more robust, hardware-agnostic infrastructure. Whether you are managing
  massive fleets of GPUs, need better handling of failures, or simply looking for
  better ways to define resource fallback options, the upgrades to DRA in 1.36 have
  something for you. Let''s dive into the new features and graduations! The community
  has been hard at work stabilizing core DRA concepts. In Kubernetes 1.36, several
  highly anticipated features have graduated to Beta and Stable. Hardware heterogeneity
  is a reality in most clusters. With the Prioritized list feature, you can confidently
  define fallback preferences when requesting devices. Instead of hardcoding a request
  for a specific device model, you can specify an ordered list of preferences (e.
  g. , "Give me an H100, but if none are available, fall back to an A100").'
---
Open the original post ↗ https://kubernetes.io/blog/2026/05/07/kubernetes-v1-36-dra-136-updates/
