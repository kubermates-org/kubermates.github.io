---
title: 'Kubernetes 1.33: Job''s SuccessPolicy Goes GA'
date: '2025-05-15T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/05/15/kubernetes-1-33-jobs-success-policy-goes-ga/
post_kind: link
draft: false
tldr: 'Kubernetes 1.33: Job''s SuccessPolicy Goes GA About Job''s Success Policy How
  it works Learn more Get involved On behalf of the Kubernetes project, I''m pleased
  to announce that Job success policy has graduated to General Availability (GA) as
  part of the v1.33 release. In batch workloads, you might want to use leader-follower
  patterns like MPI , in which the leader controls the execution, including the followers''
  lifecycle.'
summary: 'Kubernetes 1.33: Job''s SuccessPolicy Goes GA About Job''s Success Policy
  How it works Learn more Get involved On behalf of the Kubernetes project, I''m pleased
  to announce that Job success policy has graduated to General Availability (GA) as
  part of the v1.33 release. In batch workloads, you might want to use leader-follower
  patterns like MPI , in which the leader controls the execution, including the followers''
  lifecycle. In this case, you might want to mark it as succeeded even if some of
  the indexes failed. Unfortunately, a leader-follower Kubernetes Job that didn''t
  use a success policy, in most cases, would have to require all Pods to finish successfully
  for that Job to reach an overall succeeded state. For Kubernetes Jobs, the API allows
  you to specify the early exit criteria using the. spec. successPolicy field (you
  can only use the. spec. successPolicy field for an indexed Job ). Which describes
  a set of rules either using a list of succeeded indexes for a job, or defining a
  minimal required size of succeeded indexes. spec. successPolicy.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/15/kubernetes-1-33-jobs-success-policy-goes-ga/
