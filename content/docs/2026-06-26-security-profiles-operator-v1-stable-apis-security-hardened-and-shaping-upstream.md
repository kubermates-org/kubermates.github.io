---
title: 'Security Profiles Operator v1: Stable APIs, Security Hardened, and Shaping
  Upstream Kubernetes'
date: '2026-06-26T11:30:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/06/26/security-profiles-operator-v1-stable-apis-security-hardened-and-shaping-upstream-kubernetes/
post_kind: link
draft: false
tldr: Six years of API evolution Security audit and hardening Additional hardening
  beyond the audit scope Zero-downtime migration From operator to upstream Kubernetes
  What’s next Posted on June 26, 2026 by Sascha Grunert (Red Hat) CNCF projects highlighted
  in this post Linux provides powerful kernel-level security mechanisms, seccomp ,
  SELinux , and AppArmor , that restrict what containerized workloads can do. Each
  uses profiles that define permitted behavior, but writing, distributing, and maintaining
  those profiles by hand is tedious and error-prone.
summary: 'Six years of API evolution Security audit and hardening Additional hardening
  beyond the audit scope Zero-downtime migration From operator to upstream Kubernetes
  What’s next Posted on June 26, 2026 by Sascha Grunert (Red Hat) CNCF projects highlighted
  in this post Linux provides powerful kernel-level security mechanisms, seccomp ,
  SELinux , and AppArmor , that restrict what containerized workloads can do. Each
  uses profiles that define permitted behavior, but writing, distributing, and maintaining
  those profiles by hand is tedious and error-prone. The Security Profiles Operator
  (SPO) solves this by letting you manage security profiles as Kubernetes custom resources,
  record profiles from live workloads, and bind them to pods declaratively. With v1.0.0
  , the Security Profiles Operator graduates all eight of its Custom Resource Definition
  (CRD) APIs to v1. This is the project’s first stable release, backed by a third-party
  security audit, a full cycle of hardening work, and a zero-downtime migration path
  from every previous API version. SPO started in April 2020 as a seccomp-only operator.
  Over the following years, the project grew to cover SELinux (late 2020), AppArmor
  (late 2021), profile recording via audit logs and eBPF, OCI-based profile distribution,
  and more. Each feature introduced new CRDs, and those CRDs stayed at alpha or beta
  while the APIs matured through real-world use. Some of these APIs have been stable
  in practice for years: SeccompProfile shipped at v1beta1 for over four years, SPOD
  at v1alpha1 for over five. Downstream consumers needed a stable version label to
  commit to long-term support. The SPO has been available on OperatorHub since 2022
  and has shipped as part of Red Hat OpenShift since version 4.12. The window before
  v1 was the last chance to make breaking changes, and the team used it.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/06/26/security-profiles-operator-v1-stable-apis-security-hardened-and-shaping-upstream-kubernetes/
