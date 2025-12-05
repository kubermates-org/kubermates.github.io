---
title: 5 Reasons to Switch to the Calico Ingress Gateway (and How to Migrate Smoothly)
date: '2025-11-24T21:35:29+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/5-reasons-to-switch-to-the-calico-ingress-gateway-and-how-to-migrate-smoothly/
post_kind: link
draft: false
tldr: 'The End of Ingress NGINX Controller is Coming: What Comes Next? Reason 1: The
  Future Is Gateway API and Ingress Is Being Left Behind Reason 2: Production-Grade
  Envoy for Performance & Reliability Reason 3: Built-In Web Application Firewall
  (WAF) & L3–L7 Security Reason 4: Advanced Traffic Management Out of the Box Reason
  5: A Smooth Migration Path Using Standard Gateway API Resources Why Migrate to the
  Calico Ingress Gateway? Migration Prerequisites Best Practices for a Smooth Migration
  Migration Workflow Overview 1️⃣ Step 1: Enable the Calico Ingress Gateway 2️⃣ Step
  2: Create Your Gateway 3️⃣ Step 3: Convert Ingress resources to HTTPRoutes 4️⃣ Step
  4: Validate and Redirect Traffic Integrating Calico Network Policy The Ingress NGINX
  Controller is approaching retirement , which has pushed many teams to evaluate their
  long-term ingress strategy. The familiar Ingress resource has served well, but it
  comes with clear limits: annotations that differ by vendor, limited extensibility,
  and few options for separating operator and developer responsibilities.'
summary: 'The End of Ingress NGINX Controller is Coming: What Comes Next? Reason 1:
  The Future Is Gateway API and Ingress Is Being Left Behind Reason 2: Production-Grade
  Envoy for Performance & Reliability Reason 3: Built-In Web Application Firewall
  (WAF) & L3–L7 Security Reason 4: Advanced Traffic Management Out of the Box Reason
  5: A Smooth Migration Path Using Standard Gateway API Resources Why Migrate to the
  Calico Ingress Gateway? Migration Prerequisites Best Practices for a Smooth Migration
  Migration Workflow Overview 1️⃣ Step 1: Enable the Calico Ingress Gateway 2️⃣ Step
  2: Create Your Gateway 3️⃣ Step 3: Convert Ingress resources to HTTPRoutes 4️⃣ Step
  4: Validate and Redirect Traffic Integrating Calico Network Policy The Ingress NGINX
  Controller is approaching retirement , which has pushed many teams to evaluate their
  long-term ingress strategy. The familiar Ingress resource has served well, but it
  comes with clear limits: annotations that differ by vendor, limited extensibility,
  and few options for separating operator and developer responsibilities. The Gateway
  API addresses these challenges with a more expressive, standardized, and portable
  model for service networking. For organizations migrating off Ingress NGINX, the
  Calico Ingress Gateway, a production-hardened, 100% upstream distribution of Envoy
  Gateway, provides the most seamless and secure path forward. If you’re evaluating
  your options, here are the five biggest reasons teams are switching now followed
  by a step-by-step migration guide to help you make the move with confidence. Ingress
  NGINX is entering retirement. Maintaining it will become increasingly difficult
  as ecosystem support slows. The Gateway API is the replacement for Ingress and provides:
  A portable and standardized configuration model Consistent behaviour across vendors
  Cleaner separation of roles More expressive routing Support for multiple protocols
  Calico implements the Gateway API directly and gives you an upgrade path without
  shortcuts or proprietary extensions. The Gateway API is designed to replace these
  gaps with: A vendor-neutral, standard spec Role separation through GatewayClass,
  Gateway, HTTPRoute Support for richer routing, policy, and protocols A more extensible,
  future-proof foundation The Calico Ingress Gateway implements the Gateway API using
  Envoy Gateway which gives you all of these benefits with upstream compatibility.
  Calico Ingress Gateway is built on a 100 percent upstream and production-hardened
  Envoy distribution. You get: High-performance L7 traffic handling Seamless Envoy
  ecosystem compatibility Robust resiliency features (timeouts, retries, circuit breaking,
  etc. ) Envoy-native telemetry and observability If you’re currently struggling with
  NGINX’s limited L7 behaviour or annotation-driven configuration, Envoy provides
  a dramatic step up in capability.'
---
Open the original post ↗ https://www.tigera.io/blog/5-reasons-to-switch-to-the-calico-ingress-gateway-and-how-to-migrate-smoothly/
