---
title: BackendTLSPolicy expands Gateway API transport security
date: '2026-07-03T00:00:00+00:00'
tags:
- openshift
source: OpenShift Blog
external_url: https://www.redhat.com/en/blog/backendtlspolicy-expands-gateway-api-transport-security
post_kind: link
draft: false
tldr: BackendTLSPolicy expands Gateway API transport security How Gateway API features
  make it into OpenShift Modern network ingress with OpenShift features Understanding
  BackendTLSPolicy Red Hat OpenShift Container Platform | Product Trial About the
  author Candace Holman More like this Introducing Red Hat OpenShift Service Mesh
  3.4 The new currency of enterprise velocity Collaboration In Product Security |
  Compiler Keeping Track Of Vulnerabilities With CVEs | Compiler Keep exploring Browse
  by channel Automation Artificial intelligence Open hybrid cloud Security Edge computing
  Infrastructure Applications Virtualization Share BackendTLSPolicy is a Kubernetes
  resource that allows the specification of additional Transport Layer Security (TLS)
  encryption in Gateway API. It gives Gateway API users on Red Hat OpenShift access
  to the same level of secured traffic as the OpenShift route provides with re-encrypt
  termination, and is now available in Red Hat OpenShift 4.22.
summary: BackendTLSPolicy expands Gateway API transport security How Gateway API features
  make it into OpenShift Modern network ingress with OpenShift features Understanding
  BackendTLSPolicy Red Hat OpenShift Container Platform | Product Trial About the
  author Candace Holman More like this Introducing Red Hat OpenShift Service Mesh
  3.4 The new currency of enterprise velocity Collaboration In Product Security |
  Compiler Keeping Track Of Vulnerabilities With CVEs | Compiler Keep exploring Browse
  by channel Automation Artificial intelligence Open hybrid cloud Security Edge computing
  Infrastructure Applications Virtualization Share BackendTLSPolicy is a Kubernetes
  resource that allows the specification of additional Transport Layer Security (TLS)
  encryption in Gateway API. It gives Gateway API users on Red Hat OpenShift access
  to the same level of secured traffic as the OpenShift route provides with re-encrypt
  termination, and is now available in Red Hat OpenShift 4.22. Re-encrypt TLS termination
  is already used for the OpenShift route that provides access to the web console,
  and provides encrypted login functionality to customer applications. BackendTLSPolicy
  Gateway API is the open source, next-generation network ingress solution developed
  as a project of the Kubernetes networking community to replace its legacy Kubernetes
  ingress solution. OpenShift began supporting Gateway API as a general availability
  feature in release 4.19. BackendTLSPolicy is a recent contribution championed by
  Red Hat in order to provide functionality matching the existing OpenShift route
  re-encrypt TLS feature. BackendTLSPolicy Those of us on the Red Hat OpenShift Network
  Engineering team get a lot of questions about how open source Gateway API features
  make it into OpenShift as a router feature. The process is semi-predictable and
  is dependent on our chosen implementation, Istio via Red Hat OpenShift Service Mesh.
  The first step in the process is to propose and get acceptance of a feature in the
  Gateway API community. After the feature is promoted to the stable channel and released
  upstream, Istio must document its conformance with Gateway API. Next, the OpenShift
  Service Mesh team upgrades to the Istio version containing that feature. Then the
  Network Engineering team upgrades to the conformant OpenShift Service Mesh version
  and Gateway API custom resource definitions.
---
Open the original post ↗ https://www.redhat.com/en/blog/backendtlspolicy-expands-gateway-api-transport-security
