---
title: 'The Signal in the Storm: Why Chasing More Data Misses the Point'
date: '2025-08-29T17:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/08/29/the-signal-in-the-storm-why-chasing-more-data-misses-the-point/
post_kind: link
draft: false
tldr: 'Posted on August 29, 2025 by Endre Sara, Co-Founder at Causely CNCF projects
  highlighted in this post As OpenTelemetry adoption has exploded, so has the volume
  of telemetry data moving through modern observability pipelines. But despite collecting
  more logs, metrics, and traces than ever before, teams are still struggling to answer
  the most basic questions during incidents: What broke? Where? And why? In my recent
  talk at OpenTelemetry Community Day, “ T he Signal in the Storm: Practical Strategies
  for Managing Telemetry Overload ,” I laid out a different path forward, one focused
  not on volume, but on meaning.'
summary: 'Posted on August 29, 2025 by Endre Sara, Co-Founder at Causely CNCF projects
  highlighted in this post As OpenTelemetry adoption has exploded, so has the volume
  of telemetry data moving through modern observability pipelines. But despite collecting
  more logs, metrics, and traces than ever before, teams are still struggling to answer
  the most basic questions during incidents: What broke? Where? And why? In my recent
  talk at OpenTelemetry Community Day, “ T he Signal in the Storm: Practical Strategies
  for Managing Telemetry Overload ,” I laid out a different path forward, one focused
  not on volume, but on meaning. More telemetry doesn’t guarantee more understanding.
  In many cases, it gives you the illusion of control while silently eroding your
  ability to reason about the system. That illusion becomes expensive, especially
  when telemetry pipelines are optimized for ingestion, not insight. Observability
  Needs a Better Model Traditional observability relies on emitting and aggregating
  raw signals (spans, logs, and metrics), then querying across that pile post-hoc.
  That model assumes the data will be useful after something goes wrong. But today’s
  distributed, dynamic, multi-tenant AI-driven systems don’t give you that luxury.
  The cost of collecting all raw signals without semantics and without context is
  too high. We need a shift: from streams of telemetry to structured, semantic representations
  of how systems behave. That starts by modeling the actual components of the system
  (entities) and the relationships between them. Not as metadata bolted onto spans,
  but as first-class signals.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/08/29/the-signal-in-the-storm-why-chasing-more-data-misses-the-point/
