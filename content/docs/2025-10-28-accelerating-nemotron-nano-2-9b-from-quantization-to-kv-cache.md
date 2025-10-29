---
title: 'Accelerating  Nemotron Nano 2 9B: From Quantization to KV-Cache'
date: '2025-10-28T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/accelerating-nemotron-nano-2-9b-quantization-kv-cache
post_kind: link
draft: false
tldr: 'Accelerating Nemotron Nano 2 9B: From Quantization to KV-Cache A more efficient
  Nemotron for all Why INT4 (W4A16)? Unlocking Long-Context performance: vLLM and
  the hybrid Mamba-2-Transformer architecture Performance Accuracy Compressed Nemotron
  in action Deploy on vLLM Deploy on Red Hat AI Deploy on Red Hat AI Inference Server
  Deploy on Red Hat OpenShift AI Validated for the enterprise: Deploying with confidence
  Open and scalable AI The adaptable enterprise: Why AI readiness is disruption readiness
  About the authors Rob Greenberg Eldar Kurtić Mark Vaykhansky Shani Alisar Alexandre
  Marques Tyler Michael Smith More like this Blog post Blog post Original podcast
  Original podcast Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share Red Hat is announcing the latest addition to our portfolio of validated and
  optimized models: a compressed version of NVIDIA Nemotron-Nano-9B-v2. By leveraging
  the open source LLM Compressor library, we have created a new INT4 (W4A16) variant
  that unlocks significant performance gains on NVIDIA AI infrastructure with negligible
  impact on the model''s reasoning capabilities.'
summary: 'Accelerating Nemotron Nano 2 9B: From Quantization to KV-Cache A more efficient
  Nemotron for all Why INT4 (W4A16)? Unlocking Long-Context performance: vLLM and
  the hybrid Mamba-2-Transformer architecture Performance Accuracy Compressed Nemotron
  in action Deploy on vLLM Deploy on Red Hat AI Deploy on Red Hat AI Inference Server
  Deploy on Red Hat OpenShift AI Validated for the enterprise: Deploying with confidence
  Open and scalable AI The adaptable enterprise: Why AI readiness is disruption readiness
  About the authors Rob Greenberg Eldar Kurtić Mark Vaykhansky Shani Alisar Alexandre
  Marques Tyler Michael Smith More like this Blog post Blog post Original podcast
  Original podcast Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share Red Hat is announcing the latest addition to our portfolio of validated and
  optimized models: a compressed version of NVIDIA Nemotron-Nano-9B-v2. By leveraging
  the open source LLM Compressor library, we have created a new INT4 (W4A16) variant
  that unlocks significant performance gains on NVIDIA AI infrastructure with negligible
  impact on the model''s reasoning capabilities. This release continues our commitment
  to providing enterprises with open, flexible, and efficient AI solutions that are
  ready for production deployment across the hybrid cloud. Key benefits include: Smaller
  and faster Nemotron : A new, compressed Nemotron-Nano-9B-v2 model in an INT4 (W4A16)
  format, created using LLM Compressor, offers a smaller version which performs best
  at latency sensitive use cases. Optimized for NVIDIA accelerated computing : The
  INT4 model coupled with our open-source Machete , a mixed-input GEMM kernel optimized
  for NVIDIA Hopper GPUs, is engineered to deliver substantial improvements in inference
  speed and efficiency in vLLM. Validated for the enterprise : This model has been
  rigorously tested and validated by Red Hat, providing the confidence and predictability
  needed to deploy AI workloads in enterprise environments on Red Hat AI. Open and
  extensible : The model is available in the Red Hat AI repository on Hugging Face
  , ready for deployment with vLLM and further customization using LLM Compressor.
  Hybrid model support in vLLM : With the release of the vLLM V1 engine, hybrid models,
  like Nemotron-Nano-9B-v2, have become first-class citizens through an exceptionally
  efficient implementation that delivers blazing performance. NVIDIA Nemotron-Nano-9B-v2
  stands out for its innovative hybrid Mamba-Transformer architecture, which is specifically
  designed to accelerate the long reasoning traces common in agentic AI tasks. This
  9-billion-parameter model delivers exceptional performance, generating responses
  up to six times faster than comparable dense models while supporting a 128K token
  context length and a wide range of languages. This model also has a “thinking budget”
  feature that limits the model from overthinking, allowing it to optimize the model
  for accuracy, performance, and inference cost. To make this powerful model even
  more accessible and efficient for enterprise use, we have applied state-of-the-art
  compression techniques using LLM Compressor.'
---
Open the original post ↗ https://www.redhat.com/en/blog/accelerating-nemotron-nano-2-9b-quantization-kv-cache
