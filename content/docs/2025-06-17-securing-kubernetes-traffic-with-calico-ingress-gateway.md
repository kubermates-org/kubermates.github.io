---
title: Securing Kubernetes Traffic with Calico Ingress Gateway
date: '2025-06-17T16:26:04+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/securing-kubernetes-traffic-with-calico-ingress-gateway/
post_kind: link
draft: false
tldr: If you’ve managed traffic in Kubernetes, you’ve likely navigated the world of
  Ingress controllers. For years, Ingress has been the standard way of getting our
  HTTP/S services exposed.
summary: 'If you’ve managed traffic in Kubernetes, you’ve likely navigated the world
  of Ingress controllers. For years, Ingress has been the standard way of getting
  our HTTP/S services exposed. But let’s be honest, it often felt like a compromise.
  We wrestled with controller-specific annotations to unlock critical features, blurred
  the lines between infrastructure and application concerns, and sometimes wished
  for richer protocol support or a more standardized approach. This “pile of vendor
  annotations,” while functional, highlighted the limitations of a standard that struggled
  to keep pace with the complex demands of modern, multi-team environments and even
  led to security vulnerabilities. Yes, and it’s a crucial one. The Kubernetes Gateway
  API isn’t just an Ingress v2; it’s a fundamental redesign, the “future” of Kubernetes
  ingress, built by the community to address these very challenges head-on. There
  are three main points that I came across while evaluating GatewayAPI and Ingress
  controllers: The Ingress controller landscape is a mishmash of vendors with cool
  ideas. While they all can route HTTP/S traffic into your cluster, expanding your
  services to include other protocols puts you at the mercy of that vendor and the
  capabilities that they implement. On top of that, if you try to migrate from your
  old Ingress Controller to a new one at some point, there is that sweet conversation
  of vendor lock-in which ties your hands. If you are wondering how vendor lock-in
  plays a role here, then take a closer look at your Ingress resources, don’t they
  all share some sort of annotation? That “pile of vendor annotations,” while functional,
  is specific to that one great solution you are currently using, highlighting the
  limitations of a standard that struggled to keep pace and even led to security vulnerabilities.
  While Ingress isn’t disappearing tomorrow, the direction is clear.'
---
Open the original post ↗ https://www.tigera.io/blog/securing-kubernetes-traffic-with-calico-ingress-gateway/
