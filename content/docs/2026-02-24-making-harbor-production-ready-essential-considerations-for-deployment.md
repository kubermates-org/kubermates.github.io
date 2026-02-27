---
title: 'Making Harbor production-ready: Essential considerations for deployment'
date: '2026-02-24T12:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/02/24/making-harbor-production-ready-essential-considerations-for-deployment/
post_kind: link
draft: false
tldr: 2. Security best practices Conclusion Posted on February 24, 2026 by Dhruv Tyagi
  and Daniel Jiang, Broadcom CNCF projects highlighted in this post Harbor is an open-source
  container registry that secures artifacts with policies and role-based access control,
  ensuring images are scanned for vulnerabilities and signed as trusted.
summary: '2. Security best practices Conclusion Posted on February 24, 2026 by Dhruv
  Tyagi and Daniel Jiang, Broadcom CNCF projects highlighted in this post Harbor is
  an open-source container registry that secures artifacts with policies and role-based
  access control, ensuring images are scanned for vulnerabilities and signed as trusted.
  To learn more about Harbor and how to deploy it on a Virtual Machine (VM) and in
  Kubernetes (K8s), refer to parts 1 and 2 of the series. While deploying Harbor is
  straightforward, making it production-ready requires careful consideration of several
  key aspects. This blog outlines critical factors to ensure your Harbor instance
  is robust, secure, and scalable for production environments. For this blog, we will
  focus on Harbor deployed on Kubernetes via Helm as our base and provide suggestions
  for this specific deployment. For a production environment, single points of failure
  are unacceptable, especially for an image registry that will act as a central repository
  for storing and pulling images and artifacts for development and production applications.
  Thus, implementing high availability for Harbor is crucial and involves several
  key considerations: Deploy with an Ingress: Configure a Kubernetes Service of type
  Ingress controller (e. g. Traefik) in front of your Harbor instances to distribute
  incoming traffic efficiently and provide a unified entry point along with cert-manager
  for certificate management. You can specify this in your values. yaml file under:
  expose: type: ingress tls: enabled: true certSource: secret ingress: hosts: core:
  harbor.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/02/24/making-harbor-production-ready-essential-considerations-for-deployment/
