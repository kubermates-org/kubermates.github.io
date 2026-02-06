---
title: 'Migrating from NGINX Ingress to Calico Ingress Gateway: A Step-by-Step Guide'
date: '2026-02-05T21:00:48+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/migrating-from-nginx-ingress-to-calico-ingress-gateway-a-step-by-step-guide/
post_kind: link
draft: false
tldr: 'A Brief History Why the Industry is Standardizing on Gateway API Prerequisites
  & Preparation Create TLS Secrets (Required for HTTPS) Migration Guide: Table of
  Contents Phase 1: Enabling Calico Ingress Gateway Phase 2: Converting Ingress Resources
  to Gateway API Examples of Ingress to HTTPRoute conversion Phase 3: Verification
  & Cutover Strategies Final Traffic Cutover Step 1: Redirect Traffic to the New Gateway
  Step 2: Monitor the Cutover Step 3: Decommissioning NGINX Troubleshooting & FAQ
  Appendix: Automating Certificate Management (TLS) with Cert-Manager 1. Install cert-manager
  2.'
summary: 'A Brief History Why the Industry is Standardizing on Gateway API Prerequisites
  & Preparation Create TLS Secrets (Required for HTTPS) Migration Guide: Table of
  Contents Phase 1: Enabling Calico Ingress Gateway Phase 2: Converting Ingress Resources
  to Gateway API Examples of Ingress to HTTPRoute conversion Phase 3: Verification
  & Cutover Strategies Final Traffic Cutover Step 1: Redirect Traffic to the New Gateway
  Step 2: Monitor the Cutover Step 3: Decommissioning NGINX Troubleshooting & FAQ
  Appendix: Automating Certificate Management (TLS) with Cert-Manager 1. Install cert-manager
  2. Enable Gateway API Support 3. Configure Let’s Encrypt ClusterIssuer 4. Annotate
  Gateways for Certificate Management Migration Summary Start Your Gateway API Migration
  with Calico In our previous post, we addressed the most common questions platform
  teams are asking as they prepare for the retirement of the NGINX Ingress Controller.
  With the March 2026 deadline fast approaching, this guide provides a hands-on, step-by-step
  walkthrough for migrating to the Kubernetes Gateway API using Calico Ingress Gateway.
  You will learn how to translate NGINX annotations into HTTPRoute rules, run both
  models side by side, and safely cut over live traffic. The announced retirement
  of the NGINX Ingress Controller has created a forced migration path for the many
  teams that relied on it as the industry standard. While the Ingress API is not yet
  officially deprecated, the Kubernetes SIG Network has designated the Gateway API
  as its official successor. Legacy Ingress will no longer receive enhancements and
  exists primarily for backward compatibility. While the Ingress API served the community
  for years, it reached a functional ceiling. Calico Ingress Gateway implements the
  Gateway API to provide: Role-Oriented Design: Clear separation between the infrastructure
  (managed by SREs) and routing logic (managed by Developers).'
---
Open the original post ↗ https://www.tigera.io/blog/migrating-from-nginx-ingress-to-calico-ingress-gateway-a-step-by-step-guide/
