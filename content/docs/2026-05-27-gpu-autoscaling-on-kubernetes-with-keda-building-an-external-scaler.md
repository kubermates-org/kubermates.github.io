---
title: GPU autoscaling on Kubernetes with KEDA: Building an external scaler
date: '2026-05-27T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/05/27/gpu-autoscaling-on-kubernetes-with-keda-building-an-external-scaler/
post_kind: link
draft: false
tldr: 'The problem The architecture What you can scale on Pre-built profiles Quick
  start Install with Helm Create a ScaledObject Testing without GPUs What’s next Posted
  on May 27, 2026 by Pavan Madduri (Senior Cloud Platform Engineer @ Grainger | CNCF
  Golden Kubestronaut) CNCF projects highlighted in this post If you run GPU workloads
  on Kubernetes — vLLM, Triton, training jobs, or the newer agentic inference stacks
  — you’ve probably hit a familiar problem: the default autoscaling path still reasons
  about CPU and memory, while the GPU that is actually doing the work stays hidden.
  That mismatch wastes expensive accelerator capacity, pushes up inference latency,
  and creates unnecessary power draw at exactly the point where enterprises are trying
  to scale LLMs and Agentic Ops responsibly.'
summary: 'The problem The architecture What you can scale on Pre-built profiles Quick
  start Install with Helm Create a ScaledObject Testing without GPUs What’s next Posted
  on May 27, 2026 by Pavan Madduri (Senior Cloud Platform Engineer @ Grainger | CNCF
  Golden Kubestronaut) CNCF projects highlighted in this post If you run GPU workloads
  on Kubernetes — vLLM, Triton, training jobs, or the newer agentic inference stacks
  — you’ve probably hit a familiar problem: the default autoscaling path still reasons
  about CPU and memory, while the GPU that is actually doing the work stays hidden.
  That mismatch wastes expensive accelerator capacity, pushes up inference latency,
  and creates unnecessary power draw at exactly the point where enterprises are trying
  to scale LLMs and Agentic Ops responsibly. I wanted KEDA to scale on the signals
  that matter for GPU workloads: utilization, memory, temperature, and power draw.
  In practice, this is not only a cost problem. It is also a GreenOps problem, because
  wasted GPU cycles translate directly into wasted energy and higher Scope 3 emissions.
  Turns out, that is harder than it sounds. KEDA is built with CGO_ENABLED=0. The
  NVIDIA Management Library (NVML) – the standard way to read GPU metrics – requires
  CGO. So you can’t just add a GPU scaler to KEDA core the way you’d add a Prometheus
  or Kafka scaler. There’s a second problem too. KEDA’s operator runs as a single
  deployment. NVML calls are local — they read metrics from the GPU on the same node.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/05/27/gpu-autoscaling-on-kubernetes-with-keda-building-an-external-scaler/
