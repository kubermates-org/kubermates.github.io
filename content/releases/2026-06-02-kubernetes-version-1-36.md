---
title: Kubernetes version 1.36
date: '2026-06-02T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions-standard.html#kubernetes-1-36
post_kind: release
draft: false
tldr: Review release notes for Kubernetes versions on standard support Kubernetes
  1.36 Kubernetes 1.35 Kubernetes 1.34 Kubernetes 1.33 View a markdown version of
  this page Help improve this page To contribute to this user guide, choose the Edit
  this page on GitHub link that is located in the right pane of every page. Register
  for upcoming Amazon EKS workshops.
summary: 'Review release notes for Kubernetes versions on standard support Kubernetes
  1.36 Kubernetes 1.35 Kubernetes 1.34 Kubernetes 1.33 View a markdown version of
  this page Help improve this page To contribute to this user guide, choose the Edit
  this page on GitHub link that is located in the right pane of every page. Register
  for upcoming Amazon EKS workshops. This topic gives important changes to be aware
  of for each Kubernetes version in standard support. When upgrading, carefully review
  the changes that have occurred between the old and new versions for your cluster.
  Kubernetes 1.36 is now available in Amazon EKS. For more information about Kubernetes
  1.36 , see the official release announcement. 1.36 1.36 gitRepo Volume Removal:
  The gitRepo volume type is permanently disabled in Kubernetes 1.36 and cannot be
  re-enabled. The Kubernetes API still accepts Pods with gitRepo volumes, but the
  kubelet will refuse to run them and return an error. Action required: Migrate to
  init containers or git-sync sidecar containers before upgrading to 1.36. For more
  information, see KEP-5040. gitRepo Volume Removal: The gitRepo volume type is permanently
  disabled in Kubernetes 1.36 and cannot be re-enabled. The Kubernetes API still accepts
  Pods with gitRepo volumes, but the kubelet will refuse to run them and return an
  error.'
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions-standard.html#kubernetes-1-36
