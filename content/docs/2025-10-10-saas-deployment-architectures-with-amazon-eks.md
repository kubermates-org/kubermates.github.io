---
title: SaaS deployment architectures with Amazon EKS
date: '2025-10-10T21:13:56+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/saas-deployment-architectures-with-amazon-eks/
post_kind: link
draft: false
tldr: SaaS deployment architectures with Amazon EKS Patterns for managing remote environment
  with Amazon EKS in its core Shared responsibility Building distributed SaaS on Kubernetes
  Application packaging and deployment SaaS Provider Hosted Remote Application Plane
  Customer Hosted Data Plane with EKS Hybrid Nodes Conclusion About the authors As
  companies scale their software as a service (SaaS) offerings, they’re expanding
  their market reach by offering flexible deployment options directly within their
  customers’ environments. This versatile deployment model enables organizations to
  maintain data sovereignty, meet compliance standards, achieve optimal performance
  through reduced latency, and maximize efficiency by running applications close to
  existing customer datasets.
summary: 'SaaS deployment architectures with Amazon EKS Patterns for managing remote
  environment with Amazon EKS in its core Shared responsibility Building distributed
  SaaS on Kubernetes Application packaging and deployment SaaS Provider Hosted Remote
  Application Plane Customer Hosted Data Plane with EKS Hybrid Nodes Conclusion About
  the authors As companies scale their software as a service (SaaS) offerings, they’re
  expanding their market reach by offering flexible deployment options directly within
  their customers’ environments. This versatile deployment model enables organizations
  to maintain data sovereignty, meet compliance standards, achieve optimal performance
  through reduced latency, and maximize efficiency by running applications close to
  existing customer datasets. SaaS providers can embrace this approach to serve a
  broader range of industries and unlock new business opportunities, particularly
  in highly regulated sectors and performance-sensitive markets. This method of extending
  the deployment environments into the tenant’s owned environments has been labelled
  “SaaS Anywhere” in this post. Although SaaS Anywhere solves important challenges
  related to managing remote customers’ environments, they introduce significant complexity
  in management and operation. SaaS providers must develop robust systems for provisioning
  and maintaining their application stack across numerous customer environments, implement
  cross-account monitoring solutions, manage distributed lifecycle updates, and provide
  consistent security controls. All of this is done while maintaining operational
  excellence at scale. In this post we explore patterns and practices for building
  and operating these distributed Amazon Elastic Kubernetes Service (Amazon EKS )-based
  applications effectively. When designing SaaS solutions, organizations typically
  employ one of three deployment models, each offering distinct advantages for specific
  use cases: SaaS Provider Hosted : Both data and control planes reside in the provider’s
  Amazon Web Services (AWS) account, optimizing for operational efficiency and rapid
  customer onboarding. Although lightweight agents may exist in customer environments
  for telemetry, all core processing remains provider hosted. Remote Application Plane
  : The data plane runs in the customer’s environment while the control plane stays
  in the provider’s account. This model balances compliance needs with operational
  efficiency, allowing customers to maintain data sovereignty while using AWS services.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/saas-deployment-architectures-with-amazon-eks/
