---
title: 'OTel and mesh-derived metrics: A 2026 reference'
date: '2026-06-29T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/06/29/otel-and-mesh-derived-metrics-a-2026-reference/
post_kind: link
draft: false
tldr: 'What OTel covers What mesh-derived metrics cover The overlap The non-overlap
  The integration pattern A short note on cardinality Where each one earns its place
  Posted on June 29, 2026 by Mesut Oezdil, DevOps Engineer (written on behalf of Buoyant)
  CNCF projects highlighted in this post If you already run an OpenTelemetry pipeline,
  you have good visibility into what your applications are doing. This blog post is
  about what you don’t see yet: the east-west traffic between your services, measured
  at the network layer with zero changes to your application code.'
summary: 'What OTel covers What mesh-derived metrics cover The overlap The non-overlap
  The integration pattern A short note on cardinality Where each one earns its place
  Posted on June 29, 2026 by Mesut Oezdil, DevOps Engineer (written on behalf of Buoyant)
  CNCF projects highlighted in this post If you already run an OpenTelemetry pipeline,
  you have good visibility into what your applications are doing. This blog post is
  about what you don’t see yet: the east-west traffic between your services, measured
  at the network layer with zero changes to your application code. Linkerd’s proxy
  provides those metrics. Once a workload is meshed, the proxy immediately emits golden
  metrics for every inbound and outbound request. No need for instrumentation, SDK
  calls, or image rebuild. This blog post shows what those metrics look like, where
  they overlap with OTel, where they don’t, and how to wire them into an existing
  OTel Collector pipeline so both layers land in the same backend. If you come from
  the mesh side and are wondering what OTel adds, you’ll learn that too. The setup
  The reference environment is K3s v1.34.6 (single node), Linkerd 2.19+ (tested on
  edge-26.5.5, June 2026), the OpenTelemetry Demo (Astronomy Shop) as the meshed workload,
  OTel Collector contrib 0.118.0 as a DaemonSet, and VictoriaMetrics with Grafana.
  The working Collector config and Grafana dashboard are available as downloads at
  the end of this post. The OpenTelemetry specification defines three signal types:
  traces, metrics, and logs. Traces follow a request across service boundaries and
  give you the full call graph. Metrics capture numeric measurements over time: counters,
  gauges, and histograms.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/06/29/otel-and-mesh-derived-metrics-a-2026-reference/
