---
title: Introducing the Metaflow-Kubeflow Integration
date: '2026-02-04T00:00:00-06:00'
tags:
- kubeflow
- kubernetes
source: Kubeflow Blog
external_url: https://blog.kubeflow.org/metaflow/
post_kind: link
draft: false
tldr: 'A tale of two flows: Metaflow and Kubeflow Why Metaflow → Kubeflow Development
  Scaling Deployment Metaflow → Kubeflow in practice Feedback welcome! A tale of two
  flows: Metaflow and Kubeflow Why Metaflow → Kubeflow Development Scaling Deployment
  Development Scaling Deployment Metaflow → Kubeflow in practice Feedback welcome!
  Metaflow is a Python framework for building and operating ML and AI projects, originally
  developed and open-sourced by Netflix in 2019. In many ways, Kubeflow and Metaflow
  are cousins: closely related in spirit, but designed with distinct goals and priorities.'
summary: 'A tale of two flows: Metaflow and Kubeflow Why Metaflow → Kubeflow Development
  Scaling Deployment Metaflow → Kubeflow in practice Feedback welcome! A tale of two
  flows: Metaflow and Kubeflow Why Metaflow → Kubeflow Development Scaling Deployment
  Development Scaling Deployment Metaflow → Kubeflow in practice Feedback welcome!
  Metaflow is a Python framework for building and operating ML and AI projects, originally
  developed and open-sourced by Netflix in 2019. In many ways, Kubeflow and Metaflow
  are cousins: closely related in spirit, but designed with distinct goals and priorities.
  Metaflow emerged from Netflix’s need to empower data scientists and ML/AI developers
  with developer-friendly, Python-native tooling, so that they could easily iterate
  quickly on ideas, compare modeling approaches, and ship the best solutions to production
  without heavy engineering or DevOps involvement. On the infrastructure side, Metaflow
  started with AWS-native services like AWS Batch and Step Functions, later expanding
  to provide first-class support for the Kubernetes ecosystem and other hyperscaler
  clouds. In contrast, Kubeflow began as a set of Kubernetes operators for distributed
  TensorFlow and Jupyter Notebook management. Over time, it has evolved into a comprehensive
  Cloud Native AI ecosystem, offering a broad set of tools out of the box. These include
  Trainer, Katib, Spark Operator for orchestrating distributed AI workloads, Workspaces
  for interactive development environments, Hub for AI catalog and artifacts management,
  KServe for model serving, and Pipelines to deploy end-to-end ML workflows and stitching
  Kubeflow components together. Over the years, Metaflow has delighted end users with
  its intuitive APIs, while Kubeflow has delivered tons of value to infrastructure
  teams through its robust platform components. This complementary nature of the tools
  motivated us to build a bridge between the two: you can now author projects in Metaflow
  and deploy them as Kubeflow Pipelines , side by side with your existing Kubeflow
  workloads. In the most recent CNCF Technology Radar survey from October 2025, Metaflow
  got the highest positive scores in the “ likelihood to recommend ” and “ usefulness
  ” categories, reflecting its success in providing a set of stable, productivity-boosting
  APIs for ML/AI developers. Metaflow spans the entire development lifecycle—from
  early experimentation to production deployment and ongoing operations. To give you
  an idea, the core features below illustrate the breadth of its API surface, grouped
  by project stage: Straightforward APIs for creating and composing workflows.'
---
Open the original post ↗ https://blog.kubeflow.org/metaflow/
