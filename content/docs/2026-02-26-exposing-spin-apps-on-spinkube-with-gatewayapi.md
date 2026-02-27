---
title: Exposing Spin apps on SpinKube with GatewayAPI
date: '2026-02-26T12:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/02/26/exposing-spin-apps-on-spinkube-with-gatewayapi/
post_kind: link
draft: false
tldr: What is SpinKube What is Gateway API Build and deploy the Spin apps to Kubernetes
  Testing the Spin app Installing Gateway API CRDs and Controller Creating application-specific
  Gateway API Resources Accessing the Spin apps Conclusion Posted on February 26,
  2026 by Thorsten Hans, SpinKube Maintainer and Senior Developer Advocate, Akamai
  CNCF projects highlighted in this post The Gateway API isn’t just an “Ingress v2”,
  it’s an entirely revamped approach for exposing services from within Kubernetes
  and eliminates the need of encoding routing capabilities into vendor-specific, unstructured
  annotations. In this post, we will explore how to expose WebAssembly applications
  built using the CNCF Spin framework and served by SpinKube using the Gateway API.
summary: What is SpinKube What is Gateway API Build and deploy the Spin apps to Kubernetes
  Testing the Spin app Installing Gateway API CRDs and Controller Creating application-specific
  Gateway API Resources Accessing the Spin apps Conclusion Posted on February 26,
  2026 by Thorsten Hans, SpinKube Maintainer and Senior Developer Advocate, Akamai
  CNCF projects highlighted in this post The Gateway API isn’t just an “Ingress v2”,
  it’s an entirely revamped approach for exposing services from within Kubernetes
  and eliminates the need of encoding routing capabilities into vendor-specific, unstructured
  annotations. In this post, we will explore how to expose WebAssembly applications
  built using the CNCF Spin framework and served by SpinKube using the Gateway API.
  SpinKube , a CNCF sandbox project, is an open-source stack for running serverless
  WebAssembly applications (Spin apps) on top of Kubernetes. Although SpinKube leverages
  Kubernetes primitives like Deployments, Services and Pods, there are no containers
  involved for running your serverless Spin apps at all. Instead, it leverages a containerd-shim
  implementation and spawns processes on the underlying Kubernetes worker nodes for
  running Spin apps. containerd-shim You can learn more about SpinKube and find detailed
  instructions on how to deploy SpinKube to your Kubernetes cluster at https://spinkube.
  dev. The Gateway API is the modern, role-oriented successor to the legacy Ingress
  resource, designed to provide a more expressive and extensible networking interface
  for Kubernetes. Unlike Ingress, which often relies on a messy sprawl of vendor-specific
  annotations to handle complex logic, the Gateway API breaks traffic management into
  atomic resources — GatewayClass, Gateway , and routes (like HTTPRoute or GRPCRoute
  ). Ingress GatewayClass, Gateway HTTPRoute GRPCRoute This separation allows infrastructure
  admins to manage the entry points while giving developers control over how their
  specific services are exposed, enabling native support for advanced traffic patterns
  like canary rollouts, header-based routing, and traffic mirroring without the need
  for bespoke configurations. To dive deeper into the technical specifications and
  resource hierarchy, head over to the official Gateway API documentation. Provisioning
  a Kubernetes cluster, installing SpinKube and implementing Spin apps are considered
  beyond the scope of this article.
---
Open the original post ↗ https://www.cncf.io/blog/2026/02/26/exposing-spin-apps-on-spinkube-with-gatewayapi/
