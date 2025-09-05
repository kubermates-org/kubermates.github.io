---
title: How to run AI model inference with GPUs on Amazon EKS Auto Mode
date: '2025-09-04T16:12:23+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/how-to-run-ai-model-inference-with-gpus-on-amazon-eks-auto-mode/
post_kind: link
draft: false
tldr: How to run AI model inference with GPUs on Amazon EKS Auto Mode Key features
  that make EKS Auto Mode ideal for AI/ML workloads Walkthrough Prerequisites Set
  up environment variables Set up EKS Auto Mode cluster and run a model Reducing model
  cold start time in AI inference workloads Conclusion About the authors AI model
  inference using GPUs is becoming a core part of modern applications, powering real-time
  recommendations, intelligent assistants, content generation, and other latency-sensitive
  AI features. Kubernetes has become the orchestrator of choice for running inference
  workloads, and organizations want to use its capabilities while still maintaining
  a strong focus on rapid innovation and time-to-market.
summary: 'How to run AI model inference with GPUs on Amazon EKS Auto Mode Key features
  that make EKS Auto Mode ideal for AI/ML workloads Walkthrough Prerequisites Set
  up environment variables Set up EKS Auto Mode cluster and run a model Reducing model
  cold start time in AI inference workloads Conclusion About the authors AI model
  inference using GPUs is becoming a core part of modern applications, powering real-time
  recommendations, intelligent assistants, content generation, and other latency-sensitive
  AI features. Kubernetes has become the orchestrator of choice for running inference
  workloads, and organizations want to use its capabilities while still maintaining
  a strong focus on rapid innovation and time-to-market. But here’s the challenge:
  while teams see the value of Kubernetes for its dynamic scaling and efficient resource
  management, they often get slowed down by the need to learn Kubernetes concepts,
  manage cluster configurations, and handle security updates. This shifts focus away
  from what matters most: deploying and optimizing AI models. That is where Amazon
  Elastic Kubernetes Service (Amazon EKS) Auto Mode comes in. EKS Auto Mode Automates
  node creation, manages core capabilities , and handles upgrades and security patching.
  In turn, this enables to run your inference workloads without the operational overhead.
  In this post, we show you how to swiftly deploy inference workloads on EKS Auto
  Mode. We also demonstrate key features that streamline GPU management, show best
  practices for model deployment, and walk through a practical example by deploying
  open weight models from OpenAI using vLLM. Whether you’re building a new AI/machine
  learning (ML) platform or optimizing existing workflows, these patterns help you
  accelerate development while maintaining operational efficiency. In this section,
  we take a closer look at the GPU-specific features that come pre-configured and
  ready to use with an EKS Auto Mode cluster. These capabilities are also available
  in self-managed Amazon EKS environments, but they typically need manual setup and
  tuning.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/how-to-run-ai-model-inference-with-gpus-on-amazon-eks-auto-mode/
