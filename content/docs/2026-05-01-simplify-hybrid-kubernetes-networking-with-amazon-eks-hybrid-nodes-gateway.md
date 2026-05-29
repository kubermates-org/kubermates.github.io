---
title: Simplify hybrid Kubernetes networking with Amazon EKS Hybrid Nodes gateway
date: '2026-05-01T15:53:15+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/simplify-hybrid-kubernetes-networking-with-amazon-eks-hybrid-nodes-gateway/
post_kind: link
draft: false
tldr: Simplify hybrid Kubernetes networking with Amazon EKS Hybrid Nodes gateway Overview
  Architecture Prerequisites Walkthrough Creating an EKS cluster enabled with EKS
  Auto Mode and EKS Hybrid Nodes Prepare hybrid nodes Install Cilium CNI Prepare hybrid
  nodes gateway installation Install EKS Hybrid Nodes gateway Testing Cross-environment
  pod-to-pod test VPC-to-hybrid pod test Failover test Cleaning up Additional considerations
  Conclusion About the authors Organizations are increasingly adopting Amazon Elastic
  Kubernetes Service (Amazon EKS) and Amazon EKS Hybrid Nodes as they migrate and
  modernize applications across cloud and on-premises environments. Amazon EKS Hybrid
  Nodes enables users to integrate their on-premises and edge computing infrastructure
  with EKS clusters as remote nodes.
summary: 'Simplify hybrid Kubernetes networking with Amazon EKS Hybrid Nodes gateway
  Overview Architecture Prerequisites Walkthrough Creating an EKS cluster enabled
  with EKS Auto Mode and EKS Hybrid Nodes Prepare hybrid nodes Install Cilium CNI
  Prepare hybrid nodes gateway installation Install EKS Hybrid Nodes gateway Testing
  Cross-environment pod-to-pod test VPC-to-hybrid pod test Failover test Cleaning
  up Additional considerations Conclusion About the authors Organizations are increasingly
  adopting Amazon Elastic Kubernetes Service (Amazon EKS) and Amazon EKS Hybrid Nodes
  as they migrate and modernize applications across cloud and on-premises environments.
  Amazon EKS Hybrid Nodes enables users to integrate their on-premises and edge computing
  infrastructure with EKS clusters as remote nodes. This creates a unified Kubernetes
  management experience across distributed environments while addressing latency,
  compliance, and data residency requirements. However, managing hybrid Kubernetes
  networking between the Amazon Virtual Private Cloud (Amazon VPC) and on-premises
  nodes can be challenging, often requiring network changes and coordination between
  Kubernetes platform teams and network infrastructure teams. A common architecture
  requirement for EKS Hybrid Nodes is to make on-premises pod networks routable across
  hybrid networks, which some customers cannot achieve due to constraints like overlapping
  IP addresses or complex BGP routing requirements. We are excited to announce the
  general availability of the Amazon EKS Hybrid Nodes gateway , a new feature for
  Amazon EKS that simplifies hybrid Kubernetes networking for Amazon EKS Hybrid Nodes.
  The Amazon EKS Hybrid Nodes gateway automatically manages and forwards pod-to-pod
  traffic between the EKS VPC and on-premises environments, eliminating the need for
  complex networking changes to existing on-premises infrastructure. It also handles
  the control plane to webhook connectivity and allows AWS services such as Application
  Load Balancers , and Amazon Managed Service for Prometheus to seamlessly communicate
  with remote pods running on hybrid nodes. EKS Hybrid Nodes gateway supports a range
  of use cases, including: Cross-environment pod-to-pod networking & cloud migrations:
  Organizations migrating applications to Amazon EKS while maintaining some workloads
  on-premises due to data residency, compliance, or infrastructure requirements. The
  gateway enables seamless pod-to-pod communication between cloud and on-premises
  without requiring network infrastructure changes. Webhook operations: Customers
  running admission controllers and policy enforcement tools (cert-manager, OPA, Kyverno)
  on hybrid nodes. The gateway automatically routes control plane traffic to webhook
  endpoints on hybrid nodes, removing the need to make on-premises pod networks routable.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/simplify-hybrid-kubernetes-networking-with-amazon-eks-hybrid-nodes-gateway/
