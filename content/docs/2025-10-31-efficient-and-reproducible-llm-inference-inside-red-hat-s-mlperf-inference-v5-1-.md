---
title: 'Efficient and reproducible LLM inference: Inside Red Hat’s MLPerf Inference
  v5.1 submissions'
date: '2025-10-31T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/efficient-and-reproducible-llm-inference-red-hat-mlperf-inference-v51-results
post_kind: link
draft: false
tldr: 'Efficient and reproducible LLM inference: Inside Red Hat’s MLPerf Inference
  v5.1 submissions Executive summary Introduction MLPerf test scenarios and vLLM harness
  MLPerf test scenarios vLLM harness Benchmarking setup and results Model and dataset
  Performance tuning: Autotune Results Future outlook and concluding remarks The adaptable
  enterprise: Why AI readiness is disruption readiness About the authors Naveen Miriyalu
  Diane Feddema Michey Mehta Keith Valin Michael Goin Ashish Kamra Jean Hsiao More
  like this Blog post Blog post Original podcast Original podcast Keep exploring Browse
  by channel Automation Artificial intelligence Open hybrid cloud Security Edge computing
  Infrastructure Applications Virtualization Share As generative AI (gen AI) workloads
  become central to enterprise applications, benchmarking their inference performance
  has never been more critical for understanding the limits of their capabilities.
  In MLPerf Inference v5.1, Meta’s Llama 3.1-8B was featured for the first time.'
summary: 'Efficient and reproducible LLM inference: Inside Red Hat’s MLPerf Inference
  v5.1 submissions Executive summary Introduction MLPerf test scenarios and vLLM harness
  MLPerf test scenarios vLLM harness Benchmarking setup and results Model and dataset
  Performance tuning: Autotune Results Future outlook and concluding remarks The adaptable
  enterprise: Why AI readiness is disruption readiness About the authors Naveen Miriyalu
  Diane Feddema Michey Mehta Keith Valin Michael Goin Ashish Kamra Jean Hsiao More
  like this Blog post Blog post Original podcast Original podcast Keep exploring Browse
  by channel Automation Artificial intelligence Open hybrid cloud Security Edge computing
  Infrastructure Applications Virtualization Share As generative AI (gen AI) workloads
  become central to enterprise applications, benchmarking their inference performance
  has never been more critical for understanding the limits of their capabilities.
  In MLPerf Inference v5.1, Meta’s Llama 3.1-8B was featured for the first time. This
  post presents Red Hat’s submissions using the FP8 quantized llama 3.1-8b model with
  vLLM 0.10.0 on Red Hat Enterprise Linux (RHEL) 9.6, outlining our approach to achieving
  reproducible, high-throughput LLM inference. Our configuration delivered competitive
  single-GPU performance, achieving 5777 tokens/sec (Offline) and 5103 tokens/sec
  (Server) on a single H100 GPU, and 1642 tokens/sec (Offline) and 1207 tokens/sec
  (Server) on a single L40S GPU. In this article, you’ll hear about MLPerf test scenarios,
  benchmark setup, tuning methodology, and results, and learn how these efforts align
  with Red Hat’s broader strategy to deliver open, scalable, and production-grade
  AI inference platforms. The accelerated pace of innovation in large language models
  (LLMs) and their associated ecosystems has increased widespread adoption across
  virtually every industry. This momentum is fueled by continual advancements in hardware
  accelerators, including modern GPUs and custom AI Application-Specific Integrated
  Circuits (ASICs) that unlock an unprecedented level of parallelism and computational
  throughput. Complementing these advancements, software-layer innovations are transforming
  how efficiently these hardware capabilities are harnessed. At the heart of this
  software evolution are inference engines, which serve as the execution backbone
  for deploying foundation models. These engines optimize how model weights, activation
  patterns, and memory flows are mapped to underlying hardware, achieving substantial
  gains in latency, throughput, and energy efficiency. Modern inference engines dynamically
  adapt to heterogeneous environments across cloud, edge, and on-premise deployments.
  They also integrate advanced scheduling, quantization, caching, and compilation
  techniques to accelerate end-to-end inference pipelines.'
---
Open the original post ↗ https://www.redhat.com/en/blog/efficient-and-reproducible-llm-inference-red-hat-mlperf-inference-v51-results
