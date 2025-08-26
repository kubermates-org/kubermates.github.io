---
title: 'Migrate to Amazon EKS: Data plane cost modeling with Karpenter and KWOK'
date: '2025-08-21T18:18:42+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/migrate-to-amazon-eks-data-plane-cost-modeling-with-karpenter-and-kwok/
post_kind: link
draft: false
tldr: 'When migrating Kubernetes clusters to Amazon Elastic Kubernetes Service (Amazon
  EKS) , organizations typically follow three phases: assessment, mobilize, and migrate
  and modernize. The assessment phase involves evaluating technical feasibility for
  Amazon EKS workloads, analyzing current Kubernetes environments, identifying compatibility
  issues, estimating costs, and determining timelines with business impact considerations.'
summary: 'When migrating Kubernetes clusters to Amazon Elastic Kubernetes Service
  (Amazon EKS) , organizations typically follow three phases: assessment, mobilize,
  and migrate and modernize. The assessment phase involves evaluating technical feasibility
  for Amazon EKS workloads, analyzing current Kubernetes environments, identifying
  compatibility issues, estimating costs, and determining timelines with business
  impact considerations. During the mobilize phase, organizations create detailed
  migration plans, establish EKS environments with proper networking and security,
  train teams, and develop testing procedures. The final migrate and modernize phase
  involves transferring applications and data, validating functionality, implementing
  cloud-centered features, optimizing resources and costs, and enhancing observability
  to fully use AWS capabilities. One of the most significant challenges organizations
  face during the process is cost estimation, which happens in the assessment phase.
  Karpenter is an open source Kubernetes node autoscaler that efficiently provisions
  just-in-time compute resources to match workload demands. Unlike traditional autoscalers,
  Karpenter directly integrates with cloud providers to make intelligent, real-time
  decisions about instance types, availability zones, and capacity options. It evaluates
  pod requirements and constraints to select optimal instances, considering factors
  such as CPU, memory, price, and availability. Karpenter can consolidate workloads
  for cost efficiency and rapidly scale from zero to handle sudden demand spikes.
  It supports both spot and on-demand instances, and automatically terminates nodes
  when they’re no longer needed, optimizing cluster resource utilization and reducing
  cloud costs. Karpenter uses the concept of Providers to interact with different
  infrastructure platforms for provisioning and managing compute resources. KWOK (Kubernetes
  WithOut Kubelet) is a toolkit that simulates data plane nodes without allocating
  actual infrastructure, and can be used as a provider to create lightweight testing
  environments that enable developers to validate provisioning decisions, try various
  (virtual) instance types, and debug scaling behaviors.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/migrate-to-amazon-eks-data-plane-cost-modeling-with-karpenter-and-kwok/
