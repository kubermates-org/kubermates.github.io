---
title: 'Kubernetes v1.35: Watch Based Route Reconciliation in the Cloud Controller
  Manager'
date: '2025-12-30T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/12/30/kubernetes-v1-35-watch-based-route-reconciliation-in-ccm/
post_kind: link
draft: false
tldr: 'Kubernetes v1.35: Watch Based Route Reconciliation in the Cloud Controller
  Manager What''s new? About the feature gate How can I learn more? Up to and including
  Kubernetes v1.34, the route controller in Cloud Controller Manager (CCM) implementations
  built using the k8s. io/cloud-provider library reconciles routes at a fixed interval.'
summary: 'Kubernetes v1.35: Watch Based Route Reconciliation in the Cloud Controller
  Manager What''s new? About the feature gate How can I learn more? Up to and including
  Kubernetes v1.34, the route controller in Cloud Controller Manager (CCM) implementations
  built using the k8s. io/cloud-provider library reconciles routes at a fixed interval.
  This causes unnecessary API requests to the cloud provider when there are no changes
  to routes. Other controllers implemented through the same library already use watch-based
  mechanisms, leveraging informers to avoid unnecessary API calls. A new feature gate
  is being introduced in v1.35 to allow changing the behavior of the route controller
  to use watch-based informers. The feature gate CloudControllerManagerWatchBasedRoutesReconciliation
  has been introduced to k8s. io/cloud-provider in alpha stage by SIG Cloud Provider.
  To enable this feature you can use --feature-gate=CloudControllerManagerWatchBasedRoutesReconciliation=true
  in the CCM implementation you are using. CloudControllerManagerWatchBasedRoutesReconciliation
  --feature-gate=CloudControllerManagerWatchBasedRoutesReconciliation=true This feature
  gate will trigger the route reconciliation loop whenever a node is added, deleted,
  or the fields. spec. podCIDRs or. status.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/12/30/kubernetes-v1-35-watch-based-route-reconciliation-in-ccm/
