---
title: 'Red Hat and NVIDIA: Setting standards for high-performance AI inference'
date: '2026-04-02T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/red-hat-and-nvidia-setting-standards-high-performance-ai-inference
post_kind: link
draft: false
tldr: 'Red Hat and NVIDIA: Setting standards for high-performance AI inference Results
  at a glance Qwen3-VL-235B (multimodal vision model) GPT-OSS-120B Whisper large-V3
  (speech-to-text) Delivering greater efficiency and ROI About the author Ashish Kamra
  More like this Red Hat AI tops MLPerf Inference v6.0 with vLLM on Qwen3-VL, Whisper,
  and GPT-OSS-120B Running LLMs dynamically, in production, on limited resources,
  is hard. We think there’s room for another approach… Technically Speaking | Build
  a production-ready AI toolbox Technically Speaking | Platform engineering for AI
  agents Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share Red Hat is proud
  to announce industry-leading results from the latest MLPerf Inference v6.0 benchmarks,
  achieved through deep engineering co-design with NVIDIA.'
summary: 'Red Hat and NVIDIA: Setting standards for high-performance AI inference
  Results at a glance Qwen3-VL-235B (multimodal vision model) GPT-OSS-120B Whisper
  large-V3 (speech-to-text) Delivering greater efficiency and ROI About the author
  Ashish Kamra More like this Red Hat AI tops MLPerf Inference v6.0 with vLLM on Qwen3-VL,
  Whisper, and GPT-OSS-120B Running LLMs dynamically, in production, on limited resources,
  is hard. We think there’s room for another approach… Technically Speaking | Build
  a production-ready AI toolbox Technically Speaking | Platform engineering for AI
  agents Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share Red Hat is proud
  to announce industry-leading results from the latest MLPerf Inference v6.0 benchmarks,
  achieved through deep engineering co-design with NVIDIA. These results demonstrate
  that when you combine Red Hat’s open-source leadership with NVIDIA’s leading AI
  infrastructure, the result is a versatile, proven platform ready for any enterprise
  inference workload—from vision and speech to complex reasoning. Our latest submissions
  focused on maximizing the potential of the NVIDIA HGX H200 and NVIDIA HGX B200 systems,
  proving that software optimization is just as critical as raw horsepower for achieving
  peak ROI. Across language, vision, and speech models, Red Hat’s stack delivered
  top-tier throughput and latency results on NVIDIA AI infrastructure. Model Category
  Model GPU Configuration Scenario Leading Results Vision Qwen3-VL-235B 8× NVIDIA
  B200 Server 67.9 samples/sec Reasoning GPT-OSS-120B 8× NVIDIA B200 Offline 93,071
  tokens/sec Speech Whisper-Large-v3 8× NVIDIA H200 Offline 36,396 tokens/sec The
  Qwen3-VL-235B model, a massive 235-billion-parameter multimodal vision-language
  model, represents a significant challenge for inference engines due to highly variable
  image resolutions. Using NVIDIA Blackwell GPUs running on Red Hat Enterprise Linux
  (RHEL) with vLLM and NVIDIA Dynamo , we achieved the highest offline throughput
  in our class. Notably, our Blackwell submission exceeded the next top performer
  by 50% in the Server scenario. Key engineering wins: Triton-based improvements:
  Optimizations to the vision encoder yielded 30-40% faster ViT processing. FlashInfer
  Mixture-of-Experts (MoE) kernels: These specialized kernels handled the MoE architecture
  with extreme efficiency. FP8 Multimodal Attention: Leveraging NVIDIA’s advanced
  data formats to lower cost per token without sacrificing accuracy. Our submission
  for GPT-OSS-120B marks the first time a model of this scale has been benchmarked
  on Kubernetes infrastructure for MLPerf.'
---
Open the original post ↗ https://www.redhat.com/en/blog/red-hat-and-nvidia-setting-standards-high-performance-ai-inference
