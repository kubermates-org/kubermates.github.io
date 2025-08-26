---
title: 'Kubernetes v1.33: Continuing the transition from Endpoints to EndpointSlices'
date: '2025-04-24T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/04/24/endpoints-deprecation/
post_kind: link
draft: false
tldr: Since the addition of EndpointSlices ( KEP-752 ) as alpha in v1. 15 and later
  GA in v1.
summary: 'Since the addition of EndpointSlices ( KEP-752 ) as alpha in v1. 15 and
  later GA in v1. 21, the Endpoints API in Kubernetes has been gathering dust. New
  Service features like dual-stack networking and traffic distribution are only supported
  via the EndpointSlice API, so all service proxies, Gateway API implementations,
  and similar controllers have had to be ported from using Endpoints to using EndpointSlices.
  At this point, the Endpoints API is really only there to avoid breaking end user
  workloads and scripts that still make use of it. As of Kubernetes 1. 33, the Endpoints
  API is now officially deprecated, and the API server will return warnings to users
  who read or write Endpoints resources rather than using EndpointSlices. Eventually,
  the plan (as documented in KEP-4974 ) is to change the Kubernetes Conformance criteria
  to no longer require that clusters run the Endpoints controller (which generates
  Endpoints objects based on Services and Pods), to avoid doing work that is unneeded
  in most modern-day clusters. Thus, while the Kubernetes deprecation policy means
  that the Endpoints type itself will probably never completely go away, users who
  still have workloads or scripts that use the Endpoints API should start migrating
  them to EndpointSlices. For end users, the biggest change between the Endpoints
  API and the EndpointSlice API is that while every Service with a selector has exactly
  1 Endpoints object (with the same name as the Service), a Service may have any number
  of EndpointSlices associated with it: In this case, because the service is dual
  stack, it has 2 EndpointSlices: 1 for IPv4 addresses and 1 for IPv6 addresses. (The
  Endpoints API does not support dual stack, so the Endpoints object shows only the
  addresses in the cluster''s primary address family. ) Although any Service with
  multiple endpoints can have multiple EndpointSlices, there are three main cases
  where you will see this: An EndpointSlice can only represent endpoints of a single
  IP family, so dual-stack Services will have separate EndpointSlices for IPv4 and
  IPv6.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/04/24/endpoints-deprecation/
