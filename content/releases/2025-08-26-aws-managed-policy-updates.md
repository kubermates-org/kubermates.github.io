---
title: AWS managed policy updates
date: '2025-08-26T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/security-iam-awsmanpol.html
post_kind: release
draft: false
tldr: Help improve this page To contribute to this user guide, choose the Edit this
  page on GitHub link that is located in the right pane of every page. An AWS managed
  policy is a standalone policy that is created and administered by AWS.
summary: "Help improve this page To contribute to this user guide, choose the Edit\
  \ this page on GitHub link that is located in the right pane of every page. An AWS\
  \ managed policy is a standalone policy that is created and administered by AWS.\
  \ AWS managed policies are designed to provide permissions for many common use cases\
  \ so that you can start assigning permissions to users, groups, and roles. Keep\
  \ in mind that AWS managed policies might not grant least-privilege permissions\
  \ for your specific use cases because theyâ\x80\x99re available for all AWS customers\
  \ to use. We recommend that you reduce permissions further by defining customer\
  \ managed policies that are specific to your use cases. You cannot change the permissions\
  \ defined in AWS managed policies. If AWS updates the permissions defined in an\
  \ AWS managed policy, the update affects all principal identities (users, groups,\
  \ and roles) that the policy is attached to. AWS is most likely to update an AWS\
  \ managed policy when a new AWS service is launched or new API operations become\
  \ available for existing services. For more information, see AWS managed policies\
  \ in the IAM User Guide. You can attach the AmazonEKS_CNI_Policy to your IAM entities.\
  \ Before you create an Amazon EC2 node group, this policy must be attached to either\
  \ the node IAM role , or to an IAM role thatâ\x80\x99s used specifically by the\
  \ Amazon VPC CNI plugin for Kubernetes. This is so that it can perform actions on\
  \ your behalf."
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/security-iam-awsmanpol.html
