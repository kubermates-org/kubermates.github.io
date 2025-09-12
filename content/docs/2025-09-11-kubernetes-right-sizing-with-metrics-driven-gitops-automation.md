---
title: Kubernetes right-sizing with metrics-driven GitOps automation
date: '2025-09-11T15:17:23+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/kubernetes-right-sizing-with-metrics-driven-gitops-automation/
post_kind: link
draft: false
tldr: Kubernetes right-sizing with metrics-driven GitOps automation Understanding
  the challenges of resource management in Amazon EKS The impact of inefficient resource
  management Existing solutions for Kubernetes resource management How the proposed
  solution addresses the challenges Solution overview Workflow overview Key architectural
  considerations Walkthrough Prerequisites Implementing a GitOps-driven automation
  for resource optimization GitOps principle Setting up the recommendation generator
  Environment and metrics source Local or External Installation Automating the GitOps
  workflow Cleaning up Conclusion About the authors Efficient resource allocation
  in Kubernetes is essential for optimizing application performance and controlling
  costs. In Amazon Elastic Kubernetes Service (Amazon EKS) , managing resource requests
  and limits manually can be challenging and error-prone.
summary: Kubernetes right-sizing with metrics-driven GitOps automation Understanding
  the challenges of resource management in Amazon EKS The impact of inefficient resource
  management Existing solutions for Kubernetes resource management How the proposed
  solution addresses the challenges Solution overview Workflow overview Key architectural
  considerations Walkthrough Prerequisites Implementing a GitOps-driven automation
  for resource optimization GitOps principle Setting up the recommendation generator
  Environment and metrics source Local or External Installation Automating the GitOps
  workflow Cleaning up Conclusion About the authors Efficient resource allocation
  in Kubernetes is essential for optimizing application performance and controlling
  costs. In Amazon Elastic Kubernetes Service (Amazon EKS) , managing resource requests
  and limits manually can be challenging and error-prone. This post introduces an
  automated, and GitOps-driven approach to resource optimization using Amazon Web
  Services (AWS) services such as Amazon Managed Service for Prometheus and Amazon
  Bedrock. This approach is particularly beneficial for users who prefer non-intrusive
  methods for resource optimization. Understanding resource management in Kubernetes
  is crucial for optimal cluster performance. When deploying pods, the Kubernetes
  scheduler evaluates resource requests to find suitable nodes that can accommodate
  the specified CPU and memory requirements. These requests act as the minimum guaranteed
  resources for the pod, while limits serve as upper bounds to prevent any single
  pod from monopolizing node resources. Over-provisioning and under-provisioning of
  resources in Kubernetes can lead to increased costs and performance issues. Striking
  the right balance is essential for optimal resource usage. In a shared environment,
  one pod consuming excessive resources can degrade the performance of others on the
  same node. Applications with fluctuating resource demands can be challenging to
  manage. Without adaptive resource allocation strategies, these workloads may experience
  performance degradation or resource waste.
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/kubernetes-right-sizing-with-metrics-driven-gitops-automation/
