---
title: Implementing granular failover in multi-Region Amazon EKS
date: '2025-09-18T14:13:01+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/implementing-granular-failover-in-multi-region-amazon-eks/
post_kind: link
draft: false
tldr: Implementing granular failover in multi-Region Amazon EKS Typical architecture
  The all-or-nothing health check problem Solution overview Prerequisites Walkthrough
  Configure environment variables Create EKS clusters in Region 1 and Region 2 Create
  IngressClass configuration Deploy app1 and app2 on the EKS clusters Configure Route
  53 health checks for app1 and app2 Configure Route 53 alias records for app1 and
  app2 Test application failure Things to know Cleaning up Conclusion About the authors
  Enterprises across industries operate tens of millions of Amazon Elastic Kubernetes
  Service (Amazon EKS) clusters annually, supporting use cases from web/mobile applications
  to data processing, machine learning (ML), generative AI, gaming, and Internet of
  Things (IoT). As organizations increasingly adopt multi-tenant platform models where
  multiple application teams share an EKS cluster, they need more granular control
  over application availability in their multi-Region architectures—particularly for
  serving global users and meeting strict regulatory requirements.
summary: 'Implementing granular failover in multi-Region Amazon EKS Typical architecture
  The all-or-nothing health check problem Solution overview Prerequisites Walkthrough
  Configure environment variables Create EKS clusters in Region 1 and Region 2 Create
  IngressClass configuration Deploy app1 and app2 on the EKS clusters Configure Route
  53 health checks for app1 and app2 Configure Route 53 alias records for app1 and
  app2 Test application failure Things to know Cleaning up Conclusion About the authors
  Enterprises across industries operate tens of millions of Amazon Elastic Kubernetes
  Service (Amazon EKS) clusters annually, supporting use cases from web/mobile applications
  to data processing, machine learning (ML), generative AI, gaming, and Internet of
  Things (IoT). As organizations increasingly adopt multi-tenant platform models where
  multiple application teams share an EKS cluster, they need more granular control
  over application availability in their multi-Region architectures—particularly for
  serving global users and meeting strict regulatory requirements. Although multi-tenant
  models optimize resource usage and reduce operational overhead, they present challenges
  when applications need individualized Recovery Point Objective (RPO) and Recovery
  Time Objective (RTO) targets across multiple AWS Regions. Traditional approaches
  force uniform failover policies across all applications where a single application’s
  failure creates an unnecessary compromise between operational efficiency and application-specific
  resilience. In this post, we demonstrate how to configure Amazon Route 53 to enable
  unique failover behavior for each application within your multi-tenant Amazon EKS
  environment across AWS Regions, which allows you to maintain the cost benefits of
  shared infrastructure while meeting diverse availability requirements. Before diving
  into the solution, we demonstrate how a typical multi-Region multi-tenant Amazon
  EKS architecture is structured, and the key components that enable Regional traffic
  routing. Figure 1 consists of the following key components: Route 53 Routes traffic
  to the Application Load Balancer (ALB) in the respective Region Makes sure of high
  availability and resiliency during failure events Routes traffic to the Application
  Load Balancer (ALB) in the respective Region Makes sure of high availability and
  resiliency during failure events AWS Load Balancer Controller Exposes applications
  running on the EKS cluster through ALB Uses IP target type to register application
  Pods to the ALB Exposes applications running on the EKS cluster through ALB Uses
  IP target type to register application Pods to the ALB The Route 53 configuration
  details are as follows: Regional Routing Each AWS Region uses a Route 53 alias record
  to route traffic to its Region-specific ALB. Example: app1. example. com points
  to ALB in Region 1 Example: app2. example. com points to ALB in Region 2 Each AWS
  Region uses a Route 53 alias record to route traffic to its Region-specific ALB.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/implementing-granular-failover-in-multi-region-amazon-eks/
