---
title: Announcing Kyverno release 1.18!
date: '2026-05-05T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/05/05/announcing-kyverno-release-1-18/
post_kind: link
draft: false
tldr: TL;DR Security improvements CLI expansion and developer experience Expanded
  policy support Reliability and usability improvements Policy engine improvements
  Fine-grained success event filtering Performance and scalability CEL and policy
  execution enhancements Image verification improvements Policies Helm chart enhancements
  Updated support policy Why this change What this means for users ClusterPolicy deprecation
  reminder What you should do Community updates Join the community Getting started
  and upgrading Upgrade Install Release Notes What’s next Conclusion Posted on May
  5, 2026 by Cortney Nickerson, Kyverno Contributor CNCF projects highlighted in this
  post We’re excited to announce the release of Kyverno 1.18, our first release since
  graduating within the Cloud Native Computing Foundation. This release builds on
  Kyverno’s growing role as a Kubernetes-native policy engine, with major investments
  in security, CLI capabilities, and policy engine reliability.
summary: 'TL;DR Security improvements CLI expansion and developer experience Expanded
  policy support Reliability and usability improvements Policy engine improvements
  Fine-grained success event filtering Performance and scalability CEL and policy
  execution enhancements Image verification improvements Policies Helm chart enhancements
  Updated support policy Why this change What this means for users ClusterPolicy deprecation
  reminder What you should do Community updates Join the community Getting started
  and upgrading Upgrade Install Release Notes What’s next Conclusion Posted on May
  5, 2026 by Cortney Nickerson, Kyverno Contributor CNCF projects highlighted in this
  post We’re excited to announce the release of Kyverno 1.18, our first release since
  graduating within the Cloud Native Computing Foundation. This release builds on
  Kyverno’s growing role as a Kubernetes-native policy engine, with major investments
  in security, CLI capabilities, and policy engine reliability. It also continues
  our transition toward CEL-based policy types, setting the foundation for the future
  of policy as code. Kyverno 1.18 delivers: Stronger security controls for HTTP-based
  policy execution and multiple CVE mitigations Significant CLI enhancements for testing
  and applying modern policy types Policy engine improvements for performance, observability,
  and scalability Enhancements to the policies Helm chart for better customization
  There are no breaking changes in this release, but ClusterPolicy deprecation remains
  on track, and users should begin migrating to the newer policy types. Security is
  a core pillar of Kyverno, and 1.18 introduces important safeguards for policy execution.
  Kyverno policies can call external services via HTTP CEL libraries. In 1.18, this
  capability is significantly hardened: Blocklist/allowlist enforcement: by default,
  unsafe addresses like loopback and metadata services are blocked. Users can configure
  an allow list and a block list for cluster-scoped and namespaced policies. Additionally,
  HTTP calls from namespaced policies are default disabled, and need to be explicitly
  enabled using configuration flags. These changes help prevent SSRF-style abuse.
  See CVE-2026-4789 for details. Scoped token authorization: Previously, Kyverno HTTP
  calls included a token which could be used to impersonate Kyverno controllers.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/05/05/announcing-kyverno-release-1-18/
