---
title: Introducing Seekable OCI Parallel Pull mode for Amazon EKS
date: '2025-08-27T19:13:44+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/introducing-seekable-oci-parallel-pull-mode-for-amazon-eks/
post_kind: link
draft: false
tldr: Introducing Seekable OCI Parallel Pull mode for Amazon EKS Introducing Parallel
  Pull mode for the SOCI snapshotter Understanding image pulls SOCI Parallel Pull
  details Performance consideration SOCI Parallel Pull in action Tuning configuration
  Benchmark Getting started with SOCI Parallel Pull Mode About the authors Containerization
  has transformed how customers build and deploy modern cloud native applications,
  offering unparalleled benefits in portability, scalability, and operational efficiency.
  Containers provide integrated dependency management and enable a standard distribution
  and deployment model for any workload.
summary: Introducing Seekable OCI Parallel Pull mode for Amazon EKS Introducing Parallel
  Pull mode for the SOCI snapshotter Understanding image pulls SOCI Parallel Pull
  details Performance consideration SOCI Parallel Pull in action Tuning configuration
  Benchmark Getting started with SOCI Parallel Pull Mode About the authors Containerization
  has transformed how customers build and deploy modern cloud native applications,
  offering unparalleled benefits in portability, scalability, and operational efficiency.
  Containers provide integrated dependency management and enable a standard distribution
  and deployment model for any workload. With Amazon Elastic Kubernetes Service (Amazon
  EKS), Kubernetes has emerged as a go-to solution for customers running large-scale
  containerized workloads that need to efficiently scale to meet evolving needs. However,
  one persistent challenge continues to impact specific deployment and scaling aspects
  of Kubernetes workload operations. Container image pulls, particularly when working
  with large and complex container images, can directly impact the responsiveness
  and agility of your systems. With the growth of AI/ML workloads, where we see particularly
  large images, this directly impacts operations as images may take several minutes
  to pull and prepare. In our recent Under the Hood post for EKS Ultra Scale Clusters,
  we briefly touched on our evolving solution for this problem, Seekable OCI (SOCI)
  Parallel Pull. In this post, we’ll explain how container image pulls work and how
  they impact deployment and scaling operations, we’ll dive deeper into how SOCI parallel
  pull works, and finally show how it can help you improve image pull performance
  with your workloads on Amazon EKS. As average container image sizes have grown in
  recent years, container startup performance has become a critical element of modern
  cloud native system performance. Image pull and preparation can account for more
  than 75% of total startup time for new and scaling workloads. This challenge is
  particularly acute with the rise of AI/ML workloads on Amazon EKS. These workloads
  have driven significant growth in container image sizes, where images are commonly
  tens of gigabytes in size.
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/introducing-seekable-oci-parallel-pull-mode-for-amazon-eks/
