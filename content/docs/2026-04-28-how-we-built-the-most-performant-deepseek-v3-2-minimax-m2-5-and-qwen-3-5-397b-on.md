---
title: How we built the most performant DeepSeek V3.2, MiniMax-M2.5 and Qwen 3.5 397B
  on DigitalOcean Serverless Inference
date: '2026-04-28T09:00:00.024000+00:00'
tags:
- kubernetes
source: Digital Ocean
external_url: https://www.digitalocean.com/blog/how-we-built-fastest-deepseek-minimax-qwen-on-blackwell-ultra
post_kind: link
draft: false
tldr: How we built the most performant DeepSeek V3. 2, MiniMax-M2.
summary: 'How we built the most performant DeepSeek V3. 2, MiniMax-M2. 5 and Qwen
  3.5 397B on DigitalOcean Serverless Inference Why fast inference matters Leading
  the Artificial Analysis benchmarks on speed The engineering behind the numbers Hardware:
  The Power of NVIDIA Blackwell Ultra Model Quantization: Efficiency of NVFP4 Inference
  Engine: Performance optimizations of vLLM Real world performance The path forward:
  Scaling intelligence About the author(s) Start building today Related Articles How
  We Built DigitalOcean Inference Router Your Model Doesn''t Matter. Your Infrastructure
  Does. DigitalOcean Dedicated Inference: A Technical Deep Dive By Debarshi Raha and
  Bhaskar Dutt Updated: April 29, 2026 6 min read Today at Deploy, we are announcing
  the general availability of DeepSeek V3. 2, MiniMax-M2. 5, and Qwen 3.5 397B on
  DigitalOcean Serverless Inference. On DeepSeek V3. 2 and Qwen 3.5 397B, we deliver
  #1 output speed across all providers Artificial Analysis tested. On DeepSeek V3.
  2 specifically, that translates to 230 output tokens per second and sub-1-second
  Time-to-First-Token (TTFT) for 10,000 input tokens. This post covers how we got
  there: the GPU-level work, the serving stack tuning, and the specific technical
  tradeoffs we made along the way.'
---
Open the original post ↗ https://www.digitalocean.com/blog/how-we-built-fastest-deepseek-minimax-qwen-on-blackwell-ultra
