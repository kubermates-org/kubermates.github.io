---
title: 'Kubernetes v1.33: Job''s Backoff Limit Per Index Goes GA'
date: '2025-05-13T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/05/13/kubernetes-v1-33-jobs-backoff-limit-per-index-goes-ga/
post_kind: link
draft: false
tldr: 'Kubernetes v1. 33: Job''s Backoff Limit Per Index Goes GA About backoff limit
  per index How backoff limit per index works Example Learn more Get involved In Kubernetes
  v1.'
summary: 'Kubernetes v1. 33: Job''s Backoff Limit Per Index Goes GA About backoff
  limit per index How backoff limit per index works Example Learn more Get involved
  In Kubernetes v1. 33, the Backoff Limit Per Index feature reaches general availability
  (GA). This blog describes the Backoff Limit Per Index feature and its benefits.
  When you run workloads on Kubernetes, you must consider scenarios where Pod failures
  can affect the completion of your workloads. Ideally, your workload should tolerate
  transient failures and continue running. To achieve failure tolerance in a Kubernetes
  Job, you can set the spec. backoffLimit field. This field specifies the total number
  of tolerated failures. spec. backoffLimit However, for workloads where every index
  is considered independent, like embarassingly parallel workloads - the spec. backoffLimit
  field is often not flexible enough.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/13/kubernetes-v1-33-jobs-backoff-limit-per-index-goes-ga/
