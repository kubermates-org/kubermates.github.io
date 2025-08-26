---
title: Introducing JobSet
date: '2025-03-23T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/03/23/introducing-jobset/
post_kind: link
draft: false
tldr: 'Authors : Daniel Vega-Myhre (Google), Abdullah Gharaibeh (Google), Kevin Hannon
  (Red Hat) In this article, we introduce JobSet , an open source API for representing
  distributed jobs. The goal of JobSet is to provide a unified API for distributed
  ML training and HPC workloads on Kubernetes.'
summary: 'Authors : Daniel Vega-Myhre (Google), Abdullah Gharaibeh (Google), Kevin
  Hannon (Red Hat) In this article, we introduce JobSet , an open source API for representing
  distributed jobs. The goal of JobSet is to provide a unified API for distributed
  ML training and HPC workloads on Kubernetes. The Kubernetes community’s recent enhancements
  to the batch ecosystem on Kubernetes has attracted ML engineers who have found it
  to be a natural fit for the requirements of running distributed training workloads.
  Large ML models (particularly LLMs) which cannot fit into the memory of the GPU
  or TPU chips on a single host are often distributed across tens of thousands of
  accelerator chips, which in turn may span thousands of hosts. As such, the model
  training code is often containerized and executed simultaneously on all these hosts,
  performing distributed computations which often shard both the model parameters
  and/or the training dataset across the target accelerator chips, using communication
  collective primitives like all-gather and all-reduce to perform distributed computations
  and synchronize gradients between hosts. These workload characteristics make Kubernetes
  a great fit for this type of workload, as efficiently scheduling and managing the
  lifecycle of containerized applications across a cluster of compute resources is
  an area where it shines. It is also very extensible, allowing developers to define
  their own Kubernetes APIs, objects, and controllers which manage the behavior and
  life cycle of these objects, allowing engineers to develop custom distributed training
  orchestration solutions to fit their needs. However, as distributed ML training
  techniques continue to evolve, existing Kubernetes primitives do not adequately
  model them alone anymore. Furthermore, the landscape of Kubernetes distributed training
  orchestration APIs has become fragmented, and each of the existing solutions in
  this fragmented landscape has certain limitations that make it non-optimal for distributed
  ML training. For example, the KubeFlow training operator defines custom APIs for
  different frameworks (e. g. PyTorchJob, TFJob, MPIJob, etc.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/03/23/introducing-jobset/
