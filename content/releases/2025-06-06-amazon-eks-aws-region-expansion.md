---
title: Amazon EKS AWS Region expansion
date: '2025-06-06T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/doc-history.html
post_kind: release
draft: false
tldr: Document history Help improve this page To contribute to this user guide, choose
  the Edit this page on GitHub link that is located in the right pane of every page.
  The following table describes some of the major updates and new features for the
  Amazon EKS User Guide.
summary: Document history Help improve this page To contribute to this user guide,
  choose the Edit this page on GitHub link that is located in the right pane of every
  page. The following table describes some of the major updates and new features for
  the Amazon EKS User Guide. August 27, 2025 AWS managed policy updates Added permission
  to AmazonEKSServiceRolePolicy. This role can attach new access policy AmazonEKSEventPolicy.
  Restricted permissions for ec2:DeleteLaunchTemplate and ec2:TerminateInstances.
  AmazonEKSServiceRolePolicy AmazonEKSEventPolicy ec2:DeleteLaunchTemplate ec2:TerminateInstances
  August 26, 2025 Cross-service confused deputy prevention Added a topic with an example
  trust policy that you can apply for Cross-service confused deputy prevention. Amazon
  EKS accepts the aws:SourceArn and aws:SourceAccount conditions in the trust policy
  of an EKS cluster role. aws:SourceArn aws:SourceAccount August 19, 2025 Amazon EKS
  platform version update This is a new platform version with security fixes and enhancements.
  This includes new patch versions of Kubernetes 1.33.2 , 1.32.6 , 1.31.10 , and 1.30.14.
  1.33.2 1.32.6 1.31.10 1.30.14 July 30, 2025 VPC CNI Multi-NIC feature for multi-homed
  pods Amazon EKS adds multi-homed pods to the VPC CNI. Now you can configure a workload
  and the VPC CNI assigned IP addresses from every NIC on the EC2 instance to each
  pod. The application can make concurrent connections to use the bandwidth from each
  NIC.
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/doc-history.html
