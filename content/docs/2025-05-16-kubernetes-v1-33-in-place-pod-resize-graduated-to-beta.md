---
title: 'Kubernetes v1.33: In-Place Pod Resize Graduated to Beta'
date: '2025-05-16T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/
post_kind: link
draft: false
tldr: 'Kubernetes v1.33: In-Place Pod Resize Graduated to Beta What is in-place Pod
  resize? Why does in-place Pod resize matter? What''s changed between Alpha and Beta?
  Notable user-facing changes Stability and reliability enhancements What''s next?
  Getting started and providing feedback On behalf of the Kubernetes project, I am
  excited to announce that the in-place Pod resize feature (also known as In-Place
  Pod Vertical Scaling), first introduced as alpha in Kubernetes v1.27, has graduated
  to Beta and will be enabled by default in the Kubernetes v1.33 release! This marks
  a significant milestone in making resource management for Kubernetes workloads more
  flexible and less disruptive. Traditionally, changing the CPU or memory resources
  allocated to a container required restarting the Pod.'
summary: 'Kubernetes v1.33: In-Place Pod Resize Graduated to Beta What is in-place
  Pod resize? Why does in-place Pod resize matter? What''s changed between Alpha and
  Beta? Notable user-facing changes Stability and reliability enhancements What''s
  next? Getting started and providing feedback On behalf of the Kubernetes project,
  I am excited to announce that the in-place Pod resize feature (also known as In-Place
  Pod Vertical Scaling), first introduced as alpha in Kubernetes v1.27, has graduated
  to Beta and will be enabled by default in the Kubernetes v1.33 release! This marks
  a significant milestone in making resource management for Kubernetes workloads more
  flexible and less disruptive. Traditionally, changing the CPU or memory resources
  allocated to a container required restarting the Pod. While acceptable for many
  stateless applications, this could be disruptive for stateful services, batch jobs,
  or any workloads sensitive to restarts. In-place Pod resizing allows you to change
  the CPU and memory requests and limits assigned to containers within a running Pod,
  often without requiring a container restart. Here''s the core idea: The spec. containers[*].
  resources field in a Pod specification now represents the desired resources and
  is mutable for CPU and memory. spec. containers[*]. resources The status. containerStatuses[*].
  resources field reflects the actual resources currently configured on a running
  container.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/
