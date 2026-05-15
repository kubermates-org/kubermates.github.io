---
title: 'Kubernetes v1.36: Mutable Pod Resources for Suspended Jobs (beta)'
date: '2026-04-27T10:35:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/04/27/kubernetes-v1-36-mutable-pod-resources-for-suspended-jobs/
post_kind: link
draft: false
tldr: 'Kubernetes v1.36: Mutable Pod Resources for Suspended Jobs (beta) Why mutable
  pod resources for suspended Jobs? How it works What''s new in beta Try it out Considerations
  Running Jobs that are suspended Pod replacement policy ResourceClaims Getting involved
  Kubernetes v1.36 promotes the ability to modify container resource requests and
  limits in the pod template of a suspended Job to beta. First introduced as alpha
  in v1.35, this feature allows queue controllers and cluster administrators to adjust
  CPU, memory, GPU, and extended resource specifications on a Job while it is suspended,
  before it starts or resumes running.'
summary: 'Kubernetes v1.36: Mutable Pod Resources for Suspended Jobs (beta) Why mutable
  pod resources for suspended Jobs? How it works What''s new in beta Try it out Considerations
  Running Jobs that are suspended Pod replacement policy ResourceClaims Getting involved
  Kubernetes v1.36 promotes the ability to modify container resource requests and
  limits in the pod template of a suspended Job to beta. First introduced as alpha
  in v1.35, this feature allows queue controllers and cluster administrators to adjust
  CPU, memory, GPU, and extended resource specifications on a Job while it is suspended,
  before it starts or resumes running. Batch and machine learning workloads often
  have resource requirements that are not precisely known at Job creation time. The
  optimal resource allocation depends on current cluster capacity, queue priorities,
  and the availability of specialized hardware like GPUs. Before this feature, resource
  requirements in a Job''s pod template were immutable once set. If a queue controller
  like Kueue determined that a suspended Job should run with different resources,
  the only option was to delete and recreate the Job, losing any associated metadata,
  status, or history. This feature also provides a way to let a specific Job instance
  for a CronJob progress slowly with reduced resources, rather than outright failing
  to run if the cluster is heavily loaded. Consider a machine learning training Job
  initially requesting 4 GPUs: apiVersion : batch/v1 kind : Job metadata : name :
  training-job-example-abcd123 labels : app. kubernetes. io/name : trainer spec :
  suspend : true template : metadata : annotations : kubernetes. io/description :
  "ML training, ID abcd123" spec : containers : - name : trainer image : example-registry.
  example.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/04/27/kubernetes-v1-36-mutable-pod-resources-for-suspended-jobs/
