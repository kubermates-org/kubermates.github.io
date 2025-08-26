---
title: Update strategies for managed node groups
date: '2025-01-27T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/managed-node-update-behavior.html#managed-node-update-upgrade
post_kind: release
draft: false
tldr: Help improve this page To contribute to this user guide, choose the Edit this
  page on GitHub link that is located in the right pane of every page. The Amazon
  EKS managed worker node upgrade strategy has four different phases described in
  the following sections.
summary: "Help improve this page To contribute to this user guide, choose the Edit\
  \ this page on GitHub link that is located in the right pane of every page. The\
  \ Amazon EKS managed worker node upgrade strategy has four different phases described\
  \ in the following sections. The setup phase has these steps: It creates a new Amazon\
  \ EC2 launch template version for the Auto Scaling Group thatâ\x80\x99s associated\
  \ with your node group. The new launch template version uses the target AMI or a\
  \ custom launch template version for the update. It updates the Auto Scaling Group\
  \ to use the latest launch template version. It determines the maximum quantity\
  \ of nodes to upgrade in parallel using the updateConfig property for the node group.\
  \ The maximum unavailable has a quota of 100 nodes. The default value is one node.\
  \ For more information, see the updateConfig property in the Amazon EKS API Reference.\
  \ When upgrading the nodes in a managed node group, the upgraded nodes are launched\
  \ in the same Availability Zone as those that are being upgraded. To guarantee this\
  \ placement, we use Amazon EC2â\x80\x99s Availability Zone Rebalancing. For more\
  \ information, see Availability Zone Rebalancing in the Amazon EC2 Auto Scaling\
  \ User Guide."
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/managed-node-update-behavior.html#managed-node-update-upgrade
