---
title: Using Istio to manage high-traffic services
date: '2026-01-06T12:46:40+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/01/06/using-istio-to-manage-high-traffic-services/
post_kind: link
draft: false
tldr: Why Istio? Preserving real client IPs with Proxy Protocol IP based access control
  Query parameter-based routing Automatic failure isolation with Outlier Detection
  Graceful shutdown for long-lived connections Key takeaways from production Conclusion
  Posted on January 6, 2026 by Ihyeok Song, STCLab SRE Team CNCF projects highlighted
  in this post At STCLab , we operate high-traffic SaaS platforms that require real-time
  traffic control and bot mitigation. Handling millions of concurrent connections
  and identifying malicious bots in real-time requires exceptional infrastructure
  stability.
summary: 'Why Istio? Preserving real client IPs with Proxy Protocol IP based access
  control Query parameter-based routing Automatic failure isolation with Outlier Detection
  Graceful shutdown for long-lived connections Key takeaways from production Conclusion
  Posted on January 6, 2026 by Ihyeok Song, STCLab SRE Team CNCF projects highlighted
  in this post At STCLab , we operate high-traffic SaaS platforms that require real-time
  traffic control and bot mitigation. Handling millions of concurrent connections
  and identifying malicious bots in real-time requires exceptional infrastructure
  stability. To achieve this, we rely on Istio. While Istio offers a vast ecosystem
  of features, this post focuses on just a select few capabilities that have proven
  most critical in our production environment. Whether you are currently evaluating
  Istio for adoption or looking for practical use cases, we hope these selected insights
  serve as a helpful guide. Istio operates as a control plane managing Envoy proxies
  deployed alongside your containers. Every Istio configuration (VirtualService, DestinationRule,
  AuthorizationPolicy) translates into Envoy’s native config. This matters for two
  reasons: Istio’s abstractions handle most use cases elegantly, and when they’re
  not enough, EnvoyFilter gives direct access to Envoy’s capabilities. We use both
  throughout our infrastructure. For our bot mitigation platform, accurate client
  IPs are everything. Without them, bot detection accuracy drops significantly. The
  challenge: when traffic passes through AWS NLB, the original client IP gets lost.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/01/06/using-istio-to-manage-high-traffic-services/
