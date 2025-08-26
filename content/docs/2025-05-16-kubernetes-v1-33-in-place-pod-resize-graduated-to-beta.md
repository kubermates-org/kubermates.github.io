---
title: 'Kubernetes v1.33: In-Place Pod Resize Graduated to Beta'
date: '2025-05-16T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/
post_kind: link
draft: false
tldr: On behalf of the Kubernetes project, I am excited to announce that the in-place
  Pod resize feature (also known as In-Place Pod Vertical Scaling), first introduced
  as alpha in Kubernetes v1. 27, has graduated to Beta and will be enabled by default
  in the Kubernetes v1.
summary: 'On behalf of the Kubernetes project, I am excited to announce that the in-place
  Pod resize feature (also known as In-Place Pod Vertical Scaling), first introduced
  as alpha in Kubernetes v1. 27, has graduated to Beta and will be enabled by default
  in the Kubernetes v1. 33 release! This marks a significant milestone in making resource
  management for Kubernetes workloads more flexible and less disruptive. Traditionally,
  changing the CPU or memory resources allocated to a container required restarting
  the Pod. While acceptable for many stateless applications, this could be disruptive
  for stateful services, batch jobs, or any workloads sensitive to restarts. In-place
  Pod resizing allows you to change the CPU and memory requests and limits assigned
  to containers within a running Pod, often without requiring a container restart.
  Here''s the core idea: You can try it out on a v1. 33 Kubernetes cluster by using
  kubectl to edit a Pod (requires kubectl v1. 32+): For detailed usage instructions
  and examples, please refer to the official Kubernetes documentation: Resize CPU
  and Memory Resources assigned to Containers. Kubernetes still excels at scaling
  workloads horizontally (adding or removing replicas), but in-place Pod resizing
  unlocks several key benefits for vertical scaling: Since the alpha release in v1.
  27, significant work has gone into maturing the feature, improving its stability,
  and refining the user experience based on feedback and further development. Here
  are the key changes: Graduating to Beta means the feature is ready for broader adoption,
  but development doesn''t stop here! Here''s what the community is focusing on next:
  With the InPlacePodVerticalScaling feature gate enabled by default in v1.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/
