---
title: Canary delivery with Argo Rollout and Amazon VPC Lattice for Amazon EKS
date: '2025-08-12T23:55:07+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/canary-delivery-with-argo-rollout-and-amazon-vpc-lattice-for-amazon-eks/
post_kind: link
draft: false
tldr: Modern application delivery demands agility and reliability, where updates are
  rolled out progressively while making sure of the minimal impact on end users. Progressive
  delivery strategies, such as canary deployments, allow organizations to release
  new features by shifting traffic incrementally between old and new versions of a
  service.
summary: 'Modern application delivery demands agility and reliability, where updates
  are rolled out progressively while making sure of the minimal impact on end users.
  Progressive delivery strategies, such as canary deployments, allow organizations
  to release new features by shifting traffic incrementally between old and new versions
  of a service. This allows organizations to first release features to a small subset
  of users, monitor system behavior and performance in real time, and automatically
  roll back if anomalies are detected. This is particularly valuable in modern microservices
  environments running on platforms such as Amazon Elastic Kubernetes Service (Amazon
  EKS) , where service meshes and traffic routers provide the necessary infrastructure
  for fine-grained control over traffic routing. This post explores an architectural
  approach to implementing progressive delivery using Amazon VPC Lattice, Amazon CloudWatch
  Synthetics , and Argo Rollouts. The solution uses VPC Lattice for enhanced traffic
  control across microservices, CloudWatch Synthetics for real-time health and validation
  monitoring, and Argo Rollouts for orchestrating canary updates. The content in this
  post addresses readers who are already familiar with networking constructs on Amazon
  Web Services (AWS), such as Amazon Virtual Private Cloud (Amazon VPC) , CloudWatch
  Synthetics and Amazon EKS. Instead of defining these services, we focus on their
  capabilities and integration with VPC Lattice. We also build upon your existing
  understanding of VPC Lattice concepts and Argo Rollouts. For more background on
  Amazon VPC Lattice, we recommend that you review the post, Build secure multi-account
  multi-VPC connectivity for your applications with Amazon VPC Lattice , and the collection
  of resources in the VPC Lattice Getting started guide. The architecture integrates
  multiple AWS services and Kubernetes-native components, providing a comprehensive
  solution for progressive delivery: In this section we consider an application running
  on Amazon EKS, where a new version of a microservice— prodDetail v2 —needs to be
  rolled out with minimal impact to users relying on the stable version v1. To do
  this, we implement a canary deployment strategy using VPC Lattice, Argo Rollouts,
  CloudWatch Synthetics, and AnalysisTemplates.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/canary-delivery-with-argo-rollout-and-amazon-vpc-lattice-for-amazon-eks/
