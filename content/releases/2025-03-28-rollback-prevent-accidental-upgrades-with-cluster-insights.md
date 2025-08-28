---
title: 'Rollback: Prevent accidental upgrades with cluster insights'
date: '2025-03-28T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/update-cluster.html#update-cluster-control-plane
post_kind: release
draft: false
tldr: 'Update existing cluster to new Kubernetes version Considerations for Amazon
  EKS Auto Mode Summary Step 1: Prepare for upgrade Step 2: Review upgrade considerations
  Review upgrade insights Detailed considerations Step 3: Update cluster control plane
  Update cluster - eksctl Update cluster - AWS console Update cluster - AWS CLI Step
  4: Update cluster components Downgrade the Kubernetes version for an Amazon EKS
  cluster Help improve this page To contribute to this user guide, choose the Edit
  this page on GitHub link that is located in the right pane of every page. When a
  new Kubernetes version is available in Amazon EKS, you can update your Amazon EKS
  cluster to the latest version.'
summary: "Update existing cluster to new Kubernetes version Considerations for Amazon\
  \ EKS Auto Mode Summary Step 1: Prepare for upgrade Step 2: Review upgrade considerations\
  \ Review upgrade insights Detailed considerations Step 3: Update cluster control\
  \ plane Update cluster - eksctl Update cluster - AWS console Update cluster - AWS\
  \ CLI Step 4: Update cluster components Downgrade the Kubernetes version for an\
  \ Amazon EKS cluster Help improve this page To contribute to this user guide, choose\
  \ the Edit this page on GitHub link that is located in the right pane of every page.\
  \ When a new Kubernetes version is available in Amazon EKS, you can update your\
  \ Amazon EKS cluster to the latest version. Once you upgrade a cluster, you canâ\x80\
  \x99t downgrade to a previous version. Before you update to a new Kubernetes version,\
  \ we recommend that you review the information in Understand the Kubernetes version\
  \ lifecycle on EKS and the update steps in this topic. New Kubernetes versions sometimes\
  \ introduce significant changes. Therefore, we recommend that you test the behavior\
  \ of your applications against a new Kubernetes version before you update your production\
  \ clusters. You can do this by building a continuous integration workflow to test\
  \ your application behavior before moving to a new Kubernetes version. The update\
  \ process consists of Amazon EKS launching new API server nodes with the updated\
  \ Kubernetes version to replace the existing ones. Amazon EKS performs standard\
  \ infrastructure and readiness health checks for network traffic on these new nodes\
  \ to verify that theyâ\x80\x99re working as expected. However, once youâ\x80\x99\
  ve started the cluster upgrade, you canâ\x80\x99t pause or stop it. If any of these\
  \ checks fail, Amazon EKS reverts the infrastructure deployment, and your cluster\
  \ remains on the prior Kubernetes version. Running applications arenâ\x80\x99t affected,\
  \ and your cluster is never left in a non-deterministic or unrecoverable state."
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/update-cluster.html#update-cluster-control-plane
