---
title: Securing Kubernetes Traffic with Calico Ingress Gateway
date: '2025-06-17T16:26:04+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/securing-kubernetes-traffic-with-calico-ingress-gateway/
post_kind: link
draft: false
tldr: Wait a second, is this the ‘Ingress vs. Gateway API’ debate? What makes Gateway
  API different? The Ingress Rut The purpose of this blog post Requirements Spin up
  a Kubernetes Cluster Install Calico with Operator Deploy a Demo Application Enable
  Calico Ingress Gateway Deploy Gateway API Resources Gateway HTTPRoute SSL Certificate
  and Automated Certification Process with Cert-Manager Gateway API integration ClusterIssuer
  Enabling HTTPS using Calico Ingress Gateway Force Redirect to HTTPS Clean up Conclusion
  If you’ve managed traffic in Kubernetes, you’ve likely navigated the world of Ingress
  controllers.
summary: 'Wait a second, is this the ‘Ingress vs. Gateway API’ debate? What makes
  Gateway API different? The Ingress Rut The purpose of this blog post Requirements
  Spin up a Kubernetes Cluster Install Calico with Operator Deploy a Demo Application
  Enable Calico Ingress Gateway Deploy Gateway API Resources Gateway HTTPRoute SSL
  Certificate and Automated Certification Process with Cert-Manager Gateway API integration
  ClusterIssuer Enabling HTTPS using Calico Ingress Gateway Force Redirect to HTTPS
  Clean up Conclusion If you’ve managed traffic in Kubernetes, you’ve likely navigated
  the world of Ingress controllers. For years, Ingress has been the standard way of
  getting our HTTP/S services exposed. But let’s be honest, it often felt like a compromise.
  We wrestled with controller-specific annotations to unlock critical features, blurred
  the lines between infrastructure and application concerns, and sometimes wished
  for richer protocol support or a more standardized approach. This “pile of vendor
  annotations,” while functional, highlighted the limitations of a standard that struggled
  to keep pace with the complex demands of modern, multi-team environments and even
  led to security vulnerabilities. Yes, and it’s a crucial one. The Kubernetes Gateway
  API isn’t just an Ingress v2; it’s a fundamental redesign, the “future” of Kubernetes
  ingress, built by the community to address these very challenges head-on. There
  are three main points that I came across while evaluating GatewayAPI and Ingress
  controllers: Standardization & Portability: It aims to provide a core, standard
  way to manage ingress, reducing reliance on vendor-specific hacks and making it
  easier to switch implementations – change the class, and it should “just work. ”
  Role-Based Architecture: Its biggest win is arguably the separation of concerns.
  Infrastructure teams can manage the Gateway (the entry point, TLS, ports), while
  application teams manage their HTTPRoutes (or TCPRoutes, etc. ), defining where
  their specific traffic should go.'
---
Open the original post ↗ https://www.tigera.io/blog/securing-kubernetes-traffic-with-calico-ingress-gateway/
