---
title: 'Amazon EKS Blueprints for CDK: Now supporting Amazon EKS Auto Mode'
date: '2025-11-26T22:28:12+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/amazon-eks-blueprints-for-cdk-now-supporting-amazon-eks-auto-mode/
post_kind: link
draft: false
tldr: 'Amazon EKS Blueprints for CDK: Now supporting Amazon EKS Auto Mode What is
  EKS Blueprints for CDK? What is EKS Auto Mode? Prerequisites Implementing EKS Auto
  Mode with EKS Blueprints for CDK Pattern 1: Basic EKS Auto Mode cluster Pattern
  2: EKS Auto Mode cluster with custom ARM NodePool for workloads Pattern 3: EKS Auto
  Mode cluster with custom AI Accelerator NodePool for AI/ML workloads Cleaning up
  Benefits of using EKS Auto Mode with EKS Blueprints Conclusion About the authors
  Amazon EKS Blueprints for CDK has recently added support for EKS Auto Mode , a significant
  enhancement that streamlines Kubernetes management by automatically provisioning
  infrastructure, choosing optimal compute instances, dynamically scaling resources,
  continuously optimizing costs, managing core add-ons, patching operating systems,
  and integrating with Amazon Web Services (AWS) security services. EKS Blueprints
  for CDK is an open source framework that helps AWS customers bootstrap and configure
  production-ready Amazon Elastic Kubernetes Service (Amazon EKS) clusters with the
  AWS Cloud Development Kit (AWS CDK).'
summary: 'Amazon EKS Blueprints for CDK: Now supporting Amazon EKS Auto Mode What
  is EKS Blueprints for CDK? What is EKS Auto Mode? Prerequisites Implementing EKS
  Auto Mode with EKS Blueprints for CDK Pattern 1: Basic EKS Auto Mode cluster Pattern
  2: EKS Auto Mode cluster with custom ARM NodePool for workloads Pattern 3: EKS Auto
  Mode cluster with custom AI Accelerator NodePool for AI/ML workloads Cleaning up
  Benefits of using EKS Auto Mode with EKS Blueprints Conclusion About the authors
  Amazon EKS Blueprints for CDK has recently added support for EKS Auto Mode , a significant
  enhancement that streamlines Kubernetes management by automatically provisioning
  infrastructure, choosing optimal compute instances, dynamically scaling resources,
  continuously optimizing costs, managing core add-ons, patching operating systems,
  and integrating with Amazon Web Services (AWS) security services. EKS Blueprints
  for CDK is an open source framework that helps AWS customers bootstrap and configure
  production-ready Amazon Elastic Kubernetes Service (Amazon EKS) clusters with the
  AWS Cloud Development Kit (AWS CDK). Customers can describe the desired state of
  their Amazon EKS environment with worker nodes, auto scaling, networking, and Kubernetes
  add-ons as an infrastructure as code (IaC) blueprint. These blueprints can be used
  in pipelines to set up consistent environments across AWS accounts and AWS Regions.
  EKS Blueprints is part of the broader initiative by AWS launched in 2022: Bootstrapping
  clusters with EKS Blueprints | Amazon Web Services. EKS Blueprints can bootstrap
  your clusters with Amazon EKS add-ons, and many popular open source add-ons, such
  as ArgoCD, Nginx, Keda, Fluent Bit, FluxCD, and more. The framework automatically
  chooses compatible versions for core Amazon EKS add-ons based on your Kubernetes
  version, eliminating the guesswork of which add-on versions work together. When
  you upgrade your cluster, the add-on versions automatically update to maintain compatibility,
  preventing version mismatch errors. EKS Blueprints comes with built-in compatibility
  handling for your add-ons, so that each add-on you deploy is compatible with your
  cluster’s configuration. Feedback and support for this framework is available through
  GitHub issues. EKS Blueprints provides specialized cluster builders that come pre-configured
  with the right add-ons and best practices for specific workloads. Whether you’re
  building observability stacks with Prometheus and Grafana, GPU clusters for machine
  learning (ML), Windows environments for.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/amazon-eks-blueprints-for-cdk-now-supporting-amazon-eks-auto-mode/
