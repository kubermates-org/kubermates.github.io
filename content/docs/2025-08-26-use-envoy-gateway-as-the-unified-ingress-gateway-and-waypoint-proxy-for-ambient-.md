---
title: Use Envoy Gateway as the Unified Ingress Gateway and Waypoint Proxy for Ambient
  Mesh
date: '2025-08-26T13:09:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/08/26/use-envoy-gateway-as-the-unified-ingress-gateway-and-waypoint-proxy-for-ambient-mesh/
post_kind: link
draft: false
tldr: Posted on August 26, 2025 by Huabing (Robin) Zhao, Software Engineer & Ric Hincapié,
  DevOps and Support Engineer at Tetrate In this article, we’ll look at how you can
  use Envoy Gateway , an Envoy project open source solution, together with Istio when
  running in Ambient mode. This allows you to easily leverage the power of Envoy’s
  L7 capabilities for Ingress and east-west traffic in your mesh with easy-to-use
  CRDs.
summary: 'Posted on August 26, 2025 by Huabing (Robin) Zhao, Software Engineer & Ric
  Hincapié, DevOps and Support Engineer at Tetrate In this article, we’ll look at
  how you can use Envoy Gateway , an Envoy project open source solution, together
  with Istio when running in Ambient mode. This allows you to easily leverage the
  power of Envoy’s L7 capabilities for Ingress and east-west traffic in your mesh
  with easy-to-use CRDs. To understand how this integration works, let’s first take
  a quick look at Ambient Mesh itself. Also known as Istio Ambient mode , it’s a sidecar-less
  service mesh architecture that aims to simplify deployments and can boost efficiency
  for specific use cases. Unlike sidecar-based meshes, Ambient splits the data plane
  into two key components: the ztunnel , which secures service-to-service communication,
  and the Waypoint Proxy , which handles Layer 7 traffic routing and policy enforcement.
  On the other side, Envoy Gateway is a Kubernetes-native API gateway built on top
  of Envoy Proxy. It’s designed to work seamlessly with the Kubernetes Gateway API
  and takes a batteries-included approach—offering built-in support for authentication,
  authorization, rate limiting, CORS handling, header manipulation, and more. These
  capabilities are exposed through familiar Kubernetes-style APIs, letting you fully
  tap into Envoy’s power without needing complex configurations. Because both Ambient
  Mesh and Envoy Gateway are built on top of Envoy, they share a common foundation.
  This makes integration straightforward and allows Envoy Gateway to act as both the
  Ingress Gateway and Waypoint Proxy —giving you a consistent and powerful way to
  manage traffic and apply Layer 7 policies across your mesh. While Ambient Mesh simplifies
  service mesh operations by removing sidecars, its feature set doesn’t yet match
  the maturity of the sidecar-based model. Some advanced Layer 7 capabilities are
  either missing, considered experimental, or require extra complexity to configure
  in native Ambient mode.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/08/26/use-envoy-gateway-as-the-unified-ingress-gateway-and-waypoint-proxy-for-ambient-mesh/
