---
title: 'Gateway API v1.2: WebSockets, Timeouts, Retries, and More'
date: '2024-11-21T09:00:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2024/11/21/gateway-api-v1-2/
post_kind: link
draft: false
tldr: Kubernetes SIG Network is delighted to announce the general availability of
  Gateway API v1. 2! This version of the API was released on October 3, and we're
  delighted to report that we now have a number of conformant implementations of it
  for you to try out.
summary: 'Kubernetes SIG Network is delighted to announce the general availability
  of Gateway API v1. 2! This version of the API was released on October 3, and we''re
  delighted to report that we now have a number of conformant implementations of it
  for you to try out. Gateway API v1. 2 brings a number of new features to the Standard
  channel (Gateway API''s GA release channel), introduces some new experimental features,
  and inaugurates our new release process — but it also brings two breaking changes
  that you''ll want to be careful of. Now that the v1 versions of GRPCRoute and ReferenceGrant
  have graduated to Standard, the old v1alpha2 versions have been removed from both
  the Standard and Experimental channels, in order to ease the maintenance burden
  that perpetually supporting the old versions would place on the Gateway API community.
  Before upgrading to Gateway API v1. 2, you''ll want to confirm that any implementations
  of Gateway API have been upgraded to support the v1 API version of these resources
  instead of the v1alpha2 API version. Note that even if you''ve been using v1 in
  your YAML manifests, a controller may still be using v1alpha2 which would cause
  it to fail during this upgrade. Additionally, Kubernetes itself goes to some effort
  to stop you from removing a CRD version that it thinks you''re using: check out
  the release notes for more information about what you need to do to safely upgrade.
  A much smaller breaking change:. status. supportedFeatures in a Gateway is now a
  list of objects instead of a list of strings.'
---
Open the original post ↗ https://kubernetes.io/blog/2024/11/21/gateway-api-v1-2/
