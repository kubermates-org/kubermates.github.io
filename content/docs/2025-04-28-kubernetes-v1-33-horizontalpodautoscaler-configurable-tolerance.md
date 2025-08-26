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
  a new alpha feature first available in Kubernetes 1.
summary: This post describes configurable tolerance for horizontal Pod autoscaling
  , a new alpha feature first available in Kubernetes 1. 33. Horizontal Pod Autoscaling
  is a well-known Kubernetes feature that allows your workload to automatically resize
  by adding or removing replicas based on resource utilization. Let's say you have
  a web application running in a Kubernetes cluster with 50 replicas. You configure
  the HorizontalPodAutoscaler (HPA) to scale based on CPU utilization, with a target
  of 75% utilization. Now, imagine that the current CPU utilization across all replicas
  is 90%, which is higher than the desired 75%.
---
Open the original post ↗ https://kubernetes.io/blog/2025/04/28/kubernetes-v1-33-hpa-configurable-tolerance/
