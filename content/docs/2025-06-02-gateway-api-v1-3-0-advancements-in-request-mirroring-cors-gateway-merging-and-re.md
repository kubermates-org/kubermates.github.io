---
title: 'Gateway API v1.3.0: Advancements in Request Mirroring, CORS, Gateway Merging,
  and Retry Budgets'
date: '2025-06-02T09:00:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/06/02/gateway-api-v1-3/
post_kind: link
draft: false
tldr: 'Gateway API v1.3.0: Advancements in Request Mirroring, CORS, Gateway Merging,
  and Retry Budgets Graduation to Standard channel Percentage-based request mirroring
  Additions to Experimental channel CORS filtering XListenerSets (standardized mechanism
  for Listener and Gateway merging) Retry budgets (XBackendTrafficPolicy) Try it out
  Get involved Related Kubernetes blog articles Join us in the Kubernetes SIG Network
  community in celebrating the general availability of Gateway API v1.3.0! We are
  also pleased to announce that there are already a number of conformant implementations
  to try, made possible by postponing this blog announcement. Version 1.3.0 of the
  API was released about a month ago on April 24, 2025.'
summary: 'Gateway API v1.3.0: Advancements in Request Mirroring, CORS, Gateway Merging,
  and Retry Budgets Graduation to Standard channel Percentage-based request mirroring
  Additions to Experimental channel CORS filtering XListenerSets (standardized mechanism
  for Listener and Gateway merging) Retry budgets (XBackendTrafficPolicy) Try it out
  Get involved Related Kubernetes blog articles Join us in the Kubernetes SIG Network
  community in celebrating the general availability of Gateway API v1.3.0! We are
  also pleased to announce that there are already a number of conformant implementations
  to try, made possible by postponing this blog announcement. Version 1.3.0 of the
  API was released about a month ago on April 24, 2025. Gateway API v1.3.0 brings
  a new feature to the Standard channel (Gateway API''s GA release channel): percentage-based
  request mirroring , and introduces three new experimental features: cross-origin
  resource sharing (CORS) filters, a standardized mechanism for listener and gateway
  merging, and retry budgets. Also see the full release notes and applaud the v1.3.0
  release team next time you see them. Graduation to the Standard channel is a notable
  achievement for Gateway API features, as inclusion in the Standard release channel
  denotes a high level of confidence in the API surface and provides guarantees of
  backward compatibility. Of course, as with any other Kubernetes API, Standard channel
  features can continue to evolve with backward-compatible additions over time, and
  we (SIG Network) certainly expect further refinements and improvements in the future.
  For more information on how all of this works, refer to the Gateway API Versioning
  Policy. Leads: Lior Lieberman , Jake Bennert GEP-3171: Percentage-Based Request
  Mirroring Percentage-based request mirroring is an enhancement to the existing support
  for HTTP request mirroring , which allows HTTP requests to be duplicated to another
  backend using the RequestMirror filter type. Request mirroring is particularly useful
  in blue-green deployment. It can be used to assess the impact of request scaling
  on application performance without impacting responses to clients. The previous
  mirroring capability worked on all the requests to a backendRef. Percentage-based
  request mirroring allows users to specify a subset of requests they want to be mirrored,
  either by percentage or fraction.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/06/02/gateway-api-v1-3/
