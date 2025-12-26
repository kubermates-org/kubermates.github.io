---
title: 'Kubernetes 1.35: In-Place Pod Resize Graduates to Stable'
date: '2025-12-19T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/12/19/kubernetes-v1-35-in-place-pod-resize-ga/
post_kind: link
draft: false
tldr: 'Kubernetes 1.35: In-Place Pod Resize Graduates to Stable What is in-place Pod
  Resize? How can I start using in-place Pod Resize? How does this help me? Changes
  between beta (1.33) and stable (1.35) What''s next? Integration with autoscalers
  and other projects Feature expansion Improved stability Providing feedback This
  release marks a major step: more than 6 years after its initial conception, the
  In-Place Pod Resize feature (also known as In-Place Pod Vertical Scaling), first
  introduced as alpha in Kubernetes v1.27, and graduated to beta in Kubernetes v1.33,
  is now stable (GA) in Kubernetes 1.35! This graduation is a major milestone for
  improving resource efficiency and flexibility for workloads running on Kubernetes.
  In the past, the CPU and memory resources allocated to a container in a Pod were
  immutable.'
summary: 'Kubernetes 1.35: In-Place Pod Resize Graduates to Stable What is in-place
  Pod Resize? How can I start using in-place Pod Resize? How does this help me? Changes
  between beta (1.33) and stable (1.35) What''s next? Integration with autoscalers
  and other projects Feature expansion Improved stability Providing feedback This
  release marks a major step: more than 6 years after its initial conception, the
  In-Place Pod Resize feature (also known as In-Place Pod Vertical Scaling), first
  introduced as alpha in Kubernetes v1.27, and graduated to beta in Kubernetes v1.33,
  is now stable (GA) in Kubernetes 1.35! This graduation is a major milestone for
  improving resource efficiency and flexibility for workloads running on Kubernetes.
  In the past, the CPU and memory resources allocated to a container in a Pod were
  immutable. This meant changing them required deleting and recreating the entire
  Pod. For stateful services, batch jobs, or latency-sensitive workloads, this was
  an incredibly disruptive operation. In-Place Pod Resize makes CPU and memory requests
  and limits mutable, allowing you to adjust these resources within a running Pod,
  often without requiring a container restart. Key Concept: Desired Resources: A container''s
  spec. containers[*]. resources field now represents the desired resources. For CPU
  and memory, these fields are now mutable. spec. containers[*]. resources Actual
  Resources: The status.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/12/19/kubernetes-v1-35-in-place-pod-resize-ga/
