---
title: Track inter-AZ and NAT gateway traffic with EKS Container Network Observability
date: '2026-05-05T15:18:25+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/track-inter-az-and-nat-gateway-traffic-with-eks-container-network-observability/
post_kind: link
draft: false
tldr: 'Track inter-AZ and NAT gateway traffic with EKS Container Network Observability
  Container Network Observability in Amazon EKS Prerequisites Use case 1: Identifying
  inter-AZ traffic Handling inter-AZ traffic Traffic Distribution Control Verifying
  hints in EndpointSlices Considerations for Traffic Distribution Control Use case
  2: Identifying NAT gateway processing bytes Identifying NAT gateway traffic using
  the External view Handling NAT gateway traffic Query Network Flow Monitor using
  AWS Command Line Interface Using an AI agent to automate network cost findings Running
  your agent Clean up Conclusion About the authors Teams running microservices on
  Amazon Elastic Kubernetes Service (Amazon EKS) struggle to identify which services
  drive their data transfer costs. As clusters grow and service-to-service communication
  increases, inter-AZ traffic (data transfer between zones within the same region)
  and NAT gateway processing charges add up fast.'
summary: 'Track inter-AZ and NAT gateway traffic with EKS Container Network Observability
  Container Network Observability in Amazon EKS Prerequisites Use case 1: Identifying
  inter-AZ traffic Handling inter-AZ traffic Traffic Distribution Control Verifying
  hints in EndpointSlices Considerations for Traffic Distribution Control Use case
  2: Identifying NAT gateway processing bytes Identifying NAT gateway traffic using
  the External view Handling NAT gateway traffic Query Network Flow Monitor using
  AWS Command Line Interface Using an AI agent to automate network cost findings Running
  your agent Clean up Conclusion About the authors Teams running microservices on
  Amazon Elastic Kubernetes Service (Amazon EKS) struggle to identify which services
  drive their data transfer costs. As clusters grow and service-to-service communication
  increases, inter-AZ traffic (data transfer between zones within the same region)
  and NAT gateway processing charges add up fast. Without pod-level visibility into
  these network flows, it’s difficult to pinpoint which workloads contribute most.
  Architectural decisions such as pod placement, cross-zone communication patterns,
  and NAT gateway routing directly affect your bill in ways that are hard to trace
  and optimize. Container Network Observability in Amazon EKS gives you near-real-time
  visibility into the workloads generating these costs across your cluster. Rather
  than sifting through aggregate billing data after the fact, you can track inter-AZ
  and NAT gateway traffic at the pod-level, right where the spending originates, identifying
  optimization opportunities, prioritizing changes, and validating that adjustments
  are having the intended effect. In this post, you’ll learn how to: (1) enable Container
  Network Observability in your Amazon EKS cluster, (2) identify and reduce inter-AZ
  traffic using traffic distribution control, (3) identify and reduce NAT gateway
  costs by implementing Amazon Virtual Private Cloud (VPC) endpoints, and (4) automate
  monitoring and reporting with an AI agent. This technical guide assumes familiarity
  with Kubernetes concepts and AWS networking basics. Container Network Observability
  in Amazon EKS provides pod-level insights into your cluster network traffic. Network
  Flow Monitor powers these capabilities. Network Flow Monitor is a feature of Amazon
  CloudWatch that offers near-real-time visibility into network performance across
  your AWS compute resources, services, and beyond. With Container Network Observability
  in Amazon EKS, you can identify and analyze inter-AZ and NAT gateway traffic patterns
  within your Amazon EKS clusters.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/track-inter-az-and-nat-gateway-traffic-with-eks-container-network-observability/
