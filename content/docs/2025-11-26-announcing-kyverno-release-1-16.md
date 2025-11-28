---
title: Announcing Kyverno release 1.16
date: '2025-11-26T20:44:24+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/11/26/announcing-kyverno-release-1-16/
post_kind: link
draft: false
tldr: CEL policy types Kyverno Authz Server Introducing the Kyverno SDK Other features
  and enhancements Getting started and backward compatibility Roadmap Conclusion Posted
  on November 26, 2025 by Shuting Zhao, Kyverno Maintainer and a Staff Engineer at
  Nirmata CNCF projects highlighted in this post Kyverno 1.16 delivers major advancements
  in policy as code for Kubernetes, centered on a new generation of CEL-based policies
  now available in beta with a clear path to GA. This release introduces partial support
  for namespaced CEL policies to confine enforcement and minimize RBAC, aligning with
  least-privilege best practices.
summary: 'CEL policy types Kyverno Authz Server Introducing the Kyverno SDK Other
  features and enhancements Getting started and backward compatibility Roadmap Conclusion
  Posted on November 26, 2025 by Shuting Zhao, Kyverno Maintainer and a Staff Engineer
  at Nirmata CNCF projects highlighted in this post Kyverno 1.16 delivers major advancements
  in policy as code for Kubernetes, centered on a new generation of CEL-based policies
  now available in beta with a clear path to GA. This release introduces partial support
  for namespaced CEL policies to confine enforcement and minimize RBAC, aligning with
  least-privilege best practices. Observability is significantly enhanced with full
  metrics for CEL policies and native event generation, enabling precise visibility
  and faster troubleshooting. Security and governance get sharper controls through
  fine-grained policy exceptions tailored for CEL policies, and validation use cases
  broaden with the integration of an HTTP authorizer into ValidatingPolicy. Finally,
  we’re debuting the Kyverno SDK, laying the foundation for ecosystem integrations
  and custom tooling. CEL policy types are introduced as v1beta. The promotion plan
  provides a clear, non‑breaking path: v1 will be made available in 1.17 with GA targeted
  for 1.18. This release includes the cluster‑scoped family (Validating, Mutating,
  Generating, Deleting, ImageValidating) at v1beta1 and adds namespaced variants for
  validation, deleting, and image validation; namespaced Generating and Mutating will
  follow in 1.17. PolicyException and GlobalContextEntry will advance in step to keep
  versions aligned; see the promotion roadmap in this tracking issue. Kyverno 1.16
  introduces namespaced CEL policy types— NamespacedValidatingPolicy , NamespacedDeletingPolicy
  , and NamespacedImageValidatingPolicy —which mirror their cluster-scoped counterparts
  but apply only within the policy’s namespace. This lets teams enforce guardrails
  with least-privilege RBAC and without central changes, improving multi-tenancy and
  safety during rollout. Choose namespaced types for team-owned namespaces and cluster-scoped
  types for global controls.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/11/26/announcing-kyverno-release-1-16/
