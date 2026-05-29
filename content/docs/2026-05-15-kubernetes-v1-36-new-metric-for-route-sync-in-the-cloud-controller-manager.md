---
title: 'Kubernetes v1.36: New Metric for Route Sync in the Cloud Controller Manager'
date: '2026-05-15T10:35:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/05/15/ccm-new-metric-route-sync-total/
post_kind: link
draft: false
tldr: 'Kubernetes v1.36: New Metric for Route Sync in the Cloud Controller Manager
  A/B testing watch-based route reconciliation Example: expected behavior Where can
  I give feedback? This article was originally published with the wrong date. It was
  later republished, dated the 15th of May 2026.'
summary: 'Kubernetes v1.36: New Metric for Route Sync in the Cloud Controller Manager
  A/B testing watch-based route reconciliation Example: expected behavior Where can
  I give feedback? This article was originally published with the wrong date. It was
  later republished, dated the 15th of May 2026. Kubernetes v1.36 introduces a new
  alpha counter metric route_controller_route_sync_total to the Cloud Controller Manager
  (CCM) route controller implementation at k8s. io/cloud-provider. This metric increments
  each time routes are synced with the cloud provider. route_controller_route_sync_total
  k8s. io/cloud-provider This metric was added to help operators validate the CloudControllerManagerWatchBasedRoutesReconciliation
  feature gate introduced in Kubernetes v1.35. That feature gate switches the route
  controller from a fixed-interval loop to a watch-based approach that only reconciles
  when nodes actually change. This reduces unnecessary API calls to the infrastructure
  provider, lowering pressure on rate-limited APIs and allowing operators to make
  more efficient use of their available quota. CloudControllerManagerWatchBasedRoutesReconciliation
  To A/B test this, compare route_controller_route_sync_total with the feature gate
  disabled (default) versus enabled. In clusters where node changes are infrequent,
  you should see a significant drop in the sync rate with the feature gate turned
  on. route_controller_route_sync_total With the feature gate disabled (the default
  fixed-interval loop), the counter increments steadily regardless of whether any
  node changes occurred: # After 10 minutes with no node changes route_controller_route_sync_total
  60 # After 20 minutes, still no node changes route_controller_route_sync_total 120
  # After 10 minutes with no node changes route_controller_route_sync_total 60 # After
  20 minutes, still no node changes route_controller_route_sync_total 120 With the
  feature gate enabled (watch-based reconciliation), the counter only increments when
  nodes are actually added, removed, or updated: # After 10 minutes with no node changes
  route_controller_route_sync_total 1 # After 20 minutes, still no node changes —
  counter unchanged route_controller_route_sync_total 1 # A new node joins the cluster
  — counter increments route_controller_route_sync_total 2 # After 10 minutes with
  no node changes route_controller_route_sync_total 1 # After 20 minutes, still no
  node changes — counter unchanged route_controller_route_sync_total 1 # A new node
  joins the cluster — counter increments route_controller_route_sync_total 2 The difference
  is especially visible in stable clusters where nodes rarely change.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/05/15/ccm-new-metric-route-sync-total/
