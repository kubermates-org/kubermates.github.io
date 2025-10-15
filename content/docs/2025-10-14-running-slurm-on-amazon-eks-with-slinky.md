---
title: Running Slurm on Amazon EKS with Slinky
date: '2025-10-14T16:58:24+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/running-slurm-on-amazon-eks-with-slinky/
post_kind: link
draft: false
tldr: Running Slurm on Amazon EKS with Slinky A primer on Slurm The Slinky Project
  The use case for Slinky Architecture overview of Slurm on EKS with Slinky Slinky
  Slurm cluster components Benefits of running Slurm on EKS with Slinky Alternatives
  for running Slurm on AWS AWS ParallelCluster AWS Parallel Computing Service Amazon
  SageMaker HyperPod Alternative Kubernetes native job schedulers Volcano Apache YuniKorn
  Kueue When Slurm on EKS is right for you About the authors When building an AI infrastructure
  stack for pre-training, fine-tuning, or inference workloads, both Slurm and Kubernetes
  can be used as compute orchestration platforms to meet the needs of different teams
  and address different stages of the AI development lifecycle. However, traditionally
  this would result in managing disparate clusters of accelerated compute capacity,
  potentially duplicating operational overhead and risking resource underuse.
summary: 'Running Slurm on Amazon EKS with Slinky A primer on Slurm The Slinky Project
  The use case for Slinky Architecture overview of Slurm on EKS with Slinky Slinky
  Slurm cluster components Benefits of running Slurm on EKS with Slinky Alternatives
  for running Slurm on AWS AWS ParallelCluster AWS Parallel Computing Service Amazon
  SageMaker HyperPod Alternative Kubernetes native job schedulers Volcano Apache YuniKorn
  Kueue When Slurm on EKS is right for you About the authors When building an AI infrastructure
  stack for pre-training, fine-tuning, or inference workloads, both Slurm and Kubernetes
  can be used as compute orchestration platforms to meet the needs of different teams
  and address different stages of the AI development lifecycle. However, traditionally
  this would result in managing disparate clusters of accelerated compute capacity,
  potentially duplicating operational overhead and risking resource underuse. But
  what if you could deploy a Slurm cluster as a Kubernetes service to get the best
  of both worlds? Think of Kubernetes as a large, modern office building providing
  shared resources (for example, electricity, internet, security, HVAC) for its tenants.
  When a specialized lab moves in, needing dedicated resources such as specific power
  and temperature control, you don’t build a new building. Instead, you integrate
  the lab into the existing building infrastructure, allowing it to use shared services
  while maintaining its own precise controls for high-performance work. In the same
  way, Slurm can be ran inside a Kubernetes environment such as Amazon Elastic Kubernetes
  Service (Amazon EKS) using the open source Slinky Project. In this post, we introduce
  the Slinky Project, discuss its benefits, explore some alternatives, and leave you
  with a bit of homework to go deploy the Slurm on EKS blueprint , which uses the
  Slinky Slurm operator. Slurm is an open source, highly scalable workload manager
  and job scheduler designed for managing compute resources on compute clusters of
  all sizes. It provides three core functions: allocating access to compute resources,
  providing a framework for launching and monitoring parallel computing jobs, and
  managing queues of pending work to resolve resource contention. Slurm is widely
  used in traditional High-Performance Computing (HPC) environments and in AI training
  to manage and schedule large-scale accelerated compute workloads across multi-node
  clusters. Slurm allows researchers and engineers to efficiently allocate CPU, GPU,
  and memory resources for distributed training jobs with fine-grained control over
  resource types and job priorities. Slurm’s reliability, advanced scheduling features,
  and integration with both on-premises and cloud environments make it a preferred
  choice for handling the scale, throughput, and reproducibility that modern AI research
  and industry demand.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/running-slurm-on-amazon-eks-with-slinky/
