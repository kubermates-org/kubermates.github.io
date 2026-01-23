---
title: Simplify Kubernetes cluster management using ACK, kro and Amazon EKS
date: '2026-01-22T17:22:28+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/simplify-kubernetes-cluster-management-using-ack-kro-and-amazon-eks/
post_kind: link
draft: false
tldr: Simplify Kubernetes cluster management using ACK, kro and Amazon EKS Solution
  overview Creating ResourceGraphDefinitions that encapsulate AWS resources to create
  EKS clusters. Using CEL expressions to extract generated fields Creating cross-account
  AWS resources using ACK Bootstrapping workload cluster with add-ons Granting IAM
  permissions to add-ons Putting It All Together Source code Conclusion About the
  authors As organizations expand their adoption of Kubernetes for a growing number
  of use cases, so does the number of operational processes that are related to the
  provisioning and operations of the Kubernetes clusters.
summary: 'Simplify Kubernetes cluster management using ACK, kro and Amazon EKS Solution
  overview Creating ResourceGraphDefinitions that encapsulate AWS resources to create
  EKS clusters. Using CEL expressions to extract generated fields Creating cross-account
  AWS resources using ACK Bootstrapping workload cluster with add-ons Granting IAM
  permissions to add-ons Putting It All Together Source code Conclusion About the
  authors As organizations expand their adoption of Kubernetes for a growing number
  of use cases, so does the number of operational processes that are related to the
  provisioning and operations of the Kubernetes clusters. The process of creating
  a cluster, bootstrapping it with the organization-specific add-ons, and then managing
  it over time is complex and error-prone. Typically, these tasks involve using a
  mixture of disjointed Infrastructure as Code (IaC) pipelines, Kubernetes manifests,
  and Helm charts, which usually leads to extended time for creating new clusters,
  increased operational overhead to manage clusters, and higher risk of failure or
  downtime. In this blog post, we show how to create and manage a fleet of Amazon
  Elastic Kubernetes Service (Amazon EKS) clusters using Kube Resource Orchestrator
  (kro) , AWS Controllers for Kubernetes (ACK) , and Argo CD. These tools allow you
  to implement a GitOps-based cluster management solution to increase productivity
  and improve consistency and standardization by using the Kubernetes API for end-to-end
  operations. ACK is a tool that lets you manage AWS resources directly from Kubernetes
  using familiar declarative YAML constructs – it is a collection of Kubernetes custom
  resource definitions (CRDs) and custom controllers working together to extend the
  Kubernetes API and manage AWS resources on your behalf. Once an ACK service controller
  is installed, a Kubernetes user may create a Custom Resource (CR) corresponding
  to one of the resources exposed by the controller for creating an AWS resource.
  In the solution depicted in this blog post, we use ACK controllers to create the
  AWS resources needed for an EKS cluster. By doing that, we enable cluster management
  through the Kubernetes API and eliminate the need to use a separate IaC tool and
  build a separate pipeline for this use case. Additionally, this approach allows
  to build a GitOps flow for cluster management using tools like Argo CD. That said,
  there are several challenges involved in this approach: To create an EKS cluster,
  you need to provision several AWS resources, including a virtual private cloud (VPC),
  subnets, route tables, NAT gateways, a cluster IAM role, a node IAM role, and the
  EKS cluster itself.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/simplify-kubernetes-cluster-management-using-ack-kro-and-amazon-eks/
