---
title: Deep dive into cluster networking for Amazon EKS Hybrid Nodes
date: '2025-07-21T22:22:52+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/deep-dive-into-cluster-networking-for-amazon-eks-hybrid-nodes/
post_kind: link
draft: false
tldr: Deep dive into cluster networking for Amazon EKS Hybrid Nodes Architecture overview
  CNI considerations Load balancing considerations Prerequisites Walkthrough BGP routing
  (Cilium example) Static routing (Calico example) On-premises load balancer (MetalLB
  example) External load balancer (AWS Load Balancer Controller example) Cleaning
  up Conclusion About the author Amazon Elastic Kubernetes Service ( Amazon EKS )
  Hybrid Nodes enables organizations to integrate their existing on-premises and edge
  computing infrastructure into EKS clusters as remote nodes. EKS Hybrid Nodes provides
  you with the flexibility to run your containerized applications wherever needed,
  while maintaining standardized Kubernetes management practices and addressing latency,
  compliance, and data residency needs.
summary: Deep dive into cluster networking for Amazon EKS Hybrid Nodes Architecture
  overview CNI considerations Load balancing considerations Prerequisites Walkthrough
  BGP routing (Cilium example) Static routing (Calico example) On-premises load balancer
  (MetalLB example) External load balancer (AWS Load Balancer Controller example)
  Cleaning up Conclusion About the author Amazon Elastic Kubernetes Service ( Amazon
  EKS ) Hybrid Nodes enables organizations to integrate their existing on-premises
  and edge computing infrastructure into EKS clusters as remote nodes. EKS Hybrid
  Nodes provides you with the flexibility to run your containerized applications wherever
  needed, while maintaining standardized Kubernetes management practices and addressing
  latency, compliance, and data residency needs. EKS Hybrid Nodes accelerates infrastructure
  modernization by repurposing existing hardware investments. Organizations can harness
  the elastic scalability, high availability, and fully managed advantages of Amazon
  EKS, while making sure of operational consistency through unified workflows and
  toolsets across hybrid environments. One of the key aspects of the EKS Hybrid Nodes
  solution is the hybrid network architecture between the cloud-based Amazon EKS control
  plane and your on-premises nodes. This post dives deep into the cluster networking
  configurations, guiding you through the process of integrating an EKS cluster with
  hybrid nodes in your existing infrastructure. In this walkthrough, we set up different
  Container Network Interface (CNI) options and load balancing solutions on EKS Hybrid
  Nodes to meet your networking requirements. EKS Hybrid Nodes needs private network
  connectivity between the cloud-hosted Amazon EKS control plane and the hybrid nodes
  running in your on-premises environment. This connectivity can be established using
  either Amazon Web Services (AWS) Direct Connect or AWS Site-to-Site VPN , through
  an AWS Transit Gateway or the Virtual Private Gateway into your Amazon Virtual Private
  Cloud (Amazon VPC). For an optimal experience, AWS recommends reliable network connectivity
  with at least 100 Mbps bandwidth, and a maximum of 200ms round-trip latency, for
  hybrid nodes connecting to the AWS Region. This is general guidance rather than
  a strict requirement, and specific bandwidth and latency requirements may differ
  based on the quantity of hybrid nodes and your application’s unique characteristics.
  The node and pod Classless Inter-Domain Routing (CIDR) blocks for your hybrid nodes
  and container workloads must be within the IPv4 RFC-1918 ranges.
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/deep-dive-into-cluster-networking-for-amazon-eks-hybrid-nodes/
