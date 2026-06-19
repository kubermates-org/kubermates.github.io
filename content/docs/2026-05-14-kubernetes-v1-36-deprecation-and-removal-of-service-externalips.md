---
title: 'Kubernetes v1.36: Deprecation and removal of Service ExternalIPs'
date: '2026-05-14T10:35:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/05/14/kubernetes-v1-36-deprecation-and-removal-of-service-externalips/
post_kind: link
draft: false
tldr: 'Kubernetes v1.36: Deprecation and removal of Service ExternalIPs A note on
  terminology, and what hasn''t been deprecated Alternatives to externalIPs Using
  manually-managed LoadBalancer Services instead of externalIPs Using a non-cloud
  based load balancer controller Using Gateway API Timeline for externalIPs deprecation
  The. spec.'
summary: 'Kubernetes v1.36: Deprecation and removal of Service ExternalIPs A note
  on terminology, and what hasn''t been deprecated Alternatives to externalIPs Using
  manually-managed LoadBalancer Services instead of externalIPs Using a non-cloud
  based load balancer controller Using Gateway API Timeline for externalIPs deprecation
  The. spec. externalIPs field for Service was an early attempt to provide cloud-load-balancer-like
  functionality for non-cloud clusters. Unfortunately, the API assumes that every
  user in the cluster is fully trusted, and in any situation where that is not the
  case, it enables various security exploits, as described in CVE-2020-8554. spec.
  externalIPs Since Kubernetes 1.21, the Kubernetes project has recommended that all
  users disable. spec. externalIPs. To make that easier, Kubernetes also added an
  admission controller ( DenyServiceExternalIPs ) that can be enabled to do this.
  At the time, SIG Network felt that blocking the functionality by default was too
  large a breaking change to consider. spec. externalIPs DenyServiceExternalIPs However,
  the security problems are still there, and as a project we''re increasingly unhappy
  with the "insecure by default" state of the feature.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/05/14/kubernetes-v1-36-deprecation-and-removal-of-service-externalips/
