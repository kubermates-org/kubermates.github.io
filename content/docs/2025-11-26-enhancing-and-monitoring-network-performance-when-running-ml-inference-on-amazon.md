---
title: Enhancing and monitoring network performance when running ML Inference on Amazon
  EKS
date: '2025-11-26T20:55:13+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/enhancing-and-monitoring-network-performance-when-running-ml-inference-on-amazon-eks/
post_kind: link
draft: false
tldr: Enhancing and monitoring network performance when running ML Inference on Amazon
  EKS Current challenges with network observability for ML inference workloads Deep-dive
  into Container Network Observability in Amazon EKS ML inference workload scenario
  Setting up Container Network Observability use cases for ML inference workload Visualize
  and confirm intercommunication between services for troubleshooting Analyze Availability
  Zone (AZ) traffic pattern between deployments Network Health Indicator Investigating
  ML inference Latency using performance metrics in Amazon Manged Grafana Cleaning
  up Conclusion About the authors Amazon Elastic Kubernetes Service (Amazon EKS) has
  become a popular choice for customers looking to run their workloads in the Amazon
  Web Services (AWS) Cloud with customers increasingly choosing to run their AI and
  Machine Learning (AI/ML) workloads on Amazon EKS. Customers can use Amazon EKS to
  customize configuration to match their workload requirements.
summary: Enhancing and monitoring network performance when running ML Inference on
  Amazon EKS Current challenges with network observability for ML inference workloads
  Deep-dive into Container Network Observability in Amazon EKS ML inference workload
  scenario Setting up Container Network Observability use cases for ML inference workload
  Visualize and confirm intercommunication between services for troubleshooting Analyze
  Availability Zone (AZ) traffic pattern between deployments Network Health Indicator
  Investigating ML inference Latency using performance metrics in Amazon Manged Grafana
  Cleaning up Conclusion About the authors Amazon Elastic Kubernetes Service (Amazon
  EKS) has become a popular choice for customers looking to run their workloads in
  the Amazon Web Services (AWS) Cloud with customers increasingly choosing to run
  their AI and Machine Learning (AI/ML) workloads on Amazon EKS. Customers can use
  Amazon EKS to customize configuration to match their workload requirements. Furthermore,
  Platform teams can use it to transfer their existing container orchestration model
  and expertise when deploying new workloads and standardize on Amazon EKS. Kubernetes
  also provides access to a rich environment of popular open source AI/ML frameworks,
  tools, and inference engines such as Ray, vLLM, Triton, PyTorch. Lastly, they can
  use Kubernetes’ tested capability to auto-scale, deploy and manage containerized
  workloads at scale, and implement the full cluster automation capabilities of EKS.
  Some use cases of AI/ML workloads deployed on Amazon EKS include generative AI Model
  training for Large Language Models (LLMs), real-time and batch ML inference, and
  Retrieval Augmented Generation (RAG) Pipelines. ML inference is the process where
  a trained model generates predictions on a user’s input prompt or query. Inference
  has become an important part of modern applications and powers applications such
  as content generation, intelligent assistants, recommendation engines. Over the
  years AWS has released a suite of resources and artifacts to accelerate and streamline
  customers’ usage of Amazon EKS as their service of choice for running AI/ML workloads.
  These include AI on EKS , Best Practices for Running AI/ML workloads , Amazon EKS-optimized
  accelerated AMIs for GPU Instances , and AWS Deep Learning Containers. Recently
  AWS announced Container Network Observability in Amazon EKS , a set of Amazon EKS
  network observability features that customers can use to observe, visualize, and
  enhance their Amazon EKS network environment. In this post we explore the feature
  sets, deep dive into how it works, and explore an ML inference workload scenario
  where we use it to monitor and enhance its network performance.
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/enhancing-and-monitoring-network-performance-when-running-ml-inference-on-amazon-eks/
