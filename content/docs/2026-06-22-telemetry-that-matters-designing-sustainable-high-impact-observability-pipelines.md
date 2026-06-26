---
title: 'Telemetry that matters: Designing sustainable, high-impact observability pipelines'
date: '2026-06-22T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/06/22/telemetry-that-matters-designing-sustainable-high-impact-observability-pipelines/
post_kind: link
draft: false
tldr: 'The core problem: Over-collection and “green” observability Navigating an incident:
  From siloed signals to an observability mesh Balancing the scales: Zero-code vs.
  manual instrumentation Day 2: Optimization strategies in the pipeline Tracing the
  probabilistic frontier: Agentic and AI-driven flows Key panel takeaways Posted on
  June 22, 2026 by Diana Todea - DevRel Engineer at VictoriaMetrics and Cloud Native
  Days Romania community organizer, Laura Luttmer - Principal Product Manager at Bindplane
  (Dynatrace), Antonio Jimenez Martinez - Tech Lead Software Engineer at Cisco ThousandEyes
  As system architectures grow increasingly complex, the cloud-native community faces
  a subtle but pressing challenge: we are drowning in our own telemetry data.'
summary: 'The core problem: Over-collection and “green” observability Navigating an
  incident: From siloed signals to an observability mesh Balancing the scales: Zero-code
  vs. manual instrumentation Day 2: Optimization strategies in the pipeline Tracing
  the probabilistic frontier: Agentic and AI-driven flows Key panel takeaways Posted
  on June 22, 2026 by Diana Todea - DevRel Engineer at VictoriaMetrics and Cloud Native
  Days Romania community organizer, Laura Luttmer - Principal Product Manager at Bindplane
  (Dynatrace), Antonio Jimenez Martinez - Tech Lead Software Engineer at Cisco ThousandEyes
  As system architectures grow increasingly complex, the cloud-native community faces
  a subtle but pressing challenge: we are drowning in our own telemetry data. It is
  easier than ever to instrument an application and collect signals, but are we actually
  gaining real insights, or are we just piling up data? At the recent Observability
  Summit North America in Minneapolis, a panel of practitioners gathered to dissect
  this exact problem. This post summarizes the key strategies, shifts, and takeaways
  discussed during the panel to help engineering teams focus on the telemetry that
  truly matters. Historically, the baseline strategy for observability was simple:
  instrument everything and filter it out later. However, industry experience routinely
  shows that around 50% of collected metrics are never queried or acted upon. This
  unchecked data collection does more than just bloat storage bills; it introduces
  steep engineering overhead, increases alert noise, and heightens cognitive load
  during active incidents. A critical but frequently overlooked angle of this issue
  is green observability. Every metric stored, indexed, and processed consumes real
  compute resources, disk storage, and energy. Reducing telemetry waste isn’t just
  an infrastructure cost optimization strategy, it directly minimizes the carbon and
  environmental footprint of our cloud-native platforms. To build sustainable and
  highly reliable infrastructure, observability must be treated as a day-zero system
  design requirement. Teams need to intentionally define what a healthy system looks
  like and map out exactly which signals are needed to detect structural drift before
  pushing code to production.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/06/22/telemetry-that-matters-designing-sustainable-high-impact-observability-pipelines/
