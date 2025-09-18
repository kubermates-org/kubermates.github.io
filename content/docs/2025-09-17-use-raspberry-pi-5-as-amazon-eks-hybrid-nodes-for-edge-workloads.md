---
title: Use Raspberry Pi 5 as Amazon EKS Hybrid Nodes for edge workloads
date: '2025-09-17T15:08:59+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/use-raspberry-pi-5-as-amazon-eks-hybrid-nodes-for-edge-workloads/
post_kind: link
draft: false
tldr: 'Use Raspberry Pi 5 as Amazon EKS Hybrid Nodes for edge workloads Why Raspberry
  Pi 5? Architectural overview Getting started Step 1: Create the EKS cluster Step
  2: Set up the VPN server Add the Raspberry Pi to the cluster as a remote node Setting
  up the Container Network Interface Step 1: Install Cilium Deploying a sample application
  on Amazon EKS Hybrid Nodes with edge integration Step 1: Hardware requirements and
  setup Step 2: Deploy the DynamoDB table Step 3: Deploy the sensor application Step
  4: Deploy the frontend dashboard Conclusion About the authors Since its launch,
  Amazon Elastic Kubernetes Service (Amazon EKS) has powered tens of millions of clusters
  so that users can accelerate application deployment, optimize costs, and use the
  flexibility of Amazon Web Services (AWS) for hosting containerized applications.
  Amazon EKS eliminates the operational complexities of maintaining Kubernetes control
  plane infrastructure, while offering seamless integration with AWS resources and
  infrastructure.'
summary: 'Use Raspberry Pi 5 as Amazon EKS Hybrid Nodes for edge workloads Why Raspberry
  Pi 5? Architectural overview Getting started Step 1: Create the EKS cluster Step
  2: Set up the VPN server Add the Raspberry Pi to the cluster as a remote node Setting
  up the Container Network Interface Step 1: Install Cilium Deploying a sample application
  on Amazon EKS Hybrid Nodes with edge integration Step 1: Hardware requirements and
  setup Step 2: Deploy the DynamoDB table Step 3: Deploy the sensor application Step
  4: Deploy the frontend dashboard Conclusion About the authors Since its launch,
  Amazon Elastic Kubernetes Service (Amazon EKS) has powered tens of millions of clusters
  so that users can accelerate application deployment, optimize costs, and use the
  flexibility of Amazon Web Services (AWS) for hosting containerized applications.
  Amazon EKS eliminates the operational complexities of maintaining Kubernetes control
  plane infrastructure, while offering seamless integration with AWS resources and
  infrastructure. However, some workloads need to be run at the edge with real-time
  processing, such as latency-sensitive applications that generate large volumes of
  data. In these scenarios, when there is consistent internet connectivity available,
  users often seek the benefits of cloud integrations while continuing to use their
  on-premises hardware. That’s why we introduced Amazon EKS Hybrid Nodes at AWS re:Invent
  2024, so that users can extend their Kubernetes data plane to the edge while continuing
  to run the Kubernetes control plane in an AWS Region. Amazon EKS Hybrid Nodes unifies
  Kubernetes management across cloud, on-premises, and edge environments by enabling
  users to use their on-premises infrastructure as nodes in EKS clusters, alongside
  Amazon Elastic Compute Cloud (Amazon EC2). To demonstrate the use of Amazon EKS
  Hybrid Nodes, we explored a practical use case from the manufacturing sector. These
  environments often rely on real-time data from digital sensors that must be processed
  locally due to latency and reliability, while still using the cloud for analytics
  and long-term storage. Our use case involves reading distance values from an ultrasonic
  sensor, processing them on a local edge device running as a Hybrid Node, and storing
  them in Amazon DynamoDB on AWS. In this post, we demonstrate how to implement Amazon
  EKS Hybrid Nodes using the Raspberry Pi 5 , a popular edge computing platform. We
  cover the following: Setting up an EKS cluster that seamlessly connects cloud and
  edge infrastructure Securing connectivity using the WireGuard VPN for site-to-site
  communication Enabling container networking with Cilium for hybrid node deployments
  Demonstrating a real-world Internet of Things (IoT) application that demonstrates
  the power of edge-cloud integration The Raspberry Pi 5 is compact and can be deployed
  at the edge so that you can process data before it is transmitted to the cloud.
  Building on this strength, we created a microservices-based application partly running
  on the edge on a Raspberry Pi 5 and partly on AWS in the cloud.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/use-raspberry-pi-5-as-amazon-eks-hybrid-nodes-for-edge-workloads/
