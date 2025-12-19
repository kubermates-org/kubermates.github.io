---
title: 'Deep dive: Streamlining GitOps with Amazon EKS capability for Argo CD'
date: '2025-12-18T17:27:31+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/deep-dive-streamlining-gitops-with-amazon-eks-capability-for-argo-cd/
post_kind: link
draft: false
tldr: 'Deep dive: Streamlining GitOps with Amazon EKS capability for Argo CD Architecture
  overview: Hub-and-Spoke topology Prerequisites Solution Walkthrough Configure AWS
  IAM Identity Center Create hub cluster with Argo CD Capability Create spoke clusters
  Register clusters with Argo CD Configure Git sources Native ECR integration Implement
  multi-tenancy with projects Scale deployments with ApplicationSets CI/CD pipeline
  integration Operational visibility Clean up Conclusion About the authors Organizations
  use GitOps as the standard for managing Kubernetes deployments at scale. Running
  Argo CD in production means managing high availability, upgrades, Single Sign-On
  (SSO) configuration, and cross-cluster connectivity.'
summary: 'Deep dive: Streamlining GitOps with Amazon EKS capability for Argo CD Architecture
  overview: Hub-and-Spoke topology Prerequisites Solution Walkthrough Configure AWS
  IAM Identity Center Create hub cluster with Argo CD Capability Create spoke clusters
  Register clusters with Argo CD Configure Git sources Native ECR integration Implement
  multi-tenancy with projects Scale deployments with ApplicationSets CI/CD pipeline
  integration Operational visibility Clean up Conclusion About the authors Organizations
  use GitOps as the standard for managing Kubernetes deployments at scale. Running
  Argo CD in production means managing high availability, upgrades, Single Sign-On
  (SSO) configuration, and cross-cluster connectivity. This operational scope grows
  with each additional cluster across regions or AWS accounts. Amazon Elastic Kubernetes
  Service (EKS) Capability for Argo CD – referred to as “Argo CD Capability” in the
  remainder of this blog post – is part of the newly launched Amazon EKS Capabilities
  feature. It provides a fully managed GitOps continuous deployment solution that
  eliminates the operational overhead of running Argo CD on your clusters. The capability
  runs in AWS managed service accounts outside of your clusters, with AWS handling
  scaling, upgrades, inter-cluster communications, and offering native integrations
  with other AWS services such as AWS Secret Manager , Amazon Elastic Container Registry
  (ECR) , AWS CodeCommit and AWS CodeConnections. In this deep dive, we explore advanced
  scenarios with Argo CD including hub-and-spoke multi-cluster deployments, native
  AWS service integrations, multi-tenancy implementation, scaling with advanced Argo
  CD configurations and integration with CI/CD pipeline. For a detailed comparison
  with self-managed solutions, see Comparing EKS Capability for Argo CD to self-managed
  Argo CD. In a hub-and-spoke architecture, the Argo CD Capability is created on a
  dedicated central EKS cluster (the hub) that serves as the control plane for GitOps
  operations, and it is not created on the spoke clusters. Although Argo CD in the
  central hub cluster can technically manage and deploy applications to both the hub
  and the spoke clusters, in this blog the hub cluster is designed exclusively for
  management tasks and does not host any business workloads. “Figure 1: Sample topology
  of hub-and-spoke model for Argo CD Capability” This topology provides platform teams
  with a single pane of glass to orchestrate deployments across an entire fleet of
  clusters—whether they’re in different regions, accounts, or have private Kubernetes
  API endpoints. Before you begin, verify that you have the following tools and configurations
  in place.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/deep-dive-streamlining-gitops-with-amazon-eks-capability-for-argo-cd/
