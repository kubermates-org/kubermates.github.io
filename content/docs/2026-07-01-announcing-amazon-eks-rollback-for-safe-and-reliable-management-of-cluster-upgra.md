---
title: Announcing Amazon EKS Rollback for safe and reliable management of cluster
  upgrades
date: '2026-07-01T17:32:29+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/announcing-amazon-eks-rollback-for-safe-and-reliable-management-of-cluster-upgrades/
post_kind: link
draft: false
tldr: 'Announcing Amazon EKS Rollback for safe and reliable management of cluster
  upgrades How EKS Version Rollback works EKS Auto Mode rollback Scaling during rollback
  Getting started with EKS Version Rollback Using the AWS CLI Using the Amazon EKS
  console Salesforce’s journey adopting EKS rollback Pre-conditions for rollback eligibility
  Recommended process: Staged upgrade with a control-plane bake period Example scenarios
  Scope of rollback insights Considerations Now available About the authors Today,
  we’re announcing Amazon EKS Version Rollback , a new capability that allows cluster
  administrators to safely roll back Kubernetes version upgrades on Amazon Elastic
  Kubernetes Service (Amazon EKS) clusters. With this feature, you can now confidently
  roll out new version upgrades across your EKS fleet with an additional safety net.'
summary: 'Announcing Amazon EKS Rollback for safe and reliable management of cluster
  upgrades How EKS Version Rollback works EKS Auto Mode rollback Scaling during rollback
  Getting started with EKS Version Rollback Using the AWS CLI Using the Amazon EKS
  console Salesforce’s journey adopting EKS rollback Pre-conditions for rollback eligibility
  Recommended process: Staged upgrade with a control-plane bake period Example scenarios
  Scope of rollback insights Considerations Now available About the authors Today,
  we’re announcing Amazon EKS Version Rollback , a new capability that allows cluster
  administrators to safely roll back Kubernetes version upgrades on Amazon Elastic
  Kubernetes Service (Amazon EKS) clusters. With this feature, you can now confidently
  roll out new version upgrades across your EKS fleet with an additional safety net.
  The release cycle of three minor versions annually requires you to regularly upgrade
  your clusters to maintain security and functionality. However, performing Kubernetes
  version upgrades can be challenging. New versions often introduce changes that can
  affect existing applications, such as feature additions, API deprecations, and internal
  component modifications. By design, open source Kubernetes doesn’t include the ability
  to roll back the Kubernetes control plane after an upgrade is complete. Without
  a native rollback path, many organizations adopted expensive mitigation strategies.
  These include blue/green deployments that double infrastructure costs, or manual
  snapshots of cluster state that consume significant engineering time, all to create
  a safety net that didn’t exist natively. With Amazon EKS Version Rollback, you can
  now safely revert your Kubernetes control plane to a known good state if you discover
  issues after an upgrade. For clusters using EKS Auto Mode, the rollback capability
  extends to the data plane as well, providing comprehensive protection across your
  entire cluster. This capability provides two critical benefits. First, it gives
  you a reliable safety net for production upgrades and a way to meet regulatory requirements
  for disaster recovery plans.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/announcing-amazon-eks-rollback-for-safe-and-reliable-management-of-cluster-upgrades/
