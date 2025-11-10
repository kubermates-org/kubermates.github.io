---
title: 'Gateway API 1.4: New Features'
date: '2025-11-06T09:00:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/11/06/gateway-api-v1-4/
post_kind: link
draft: false
tldr: 'Gateway API 1.4: New Features Graduations to Standard Channel Backend TLS policy
  Status information about the features that an implementation supports Named rules
  for Routes Experimental channel changes Enabling external Auth for HTTPRoute Mesh
  resource Introducing default Gateways Configuring client certificate validation
  Breaking changes Standard GRPCRoute -. spec field required (technicality) Experimental
  CORS support in HTTPRoute - breaking change for allowCredentials field Improving
  the development and usage experience Try it out Get involved Related Kubernetes
  blog articles Ready to rock your Kubernetes networking? The Kubernetes SIG Network
  community presented the General Availability (GA) release of Gateway API (v1.4.0)!
  Released on October 6, 2025, version 1.4.0 reinforces the path for modern, expressive,
  and extensible service networking in Kubernetes.'
summary: 'Gateway API 1.4: New Features Graduations to Standard Channel Backend TLS
  policy Status information about the features that an implementation supports Named
  rules for Routes Experimental channel changes Enabling external Auth for HTTPRoute
  Mesh resource Introducing default Gateways Configuring client certificate validation
  Breaking changes Standard GRPCRoute -. spec field required (technicality) Experimental
  CORS support in HTTPRoute - breaking change for allowCredentials field Improving
  the development and usage experience Try it out Get involved Related Kubernetes
  blog articles Ready to rock your Kubernetes networking? The Kubernetes SIG Network
  community presented the General Availability (GA) release of Gateway API (v1.4.0)!
  Released on October 6, 2025, version 1.4.0 reinforces the path for modern, expressive,
  and extensible service networking in Kubernetes. Gateway API v1.4.0 brings three
  new features to the Standard channel (Gateway API''s GA release channel): BackendTLSPolicy
  for TLS between gateways and backends supportedFeatures in GatewayClass status supportedFeatures
  Named rules for Routes and introduces three new experimental features: Mesh resource
  for service mesh configuration Default gateways to ease configuration burden** externalAuth
  filter for HTTPRoute externalAuth Leads: Candace Holman , Norwin Schnyder , Katarzyna
  Łach GEP-1897: BackendTLSPolicy BackendTLSPolicy is a new Gateway API type for specifying
  the TLS configuration of the connection from the Gateway to backend pod(s). Prior
  to the introduction of BackendTLSPolicy, there was no API specification that allowed
  encrypted traffic on the hop from Gateway to backend. The BackendTLSPolicy validation
  configuration requires a hostname. This hostname serves two purposes. It is used
  as the SNI header when connecting to the backend and for authentication, the certificate
  presented by the backend must match this hostname, unless subjectAltNames is explicitly
  specified. BackendTLSPolicy validation hostname subjectAltNames If subjectAltNames
  (SANs) are specified, the hostname is only used for SNI, and authentication is performed
  against the SANs instead. If you still need to authenticate against the hostname
  value in this case, you MUST add it to the subjectAltNames list. subjectAltNames
  hostname subjectAltNames BackendTLSPolicy validation configuration also requires
  either caCertificateRefs or wellKnownCACertificates. caCertificateRefs refer to
  one or more (up to 8) PEM-encoded TLS certificate bundles. If there are no specific
  certificates to use, then depending on your implementation, you may use wellKnownCACertificates
  , set to "System" to tell the Gateway to use an implementation-specific set of trusted
  CA Certificates.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/11/06/gateway-api-v1-4/
