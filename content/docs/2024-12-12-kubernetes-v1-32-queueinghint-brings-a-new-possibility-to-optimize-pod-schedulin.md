---
title: 'Kubernetes v1.32: QueueingHint Brings a New Possibility to Optimize Pod Scheduling'
date: '2024-12-12T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2024/12/12/scheduler-queueinghint/
post_kind: link
draft: false
tldr: 'Kubernetes v1.32: QueueingHint Brings a New Possibility to Optimize Pod Scheduling
  Scheduling queue Scheduling framework and plugins Improvements to retrying Pod scheduling
  with QueuingHint QueueingHint''s history and what''s new in v1.32 Getting involved
  How can I learn more? The Kubernetes scheduler is the core component that selects
  the nodes on which new Pods run. The scheduler processes these new Pods one by one.'
summary: 'Kubernetes v1.32: QueueingHint Brings a New Possibility to Optimize Pod
  Scheduling Scheduling queue Scheduling framework and plugins Improvements to retrying
  Pod scheduling with QueuingHint QueueingHint''s history and what''s new in v1.32
  Getting involved How can I learn more? The Kubernetes scheduler is the core component
  that selects the nodes on which new Pods run. The scheduler processes these new
  Pods one by one. Therefore, the larger your clusters, the more important the throughput
  of the scheduler becomes. Over the years, Kubernetes SIG Scheduling has improved
  the throughput of the scheduler in multiple enhancements. This blog post describes
  a major improvement to the scheduler in Kubernetes v1.32: a scheduling context element
  named QueueingHint. This page provides background knowledge of the scheduler and
  explains how QueueingHint improves scheduling throughput. The scheduler stores all
  unscheduled Pods in an internal component called the scheduling queue. The scheduling
  queue consists of the following data structures: ActiveQ : holds newly created Pods
  or Pods that are ready to be retried for scheduling. BackoffQ : holds Pods that
  are ready to be retried but are waiting for a backoff period to end. The backoff
  period depends on the number of unsuccessful scheduling attempts performed by the
  scheduler on that Pod. Unschedulable Pod Pool : holds Pods that the scheduler won''t
  attempt to schedule for one of the following reasons: The scheduler previously attempted
  and was unable to schedule the Pods. Since that attempt, the cluster hasn''t changed
  in a way that could make those Pods schedulable.'
---
Open the original post ↗ https://kubernetes.io/blog/2024/12/12/scheduler-queueinghint/
