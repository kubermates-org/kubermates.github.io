---
title: 'Kubernetes v1.32: QueueingHint Brings a New Possibility to Optimize Pod Scheduling'
date: '2024-12-12T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2024/12/12/scheduler-queueinghint/
post_kind: link
draft: false
tldr: The Kubernetes scheduler is the core component that selects the nodes on which
  new Pods run.
summary: 'The Kubernetes scheduler is the core component that selects the nodes on
  which new Pods run. The scheduler processes these new Pods one by one. Therefore,
  the larger your clusters, the more important the throughput of the scheduler becomes.
  Over the years, Kubernetes SIG Scheduling has improved the throughput of the scheduler
  in multiple enhancements. This blog post describes a major improvement to the scheduler
  in Kubernetes v1. 32: a scheduling context element named QueueingHint.'
---
Open the original post ↗ https://kubernetes.io/blog/2024/12/12/scheduler-queueinghint/
