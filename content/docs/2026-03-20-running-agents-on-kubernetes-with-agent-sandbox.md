---
title: Running Agents on Kubernetes with Agent Sandbox
date: '2026-03-20T10:00:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox/
post_kind: link
draft: false
tldr: 'Running Agents on Kubernetes with Agent Sandbox The Kubernetes advantage (and
  the abstraction gap) Introducing Kubernetes Agent Sandbox Scaling agents with extensions
  Quick start The future of agents is cloud native The landscape of artificial intelligence
  is undergoing a massive architectural shift. In the early days of generative AI,
  interacting with a model was often treated as a transient, stateless function call:
  a request that spun up, executed for perhaps 50 milliseconds, and terminated.'
summary: 'Running Agents on Kubernetes with Agent Sandbox The Kubernetes advantage
  (and the abstraction gap) Introducing Kubernetes Agent Sandbox Scaling agents with
  extensions Quick start The future of agents is cloud native The landscape of artificial
  intelligence is undergoing a massive architectural shift. In the early days of generative
  AI, interacting with a model was often treated as a transient, stateless function
  call: a request that spun up, executed for perhaps 50 milliseconds, and terminated.
  Today, the world is witnessing AI v2 eating AI v1. The ecosystem is moving from
  short-lived, isolated tasks to deploying multiple, coordinated AI agents that run
  constantly. These autonomous agents need to maintain context, use external tools,
  write and execute code, and communicate with one another over extended periods.
  As platform engineering teams look for the right infrastructure to host these new
  AI workloads, one platform stands out as the natural choice: Kubernetes. However,
  mapping these unique agentic workloads to traditional Kubernetes primitives requires
  a new abstraction. This is where the new Agent Sandbox project (currently in development
  under SIG Apps) comes into play. Kubernetes is the de facto standard for orchestrating
  cloud-native applications precisely because it solves the challenges of extensibility,
  robust networking, and ecosystem maturity. However, as AI evolves from short-lived
  inference requests to long-running, autonomous agents, we are seeing the emergence
  of a new operational pattern. AI agents, by contrast, are typically isolated, stateful,
  singleton workloads. They act as a digital workspace or execution environment for
  an LLM.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox/
