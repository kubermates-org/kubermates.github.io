---
title: Back up and restore your Amazon EKS cluster resources using Velero
date: '2026-05-12T18:19:57+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/back-up-and-restore-your-amazon-eks-cluster-resources-using-velero/
post_kind: link
draft: false
tldr: Back up and restore your Amazon EKS cluster resources using Velero Prerequisites
  Velero overview Tutorial Set up environment variables Configure Amazon S3 and IAM
  Install Velero Back up an application Restore an application Clean up Conclusion
  About the authors When you accidentally delete a production namespace or a cluster
  upgrade fails, rebuilding your Amazon Elastic Kubernetes Service (Amazon EKS) cluster
  resources means recreating every deployment, service, and persistent volume manually.
  With Velero, a backup and restore tool for Kubernetes, you capture resource definitions
  to Amazon Simple Storage Service (Amazon S3) and persistent volume data as Amazon
  Elastic Block Store (Amazon EBS) snapshots.
summary: 'Back up and restore your Amazon EKS cluster resources using Velero Prerequisites
  Velero overview Tutorial Set up environment variables Configure Amazon S3 and IAM
  Install Velero Back up an application Restore an application Clean up Conclusion
  About the authors When you accidentally delete a production namespace or a cluster
  upgrade fails, rebuilding your Amazon Elastic Kubernetes Service (Amazon EKS) cluster
  resources means recreating every deployment, service, and persistent volume manually.
  With Velero, a backup and restore tool for Kubernetes, you capture resource definitions
  to Amazon Simple Storage Service (Amazon S3) and persistent volume data as Amazon
  Elastic Block Store (Amazon EBS) snapshots. Velero supports cross-cluster restores,
  namespace-level granularity, and portability across Kubernetes distributions. If
  you need centralized, fully managed backup scheduling instead, AWS Backup for Amazon
  EKS handles that for you. In this post, you’ll learn to back up and restore Amazon
  EKS cluster resources and persistent volume data using Velero. You’ll deploy a sample
  stateful application, back it up, and restore it to a different namespace within
  the same cluster. Along the way, you’ll configure least-privilege AWS Identity and
  Access Management (AWS IAM) roles using Amazon EKS Pod Identity and scope Velero’s
  Kubernetes permissions with a custom ClusterRole. A ClusterRole is a Kubernetes
  resource that defines cluster-wide permissions. You’ll spend 45 to 60 minutes on
  this tutorial and incur costs for Amazon S3 storage (based on data stored), Amazon
  EBS snapshots (based on snapshot storage), and Amazon EKS cluster usage (based on
  cluster runtime). For detailed pricing information, see Amazon S3 Pricing, Amazon
  EBS Pricing, and Amazon EKS Pricing. Clean up instructions at the end help you remove
  all billable resources. To complete this tutorial, make sure you have the following:
  An active AWS account with permissions to create Amazon S3 buckets, IAM policies
  and roles, and Amazon EKS resources An Amazon EKS cluster running Kubernetes 1.35
  or later with Amazon EKS Auto Mode enabled.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/back-up-and-restore-your-amazon-eks-cluster-resources-using-velero/
