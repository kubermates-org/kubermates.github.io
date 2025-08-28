---
title: What’s New in Calico – Summer 2025
date: '2025-08-25T22:17:49+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/whats-new-in-calico-summer-2025/
post_kind: link
draft: false
tldr: As Kubernetes adoption scales across enterprise architectures, platform architects
  face mounting pressure to implement consistent security guardrails across distributed,
  multi-cluster environments while maintaining operational velocity. Modern infrastructure
  demands a security architecture that can adapt without introducing complexity or
  performance penalties.
summary: 'As Kubernetes adoption scales across enterprise architectures, platform
  architects face mounting pressure to implement consistent security guardrails across
  distributed, multi-cluster environments while maintaining operational velocity.
  Modern infrastructure demands a security architecture that can adapt without introducing
  complexity or performance penalties. Traditional approaches force architects to
  cobble together separate solutions for ingress protection, network policies, and
  application-layer security, creating operational friction and increasing attack
  surface. Today, we’re announcing significant enhancements to Calico that eliminate
  this architectural complexity. This release introduces native Web Application Firewall
  (WAF) capabilities integrated directly into Calico’s Ingress Gateway, enabling platform
  architects to deploy a single technology stack for both ingress management and HTTP-layer
  threat protection. Combined with enhanced Role-Based Access Controls (RBAC) controls,
  and centralized observability across heterogeneous workloads, platform architects
  can now design and implement comprehensive security all within a unified platform.
  The new features in this release can be grouped under two main categories: Ingress
  traffic into a Kubernetes cluster is a common entry point for attacks, so it’s critical
  to inspect and proactively secure it. Since clusters often receive traffic directly
  from the public internet, analyzing application-layer protocols like HTTP and gRPC
  for threats is a fundamental security requirement. While there are options to deploy
  a standalone Web Application Firewall (WAF) with your ingress controller, using
  an integrated WAF simplifies operations and can reduce both complexity and cost.
  Calico Ingress Gateway , our implementation of the Kubernetes Gateway API, now includes
  a built-in WAF that allows you to inspect, authorize, and secure ingress traffic
  at runtime. The WAF that is integrated with Ingress Gateway is the same as the one
  used in Calico’s workload-based WAF , giving you consistent threat detection across
  both ingress points and internal services. With this built-in WAF, you can define
  and enforce security rules directly within the Ingress Gateway, enabling deep inspection
  of HTTP and gRPC traffic and blocking known threats before they reach your workloads.'
---
Open the original post ↗ https://www.tigera.io/blog/whats-new-in-calico-summer-2025/
