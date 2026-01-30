---
title: 'Maximize Amazon EKS efficiency: How Auto Mode, Graviton, and Spot work together'
date: '2026-01-23T16:24:49+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/maximize-amazon-eks-efficiency-how-auto-mode-graviton-and-spot-work-together/
post_kind: link
draft: false
tldr: 'Maximize Amazon EKS efficiency: How Auto Mode, Graviton, and Spot work together
  Solution overview Getting started Steps for scenario 1: Adopting AWS Graviton instances:
  Reset Amazon EKS Auto Mode cluster before proceeding to scenario 2 Steps for scenario
  2: Adopting spot instances and handling workload restrictions: Key features of this
  NodePool: Key configuration aspects: Verification steps: Verifying workload placement
  Cleaning up Conclusion About the authors Amazon Elastic Kubernetes Service (Amazon
  EKS) Auto Mode streamlines the operation of your Amazon EKS clusters by automating
  key infrastructure components. This automation streamlines various operational tasks,
  allowing for more efficient resource allocation and management.'
summary: 'Maximize Amazon EKS efficiency: How Auto Mode, Graviton, and Spot work together
  Solution overview Getting started Steps for scenario 1: Adopting AWS Graviton instances:
  Reset Amazon EKS Auto Mode cluster before proceeding to scenario 2 Steps for scenario
  2: Adopting spot instances and handling workload restrictions: Key features of this
  NodePool: Key configuration aspects: Verification steps: Verifying workload placement
  Cleaning up Conclusion About the authors Amazon Elastic Kubernetes Service (Amazon
  EKS) Auto Mode streamlines the operation of your Amazon EKS clusters by automating
  key infrastructure components. This automation streamlines various operational tasks,
  allowing for more efficient resource allocation and management. By reducing the
  manual effort required to maintain the infrastructure, Amazon EKS Auto Mode enables
  teams to focus on higher-level strategic initiatives and application development.
  While our previous blog covered the core concepts of Amazon EKS Auto Mode, this
  blog post dives deeper into optimizing Amazon EKS Auto Mode clusters using AWS Graviton
  and Amazon EC2 Spot instances. AWS customers adopt AWS Graviton instances to achieve
  up to 40% higher price-performance ratio and up to 60% less energy to meet their
  sustainability goals. Additionally, AWS customers use Amazon EC2 Spot instances
  for eligible workloads to save up to 90% on Amazon Elastic Compute Cloud (Amazon
  EC2) On-Demand costs. We will cover AWS Graviton and Amazon EC2 Spot implementations
  on Amazon EKS Auto Mode through the following two scenarios: Deploy the retail store
  application (referenced in the previous blog) using exclusively AWS Graviton (ARM64)
  instances. Deploy the retail store application using a mix of Spot and On-Demand
  Amazon EC2 instances with the following considerations: Self-managed MySQL, a stateful
  application using persistent volumes, must run on On-Demand instances as it’s not
  suitable for Spot instances. While running a Relational Database Management System
  (RDBMS) in Kubernetes is not recommended, we’re using it here solely to demonstrate
  a stateful workload example. All other applications in the retail store application
  are eligible to run on Amazon EC2 Spot instances. All the applications in the retail
  store application can run on AMD64, ARM64, or a mix of both architectures. Self-managed
  MySQL, a stateful application using persistent volumes, must run on On-Demand instances
  as it’s not suitable for Spot instances.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/maximize-amazon-eks-efficiency-how-auto-mode-graviton-and-spot-work-together/
