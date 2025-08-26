---
title: Target secondary and cross-account roles with EKS Pod Identities
date: '2025-06-11T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/pod-id-assign-target-role.html
post_kind: release
draft: false
tldr: Help improve this page To contribute to this user guide, choose the Edit this
  page on GitHub link that is located in the right pane of every page. When running
  applications on Amazon Elastic Kubernetes Service (Amazon EKS), you might need to
  access AWS resources that exist in different AWS accounts.
summary: "Help improve this page To contribute to this user guide, choose the Edit\
  \ this page on GitHub link that is located in the right pane of every page. When\
  \ running applications on Amazon Elastic Kubernetes Service (Amazon EKS), you might\
  \ need to access AWS resources that exist in different AWS accounts. This guide\
  \ shows you how to set up cross account access using EKS Pod Identity, which enables\
  \ your Kubernetes pods to access other AWS resources using target roles. Before\
  \ you begin, ensure you have completed the following steps: Set up the Amazon EKS\
  \ Pod Identity Agent Create an EKS Pod Identity role Pod Identity enables applications\
  \ in your EKS cluster to access AWS resources across accounts through a process\
  \ called role chaining. When creating a Pod Identity association, you can provide\
  \ two IAM roles: an EKS Pod Identity role in the same account as your EKS cluster\
  \ and a Target IAM Role from the account containing your AWS resources you wish\
  \ to access, (like S3 buckets or RDS Databases). The EKS Pod Identity role must\
  \ be in your EKS clusterâ\x80\x99s account due to IAM PassRole requirements, while\
  \ the Target IAM Role can be in any AWS account. PassRole enables an AWS entity\
  \ to delegate role assumption to another service. EKS Pod Identity uses PassRole\
  \ to connect a role to a Kubernetes service account, requiring both the role and\
  \ the identity passing it to be in the same AWS account as the EKS cluster. When\
  \ your application pod needs to access AWS resources, it requests credentials from\
  \ Pod Identity. Pod Identity then automatically performs two role assumptions in\
  \ sequence: first assuming the EKS Pod Identity role , then using those credentials\
  \ to assume the Target IAM Role. This process provides your pod with temporary credentials\
  \ that have the permissions defined in the target role, allowing secure access to\
  \ resources in other AWS accounts. Due to caching mechanisms, updates to an IAM\
  \ role in an existing Pod Identity association may not take effect immediately in\
  \ the pods running on your EKS cluster."
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/pod-id-assign-target-role.html
