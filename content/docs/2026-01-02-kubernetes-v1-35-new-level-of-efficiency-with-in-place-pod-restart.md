---
title: 'Kubernetes v1.35: New level of efficiency with in-place Pod restart'
date: '2026-01-02T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/01/02/kubernetes-v1-35-restart-all-containers/
post_kind: link
draft: false
tldr: 'Kubernetes v1.35: New level of efficiency with in-place Pod restart The problem:
  when a single container restart isn''t enough and recreating pods is too costly
  Introducing the RestartAllContainers action Use cases 1. Efficient restarts for
  ML/Batch jobs 2.'
summary: 'Kubernetes v1.35: New level of efficiency with in-place Pod restart The
  problem: when a single container restart isn''t enough and recreating pods is too
  costly Introducing the RestartAllContainers action Use cases 1. Efficient restarts
  for ML/Batch jobs 2. Re-running init containers for a clean state 3. Handling high
  rate of similar tasks execution How to use it Observing the restart Learn more We
  want your feedback! The release of Kubernetes 1.35 introduces a powerful new feature
  that provides a much-requested capability: the ability to trigger a full, in-place
  restart of the Pod. This feature, Restart All Containers (alpha in 1.35), allows
  for an efficient way to reset a Pod''s state compared to resource-intensive approach
  of deleting and recreating the entire Pod. This feature is especially useful for
  AI/ML workloads allowing application developers to concentrate on their core training
  logic while offloading complex failure-handling and recovery mechanisms to sidecars
  and declarative Kubernetes configuration. With RestartAllContainers and other planned
  enhancements, Kubernetes continues to add building blocks for creating the most
  flexible, robust, and efficient platforms for AI/ML workloads. RestartAllContainers
  This new functionality is available by enabling the RestartAllContainersOnContainerExits
  feature gate. This alpha feature extends the Container Restart Rules feature , which
  graduated to beta in Kubernetes 1.35. RestartAllContainersOnContainerExits Kubernetes
  has long supported restart policies at the Pod level ( restartPolicy ) and, more
  recently, at the individual container level. These policies are great for handling
  crashes in a single, isolated process. However, many modern applications have more
  complex inter-container dependencies.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/01/02/kubernetes-v1-35-restart-all-containers/
