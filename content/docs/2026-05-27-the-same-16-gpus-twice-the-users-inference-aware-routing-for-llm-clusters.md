---
title: 'The same 16 GPUs, twice the users: Inference-aware routing for LLM clusters'
date: '2026-05-27T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/same-16-gpus-twice-users-inference-aware-routing-llm-clusters
post_kind: link
draft: false
tldr: 'The same 16 GPUs, twice the users: Inference-aware routing for LLM clusters
  The pattern that works everywhere else Where round robin reaches its limits A cache
  hit on the wrong pod is a cache miss Taking it from node to cluster Inference scheduling
  at scale: Same hardware, twice the capacity Inference scheduling (Qwen3-32B, 8x
  vLLM pods, 16x NVIDIA H100): vLLM optimizes the node, llm-d optimizes the cluster
  Experience the scale for yourself Get started with AI Inference About the author
  Naina Singh More like this Manage MCP servers on Red Hat OpenShift with the MCP
  lifecycle operator Kiali and MCP: Bringing AI-native observability to Red Hat OpenShift
  Service Mesh Technically Speaking | Build a production-ready AI toolbox Technically
  Speaking | Platform engineering for AI agents Keep exploring Browse by channel Automation
  Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share TL;DR: The same 16 GPUs, twice the users. Your
  GPU bill remains flat while capacity doubles.'
summary: 'The same 16 GPUs, twice the users: Inference-aware routing for LLM clusters
  The pattern that works everywhere else Where round robin reaches its limits A cache
  hit on the wrong pod is a cache miss Taking it from node to cluster Inference scheduling
  at scale: Same hardware, twice the capacity Inference scheduling (Qwen3-32B, 8x
  vLLM pods, 16x NVIDIA H100): vLLM optimizes the node, llm-d optimizes the cluster
  Experience the scale for yourself Get started with AI Inference About the author
  Naina Singh More like this Manage MCP servers on Red Hat OpenShift with the MCP
  lifecycle operator Kiali and MCP: Bringing AI-native observability to Red Hat OpenShift
  Service Mesh Technically Speaking | Build a production-ready AI toolbox Technically
  Speaking | Platform engineering for AI agents Keep exploring Browse by channel Automation
  Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share TL;DR: The same 16 GPUs, twice the users. Your
  GPU bill remains flat while capacity doubles. A cluster that handled 20 concurrent
  users now handles 200. These numbers are made possible by llm-d’s inference scheduler,
  built to route every request across a distributed cluster with visibility into every
  node, every queue, and every cache. Large language model (LLM) requests are slow,
  non-uniform, and expensive—the inference scheduler is built for exactly that. Every
  GPU-hour has a price, the question is how much work you are getting out of it. Kubernetes
  is how distributed services get built, deployed, and operated at scale. In a standard
  Kubernetes configuration, you define a deployment, set a replica count, and a Kubernetes
  service gives you a front door with round-robin load balancing across all your pods.
  For REST APIs, web services, and microservices, this pattern is essentially perfect.
  Requests are fast, uniform, and each one takes roughly the same sub-second time
  to complete. But the moment you start serving large generative models at scale,
  such as Llama, Mistral, or GPT-class open source models, that assumption no longer
  holds. LLM inference requests are not like normal HTTP requests, and the differences
  are what break standard load balancing: Time variability: A request can take less
  than a second or over a minute, depending on what the model is asked to do.'
---
Open the original post ↗ https://www.redhat.com/en/blog/same-16-gpus-twice-users-inference-aware-routing-llm-clusters
