---
title: 'From tokens to caches: How llm-d improves LLM observability in Red Hat OpenShift
  AI 3.0'
date: '2025-10-22T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/tokens-caches-how-llm-d-improves-llm-observability-red-hat-openshift-ai-3.0
post_kind: link
draft: false
tldr: 'From tokens to caches: How llm-d improves LLM observability in Red Hat OpenShift
  AI 3.0 New service level objectives (SLO) in the age of LLMs The challenge of managing
  these new SLOs What is llm-d? How llm-d Helps solve the observability gap Example
  PromQL queries Example dashboard Conclusion The adaptable enterprise: Why AI readiness
  is disruption readiness About the authors Christopher Nuland Sally O''Malley More
  like this Blog post Blog post Original podcast Original podcast Keep exploring Browse
  by channel Automation Artificial intelligence Open hybrid cloud Security Edge computing
  Infrastructure Applications Virtualization Share As enterprises scale large language
  models (LLMs) into production, site reliability engineers (SREs) and platform operators
  face a new set of challenges. Traditional application metrics—CPU usage, request
  throughput, memory consumption—are no longer enough.'
summary: 'From tokens to caches: How llm-d improves LLM observability in Red Hat OpenShift
  AI 3.0 New service level objectives (SLO) in the age of LLMs The challenge of managing
  these new SLOs What is llm-d? How llm-d Helps solve the observability gap Example
  PromQL queries Example dashboard Conclusion The adaptable enterprise: Why AI readiness
  is disruption readiness About the authors Christopher Nuland Sally O''Malley More
  like this Blog post Blog post Original podcast Original podcast Keep exploring Browse
  by channel Automation Artificial intelligence Open hybrid cloud Security Edge computing
  Infrastructure Applications Virtualization Share As enterprises scale large language
  models (LLMs) into production, site reliability engineers (SREs) and platform operators
  face a new set of challenges. Traditional application metrics—CPU usage, request
  throughput, memory consumption—are no longer enough. With LLMs, reliability and
  efficacy are defined by entirely new dynamics—token-level performance, cache efficiency,
  and inference pipeline latency. This article explores how llm-d , an open source
  project co-developed with the leading AI vendors (Red Hat, Google, IBM, etc. ) and
  integrated into Red Hat OpenShift AI 3.0, redefines observability for LLM workloads.
  Users expect responsive applications, including those enhanced with AI, and enterprises
  require consistent performance to turn a pilot project into a profitable production
  application at scale. While SLOs in traditional microservice architectures are usually
  framed around request latency and error rate , the user experience for LLMs depends
  on more nuanced measures, including: Time to first token (TTFT): Measures the delay
  before the initial token of a response is streamed to the user. A lower TTFT is
  needed to provide a responsive and immediate user experience, especially in interactive
  applications. Time per output token (TPOT): Indicates the speed at which tokens
  are generated after the process begins. A consistent and low TPOT provides a smooth
  and efficient streaming of the complete response to the user. Cache hit rate: Represents
  the proportion of requests that can use previously computed context stored in GPU
  memory. A high cache hit rate significantly reduces computational overhead and improves
  overall system throughput by avoiding redundant processing.'
---
Open the original post ↗ https://www.redhat.com/en/blog/tokens-caches-how-llm-d-improves-llm-observability-red-hat-openshift-ai-3.0
