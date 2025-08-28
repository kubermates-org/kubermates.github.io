---
title: 'Democratizing AI Model Training on Kubernetes: Introducing Kubeflow Trainer
  V2'
date: '2025-07-21T00:00:00-05:00'
tags:
- kubeflow
- kubernetes
source: Kubeflow Blog
external_url: https://blog.kubeflow.org/trainer/intro/
post_kind: link
draft: false
tldr: Background and Evolution User Personas Python SDK Simplified API Extensibility
  and Pipeline Framework LLMs Fine-Tuning Support Dataset and Model Initializers Use
  of JobSet API Kueue Integration MPI Support Gang-Scheduling Fault Tolerance Improvements
  What’s Next? Migration from Training Operator v1 Resources and Community Background
  and Evolution User Personas Python SDK Simplified API Extensibility and Pipeline
  Framework LLMs Fine-Tuning Support Dataset and Model Initializers Use of JobSet
  API Kueue Integration MPI Support Gang-Scheduling Fault Tolerance Improvements What’s
  Next? Migration from Training Operator v1 Resources and Community Running machine
  learning workloads on Kubernetes can be challenging. Distributed training and LLMs
  fine-tuning, in particular, involves managing multiple nodes, GPUs, large datasets,
  and fault tolerance, which often requires deep Kubernetes knowledge.
summary: 'Background and Evolution User Personas Python SDK Simplified API Extensibility
  and Pipeline Framework LLMs Fine-Tuning Support Dataset and Model Initializers Use
  of JobSet API Kueue Integration MPI Support Gang-Scheduling Fault Tolerance Improvements
  What’s Next? Migration from Training Operator v1 Resources and Community Background
  and Evolution User Personas Python SDK Simplified API Extensibility and Pipeline
  Framework LLMs Fine-Tuning Support Dataset and Model Initializers Use of JobSet
  API Kueue Integration MPI Support Gang-Scheduling Fault Tolerance Improvements What’s
  Next? Migration from Training Operator v1 Resources and Community Running machine
  learning workloads on Kubernetes can be challenging. Distributed training and LLMs
  fine-tuning, in particular, involves managing multiple nodes, GPUs, large datasets,
  and fault tolerance, which often requires deep Kubernetes knowledge. The Kubeflow
  Trainer v2 (KF Trainer) was created to hide this complexity, by abstracting Kubernetes
  from AI Practitioners and providing the easiest, most scalable way to run distributed
  PyTorch jobs. The main goals of Kubeflow Trainer v2 include: Make AI/ML workloads
  easier to manage at scale Provide a Pythonic interface to train models Deliver the
  easiest and most scalable PyTorch distributed training on Kubernetes Add built-in
  support for fine-tuning large language models Abstract Kubernetes complexity from
  AI Practitioners Consolidate efforts between Kubernetes Batch WG and Kubeflow community
  We’re deeply grateful to all contributors and community members who made the Trainer
  v2 possible with their hard work and valuable feedback. We’d like to give special
  recognition to andreyvelich , tenzen-y , electronic-waste , astefanutti , ironicbo
  , mahdikhashan , kramaranya , harshal292004 , akshaychitneni , chenyi015 and the
  rest of the contributors. We would also like to highlight ahg-g , kannon92 , and
  vsoch whose feedback was essential while we designed the Kubeflow Trainer architecture
  together with the Batch WG. See the full contributor list for everyone who helped
  make this release possible. Kubeflow Trainer v2 represents the next evolution of
  the Kubeflow Training Operator , building on over seven years of experience running
  ML workloads on Kubernetes. The journey began in 2017 when the Kubeflow project
  introduced TFJob to orchestrate TensorFlow training on Kubernetes. At that time,
  Kubernetes lacked many of the advanced batch processing features needed for distributed
  ML training, so the community had to implement these capabilities from scratch.
  Over the years, the project expanded to support multiple ML frameworks including
  PyTorch , MXNet , MPI , and XGBoost through various specialized operators. In 2021,
  these were consolidated into the unified Training Operator v1.'
---
Open the original post ↗ https://blog.kubeflow.org/trainer/intro/
