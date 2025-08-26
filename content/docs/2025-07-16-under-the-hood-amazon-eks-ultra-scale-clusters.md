---
title: 'Under the hood: Amazon EKS ultra scale clusters'
date: '2025-07-16T00:14:37+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/under-the-hood-amazon-eks-ultra-scale-clusters/
post_kind: link
draft: false
tldr: This post was co-authored by Shyam Jeedigunta, Principal Engineer, Amazon EKS;
  Apoorva Kulkarni, Sr. Specialist Solutions Architect, Containers and Raghav Tripathi,
  Sr.
summary: This post was co-authored by Shyam Jeedigunta, Principal Engineer, Amazon
  EKS; Apoorva Kulkarni, Sr. Specialist Solutions Architect, Containers and Raghav
  Tripathi, Sr. Software Dev Manager, Amazon EKS. Today, Amazon Elastic Kubernetes
  Service (Amazon EKS) announced support for clusters with up to 100,000 nodes. With
  Amazon EC2’s new generation accelerated computing instance types, this translates
  to 1. 6 million AWS Trainium chips or 800,000 NVIDIA GPUs in a single Kubernetes
  cluster. This unlocks ultra scale artificial intelligence (AI) and machine leaning
  (ML) workloads such as state-of-the-art model training, fine-tuning and agentic
  inference. Besides customers directly consuming Amazon EKS today, these improvements
  also extend to other AI/ML services like Amazon SageMaker HyperPod with EKS that
  leverage EKS as their compute layer, advancing AWS’s overall ultra scale computing
  capabilities. Our customers have made it clear that containerization of training
  jobs and operators such as Kubeflow, the ability to streamline resource provisioning
  and lifecycle through projects like Karpenter, support for pluggable scheduling
  strategies, and access to a vast ecosystem of cloud-native tools is critical for
  their success in the AI/ML domain. Kubernetes has emerged as a key enabler here
  due to its powerful and extensible API model along with robust container orchestration
  capabilities, allowing accelerated workloads to scale quickly and run reliably.
  Through multiple technical innovations, architectural improvements and open-source
  collaboration, Amazon EKS has built the next generation of its cluster control plane
  and data plane for ultra scale, with full Kubernetes conformance. At AWS, we recommend
  customers running general-purpose applications with low coupling and horizontal
  scalability to follow a cell-based architecture as the strategy to sustain growth.
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/under-the-hood-amazon-eks-ultra-scale-clusters/
