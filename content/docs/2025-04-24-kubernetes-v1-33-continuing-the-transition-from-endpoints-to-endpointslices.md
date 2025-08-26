---
title: 'Kubernetes v1.33: Continuing the transition from Endpoints to EndpointSlices'
date: '2025-04-24T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/04/24/endpoints-deprecation/
post_kind: link
draft: false
tldr: Since the addition of EndpointSlices ( KEP-752 ) as alpha in v1.
summary: Since the addition of EndpointSlices ( KEP-752 ) as alpha in v1. 15 and later
  GA in v1. 21, the Endpoints API in Kubernetes has been gathering dust. New Service
  features like dual-stack networking and traffic distribution are only supported
  via the EndpointSlice API, so all service proxies, Gateway API implementations,
  and similar controllers have had to be ported from using Endpoints to using EndpointSlices.
  At this point, the Endpoints API is really only there to avoid breaking end user
  workloads and scripts that still make use of it. As of Kubernetes 1.
---
Open the original post ↗ https://kubernetes.io/blog/2025/04/24/endpoints-deprecation/
