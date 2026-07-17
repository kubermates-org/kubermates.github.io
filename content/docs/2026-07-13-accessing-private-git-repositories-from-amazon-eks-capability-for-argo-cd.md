---
title: Accessing private Git repositories from Amazon EKS capability for Argo CD
date: '2026-07-13T16:46:33+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/accessing-private-git-repositories-from-amazon-eks-capability-for-argo-cd/
post_kind: link
draft: false
tldr: Accessing private Git repositories from Amazon EKS capability for Argo CD Architecture
  overview Solution walkthrough Prerequisites Connect private Git server with AWS
  CodeConnections Create a sample Argo CD application Under the hood Clean up Conclusion
  About the authors Organizations adopting GitOps on Amazon Elastic Kubernetes Service
  (Amazon EKS) often need to pull application manifests from private Git repositories
  that are not publicly accessible. Amazon EKS capability for Argo CD (referred to
  as ‘Argo CD capability’ throughout this post) can access publicly hosted Git repositories
  using Argo CD repository secrets.
summary: 'Accessing private Git repositories from Amazon EKS capability for Argo CD
  Architecture overview Solution walkthrough Prerequisites Connect private Git server
  with AWS CodeConnections Create a sample Argo CD application Under the hood Clean
  up Conclusion About the authors Organizations adopting GitOps on Amazon Elastic
  Kubernetes Service (Amazon EKS) often need to pull application manifests from private
  Git repositories that are not publicly accessible. Amazon EKS capability for Argo
  CD (referred to as ‘Argo CD capability’ throughout this post) can access publicly
  hosted Git repositories using Argo CD repository secrets. However, connecting Argo
  CD capability to private Git repositories presents challenges, because the capability
  cannot directly access repositories that are not publicly accessible. The Argo CD
  capability doesn’t have direct access to the customer’s Amazon Virtual Private Cloud
  (VPC) network, so it can’t reach privately hosted Git servers. When you want to
  securely connect Argo CD capability to private repositories within your VPC, AWS
  CodeConnections provides authentication based on AWS Identity and Access Management
  (IAM) while maintaining your security posture. In this post, we walk you through
  three main steps: First, you create an AWS CodeConnections host in your VPC with
  connectivity to your private Git server. Second, you establish a connection that
  Argo CD can use. Finally, you deploy a sample application to verify the integration.
  By the end, you have a secure way to deploy applications from private repositories.
  The architecture diagram illustrates a secure GitOps workflow in which an Amazon
  EKS cluster with Argo CD capability accesses private Git repositories through AWS
  CodeConnections. An AWS CodeConnection is created in a VPC which has private network
  connectivity to an on-premises data center where a private Git server is hosted.
  Argo CD capability uses an IAM role to access the connection, and then pulls the
  latest configurations and synchronizes them to an EKS cluster.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/accessing-private-git-repositories-from-amazon-eks-capability-for-argo-cd/
