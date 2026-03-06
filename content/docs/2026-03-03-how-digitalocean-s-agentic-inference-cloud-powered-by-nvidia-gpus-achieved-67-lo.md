---
title: How DigitalOcean’s Agentic Inference Cloud powered by NVIDIA GPUs Achieved
  67% Lower Inference Costs for Workato
date: '2026-03-03T04:55:00.051000+00:00'
tags:
- kubernetes
source: Digital Ocean
external_url: https://www.digitalocean.com/blog/workato-nvidia-technical-deep-dive-agentic-inference-cloud
post_kind: link
draft: false
tldr: 'How DigitalOcean’s Agentic Inference Cloud powered by NVIDIA GPUs Achieved
  67% Lower Inference Costs for Workato How LLMs Process Requests and Why It Gets
  Expensive at Scale How KV-Aware Routing Addresses the Problem NVIDIA Dynamo with
  DOKS: The Orchestration Brain for KV-Aware Routing Inference Stack Architecture
  The Two Configurations Tested Configuration 1: No KV-Aware Routing Configuration
  2: KV-Aware Routing Tuning TTFT: Prefill Cost & KV Reuse TPOT / ITL: Decode Load
  Balancing QPS & Token Throughput: GPU Utilization Conclusion About the author(s)
  Related Articles DigitalOcean Gradient™ AI GPU Droplets Optimized for Inference:
  Increasing Throughput at Lower the Cost LLM Inference Benchmarking - Measure What
  Matters Technical Deep Dive: How we Created a Security-hardened 1-Click Deploy OpenClaw
  By Rithish Ramesh , Karnik Modi , Piyush Srivastava , and Tim Kim Updated: March
  4, 2026 11 min read Workato’s AI Research Lab is focused on helping customers extend
  their production automation with agentic AI capabilities, systems that can reason,
  act, and orchestrate work across the business. At Workato’s scale, processing 1
  trillion automated workloads, LLM inference efficiency is a hard requirement: every
  millisecond of latency and every wasted GPU cycle directly impacts cost, throughput,
  and reliability.'
summary: 'How DigitalOcean’s Agentic Inference Cloud powered by NVIDIA GPUs Achieved
  67% Lower Inference Costs for Workato How LLMs Process Requests and Why It Gets
  Expensive at Scale How KV-Aware Routing Addresses the Problem NVIDIA Dynamo with
  DOKS: The Orchestration Brain for KV-Aware Routing Inference Stack Architecture
  The Two Configurations Tested Configuration 1: No KV-Aware Routing Configuration
  2: KV-Aware Routing Tuning TTFT: Prefill Cost & KV Reuse TPOT / ITL: Decode Load
  Balancing QPS & Token Throughput: GPU Utilization Conclusion About the author(s)
  Related Articles DigitalOcean Gradient™ AI GPU Droplets Optimized for Inference:
  Increasing Throughput at Lower the Cost LLM Inference Benchmarking - Measure What
  Matters Technical Deep Dive: How we Created a Security-hardened 1-Click Deploy OpenClaw
  By Rithish Ramesh , Karnik Modi , Piyush Srivastava , and Tim Kim Updated: March
  4, 2026 11 min read Workato’s AI Research Lab is focused on helping customers extend
  their production automation with agentic AI capabilities, systems that can reason,
  act, and orchestrate work across the business. At Workato’s scale, processing 1
  trillion automated workloads, LLM inference efficiency is a hard requirement: every
  millisecond of latency and every wasted GPU cycle directly impacts cost, throughput,
  and reliability. To make agentic workloads production-ready, the team needed an
  inference stack built for production scale – delivering predictable performance
  and unit economics at scale, not just raw compute. DigitalOcean partnered with Workato’s
  AI Research Lab team to design and tune this deployment on its Agentic Inference
  Cloud, using NVIDIA Dynamo with vLLM on DigitalOcean Kubernetes Service (DOKS).
  To support 100K-token context lengths without degrading performance, NVIDIA H200
  GPUs were selected for their 141GB HBM3e memory capacity. The memory footprint of
  the workload was around 125 GB (comprising the model weights, key value cache, and
  activation buffer), so a single NVIDIA H200 GPU is able to fit the whole footprint.
  However, the team used 8-way tensor parallelism per node to maximize sustained throughput
  and latency stability under a concurrent load. DigitalOcean tested across two different
  configurations for Workato, and afterwards, the results for NVIDIA Dynamo + vLLM
  on DOKS showed: Best in class queries-per-second across all tested configurations
  67% higher throughput per GPU with 79% lower end-to-end latency and 77% time-to-first-token
  compared to different configurations on identical hardware 33% lower hardware cost
  using a NVIDIA H200 GPU vs. a NVIDIA A100 GPU for equivalent performance 67% lower
  model cost while using half the GPUs The key here was to introduce key/value (KV)-aware
  routing in order to reduce redundancies and capture maximum value across performance
  and cost for the inference stack. Before getting into the architecture decisions,
  it’s worth understanding the mechanics that drive inference cost and why this is
  a complex problem that Workato needed to solve. Every LLM inference request goes
  through two phases: Prefill is where the model processes the entire input prompt
  and builds up internal memory, called key/value (KV) states, for every token it
  has read. This phase is compute-heavy and scales quadratically (O(n2)) with input
  sequence length.'
---
Open the original post ↗ https://www.digitalocean.com/blog/workato-nvidia-technical-deep-dive-agentic-inference-cloud
