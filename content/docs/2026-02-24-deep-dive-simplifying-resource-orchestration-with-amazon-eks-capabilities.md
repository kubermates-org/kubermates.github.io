---
title: 'Deep dive: Simplifying resource orchestration with Amazon EKS Capabilities'
date: '2026-02-24T18:09:31+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/deep-dive-simplifying-resource-orchestration-with-amazon-eks-capabilities/
post_kind: link
draft: false
tldr: 'Deep dive: Simplifying resource orchestration with Amazon EKS Capabilities
  The Kubernetes Resource Model and EKS capabilities EKS capabilities at-a-glance
  Getting started with enabling ACK and kro capabilities Prerequisites Step by step
  guide: What happens behind the scenes Declarative AWS Resources Management: Complex
  application stacks orchestration: Solution walkthrough: Key considerations Multi-cluster
  management Monitoring and operations Cleanup Conclusion About the authors As organizations
  scale their Kubernetes operations, teams face mounting operational complexity. While
  teams focus on building and deploying applications, they must also maintain Kubernetes
  platform components like GitOps controllers and infrastructure orchestrators.'
summary: 'Deep dive: Simplifying resource orchestration with Amazon EKS Capabilities
  The Kubernetes Resource Model and EKS capabilities EKS capabilities at-a-glance
  Getting started with enabling ACK and kro capabilities Prerequisites Step by step
  guide: What happens behind the scenes Declarative AWS Resources Management: Complex
  application stacks orchestration: Solution walkthrough: Key considerations Multi-cluster
  management Monitoring and operations Cleanup Conclusion About the authors As organizations
  scale their Kubernetes operations, teams face mounting operational complexity. While
  teams focus on building and deploying applications, they must also maintain Kubernetes
  platform components like GitOps controllers and infrastructure orchestrators. This
  dual burden slows development velocity and diverts engineering resources from building
  features to operating platform tools. Amazon Elastic Kubernetes Service (Amazon
  EKS) Capabilities address these challenges with a fully managed, Kubernetes-native
  tools for both Amazon EKS standard and EKS Auto Mode that runs in AWS-managed infrastructure.
  Figure 1: EKS Managed Capabilities with standard Amazon EKS cluster Figure 2: EKS
  Managed Capabilities with Amazon EKS Auto Mode cluster Since the launch, three foundational
  capabilities are available: continuous deployment with Argo CD, AWS resource management
  through AWS Controllers for Kubernetes (ACK) , and dynamic resource orchestration
  using Kube Resource Orchestrator (kro). This unified approach accelerates deployment
  velocity, enabling platform teams to support more applications while maintaining
  consistent security and compliance standards across all clusters. This blog post
  focuses on ACK and kro capabilities. For a deep dive on Amazon EKS capability for
  Argo CD, check out Deep dive: Streamlining GitOps with Amazon EKS capability for
  Argo CD. The Kubernetes Resource Model provides a declarative framework where you
  define your desired state, and Kubernetes continuously reconciles the actual state
  with your intentions. ACK and kro extend this model in complementary ways: ACK enables
  the management of AWS resources using Kubernetes APIs, allowing you to create and
  manage Amazon Simple Storage Service (Amazon S3) buckets, Amazon Relational Database
  Service (Amazon RDS) databases, IAM roles and other AWS resources as if they were
  Kubernetes resources. kro enables you to create custom Kubernetes APIs that compose
  multiple resources into higher-level abstractions, which lets infrastructure teams
  define reusable patterns for common resource combinations. By combining kro and
  ACK you can compose both Kubernetes and cloud resources into unified abstractions.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/deep-dive-simplifying-resource-orchestration-with-amazon-eks-capabilities/
