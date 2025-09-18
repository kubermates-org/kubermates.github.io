---
title: 'Kubernetes v1.34: Pods Report DRA Resource Health'
date: '2025-09-17T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/09/17/kubernetes-v1-34-pods-report-dra-resource-health/
post_kind: link
draft: false
tldr: 'Kubernetes v1.34: Pods Report DRA Resource Health Why expose device health
  in Pod status? How it works A new gRPC health service Kubelet integration Populating
  the Pod status A practical example How to use this feature DRA drivers What''s next?
  The rise of AI/ML and other high-performance workloads has made specialized hardware
  like GPUs, TPUs, and FPGAs a critical component of many Kubernetes clusters. However,
  as discussed in a previous blog post about navigating failures in Pods with devices
  , when this hardware fails, it can be difficult to diagnose, leading to significant
  downtime.'
summary: 'Kubernetes v1.34: Pods Report DRA Resource Health Why expose device health
  in Pod status? How it works A new gRPC health service Kubelet integration Populating
  the Pod status A practical example How to use this feature DRA drivers What''s next?
  The rise of AI/ML and other high-performance workloads has made specialized hardware
  like GPUs, TPUs, and FPGAs a critical component of many Kubernetes clusters. However,
  as discussed in a previous blog post about navigating failures in Pods with devices
  , when this hardware fails, it can be difficult to diagnose, leading to significant
  downtime. With the release of Kubernetes v1.34, we are excited to announce a new
  alpha feature that brings much-needed visibility into the health of these devices.
  This work extends the functionality of KEP-4680 , which first introduced a mechanism
  for reporting the health of devices managed by Device Plugins. Now, this capability
  is being extended to Dynamic Resource Allocation (DRA). Controlled by the ResourceHealthStatus
  feature gate, this enhancement allows DRA drivers to report device health directly
  into a Pod''s. status field, providing crucial insights for operators and developers.
  ResourceHealthStatus. status For stateful applications or long-running jobs, a device
  failure can be disruptive and costly. By exposing device health in the. status field
  for a Pod, Kubernetes provides a standardized way for users and automation tools
  to quickly diagnose issues. If a Pod is failing, you can now check its status to
  see if an unhealthy device is the root cause, saving valuable time that might otherwise
  be spent debugging application code.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/09/17/kubernetes-v1-34-pods-report-dra-resource-health/
