---
title: Kgateway v2.1 is released!
date: '2025-11-18T15:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/11/18/kgateway-v2-1-is-released/
post_kind: link
draft: false
tldr: 🌟 What’s new in kgateway 2.1? Agentgateway integration K8s GW API 1.3.0 and
  Inference Extension 1.0.0 Global policy attachment Deep merging for extauth and
  extproc policies Additional proxy pod template customization Horizontal Pod Autoscaling
  Dynamic Forward Proxy Session Affinity Enhanced retries and timeout capabilities
  Passive health checks with outlier detection New kgateway operations dashboard 🗑️
  Deprecated or removed features Release notes Availability Thanks to our contributors!
  Get Involved Posted on November 18, 2025 by Nina Polshakova, Nadine Spies, & Michael
  Levan, Solo. io, Aryan Parashar, LFX Mentee CNCF projects highlighted in this post
  Kgateway is an open source implementation of the Kubernetes Gateway API that unifies
  ingress, API gateway, service mesh, and AI gateway capabilities in a singular modular
  control plane.
summary: '🌟 What’s new in kgateway 2.1? Agentgateway integration K8s GW API 1.3.0
  and Inference Extension 1.0.0 Global policy attachment Deep merging for extauth
  and extproc policies Additional proxy pod template customization Horizontal Pod
  Autoscaling Dynamic Forward Proxy Session Affinity Enhanced retries and timeout
  capabilities Passive health checks with outlier detection New kgateway operations
  dashboard 🗑️ Deprecated or removed features Release notes Availability Thanks to
  our contributors! Get Involved Posted on November 18, 2025 by Nina Polshakova, Nadine
  Spies, & Michael Levan, Solo. io, Aryan Parashar, LFX Mentee CNCF projects highlighted
  in this post Kgateway is an open source implementation of the Kubernetes Gateway
  API that unifies ingress, API gateway, service mesh, and AI gateway capabilities
  in a singular modular control plane. Built for performance and flexibility, it secures
  and manages traffic across legacy, cloud native, and AI-driven workloads in any
  environment. We’re excited to announce the release of kgateway v2.1. , a release
  packed with exciting new features and improvements. Here are a few select updates
  the kgateway team would like to highlight! This release marks a major milestone
  — it’s the first version to integrate the open source project agentgateway ! Agentgateway
  is a highly available, highly scalable data plane that provides AI connectivity
  for LLMs, MCP tools, AI agents, and inference workloads. As part of this evolution,
  we’re beginning the deprecation of the Envoy-based AI Gateway and the Envoy-based
  Inference Extension, since all related functionality is now implemented natively
  through agentgateway. You can still continue to use Envoy-based Gateways for API
  Gateway use cases. For this release, agentgateway support is in beta. If you’re
  trying out the agentgateway GatewayClass , we recommend following the beta release
  feed to stay up to date with improvements, bug fixes, and breaking changes as the
  implementation is refined. agentgateway GatewayClass To get started with agentgateway,
  you simply install kgateway with the following Helm values: agentgateway : enabled
  : true Then you create a Gateway with the agentgateway GatewayClass as shown here:
  agentgateway GatewayClass kubectl apply -f- <<EOF kind : Gateway apiVersion : gateway.
  networking.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/11/18/kgateway-v2-1-is-released/
