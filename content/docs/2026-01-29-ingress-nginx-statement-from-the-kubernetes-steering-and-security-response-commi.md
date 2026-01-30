---
title: 'Ingress NGINX: Statement from the Kubernetes Steering and Security Response
  Committees'
date: '2026-01-29T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/01/29/ingress-nginx-statement/
post_kind: link
draft: false
tldr: 'Ingress NGINX: Statement from the Kubernetes Steering and Security Response
  Committees In March 2026, Kubernetes will retire Ingress NGINX, a piece of critical
  infrastructure for about half of cloud native environments. The retirement of Ingress
  NGINX was announced for March 2026, after years of public warnings that the project
  was in dire need of contributors and maintainers.'
summary: 'Ingress NGINX: Statement from the Kubernetes Steering and Security Response
  Committees In March 2026, Kubernetes will retire Ingress NGINX, a piece of critical
  infrastructure for about half of cloud native environments. The retirement of Ingress
  NGINX was announced for March 2026, after years of public warnings that the project
  was in dire need of contributors and maintainers. There will be no more releases
  for bug fixes, security patches, or any updates of any kind after the project is
  retired. This cannot be ignored, brushed off, or left until the last minute to address.
  We cannot overstate the severity of this situation or the importance of beginning
  migration to alternatives like Gateway API or one of the many third-party Ingress
  controllers immediately. To be abundantly clear: choosing to remain with Ingress
  NGINX after its retirement leaves you and your users vulnerable to attack. None
  of the available alternatives are direct drop-in replacements. This will require
  planning and engineering time. Half of you will be affected. You have two months
  left to prepare. Existing deployments will continue to work, so unless you proactively
  check, you may not know you are affected until you are compromised. In most cases,
  you can check to find out whether or not you rely on Ingress NGINX by running kubectl
  get pods --all-namespaces --selector app.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/01/29/ingress-nginx-statement/
