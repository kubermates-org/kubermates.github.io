---
title: Red Hat AI tops MLPerf Inference v6.0 with vLLM on Qwen3-VL, Whisper, and GPT-OSS-120B
date: '2026-04-01T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/red-hat-ai-tops-mlperf-inference-v60-vllm-qwen3-vl-whisper-and-gpt-oss-120b
post_kind: link
draft: false
tldr: 'Red Hat AI tops MLPerf Inference v6.0 with vLLM on Qwen3-VL, Whisper, and GPT-OSS-120B
  Our results Qwen3-VL-235B (multimodal vision model) GPT-OSS-120B (reasoning model)
  Whisper Large-V3 (speech-to-text) Llama-2-70B on AMD MI350X Key takeaways What comes
  next The adaptable enterprise: Why AI readiness is disruption readiness About the
  authors Ashish Kamra Diane Feddema Michael Goin Michey Mehta Naveen Miriyalu Nikhil
  Palaskar Saša Zelenović Aanya Sharma Alberto Perdomo Harika Pothina Samuel Monson
  Sayali Bhavsar More like this Red Hat and NVIDIA: Setting standards for high-performance
  AI inference Running LLMs dynamically, in production, on limited resources, is hard.
  We think there’s room for another approach… Technically Speaking | Build a production-ready
  AI toolbox Technically Speaking | Platform engineering for AI agents Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share Red Hat is proud
  to announce our strong results from the latest industry-standard MLPerf Inference
  v6.0 benchmark.'
summary: 'Red Hat AI tops MLPerf Inference v6.0 with vLLM on Qwen3-VL, Whisper, and
  GPT-OSS-120B Our results Qwen3-VL-235B (multimodal vision model) GPT-OSS-120B (reasoning
  model) Whisper Large-V3 (speech-to-text) Llama-2-70B on AMD MI350X Key takeaways
  What comes next The adaptable enterprise: Why AI readiness is disruption readiness
  About the authors Ashish Kamra Diane Feddema Michael Goin Michey Mehta Naveen Miriyalu
  Nikhil Palaskar Saša Zelenović Aanya Sharma Alberto Perdomo Harika Pothina Samuel
  Monson Sayali Bhavsar More like this Red Hat and NVIDIA: Setting standards for high-performance
  AI inference Running LLMs dynamically, in production, on limited resources, is hard.
  We think there’s room for another approach… Technically Speaking | Build a production-ready
  AI toolbox Technically Speaking | Platform engineering for AI agents Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share Red Hat is proud
  to announce our strong results from the latest industry-standard MLPerf Inference
  v6.0 benchmark. Our submission includes four AI workloads (Whisper-Large-v3, GPT-OSS-120B,
  Qwen3-VL-235B-A22B, and Llama-2-70b) on NVIDIA (H200, B200, L40S) and AMD (MI350X)
  GPUs, running on Red Hat Enterprise Linux (RHEL) and Red Hat OpenShift AI with our
  open source inference stack: vLLM , and llm-d. We achieved top scores across several
  configurations, including the highest offline throughput on B200 for GPT-OSS-120B,
  the leading H200 result on Whisper, and the top B200 submission on Qwen3-VL, which
  exceeded the top B300 performer by 50% in the Server scenario. Enterprises use MLPerf
  to evaluate AI workload performance by comparing hardware and software stacks in
  a standardized environment. These results illustrate Red Hat AI’s ability to match
  or outperform other inference engines on the same hardware, scale distributed inference
  on OpenShift AI, and run across multiple GPU vendors without changing the software
  layer. Across language, vision, and speech models, Red Hat’s stack delivered top-tier
  throughput and latency results on NVIDIA architecture. Red Hat MLPerf Inference
  Results v6.0 Model category Model name Hardware Offline (tok/sec) Server (tok/sec)
  Software stack Notes & comparisons Vision Qwen3-VL-235B-A22B 8x B200 79.04 (samples/sec)
  67.86 (samples/sec) RHEL, vLLM Top in the leaderboard compared to all results 8x
  H200 18.02 (samples/sec) 11.05 (samples/sec) RHEL, vLLM Unique and non-comparable
  Reasoning gpt-oss-120b 8x B200 93,070.70 71,588.13 OpenShift, llm-d, vLLM Offline
  B200 8% better than closest competitor 8x H200 28,680.00 24,103.19 OpenShift, llm-d,
  vLLM Unique and non-comparable gpt-oss-120b 8x MI350X (w/Supermicro) 64,293.30 58,373.27
  vLLM, RHEL Open division submission. Improved perf by 20% post-submission Audio
  Whisper 8x H200 36,395.70 N/A RHEL, vLLM 13% better than closest competitor 2x L40S
  3,646.91 N/A RHEL, vLLM Unique and non-comparable Dense llama-2-70b 8x MI350X (w/SuperMicro)
  91,933.10 89,019.65 vLLM, RHEL Competitive with other MI350X submissions Qwen3-VL-235B-A22B-Instruct
  is a 235-billion-parameter MoE vision-language model with 22 billion active parameters.
  The MLPerf benchmark uses a Shopify product catalog dataset with 48,289 multimodal
  samples (real e-commerce product images paired with text) where the model must classify
  products into structured JSON output. Image resolution varies by up to 20x, which
  stresses the vision encoder and creates highly uneven request sizes that can disrupt
  scheduling efficiency. We submitted both H200 and B200 using RHEL and vLLM with
  CentML optimizations.'
---
Open the original post ↗ https://www.redhat.com/en/blog/red-hat-ai-tops-mlperf-inference-v60-vllm-qwen3-vl-whisper-and-gpt-oss-120b
