---
title: 'Gateway API v1.5: Moving features to Stable'
date: '2026-04-21T08:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/04/21/gateway-api-v1-5/
post_kind: link
draft: false
tldr: 'Gateway API v1.5: Moving features to Stable New release process New standard
  features ListenerSet TLSRoute HTTPRoute CORS filter Gateway client certificate validation
  Certificate selection for Gateway TLS origination ReferenceGrant promoted to v1
  Try it out Get involved The Kubernetes SIG Network community presents the release
  of Gateway API (v1.5)! Released on March 14, 2026, version 1.5 is our biggest release
  yet, and concentrates on moving existing Experimental features to Standard (Stable).
  The Gateway API v1.5.1 patch release is already available The Gateway API v1.5 brings
  six widely-requested feature promotions to the Standard channel (Gateway API''s
  GA release channel): ListenerSet TLSRoute promoted to Stable HTTPRoute CORS Filter
  Client Certificate Validation Certificate Selection for Gateway TLS Origination
  ReferenceGrant promoted to Stable Special thanks for Gateway API Contributors for
  their efforts on this release.'
summary: 'Gateway API v1.5: Moving features to Stable New release process New standard
  features ListenerSet TLSRoute HTTPRoute CORS filter Gateway client certificate validation
  Certificate selection for Gateway TLS origination ReferenceGrant promoted to v1
  Try it out Get involved The Kubernetes SIG Network community presents the release
  of Gateway API (v1.5)! Released on March 14, 2026, version 1.5 is our biggest release
  yet, and concentrates on moving existing Experimental features to Standard (Stable).
  The Gateway API v1.5.1 patch release is already available The Gateway API v1.5 brings
  six widely-requested feature promotions to the Standard channel (Gateway API''s
  GA release channel): ListenerSet TLSRoute promoted to Stable HTTPRoute CORS Filter
  Client Certificate Validation Certificate Selection for Gateway TLS Origination
  ReferenceGrant promoted to Stable Special thanks for Gateway API Contributors for
  their efforts on this release. As of Gateway API v1.5, the project has moved to
  a release train model, where on a feature freeze date, any features that are ready
  are shipped in the release. This applies to both Experimental and Standard, and
  also applies to documentation -- if the documentation isn''t ready to ship, the
  feature isn''t ready to ship. We are aiming for this to produce a more reliable
  release cadence (since we are basing our work off the excellent work done by SIG
  Release on Kubernetes itself). As part of this change, we''ve also introduced Release
  Manager and Release Shadow roles to our release team. Many thanks to Flynn (Buoyant)
  and Beka Modebadze (Google) for all the great work coordinating and filing the rough
  edges of our release process. They are both going to continue in this role for the
  next release as well. Leads: Dave Protasowski , David Jumani GEP-1713 Prior to ListenerSet,
  all listeners had to be specified directly on the Gateway object. While this worked
  well for simple use cases, it created challenges for more complex or multi-tenant
  environments: Platform teams and application teams often needed to coordinate changes
  to the same Gateway Safely delegating ownership of individual listeners was difficult
  Extending existing Gateways required direct modification of the original resource
  ListenerSet addresses these limitations by allowing listeners to be defined independently
  and then merged onto a target Gateway. ListenerSets also enable attaching more than
  64 listeners to a single, shared Gateway. This is critical for large scale deployments
  and scenarios with multiple hostnames per listener.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/04/21/gateway-api-v1-5/
