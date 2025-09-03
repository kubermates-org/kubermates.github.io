---
title: Unlocking next-generation AI performance with Dynamic Resource Allocation on
  Amazon EKS and Amazon EC2 P6e-GB200
date: '2025-09-02T23:33:59+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/unlocking-next-generation-ai-performance-with-dynamic-resource-allocation-on-amazon-eks-and-amazon-ec2-p6e-gb200/
post_kind: link
draft: false
tldr: 'Unlocking next-generation AI performance with Dynamic Resource Allocation on
  Amazon EKS and Amazon EC2 P6e-GB200 The power behind P6e-GB200: NVIDIA GB200 Grace
  Blackwell architecture Understanding EC2 P6e-GB200 UltraServer architecture Integrating
  P6e-GB200 UltraServers with Amazon EKS The challenge: running distributed AI workloads
  on Kubernetes The solution: Kubernetes DRA and IMEX How DRA solves traditional GPU
  allocation problems Topology-aware scheduling and memory coherence Workload scheduling
  flow with DRA How to use p6e-GB200 with Kubernetes DRA with Amazon EKS Prerequisites
  Step 1: Reserve P6e-GB200 UltraServer capacity Step 2: Create the EKS cluster configuration
  file Step 3: Deploy the EKS cluster Step 4: Deploy the NVIDIA GPU Operator Step
  5: Install the NVIDIA DRA Driver Step 6: Verify DRA resources Validating IMEX channel
  allocation Apply and validate Multi-node IMEX communication in action Conclusion
  About the authors The rapid evolution of agentic AI and large language models (LLMs),
  particularly reasoning models, has created unprecedented demand for computational
  resources. Today’s most advanced AI models span hundreds of billions to trillions
  of parameters and necessitate massive computational power, extensive memory footprints,
  and ultra-fast interconnects to function efficiently.'
summary: 'Unlocking next-generation AI performance with Dynamic Resource Allocation
  on Amazon EKS and Amazon EC2 P6e-GB200 The power behind P6e-GB200: NVIDIA GB200
  Grace Blackwell architecture Understanding EC2 P6e-GB200 UltraServer architecture
  Integrating P6e-GB200 UltraServers with Amazon EKS The challenge: running distributed
  AI workloads on Kubernetes The solution: Kubernetes DRA and IMEX How DRA solves
  traditional GPU allocation problems Topology-aware scheduling and memory coherence
  Workload scheduling flow with DRA How to use p6e-GB200 with Kubernetes DRA with
  Amazon EKS Prerequisites Step 1: Reserve P6e-GB200 UltraServer capacity Step 2:
  Create the EKS cluster configuration file Step 3: Deploy the EKS cluster Step 4:
  Deploy the NVIDIA GPU Operator Step 5: Install the NVIDIA DRA Driver Step 6: Verify
  DRA resources Validating IMEX channel allocation Apply and validate Multi-node IMEX
  communication in action Conclusion About the authors The rapid evolution of agentic
  AI and large language models (LLMs), particularly reasoning models, has created
  unprecedented demand for computational resources. Today’s most advanced AI models
  span hundreds of billions to trillions of parameters and necessitate massive computational
  power, extensive memory footprints, and ultra-fast interconnects to function efficiently.
  Organizations developing applications for natural language processing, scientific
  simulations, 3D content generation, and multimodal inference need infrastructure
  that can scale from today’s billion-parameter models to tomorrow’s trillion-parameter
  frontiers while maintaining performance. In this post, we explore how the new Amazon
  Elastic Compute Cloud (Amazon EC2) P6e-GB200 UltraServers are transforming distributed
  AI workload through seamless Kubernetes integration. Amazon Web Services (AWS) introduced
  the EC2 P6e-GB200 UltraServers to meet the growing demand for large-scale AI model
  training and inference. They represent a significant architectural breakthrough
  for distributed AI workloads. Furthermore, the EC2 P6e-GB200 UltraServer launch
  includes support for Amazon Elastic Kubernetes Service (Amazon EKS) , providing
  a Kubernetes-native environment for deploying and scaling from hundreds-of-billions
  to trillion-parameter models as the AI landscape continues to evolve. At the heart
  of EC2 P6e-GB200 UltraServers is the NVIDIA GB200 Grace Blackwell Superchip , which
  integrates two NVIDIA Blackwell GPUs with a NVIDIA Grace CPU. Furthermore, it provides
  NVLink-Chip-to-Chip (C2C) connection between these components, delivering 900 GB/s
  of bidirectional bandwidth, which is substantially faster than traditional PCIe
  interfaces. When deployed at rack scale, EC2 P6e-GB200 UltraServers participate
  in NVIDIA’s GB200 NVL72 architecture , creating memory-coherent domains of up to
  72 GPUs. Fifth-generation NVLink technology enables GPU-to-GPU communication across
  discrete servers within the same domain at up to 1.8 TB/s per GPU. Critical to this
  performance is Elastic Fabric Adapter (EFAv4) networking, which delivers up to 28.8
  Tbps of total network bandwidth per UltraServer.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/unlocking-next-generation-ai-performance-with-dynamic-resource-allocation-on-amazon-eks-and-amazon-ec2-p6e-gb200/
