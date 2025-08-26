---
title: 'Kubernetes v1.33: Job''s Backoff Limit Per Index Goes GA'
date: '2025-05-13T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/05/13/kubernetes-v1-33-jobs-backoff-limit-per-index-goes-ga/
post_kind: link
draft: false
tldr: In Kubernetes v1. 33, the Backoff Limit Per Index feature reaches general availability
  (GA).
summary: In Kubernetes v1. 33, the Backoff Limit Per Index feature reaches general
  availability (GA). This blog describes the Backoff Limit Per Index feature and its
  benefits. When you run workloads on Kubernetes, you must consider scenarios where
  Pod failures can affect the completion of your workloads. Ideally, your workload
  should tolerate transient failures and continue running. To achieve failure tolerance
  in a Kubernetes Job, you can set the spec. backoffLimit field. This field specifies
  the total number of tolerated failures. However, for workloads where every index
  is considered independent, like embarassingly parallel workloads - the spec. backoffLimit
  field is often not flexible enough. For example, you may choose to run multiple
  suites of integration tests by representing each suite as an index within an Indexed
  Job. In that setup, a fast-failing index (test suite) is likely to consume your
  entire budget for tolerating Pod failures, and you might not be able to run the
  other indexes.
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/13/kubernetes-v1-33-jobs-backoff-limit-per-index-goes-ga/
