---
title: 'Kubernetes v1.36: User Namespaces in Kubernetes are finally GA'
date: '2026-04-23T10:35:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/04/23/kubernetes-v1-36-userns-ga/
post_kind: link
draft: false
tldr: 'Kubernetes v1.36: User Namespaces in Kubernetes are finally GA The Problem
  with UID 0 The engine: ID-mapped mounts Using it in Kubernetes v1.36 Getting involved
  Acknowledgments After several years of development, User Namespaces support in Kubernetes
  reached General Availability (GA) with the v1.36 release. This is a Linux-only feature.'
summary: 'Kubernetes v1.36: User Namespaces in Kubernetes are finally GA The Problem
  with UID 0 The engine: ID-mapped mounts Using it in Kubernetes v1.36 Getting involved
  Acknowledgments After several years of development, User Namespaces support in Kubernetes
  reached General Availability (GA) with the v1.36 release. This is a Linux-only feature.
  For those of us working on low level container runtimes and rootless technologies,
  this has been a long awaited milestone. We finally reached the point where "rootless"
  security isolation can be used for Kubernetes workloads. This feature also enables
  a critical pattern: running workloads with privileges and still being confined in
  the user namespace. When hostUsers: false is set, capabilities like CAP_NET_ADMIN
  become namespaced , meaning they grant administrative power over container local
  resources without affecting the host. This effectively enables new use cases that
  were not possible before without running a fully privileged container. hostUsers:
  false CAP_NET_ADMIN A process running as root inside a container is also seen from
  the kernel as root on the host. If an attacker manages to break out of the container,
  whether through a kernel vulnerability or a misconfigured mount, they are root on
  the host. While there are many security measures in place for running containers,
  these measures don''t change the underlying identity of the process, it still has
  some "parts" of root. The road to GA wasn''t just about the Kubernetes API; it was
  about making the kernel work for us. In the early stages, one of the biggest blockers
  was volume ownership.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/04/23/kubernetes-v1-36-userns-ga/
