---
title: Considerations when doing AI on Kubernetes
date: '2025-09-05T16:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/09/05/considerations-when-doing-ai-on-kubernetes/
post_kind: link
draft: false
tldr: Final Thoughts Posted on September 5, 2025 by Drishti Gupta, Senior Cloud Architect
  for Google Cloud CNCF projects highlighted in this post As more teams start weaving
  generative AI (GenAI) into their apps and workflows, Kubernetes naturally comes
  up as the go-to platform. It’s a tried-and-tested solution for managing containerized
  workloads, but AI workloads are a different beast.
summary: 'Final Thoughts Posted on September 5, 2025 by Drishti Gupta, Senior Cloud
  Architect for Google Cloud CNCF projects highlighted in this post As more teams
  start weaving generative AI (GenAI) into their apps and workflows, Kubernetes naturally
  comes up as the go-to platform. It’s a tried-and-tested solution for managing containerized
  workloads, but AI workloads are a different beast. Here’s a rundown of what you
  should think about—and which tools can help—when running AI workloads in cloud-native
  environments. GenAI Workloads Need Event-Driven Infrastructure GenAI features often
  hinge on user prompts, streaming data, or background jobs. That means you need infrastructure
  that’s reactive, scalable, and lean. Knative Serving : Great for HTTP-based GenAI
  services (like LLM APIs). It automatically scales up when requests come in, and
  scales to zero when they don’t. Perfect for saving money on GPU-bound workloads.
  KEDA : Adds event-driven autoscaling based on external sources like Kafka, RabbitMQ,
  or Prometheus. It complements Knative by widening the scope of what can trigger
  scaling. Together, they give you a nimble setup that reacts fast and keeps infra
  costs manageable. Things to consider when serving LLMs in Cloud-Native Environments
  Cloud-native tooling provides robust building blocks to tackle the considerations
  below.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/09/05/considerations-when-doing-ai-on-kubernetes/
