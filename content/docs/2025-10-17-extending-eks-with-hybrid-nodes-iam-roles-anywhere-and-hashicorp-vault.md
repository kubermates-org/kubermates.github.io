---
title: 'Extending EKS with Hybrid Nodes: IAM Roles Anywhere and HashiCorp Vault'
date: '2025-10-17T20:30:49+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/extending-eks-with-hybrid-nodes-iam-roles-anywhere-and-hashicorp-vault/
post_kind: link
draft: false
tldr: 'Extending EKS with Hybrid Nodes: IAM Roles Anywhere and HashiCorp Vault Solution
  overview Prerequisites PKI architecture IAM Roles Anywhere configuration Vault certificate
  management EKS Hybrid Nodes configuration Results Cleanup Conclusion About the author
  Amazon EKS Hybrid Nodes allows businesses to flexibly make use of compute resources
  outside of AWS by extending an Amazon Elastic Kubernetes Service (Amazon EKS) data
  plane beyond the AWS Cloud boundary. Use cases for EKS Hybrid Nodes include businesses
  who have goals or requirements focusing on data sovereignty, low latency communication,
  and government or industry regulations.'
summary: 'Extending EKS with Hybrid Nodes: IAM Roles Anywhere and HashiCorp Vault
  Solution overview Prerequisites PKI architecture IAM Roles Anywhere configuration
  Vault certificate management EKS Hybrid Nodes configuration Results Cleanup Conclusion
  About the author Amazon EKS Hybrid Nodes allows businesses to flexibly make use
  of compute resources outside of AWS by extending an Amazon Elastic Kubernetes Service
  (Amazon EKS) data plane beyond the AWS Cloud boundary. Use cases for EKS Hybrid
  Nodes include businesses who have goals or requirements focusing on data sovereignty,
  low latency communication, and government or industry regulations. In this blog
  post, we’ll explore how to use AWS Identity and Access Management (IAM) Roles Anywhere
  , supported by HashiCorp Vault PKI , to facilitate joining EKS Hybrid Nodes to an
  Amazon EKS Cluster. When a node joins an EKS cluster, it uses metadata from the
  cluster – such as the cluster certificate bundle – to authenticate. Permission to
  retrieve this metadata is granted by IAM via the eks:DescribeCluster operation,
  which can be attached to an IAM Role via an IAM Policy. eks:DescribeCluster Since
  EKS Hybrid Nodes reside outside of AWS, they cannot inherit IAM Policies directly,
  and a different mechanism is required to retrieve the cluster certificate bundle.
  One recommended option is to use AWS Systems Manager (SSM) to provide nodes with
  temporary IAM credentials and permissions, including eks:DescribeCluster. Another
  option to accomplish the same outcome is to make use of an existing Public Key Infrastructure
  (PKI) and AWS IAM Roles Anywhere , which will be the focus of this blog post. eks:DescribeCluster
  IAM Roles Anywhere supports temporary credential validity periods from the default
  value of one hour up to a maximum of twelve hours. For this solution, you should
  have the following prerequisites: An AWS account An Amazon EKS Cluster ( prerequisites
  ) One or more Linux servers that will become EKS Hybrid Nodes ( compatibility )
  A HashiCorp Vault Server or Cluster Figure 1 – Vault PKI Architecture Diagram If
  you’re already using HashiCorp Vault to manage secrets and protect sensitive data,
  then you already have a PKI! Vault natively supports PKI as part of its secrets
  engine. All you must do is to enable it. vault secrets enable pki vault secrets
  enable pki Because you’ll establish a Trust between IAM Roles Anywhere (IAM-RA)
  and the Vault Certificate Authority (CA), it is important to be aware that the default
  Time To Live (TTL) for the Vault CA is 30 days.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/extending-eks-with-hybrid-nodes-iam-roles-anywhere-and-hashicorp-vault/
