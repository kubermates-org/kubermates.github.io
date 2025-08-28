---
title: 'Kubernetes v1.33: Updates to Container Lifecycle'
date: '2025-05-14T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/05/14/kubernetes-v1-33-updates-to-container-lifecycle/
post_kind: link
draft: false
tldr: 'Kubernetes v1. 33: Updates to Container Lifecycle Zero value for Sleep action
  Container stop signals Default behaviour Version skew Using container stop signals
  How do I get involved? Kubernetes v1.'
summary: 'Kubernetes v1. 33: Updates to Container Lifecycle Zero value for Sleep action
  Container stop signals Default behaviour Version skew Using container stop signals
  How do I get involved? Kubernetes v1. 33 introduces a few updates to the lifecycle
  of containers. The Sleep action for container lifecycle hooks now supports a zero
  sleep duration (feature enabled by default). There is also alpha support for customizing
  the stop signal sent to containers when they are being terminated. This blog post
  goes into the details of these new aspects of the container lifecycle, and how you
  can use them. Kubernetes v1. 29 introduced the Sleep action for container PreStop
  and PostStart Lifecycle hooks. The Sleep action lets your containers pause for a
  specified duration after the container is started or before it is terminated. This
  was needed to provide a straightforward way to manage graceful shutdowns. Before
  the Sleep action, folks used to run the sleep command using the exec action in their
  container lifecycle hooks. If you wanted to do this you''d need to have the binary
  for the sleep command in your container image.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/14/kubernetes-v1-33-updates-to-container-lifecycle/
