---
title: How to build a cost-effective observability platform with OpenTelemetry
date: '2025-12-16T15:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/12/16/how-to-build-a-cost-effective-observability-platform-with-opentelemetry/
post_kind: link
draft: false
tldr: The Challenge Observability Architecture Overview Key Architectural Decisions
  Centralized Backend, Distributed Collectors OpenTelemetry as the Universal Ingestion
  Layer Key Configurations Patterns Key Challenges The Metric Explosion Version Alignment
  Small Node OOM Conclusion Posted on December 16, 2025 by By Grace Park, DevOps Engineer,
  STCLab SRE Team CNCF projects highlighted in this post Managing millions of concurrent
  connections during global events like flash sales and online voting requires resilient,
  scalable observability. At STCLab, we operate platforms such as NetFUNNEL and BotManager
  that support up to 3.5 million simultaneous users across 200 countries.
summary: 'The Challenge Observability Architecture Overview Key Architectural Decisions
  Centralized Backend, Distributed Collectors OpenTelemetry as the Universal Ingestion
  Layer Key Configurations Patterns Key Challenges The Metric Explosion Version Alignment
  Small Node OOM Conclusion Posted on December 16, 2025 by By Grace Park, DevOps Engineer,
  STCLab SRE Team CNCF projects highlighted in this post Managing millions of concurrent
  connections during global events like flash sales and online voting requires resilient,
  scalable observability. At STCLab, we operate platforms such as NetFUNNEL and BotManager
  that support up to 3.5 million simultaneous users across 200 countries. In 2023,
  we made a pivotal decision to sunset our 20-year legacy, on-premise architecture.
  We completely restructured our platform, building NetFUNNEL 4. x from the ground
  up as a global, Kubernetes-native SaaS. Cost wasn’t the only issue. It was the consequences.
  We were forced to disable APM entirely in dev/staging environments and sample just
  5% of production traffic. Performance regressions were only caught after hitting
  production. This reactive firefighting was unsustainable. We needed a solution that
  could monitor all environments cost-effectively without compromises. We migrated
  to open observability standards with a full CNCF backing: OpenTelemetry for instrumentation
  and the LGTM stack—Loki, Grafana, Tempo, and Mimir.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/12/16/how-to-build-a-cost-effective-observability-platform-with-opentelemetry/
