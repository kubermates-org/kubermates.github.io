---
title: 'Scaling beyond IPv4: integrating IPv6 Amazon EKS clusters into existing Istio
  Service Mesh'
date: '2025-07-22T18:54:25+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/scaling-beyond-ipv4-integrating-ipv6-amazon-eks-clusters-into-existing-istio-service-mesh/
post_kind: link
draft: false
tldr: 'Scaling beyond IPv4: integrating IPv6 Amazon EKS clusters into existing Istio
  Service Mesh Amazon EKS IPv6 interoperability with IPv4 in Istio Service Mesh Solution
  overview Istio Multi-Primary Multicluster deployment model on a single network Istio
  Multi-Primary Multicluster deployment model on multi-network Walkthrough Initial
  setup Conclusion About the authors Organizations are increasingly adopting IPv6
  for their Amazon Elastic Kubernetes Service (Amazon EKS) deployments, driven by
  three key factors: depletion of private IPv4 addresses, the need to streamline or
  eliminate overlay networks, and improved network security requirements on Amazon
  Web Services (AWS). In IPv6-enabled EKS clusters, each pod receives a unique IPv6
  address from the Amazon Virtual Private Cloud (Amazon VPC) IPv6 range, with seamless
  compatibility facilitated by the Amazon EKS VPC Container Network Interface (CNI).'
summary: 'Scaling beyond IPv4: integrating IPv6 Amazon EKS clusters into existing
  Istio Service Mesh Amazon EKS IPv6 interoperability with IPv4 in Istio Service Mesh
  Solution overview Istio Multi-Primary Multicluster deployment model on a single
  network Istio Multi-Primary Multicluster deployment model on multi-network Walkthrough
  Initial setup Conclusion About the authors Organizations are increasingly adopting
  IPv6 for their Amazon Elastic Kubernetes Service (Amazon EKS) deployments, driven
  by three key factors: depletion of private IPv4 addresses, the need to streamline
  or eliminate overlay networks, and improved network security requirements on Amazon
  Web Services (AWS). In IPv6-enabled EKS clusters, each pod receives a unique IPv6
  address from the Amazon Virtual Private Cloud (Amazon VPC) IPv6 range, with seamless
  compatibility facilitated by the Amazon EKS VPC Container Network Interface (CNI).
  This solution effectively addresses two major IPv4 limitations: the scarcity of
  private addresses and the security vulnerabilities created by overlapping IPv4 spaces
  that need Network Address Translation (NAT) at the node level. When transitioning
  to IPv6, you likely need to run both IPv4 and IPv6 EKS clusters simultaneously.
  This is particularly important for organizations using Istio Service Mesh with Amazon
  EKS, because IPv6 clusters must integrate with the existing Service Mesh and work
  smoothly alongside IPv4 clusters. To streamline this transition, you can configure
  your Istio Service Mesh to support both your current IPv4 EKS clusters and your
  new IPv6 EKS clusters. If Istio Service Mesh isn’t part of your infrastructure,
  then we suggest exploring Amazon VPC Lattice as an alternative solution to speed
  up your IPv6 implementation on AWS. This post provides a step-by-step guide for
  combining IPv6-enabled EKS clusters with your existing Istio Service Mesh and IPv4
  workloads, enabling a graceful transition to IPv6 on AWS. This guide covers detailed
  instructions for enabling communication between IPv6 and IPv4 EKS clusters, along
  with recommended practices for implementing IPv6 across both single and multiple
  VPC configurations. The functionality of Amazon EKS IPv6 builds on the native dual-stack
  capabilities of VPC. When you enable IPv6 in your VPC, it receives both IPv4 prefixes
  and a /56 IPv6 prefix. This IPv6 prefix can come from three sources: Amazon’s Global
  Unicast Address (GUA) space, your own IPv6 range (BYOIPv6), or a Unique Local Address
  (ULA) space.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/scaling-beyond-ipv4-integrating-ipv6-amazon-eks-clusters-into-existing-istio-service-mesh/
