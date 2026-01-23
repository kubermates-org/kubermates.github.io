---
title: End-to-end recovery from AZ impairments in Amazon EKS using EKS Zonal shift
  and Istio
date: '2026-01-20T16:11:13+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/end-to-end-recovery-from-az-impairments-in-amazon-eks-using-eks-zonal-shift-and-istio/
post_kind: link
draft: false
tldr: 'End-to-end recovery from AZ impairments in Amazon EKS using EKS Zonal shift
  and Istio Solution overview Prerequisites Walkthrough Create Aurora cluster with
  three reader endpoints, with each one in a different Availability Zone Create a
  three node EKS cluster in three different Availability Zones Deploy Istio Gateway,
  VirtualService, and sample application Zonal traffic shift run-book Restoring normal
  operations after the Availability Zone impairment is resolved Cleaning up Conclusion
  About the authors What happens when one of your Availability Zones (AZs) starts
  behaving badly, but doesn’t completely fail? Picture this: your Amazon Elastic Kubernetes
  Service (Amazon EKS) cluster is humming along across three Availability Zones when
  suddenly, an Availability Zone begins experiencing subtle performance degradation—not
  a complete outage, but enough to frustrate your customers with slower response times
  and intermittent errors. This scenario represents one of the most challenging problems
  in modern cloud architecture: gray failures.'
summary: 'End-to-end recovery from AZ impairments in Amazon EKS using EKS Zonal shift
  and Istio Solution overview Prerequisites Walkthrough Create Aurora cluster with
  three reader endpoints, with each one in a different Availability Zone Create a
  three node EKS cluster in three different Availability Zones Deploy Istio Gateway,
  VirtualService, and sample application Zonal traffic shift run-book Restoring normal
  operations after the Availability Zone impairment is resolved Cleaning up Conclusion
  About the authors What happens when one of your Availability Zones (AZs) starts
  behaving badly, but doesn’t completely fail? Picture this: your Amazon Elastic Kubernetes
  Service (Amazon EKS) cluster is humming along across three Availability Zones when
  suddenly, an Availability Zone begins experiencing subtle performance degradation—not
  a complete outage, but enough to frustrate your customers with slower response times
  and intermittent errors. This scenario represents one of the most challenging problems
  in modern cloud architecture: gray failures. Unlike binary failures, where services
  are clearly up or down, gray failures create a murky middle ground where an Availability
  Zone appears healthy to your monitoring systems but delivers a degraded customer
  experience. Your Kubernetes health checks pass, your pods stay running, but your
  users are quietly suffering. The solution? End-to-end recovery from Availability
  Zone impairments that shift traffic appropriately across all three dimensions of
  your application’s communication patterns. You need to shift the obvious north-south
  traffic coming into your cluster and the east-west service-to-service communication
  within your cluster. Furthermore, you need to shift the often-overlooked outbound
  traffic to external dependencies such as Amazon Relational Database Service (Amazon
  RDS). Here’s where the magic happens: Amazon Application Recovery Controller (ARC)
  zonal shift for a Network Load Balancer (NLB) provides a mechanism to redirect external
  requests away from impaired Availability Zones. Enabling Zonal shift in EKS clusters
  handles your internal east-west Kubernetes traffic, while Istio service mesh extends
  your traffic management capabilities to external services through ServiceEntry resources.
  Together, they create a comprehensive safety net that can gracefully shift traffic
  away from an entire Availability Zone when things go sideways—before customers even
  notice. Effective monitoring is crucial for detecting when an Availability Zone
  is experiencing degradation, particularly for gray failures that don’t trigger standard
  health checks. Organizations can monitor business-critical metrics and establish
  baseline performance expectations to identify subtle degradations and initiate procedures
  to shift traffic away from impaired AZs before customer impact becomes severe.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/end-to-end-recovery-from-az-impairments-in-amazon-eks-using-eks-zonal-shift-and-istio/
