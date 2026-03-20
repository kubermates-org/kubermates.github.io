---
title: 'Meet the New Standard for High-Performance, Low-Cost Inference: NVIDIA Dynamo
  1.0 is now available to DigitalOcean Customers'
date: '2026-03-19T22:13:37.480000+00:00'
tags:
- kubernetes
source: Digital Ocean
external_url: https://www.digitalocean.com/blog/nvidia-dynamo-1-now-available
post_kind: link
draft: false
tldr: 'Meet the New Standard for High-Performance, Low-Cost Inference: NVIDIA Dynamo
  1.0 is now available to DigitalOcean Customers What is NVIDIA Dynamo 1.0? How DigitalOcean
  optimizes inference workloads with Dynamo to improve throughput and latency The
  future of inference optimization with NVIDIA and DigitalOcean About the author Connect
  with our sales team Related Articles DigitalOcean at NVIDIA GTC 2026: Building the
  AI Factory for the Agentic Era Deploy Smarter with AI: Introducing App Platform
  Skills on DigitalOcean Native. NET Buildpack Support is Now Available on App Platform
  By Waverly Swinton Published: March 19, 2026 3 min read NVIDIA Dynamo 1.0 , which
  was released on Monday at NVIDIA GTC, is now available to DigitalOcean customers
  to help drive performance enhancements and cost efficiency.'
summary: 'Meet the New Standard for High-Performance, Low-Cost Inference: NVIDIA Dynamo
  1.0 is now available to DigitalOcean Customers What is NVIDIA Dynamo 1.0? How DigitalOcean
  optimizes inference workloads with Dynamo to improve throughput and latency The
  future of inference optimization with NVIDIA and DigitalOcean About the author Connect
  with our sales team Related Articles DigitalOcean at NVIDIA GTC 2026: Building the
  AI Factory for the Agentic Era Deploy Smarter with AI: Introducing App Platform
  Skills on DigitalOcean Native. NET Buildpack Support is Now Available on App Platform
  By Waverly Swinton Published: March 19, 2026 3 min read NVIDIA Dynamo 1.0 , which
  was released on Monday at NVIDIA GTC, is now available to DigitalOcean customers
  to help drive performance enhancements and cost efficiency. NVIDIA Dynamo 1.0 offers
  a 7x inference performance increase on NVIDIA GB200 NVL systems, and by pairing
  it with DigitalOcean’s Agentic Inference Cloud, customers can achieve higher performance
  at lower costs while benefiting from seamless deployment. Working together, DigitalOcean’s
  optimizations with NVIDIA have already achieved a 67% cost savings for customers
  like Workato, and this new generation of Dynamo can unlock even greater gains for
  businesses who run production-grade agentic workflows. DigitalOcean customers can
  get access to NVIDIA Dynamo 1.0 as a container image that can be run on a Droplet
  or can deploy directly on DigitalOcean Kubernetes with an inference runtime (vLLM,
  SGlang, TensorRT). NVIDIA Dynamo is a cutting-edge, high-performance inference service
  framework specifically designed to accelerate and optimize large-scale generative
  AI and inference models. Dynamo is an orchestration layer that sits above engines
  like vLLM, SGLang, and NVIDIA TensorRT-LLM. Think of it as the distributed traffic
  controller for your GPU fleet, seamlessly orchestrating GPU and memory resources
  across a cluster and reducing bottleneck by intelligently routing requests Key technical
  breakthroughs offered by Dynamo 1.0 include: 7x Performance Boost: When paired with
  NVIDIA Blackwell Ultra GPUs, Dynamo can increase inference performance by up to
  7x, significantly lowering your cost per token. 7x Performance Boost: When paired
  with NVIDIA Blackwell Ultra GPUs, Dynamo can increase inference performance by up
  to 7x, significantly lowering your cost per token. KV-Aware Routing: Instead of
  simple round-robin load balancing, Dynamo routes requests to the specific GPUs that
  already have the relevant “memory” from previous turns of a conversation. Disaggregated
  Serving: Dynamo splits the “prefill” (reading the prompt) and “decode” (generating
  the answer) phases across different GPUs to maximize utilization and reduce latency.
  Memory Offloading: The KV Block Manager (KVBM) moves data between high-speed GPU
  memory and lower-cost storage tiers, allowing you to handle massive context windows
  without hitting memory limits.'
---
Open the original post ↗ https://www.digitalocean.com/blog/nvidia-dynamo-1-now-available
