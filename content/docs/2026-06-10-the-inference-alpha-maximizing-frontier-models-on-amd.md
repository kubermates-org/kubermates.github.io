---
title: 'The Inference Alpha: Maximizing Frontier Models on AMD'
date: '2026-06-10T14:27:49.137000+00:00'
tags:
- kubernetes
source: Digital Ocean
external_url: https://www.digitalocean.com/blog/maximize-frontier-models
post_kind: link
draft: false
tldr: 'The Inference Alpha: Maximizing Frontier Models on AMD The Proof is in the
  Throughput The Economic Thesis Why “Out-of-the-Box” Software Leaves Performance
  on the Table Problem Primer: Defining the Levers of High-Speed Inference MXFP4 (Microscaling
  Formats) MLA (Multi-Head Latent Attention) MoE (Mixture of Experts) Kernel Fusion
  Speculative Decoding Tensor Parallelism (TP) Reclaiming the Hardware Potential The
  Roadmap Ahead About the author(s) Start building today Related Articles The Inference
  Tax: How Prefix-Aware Routing Eliminates the Hidden Cost of LLMs at Scale DigitalOcean
  Serverless Inference: A Deep Dive How We Built DigitalOcean Inference Router By
  Balaji Varadarajan and Emilio Andere Updated: June 15, 2026 12 min read At DigitalOcean,
  we’re committed to providing high-performance infrastructure for the next generation
  of AI, which is why we’ve been focused on hosting frontier Large Language Models
  (LLMs) on frontier GPUs—including AMD GPUs. We see inference performance as an intricate
  systems-level challenge.'
summary: 'The Inference Alpha: Maximizing Frontier Models on AMD The Proof is in the
  Throughput The Economic Thesis Why “Out-of-the-Box” Software Leaves Performance
  on the Table Problem Primer: Defining the Levers of High-Speed Inference MXFP4 (Microscaling
  Formats) MLA (Multi-Head Latent Attention) MoE (Mixture of Experts) Kernel Fusion
  Speculative Decoding Tensor Parallelism (TP) Reclaiming the Hardware Potential The
  Roadmap Ahead About the author(s) Start building today Related Articles The Inference
  Tax: How Prefix-Aware Routing Eliminates the Hidden Cost of LLMs at Scale DigitalOcean
  Serverless Inference: A Deep Dive How We Built DigitalOcean Inference Router By
  Balaji Varadarajan and Emilio Andere Updated: June 15, 2026 12 min read At DigitalOcean,
  we’re committed to providing high-performance infrastructure for the next generation
  of AI, which is why we’ve been focused on hosting frontier Large Language Models
  (LLMs) on frontier GPUs—including AMD GPUs. We see inference performance as an intricate
  systems-level challenge. For frontier open-weight models, achieving peak output
  speed is not just about the raw hardware. It also depends on a complex interaction
  between model architecture, runtime execution, memory systems, scheduling, and decoding
  strategy. We believe there’s a significant “performance alpha” found in specialized
  inference engineering. Optimizing for both speed and cost-efficiency requires a
  much deeper approach than standard configuration sweeps. By taking a custom approach
  to the software stack, we can demonstrate that achieving performance parity with
  more expensive hardware is entirely possible. While the current software ecosystem
  often presents non-obvious hurdles, deep engineering allows us to deliver stronger
  inference economics on high-performance AMD infrastructure relative to conventional
  flagship deployments. To ground our “Performance Alpha” theory in reality, DO worked
  with Wafer to achieve high performance on specific frontier models on AMD GPUs through
  various optimizations. By utilizing Wafer’s Agent to identify inefficiencies and
  apply appropriate fixes, we were able to move beyond marginal gains toward order-of-magnitude
  improvements that change how these models are used in production. * Kimi 2.5 (High-Speed
  Single Stream) On a standard 10k input / 1. 5k output workload, a stock configuration
  on 8x MI350X/MI355x hardware delivered a baseline of 22.5 tok/s.'
---
Open the original post ↗ https://www.digitalocean.com/blog/maximize-frontier-models
