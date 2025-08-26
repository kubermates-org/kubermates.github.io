---
title: 'Kubernetes v1.33: HorizontalPodAutoscaler Configurable Tolerance'
date: '2025-04-28T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/04/28/kubernetes-v1-33-hpa-configurable-tolerance/
post_kind: link
draft: false
tldr: This post describes configurable tolerance for horizontal Pod autoscaling ,
  a new alpha feature first available in Kubernetes 1. 33.
summary: 'This post describes configurable tolerance for horizontal Pod autoscaling
  , a new alpha feature first available in Kubernetes 1. 33. Horizontal Pod Autoscaling
  is a well-known Kubernetes feature that allows your workload to automatically resize
  by adding or removing replicas based on resource utilization. Let''s say you have
  a web application running in a Kubernetes cluster with 50 replicas. You configure
  the HorizontalPodAutoscaler (HPA) to scale based on CPU utilization, with a target
  of 75% utilization. Now, imagine that the current CPU utilization across all replicas
  is 90%, which is higher than the desired 75%. The HPA will calculate the required
  number of replicas using the formula: In this example: So, the HPA will increase
  the number of replicas from 50 to 60 to reduce the load on each pod. Similarly,
  if the CPU utilization were to drop below 75%, the HPA would scale down the number
  of replicas accordingly. The Kubernetes documentation provides a detailed description
  of the scaling algorithm. In order to avoid replicas being created or deleted whenever
  a small metric fluctuation occurs, Kubernetes applies a form of hysteresis: it only
  changes the number of replicas when the current and desired metric values differ
  by more than 10%. In the example above, since the ratio between the current and
  desired metric values is \(90/75\), or 20% above target, exceeding the 10% tolerance,
  the scale-up action will proceed. This default tolerance of 10% is cluster-wide;
  in older Kubernetes releases, it could not be fine-tuned.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/04/28/kubernetes-v1-33-hpa-configurable-tolerance/
