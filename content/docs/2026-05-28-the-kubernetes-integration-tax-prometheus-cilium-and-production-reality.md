---
title: 'The Kubernetes integration tax: Prometheus, Cilium and production reality'
date: '2026-05-28T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/05/28/the-kubernetes-integration-tax-prometheus-cilium-and-production-reality/
post_kind: link
draft: false
tldr: Every team builds the same stack. Every team breaks it differently.
summary: Every team builds the same stack. Every team breaks it differently. Where
  CNCF projects collide Cluster API gave us one workflow for four clouds The architecture
  that finally stopped the bleeding Hard-won lessons from production The compounding
  cost Posted on May 28, 2026 by Rishi Mondal, SRE at Obmondo and CNCF KubeStellar
  Maintainer CNCF projects highlighted in this post I still remember the first time
  we lost sleep over something that wasn’t a bug. It was a Tuesday. Grafana dashboards
  showed blank panels for Cilium network metrics. Hubble was working fine — DNS visibility,
  TCP flows, and HTTP latency were all there in the Hubble UI. But the on-call engineer
  staring at Grafana at 2 AM couldn’t see any of it. The reason? Prometheus had no
  ServiceMonitors wired to Cilium’s agent and operator pods. Two Cloud Native Computing
  Foundation (CNCF) projects, both installed correctly, were completely invisible
  to each other. This is what’s known as the integration tax. It’s the hidden cost
  of running multiple CNCF projects together in production, and it’s where most platform
  teams spend 80% of their time — not installing projects and not tuning them individually,
  but wiring them together. Hence, they actually talk to each other.
---
Open the original post ↗ https://www.cncf.io/blog/2026/05/28/the-kubernetes-integration-tax-prometheus-cilium-and-production-reality/
