---
title: 'Tiered Network Policy: Scaling Kubernetes Security'
date: '2026-07-10T16:12:22+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/tiered-network-policy-scaling-kubernetes-security/
post_kind: link
draft: false
tldr: 'The Core Problem with Standard Kubernetes NetworkPolicy What a Scalable Solution
  Requires Why the Pass Action Matters The Kubernetes Native Answer: ClusterNetworkPolicy
  Extending the Model: Calico Tiers As Kubernetes clusters scale from a few development
  sandboxes to massive, multi-tenant production environments, platform teams often
  find themselves facing a configuration management crisis. A small number of microservices
  suddenly demand hundreds of individual Kubernetes NetworkPolicy objects.'
summary: 'The Core Problem with Standard Kubernetes NetworkPolicy What a Scalable
  Solution Requires Why the Pass Action Matters The Kubernetes Native Answer: ClusterNetworkPolicy
  Extending the Model: Calico Tiers As Kubernetes clusters scale from a few development
  sandboxes to massive, multi-tenant production environments, platform teams often
  find themselves facing a configuration management crisis. A small number of microservices
  suddenly demand hundreds of individual Kubernetes NetworkPolicy objects. Managing
  them becomes operationally expensive, auditing them is difficult, and a single developer
  misconfiguration can easily drop critical production traffic or open a massive security
  hole. To scale cluster security without slowing down engineering velocity, we must
  abandon the flat, uncoordinated rule planes of the past. The solution lies in establishing
  a clear, multi-layered framework: a hierarchy of trust powered by tiered network
  policies. Standard Kubernetes NetworkPolicy resources are genuinely useful for basic
  application microsegmentation, but they have major architectural and organizational
  bottlenecks when scaled across an enterprise: Namespace-Scoped by Design: Standard
  network policies are inherently scoped to a namespace. If your security team mandates
  a cluster-wide rule, such as blocking all internal pods from querying the cloud
  provider’s metadata API (169.254.169.254), you have to copy-paste that policy into
  every single namespace. If a developer creates a new namespace, that guardrail doesn’t
  exist until someone manually applies it. Organizational Friction: Because anyone
  with namespace access can manipulate these policies, it creates a persona gap within
  organizations. Platform & Security teams need to enforce global, un-overrideable
  guardrails (e. g. “Isolate the payments namespace from everything else”).'
---
Open the original post ↗ https://www.tigera.io/blog/tiered-network-policy-scaling-kubernetes-security/
