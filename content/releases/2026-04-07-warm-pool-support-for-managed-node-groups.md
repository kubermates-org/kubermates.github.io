---
title: Warm pool support for managed node groups
date: '2026-04-07T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/warm-pools-managed-node-groups.html
post_kind: release
draft: false
tldr: "Decrease latency for applications with long boot times using warm pools with\
  \ managed node groups How it works Considerations Configure warm pools Configuration\
  \ parameters Using the AWS CLI Update configuration Additional resources Help improve\
  \ this page To contribute to this user guide, choose the Edit this page on GitHub\
  \ link that is located in the right pane of every page. When your applications have\
  \ long initialization or boot times, scale-out events can cause delaysâ\x80\x94\
  new nodes must fully boot and join the cluster before Pods can be scheduled on them."
summary: "Decrease latency for applications with long boot times using warm pools\
  \ with managed node groups How it works Considerations Configure warm pools Configuration\
  \ parameters Using the AWS CLI Update configuration Additional resources Help improve\
  \ this page To contribute to this user guide, choose the Edit this page on GitHub\
  \ link that is located in the right pane of every page. When your applications have\
  \ long initialization or boot times, scale-out events can cause delaysâ\x80\x94\
  new nodes must fully boot and join the cluster before Pods can be scheduled on them.\
  \ This latency can impact application availability during traffic spikes or rapid\
  \ scaling events. Warm pools solve this problem by maintaining a pool of pre-initialized\
  \ EC2 instances that have already completed the bootup process. During a scale-out\
  \ event, instances move from the warm pool directly to your cluster, bypassing the\
  \ time-consuming initialization steps and significantly reducing the time it takes\
  \ for new capacity to become available. For more information, see Decrease latency\
  \ for applications that have long boot times using warm pools in the Amazon EC2\
  \ Auto Scaling User Guide. Amazon EKS managed node groups support Amazon EC2 Auto\
  \ Scaling warm pools. A warm pool maintains pre-initialized EC2 instances alongside\
  \ your Auto Scaling group that can quickly join your cluster during scale-out events.\
  \ Instances in the warm pool have already completed the bootup initialization process\
  \ and can be kept in a Stopped , Running , or Hibernated state. Stopped Running\
  \ Hibernated Amazon EKS manages warm pools throughout the node group lifecycle using\
  \ the AWSServiceRoleForAmazonEKSNodegroup service-linked role to create, update,\
  \ and delete warm pool resources. AWSServiceRoleForAmazonEKSNodegroup When you configure\
  \ a warm pool, Amazon EKS creates an EC2 Auto Scaling warm pool attached to your\
  \ node groupâ\x80\x99s Auto Scaling group. Instances launch into the warm pool,\
  \ complete the bootup initialization process, and remain in the configured state\
  \ ( Running , Stopped , or Hibernated ) until needed."
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/warm-pools-managed-node-groups.html
