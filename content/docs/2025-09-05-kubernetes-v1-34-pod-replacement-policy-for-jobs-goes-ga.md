---
title: 'Kubernetes v1.34: Pod Replacement Policy for Jobs Goes GA'
date: '2025-09-05T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/09/05/kubernetes-v1-34-pod-replacement-policy-for-jobs-goes-ga/
post_kind: link
draft: false
tldr: 'Kubernetes v1.34: Pod Replacement Policy for Jobs Goes GA About Pod Replacement
  Policy How Pod Replacement Policy works Example How can you learn more? Acknowledgments
  Get involved In Kubernetes v1.34, the Pod replacement policy feature has reached
  general availability (GA). This blog post describes the Pod replacement policy feature
  and how to use it in your Jobs.'
summary: 'Kubernetes v1.34: Pod Replacement Policy for Jobs Goes GA About Pod Replacement
  Policy How Pod Replacement Policy works Example How can you learn more? Acknowledgments
  Get involved In Kubernetes v1.34, the Pod replacement policy feature has reached
  general availability (GA). This blog post describes the Pod replacement policy feature
  and how to use it in your Jobs. By default, the Job controller immediately recreates
  Pods as soon as they fail or begin terminating (when they have a deletion timestamp).
  As a result, while some Pods are terminating, the total number of running Pods for
  a Job can temporarily exceed the specified parallelism. For Indexed Jobs, this can
  even mean multiple Pods running for the same index at the same time. This behavior
  works fine for many workloads, but it can cause problems in certain cases. For example,
  popular machine learning frameworks like TensorFlow and JAX expect exactly one Pod
  per worker index. If two Pods run at the same time, you might encounter errors such
  as: /job:worker/task:4: Duplicate task registration with task_name=/job:worker/replica:0/task:4
  /job:worker/task:4: Duplicate task registration with task_name=/job:worker/replica:0/task:4
  Additionally, starting replacement Pods before the old ones fully terminate can
  lead to: Scheduling delays by kube-scheduler as the nodes remain occupied. Unnecessary
  cluster scale-ups to accommodate the replacement Pods. Temporary bypassing of quota
  checks by workload orchestrators like Kueue. With Pod replacement policy, Kubernetes
  gives you control over when the control plane replaces terminating Pods, helping
  you avoid these issues. This enhancement means that Jobs in Kubernetes have an optional
  field.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/09/05/kubernetes-v1-34-pod-replacement-policy-for-jobs-goes-ga/
