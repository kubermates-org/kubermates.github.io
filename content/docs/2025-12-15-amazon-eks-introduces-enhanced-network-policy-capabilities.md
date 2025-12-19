---
title: Amazon EKS introduces enhanced network policy capabilities
date: '2025-12-15T22:25:17+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/amazon-eks-introduces-enhanced-network-policy-capabilities/
post_kind: link
draft: false
tldr: Amazon EKS introduces enhanced network policy capabilities What are Admin Network
  Policies? Admin Policy examples What are Application Network Policies? How are Application
  Network Policies different from regular Network Policies? Application Network Policy
  example Conclusion About the authors Today, we are excited to announce the expansion
  of native network policy support in Amazon EKS to include both Admin Policies and
  Application Network Policies. With these additional policies, Cluster Administrators
  (e.
summary: Amazon EKS introduces enhanced network policy capabilities What are Admin
  Network Policies? Admin Policy examples What are Application Network Policies? How
  are Application Network Policies different from regular Network Policies? Application
  Network Policy example Conclusion About the authors Today, we are excited to announce
  the expansion of native network policy support in Amazon EKS to include both Admin
  Policies and Application Network Policies. With these additional policies, Cluster
  Administrators (e. g. platform or security teams) can set cluster-wide security
  rules for their clusters to enhance the overall network security for their Kubernetes
  workloads. In addition, Namespace Administrators (e. g. application teams) can now
  control pod traffic to external resources using domain names as filters. This approach
  replaces the need to maintain lists of specific IP addresses (which frequently change)
  or broad CIDR ranges (which often conflict with corporate security policies), instead
  enabling the creation of a trusted list of external website and services that pods
  are allowed to access. You can think of this as a “permitted destinations” list
  for your cluster’s outbound traffic. Standard Kubernetes Network Policies in a cluster
  allow you to implement a virtual firewall, segmenting network traffic inside a cluster.
  These policies let you create rules that govern both incoming (ingress) and outgoing
  (egress) traffic. You can restrict communication based on several parameters, including
  pod labels, namespaces, IP ranges (CIDR), and specific ports.
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/amazon-eks-introduces-enhanced-network-policy-capabilities/
