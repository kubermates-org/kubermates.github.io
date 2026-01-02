---
title: Efficient image and model caching strategies for AI/ML and generative AI workloads
  on Amazon EKS
date: '2025-12-29T15:07:25+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/efficient-image-and-model-caching-strategies-for-ai-ml-and-generative-ai-workloads-on-amazon-eks/
post_kind: link
draft: false
tldr: Efficient image and model caching strategies for AI/ML and generative AI workloads
  on Amazon EKS The role of storage in AI/ML Data loading performance Storage IO for
  checkpointing Container image caching options Data volumes for Bottlerocket Secondary
  EBS volumes on AL2023 Using NVMe with RAID0 for Kubelet and Containerd Storage and
  caching options Amazon S3 S3 Express One Zone Optimizing code for Amazon S3 APIs
  Increasing per-client throughput Reducing latencies for frequently read data FSx
  for Lustre Conclusion About the authors When organizations deploy generative AI
  and machine learning (ML) workloads on Amazon Elastic Kubernetes Service (Amazon
  EKS ), implementing efficient caching strategies becomes crucial for both performance
  and cost optimization. Storage and caching play major roles throughout the lifecycle
  of any AI, ML, or generative AI workloads on Amazon EKS.
summary: Efficient image and model caching strategies for AI/ML and generative AI
  workloads on Amazon EKS The role of storage in AI/ML Data loading performance Storage
  IO for checkpointing Container image caching options Data volumes for Bottlerocket
  Secondary EBS volumes on AL2023 Using NVMe with RAID0 for Kubelet and Containerd
  Storage and caching options Amazon S3 S3 Express One Zone Optimizing code for Amazon
  S3 APIs Increasing per-client throughput Reducing latencies for frequently read
  data FSx for Lustre Conclusion About the authors When organizations deploy generative
  AI and machine learning (ML) workloads on Amazon Elastic Kubernetes Service (Amazon
  EKS ), implementing efficient caching strategies becomes crucial for both performance
  and cost optimization. Storage and caching play major roles throughout the lifecycle
  of any AI, ML, or generative AI workloads on Amazon EKS. This includes strategies
  for container image caching and storage/caching for AI/ML models during training,
  and the inferencing process for model checkpointing and tuning. Container image
  caching reduces the image pull latency, which in turn reduces the time for workloads
  to start the data processing. Storage options for model caching and checkpointing
  influences the cost and performance of the AI/ML workloads and container image caching.
  Container image caching options includes using data volumes in Bottlerocket AMIs
  and secondary Amazon Elastic Block Store (Amazon EBS) volumes on Amazon Linux 2023
  ( AL2023) optimized AMIs on Amazon EKS. Both of these options deliver significant
  reductions in container image pull time. Bottlerocket provides a smaller resource
  footprint and shorter boot times when compared to other Linux distributions, which
  helps to reduce costs by using less storage, compute, and networking resources.
  To optimize Amazon EBS performance for container workloads, use Amazon EBS-optimized
  instance types that provide dedicated bandwidth to Amazon EBS, so that gp3 volumes
  can deliver at least 90% of their provisioned IOPS performance 99% of the time (
  Amazon EBS documentation ). This approach removes the complexity of custom AMI builds
  while providing predictable storage performance for organizations handling extensive
  AI/ML container images. For AI/ML workloads, storage performance must align with
  compute performance to avoid underused GPU-based compute resources, as shown in
  the following figure. Throughput and performance bottlenecks lead to longer training
  times and increased costs.
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/efficient-image-and-model-caching-strategies-for-ai-ml-and-generative-ai-workloads-on-amazon-eks/
