---
title: 'Kubernetes v1.34: Finer-Grained Control Over Container Restarts'
date: '2025-08-29T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/08/29/kubernetes-v1-34-per-container-restart-policy/
post_kind: link
draft: false
tldr: 'Kubernetes v1.34: Finer-Grained Control Over Container Restarts The problem
  with a single restart policy Introducing per-container restart policies Use cases
  In-place restarts for training jobs Try-once init containers Pods with multiple
  containers How to use it Example 1: Restarting on specific exit codes Example 2:
  A try-once init container Example 3: Containers with different restart policies
  Learn more Roadmap Your feedback is welcome! With the release of Kubernetes 1.34,
  a new alpha feature is introduced that gives you more granular control over container
  restarts within a Pod. This feature, named Container Restart Policy and Rules ,
  allows you to specify a restart policy for each container individually, overriding
  the Pod''s global restart policy.'
summary: 'Kubernetes v1.34: Finer-Grained Control Over Container Restarts The problem
  with a single restart policy Introducing per-container restart policies Use cases
  In-place restarts for training jobs Try-once init containers Pods with multiple
  containers How to use it Example 1: Restarting on specific exit codes Example 2:
  A try-once init container Example 3: Containers with different restart policies
  Learn more Roadmap Your feedback is welcome! With the release of Kubernetes 1.34,
  a new alpha feature is introduced that gives you more granular control over container
  restarts within a Pod. This feature, named Container Restart Policy and Rules ,
  allows you to specify a restart policy for each container individually, overriding
  the Pod''s global restart policy. In addition, it also allows you to conditionally
  restart individual containers based on their exit codes. This feature is available
  behind the alpha feature gate ContainerRestartRules. ContainerRestartRules This
  has been a long-requested feature. Let''s dive into how it works and how you can
  use it. Before this feature, the restartPolicy was set at the Pod level. This meant
  that all containers in a Pod shared the same restart policy ( Always , OnFailure
  , or Never ). While this works for many use cases, it can be limiting in others.
  restartPolicy Always OnFailure Never For example, consider a Pod with a main application
  container and an init container that performs some initial setup. You might want
  the main container to always restart on failure, but the init container should only
  run once and never restart. With a single Pod-level restart policy, this wasn''t
  possible.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/08/29/kubernetes-v1-34-per-container-restart-policy/
