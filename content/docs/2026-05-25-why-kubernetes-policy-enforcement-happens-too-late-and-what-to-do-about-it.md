---
title: Why Kubernetes policy enforcement happens too late—and what to do about it
date: '2026-05-25T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/05/25/why-kubernetes-policy-enforcement-happens-too-late-and-what-to-do-about-it/
post_kind: link
draft: false
tldr: 'The timing problem in policy-as-code Rethinking the enforcement locus The missing
  layer: Review-time enforcement An experiment in review-time enforcement What changes
  when feedback moves earlier? Limitations and where this fits Practical guidance
  for platform teams Why this matters for the CNCF ecosystem The road ahead: AI agents
  as policy reasoning partners Posted on May 25, 2026 by Sajal Nigam, CNCF Community
  Member CNCF projects highlighted in this post Kubernetes has become the backbone
  of modern cloud-native infrastructure. Its flexibility lets teams move fast, compose
  complex systems from modular components, and deploy across environments with relative
  ease.'
summary: 'The timing problem in policy-as-code Rethinking the enforcement locus The
  missing layer: Review-time enforcement An experiment in review-time enforcement
  What changes when feedback moves earlier? Limitations and where this fits Practical
  guidance for platform teams Why this matters for the CNCF ecosystem The road ahead:
  AI agents as policy reasoning partners Posted on May 25, 2026 by Sajal Nigam, CNCF
  Community Member CNCF projects highlighted in this post Kubernetes has become the
  backbone of modern cloud-native infrastructure. Its flexibility lets teams move
  fast, compose complex systems from modular components, and deploy across environments
  with relative ease. But that flexibility comes with a well-known cost: configuration
  complexity. Across organizations of all sizes, a surprisingly large share of reliability
  and security incidents don’t originate in application code. They originate in misconfigured
  infrastructure—missing resource limits, overly permissive security contexts, incorrect
  RBAC bindings. These issues are common, subtle, and typically introduced during
  the normal rhythm of development work. The frustrating part? Most of them are caught
  too late. Policy-as-code tooling has matured significantly within the CNCF ecosystem.
  Tools like Open Policy Agent (OPA) , Kyverno , and Conftest give platform teams
  powerful, declarative ways to define and enforce governance rules across Kubernetes
  environments. These tools commonly operate at two stages: CI/CD pipelines — scanning
  manifests as part of automated build and test workflows Admission controllers —
  enforcing policy at the cluster boundary, blocking non-compliant resources from
  being applied Both are essential. But they share a structural limitation: by the
  time a violation is surfaced, the developer has already written the code, the pull
  request has often been reviewed, and the context has been lost. What follows is
  a familiar cycle: A CI job fails on a policy violation The developer context-switches
  back to a PR they’ve mentally closed A follow-up commit is pushed to fix the issue
  The cycle repeats This isn’t a problem with policy quality.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/05/25/why-kubernetes-policy-enforcement-happens-too-late-and-what-to-do-about-it/
