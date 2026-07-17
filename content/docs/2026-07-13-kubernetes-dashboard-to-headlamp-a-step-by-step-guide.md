---
title: 'Kubernetes Dashboard to Headlamp: A Step-by-Step Guide'
date: '2026-07-13T10:00:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/07/13/kubernetes-dashboard-to-headlamp/
post_kind: link
draft: false
tldr: 'Kubernetes Dashboard to Headlamp: A Step-by-Step Guide 1. Before you start:
  know what is changing 1.1 How Kubernetes Dashboard works 1.2 How Headlamp works
  1.3 What stays the same 1.4 What changes 2.'
summary: 'Kubernetes Dashboard to Headlamp: A Step-by-Step Guide 1. Before you start:
  know what is changing 1.1 How Kubernetes Dashboard works 1.2 How Headlamp works
  1.3 What stays the same 1.4 What changes 2. Pre-migration checklist 2.1 Write down
  what you use today 2.2 Check that kubeconfig works 2.3 Pick a rollout plan 2.4 Decide
  where Headlamp will run 2.5 Note optional dependencies 3. Choose where Headlamp
  will run (desktop or in-cluster) Option A: Desktop (user-managed) Option B: In-cluster
  (best for shared access) 4. Install Headlamp (desktop and in-cluster) 4.1 Desktop
  install (fastest way to start) 4.2 In-cluster install (shared access) 4.3 Updating
  Headlamp 4.4 Notes for in-cluster access (keep it safe) 5. Authentication and RBAC
  5.1 Desktop: use kubeconfig 5.2 In-cluster: shared access needs a sign-in plan 5.3
  RBAC: keep it least privilege 5.4 Quick troubleshooting 6. Manage multiple clusters
  Clusters come from your kubeconfig Switch clusters in the UI Optional: use more
  than one kubeconfig file Optional: add a cluster from inside Headlamp Permissions
  stay the same 7. Navigate and understand resources Find resources in familiar places
  Inspect and edit resources Use search and filters to move faster Understand relationships
  with Map View When to use lists vs Map View 8. Deploy applications with YAML From
  forms to manifests Create resources using YAML Generate YAML the easy way What if
  you use Helm or GitOps? What to expect compared to Dashboard 9. Deploy and debug
  workloads View logs Exec into running pods Check metrics and resource usage View
  events when something goes wrong How this compares to Dashboard 10. Remove Kubernetes
  Dashboard Confirm Headlamp covers your needs Uninstall the Dashboard Clean up access
  artifacts (recommended) Communicate the change 11. Post-migration checklist Access
  and visibility Authentication and RBAC Core workflows Operational confidence Cleanup
  confirmation Team alignment Kubernetes Dashboard and Headlamp both show what is
  running in a cluster, but they work differently.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/07/13/kubernetes-dashboard-to-headlamp/
