---
title: Is It Time to Migrate? A Practical Look at Kubernetes Ingress vs. Gateway API
date: '2025-06-04T14:10:48+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/is-it-time-to-migrate-a-practical-look-at-kubernetes-ingress-vs-gateway-api/
post_kind: link
draft: false
tldr: If you’ve managed traffic in Kubernetes, you’ve likely navigated the world of
  Ingress controllers. For years, Ingress has been the standard way of getting HTTP/S
  services exposed.
summary: 'If you’ve managed traffic in Kubernetes, you’ve likely navigated the world
  of Ingress controllers. For years, Ingress has been the standard way of getting
  HTTP/S services exposed. But let’s be honest, it often felt like a compromise. We
  wrestled with controller-specific annotations to unlock critical features, blurred
  the lines between infrastructure and application concerns, this complexity didn’t
  just make portability more difficult, it sometimes led to security vulnerabilities
  and other complications. As part of Calico Open Source v3. 30 , we have released
  a free and open source Calico Ingress Gateway that implements a custom built Envoy
  proxy with the Kubernetes Gateway API standard to help you navigate Ingress complexities
  with style. This blog post is designed to get you up to speed on why such a change
  might be the missing link in your environment. The challenge with traditional Ingress
  wasn’t a lack of effort, since the landscape is full of innovative solutions. However,
  the problem was the lack of a unified, expressive, and role-aware standard. Existing
  ingress controllers were capable, implemented advanced features, however at the
  same time tied you to a specific project/vendor. This meant: This “Ingress rut”
  had tangible consequences. Platform teams struggled to enforce security standards
  and provide a consistent ingress experience.'
---
Open the original post ↗ https://www.tigera.io/blog/is-it-time-to-migrate-a-practical-look-at-kubernetes-ingress-vs-gateway-api/
