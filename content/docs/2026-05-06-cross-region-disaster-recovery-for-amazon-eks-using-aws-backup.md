---
title: Cross-Region disaster recovery for Amazon EKS using AWS Backup
date: '2026-05-06T17:09:28+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/cross-region-disaster-recovery-for-amazon-eks-using-aws-backup/
post_kind: link
draft: false
tldr: 'Cross-Region disaster recovery for Amazon EKS using AWS Backup Solution overview
  Architecture diagram Prerequisites Walkthrough Phase 1: Deploy source infrastructure
  (us-east-1) Phase 2: Deploy the application Phase 3: Configure backup and cross-Region
  copy Phase 4: Deploy DR infrastructure (us-west-2) Phase 5: Restore application
  to DR cluster Cleaning up Conclusion About the authors Organizations running containerized
  workloads on Amazon Elastic Kubernetes Service (Amazon EKS) need resilient strategies
  that protect both application configurations and stateful data against Regional
  disruptions. While single-Region architectures with multi-AZ deployments serve many
  availability requirements well, some workloads demand cross-Region disaster recovery
  (DR) to meet stringent recovery time objectives (RTOs) and recovery point objectives
  (RPOs) mandated by regulatory or business continuity requirements.'
summary: 'Cross-Region disaster recovery for Amazon EKS using AWS Backup Solution
  overview Architecture diagram Prerequisites Walkthrough Phase 1: Deploy source infrastructure
  (us-east-1) Phase 2: Deploy the application Phase 3: Configure backup and cross-Region
  copy Phase 4: Deploy DR infrastructure (us-west-2) Phase 5: Restore application
  to DR cluster Cleaning up Conclusion About the authors Organizations running containerized
  workloads on Amazon Elastic Kubernetes Service (Amazon EKS) need resilient strategies
  that protect both application configurations and stateful data against Regional
  disruptions. While single-Region architectures with multi-AZ deployments serve many
  availability requirements well, some workloads demand cross-Region disaster recovery
  (DR) to meet stringent recovery time objectives (RTOs) and recovery point objectives
  (RPOs) mandated by regulatory or business continuity requirements. AWS Backup provides
  native support for Amazon EKS, so you can protect your cluster’s Kubernetes resources
  and persistent volume data in a centralized, policy-driven manner. By combining
  EKS backups with cross-Region copy capabilities, you can replicate your entire application
  state to a secondary AWS Region and restore it to an existing or new cluster when
  a disaster occurs. In this post, we walk you through a complete cross-Region DR
  implementation for Amazon EKS using AWS Backup. We deploy a stateful retail store
  application in a source Region, back it up, copy the backup to a DR Region, and
  restore the full application, including its persistent data, to a pre-provisioned
  cluster in the secondary Region. By the end of this walkthrough, you will have a
  fully functional DR environment with your application running in the secondary Region
  with all stateful data intact. The solution workflow consists of five phases: Deploy
  source infrastructure — Provision a VPC, Amazon EKS cluster, and supporting components
  in the source Region (us-east-1). Deploy the application — Deploy a stateful retail
  store application with MySQL and Redis StatefulSets backed by Amazon Elastic Block
  Store (Amazon EBS) persistent volumes. Configure backup and cross-Region copy —
  Create AWS Backup vaults in both Regions, execute an on-demand backup of the EKS
  cluster, and copy the recovery point to the DR Region. Deploy DR infrastructure
  — Provision a target EKS cluster and networking in the DR Region (us-west-2). Restore
  application to DR cluster — Use AWS Backup to restore the complete application,
  including Kubernetes resources and persistent volumes, to the existing DR cluster.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/cross-region-disaster-recovery-for-amazon-eks-using-aws-backup/
