---
title: Deploy VMware Private AI on HGX servers with Broadcom Ethernet Networking
date: '2025-09-10T04:14:57+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/09/09/deploy-vmware-private-ai-on-hgx-servers-with-broadcom-ethernet-networking/
post_kind: link
draft: false
tldr: What’s Covered in the White Paper? Key Highlights of the Solution Related Related
  Articles FinOps in VMware Cloud Foundation Deploy VMware Private AI on HGX servers
  with Broadcom Ethernet Networking Unlocking the Power of GenAI AI and Generative
  AI (Gen AI) require substantial infrastructure, and tasks like fine-tuning, customization,
  deployment, and querying can strain resources. Scaling up these operations becomes
  problematic without adequate infrastructure.
summary: 'What’s Covered in the White Paper? Key Highlights of the Solution Related
  Related Articles FinOps in VMware Cloud Foundation Deploy VMware Private AI on HGX
  servers with Broadcom Ethernet Networking Unlocking the Power of GenAI AI and Generative
  AI (Gen AI) require substantial infrastructure, and tasks like fine-tuning, customization,
  deployment, and querying can strain resources. Scaling up these operations becomes
  problematic without adequate infrastructure. Additionally, diverse compliance and
  legal requirements must be met across various industries and countries. Gen AI solutions
  must ensure access control, proper workload placement, and audit readiness to comply
  with these standards. To address these challenges, Broadcom introduced VMware Private
  AI to help customers run models next to their proprietary data. By combining innovations
  from both companies, Broadcom and NVIDIA aim to unlock the power of AI and unleash
  productivity with lower total cost of ownership (TCO). Our technical white paper,
  “ Deploy VMware Private AI on HGX servers with Broadcom Ethernet Networking ,” details
  the end-to-end deployment and configuration, focusing on DirectPath I/O (passthrough)
  GPUs and Thor 2 NICs with Tomahawk 5 Ethernet switch. This guide is essential for
  infrastructure architects, VCF administrators, and data scientists aiming to achieve
  optimal performance for their AI models in VCF. The white paper provides in-depth
  guidance on: Broadcom Thor2 NICs and NVIDIA GPUs: Learn how to effectively integrate
  Broadcom NICs and NVIDIA GPUs within Ubuntu-based Deep Learning Virtual Machines
  (DLVMs) in a VMware Cloud Foundation (VCF) environment. Network Configuration: Detailed
  instructions for configuring Ethernet Thor 2 NICs and Tomahawk 5 switches to enable
  RoCE (RDMA over Converged Ethernet) with NVIDIA GPUs, ensuring low-latency, high-throughput
  communication critical for AI workloads. Benchmark Testing: Step-by-step procedures
  for running benchmark tests with essential collective communications libraries like
  NCCL, validating the efficiency of multi-GPU operations. LLM Inference: Guidance
  on launching and benchmarking Large Language Model (LLM) inference using NVIDIA
  Inference Microservices (NIM) and vLLM, demonstrating real-world performance gains.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/09/09/deploy-vmware-private-ai-on-hgx-servers-with-broadcom-ethernet-networking/
