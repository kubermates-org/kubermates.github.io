---
title: Auto-diagnosing Kubernetes alerts with HolmesGPT and CNCF tools
date: '2026-04-21T15:06:09+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/04/21/auto-diagnosing-kubernetes-alerts-with-holmesgpt-and-cncf-tools/
post_kind: link
draft: false
tldr: 'Why we built this HolmesGPT: Letting the LLM decide what to investigate Making
  it work with Robusta Runbooks changed everything The model journey What actually
  mattered Posted on April 21, 2026 by Grace Park and Ihyeok Song, DevOps Engineer,
  STCLab SRE Team CNCF projects highlighted in this post What a two-person SRE team
  learned building an AI investigation pipeline. Spoiler: the runbooks mattered more
  than the model.'
summary: 'Why we built this HolmesGPT: Letting the LLM decide what to investigate
  Making it work with Robusta Runbooks changed everything The model journey What actually
  mattered Posted on April 21, 2026 by Grace Park and Ihyeok Song, DevOps Engineer,
  STCLab SRE Team CNCF projects highlighted in this post What a two-person SRE team
  learned building an AI investigation pipeline. Spoiler: the runbooks mattered more
  than the model. At STCLab, our SRE team supports multiple Amazon EKS clusters running
  high-traffic production workloads. We’ve got the full observability stack in place:
  OpenTelemetry feeding into Mimir, Loki, and Tempo. Robusta OSS enriches Prometheus
  alerts with error logs, Grafana links, and team mentions before dropping them into
  Slack. So the data was never the problem. The problem was what happened next. Every
  alert meant the same drill: check the pod, query Prometheus, dig through Loki, pull
  traces, try to correlate. Fifteen to twenty minutes, every single time. We wanted
  that first pass to happen automatically and show up in the same Slack thread. Alerts
  Pipeline We went with HolmesGPT (CNCF Sandbox) because of how it works: the ReAct
  pattern. The LLM reads an alert, picks a tool, reads the result, then decides what
  to check next.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/04/21/auto-diagnosing-kubernetes-alerts-with-holmesgpt-and-cncf-tools/
