---
title: Extending GPU Fractionalization and Orchestration to the edge with NVIDIA Run:ai
  and Amazon EKS
date: '2025-10-28T18:05:27+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/extending-gpu-fractionalization-and-orchestration-to-the-edge-with-nvidia-runai-and-amazon-eks/
post_kind: link
draft: false
tldr: Extending GPU Fractionalization and Orchestration to the edge with NVIDIA Run:ai
  and Amazon EKS Extensive and performant global cloud infrastructure Challenges in
  bringing AI workloads to the edge Training Inference Run:ai support for AWS Hybrid
  and Edge services Best practices for Run:ai at the edge Conclusion About the authors
  As organizations of all sizes have rapidly embraced the opportunity to pair foundation
  models (FMs) with AI agents to streamline complex workflows and processes, the demand
  for artificial intelligence and machine learning capabilities across distributed
  locations has never been stronger. For example, some organizations need to run custom,
  in-house language models within a specific geographic boundary to meet data residency
  requirements, while others require processing data locally to serve latency-sensitive
  edge inference requests.
summary: 'Extending GPU Fractionalization and Orchestration to the edge with NVIDIA
  Run:ai and Amazon EKS Extensive and performant global cloud infrastructure Challenges
  in bringing AI workloads to the edge Training Inference Run:ai support for AWS Hybrid
  and Edge services Best practices for Run:ai at the edge Conclusion About the authors
  As organizations of all sizes have rapidly embraced the opportunity to pair foundation
  models (FMs) with AI agents to streamline complex workflows and processes, the demand
  for artificial intelligence and machine learning capabilities across distributed
  locations has never been stronger. For example, some organizations need to run custom,
  in-house language models within a specific geographic boundary to meet data residency
  requirements, while others require processing data locally to serve latency-sensitive
  edge inference requests. These distributed processing needs often require running
  AI/ML workloads in local metro Points of Presence (PoPs), customer premises, and
  beyond – especially when an AWS Region is not close enough to meet performance or
  compliance requirements. Managing these distributed workloads introduces another
  challenge: the need for efficient and topology-aware GPU resource management becomes
  critical, particularly at the distributed edge, where capacity is often limited
  and requires optimal allocation. Building on these emerging needs for distributed
  AI/ML capabilities and efficient GPU resource management, Amazon Web Services (AWS)
  and NVIDIA have been working together to explore solutions native to the environments
  that customers most frequently use for model training and inference, such as Amazon
  Elastic Kubernetes Service. In a previous blog post , we showcased how NVIDIA Run:ai
  addresses key challenges in GPU resource management, including static allocation
  limitations, resource competition, and inefficient sharing in GPU clusters. The
  blog post detailed the implementation of NVIDIA Run:ai on Amazon EKS, which featured
  dynamic GPU fractions, node-level scheduling, and priority-based sharing. Since
  then, we have released NVIDIA Run:ai in AWS Marketplace , allowing customers to
  deploy the Run:ai control plane to their Amazon EKS clusters without having to manage
  the deployment of individual Helm Charts. Building on this collaboration, today
  we are extending this flexibility to the entire AWS cloud continuum, enabling you
  to optimize GPU resources wherever your workloads need to run – in an AWS Region
  , on-premises , or at the edge. That is why we are excited to announce native Run:ai
  support for Amazon EKS in AWS Local Zones (including Dedicated Local Zones), Amazon
  EKS on AWS Outposts , and Amazon EKS Hybrid Nodes. As part of this launch, you can
  now extend Run:ai environments to support a cluster of GPUs separated by hundreds
  (if not thousands) of miles across these AWS Hybrid and Edge services. This architectural
  pattern enables you to create powerful high availability and disaster recovery strategies
  while maximizing cost efficiency and complying with local data residency requirements.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/extending-gpu-fractionalization-and-orchestration-to-the-edge-with-nvidia-runai-and-amazon-eks/
