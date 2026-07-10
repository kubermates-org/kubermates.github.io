---
title: Migrate Amazon EC2 to EKS Auto Mode using Kiro CLI and MCP servers
date: '2026-07-09T16:24:54+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/migrate-amazon-ec2-to-eks-auto-mode-using-kiro-cli-and-mcp-servers/
post_kind: link
draft: false
tldr: 'Migrate Amazon EC2 to EKS Auto Mode using Kiro CLI and MCP servers Solution
  overview Architecture overview Integration of the infrastructure stack and Kiro
  Migration guide Prerequisites Preparing for the migration Performing the migration
  Post migration: Monitoring and observability Clean up Step 1: Remove EKS Auto Mode
  resources Step 2: Clean up legacy EC2 infrastructure Conclusion About the authors
  Amazon Elastic Kubernetes Service (Amazon EKS) Auto Mode offers a streamlined path
  forward, handling compute provisioning and autoscaling, node lifecycle, networking,
  cluster DNS, storage, load balancing, and GPU support. Teams interact with familiar
  Kubernetes primitives while EKS Auto Mode manages the underlying infrastructure,
  delivering a Kubernetes-native experience that eliminates operational overhead without
  sacrificing flexibility or control.'
summary: 'Migrate Amazon EC2 to EKS Auto Mode using Kiro CLI and MCP servers Solution
  overview Architecture overview Integration of the infrastructure stack and Kiro
  Migration guide Prerequisites Preparing for the migration Performing the migration
  Post migration: Monitoring and observability Clean up Step 1: Remove EKS Auto Mode
  resources Step 2: Clean up legacy EC2 infrastructure Conclusion About the authors
  Amazon Elastic Kubernetes Service (Amazon EKS) Auto Mode offers a streamlined path
  forward, handling compute provisioning and autoscaling, node lifecycle, networking,
  cluster DNS, storage, load balancing, and GPU support. Teams interact with familiar
  Kubernetes primitives while EKS Auto Mode manages the underlying infrastructure,
  delivering a Kubernetes-native experience that eliminates operational overhead without
  sacrificing flexibility or control. Migrating from Amazon Elastic Compute Cloud
  (Amazon EC2) to a Kubernetes-based architecture requires expertise across containerization,
  networking, and AWS service integration. AWS Model Context Protocol (MCP) Server
  , specialized Amazon EKS MCP Server , AWS Knowledge MCP Server , and Kiro CLI significantly
  reduce this complexity by providing automated workflows for containerization and
  deployment orchestration. Together, these tools help teams accelerate their migration
  timeline, minimize configuration errors, and apply best practices consistently throughout
  the process. In this post, you walk through a practical migration scenario where
  a Node. js web application running on EC2 instances is migrated into a highly scalable,
  containerized service on EKS Auto Mode. You will learn how to configure and use
  the AWS and Amazon EKS MCP Servers with Kiro CLI to automate critical migration
  tasks from Dockerfile creation and image optimization to Kubernetes manifest generation
  and production deployment on EKS Auto Mode. This section covers the initial and
  target architectures, their key components, and how Kiro CLI and MCP servers work
  together to orchestrate a smooth, end-to-end migration from EC2 to EKS Auto Mode.
  The following sections compare the initial EC2 architecture with the target EKS
  Auto Mode architecture. Figure 1: Initial architecture: Node. js application on
  Amazon EC2 behind an Application Load Balancer, with Amazon Cognito for authentication,
  Amazon Simple Storage Service (Amazon S3) for object storage, and Amazon DynamoDB
  for metadata.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/migrate-amazon-ec2-to-eks-auto-mode-using-kiro-cli-and-mcp-servers/
