---
title: 'Start Sidecar First: How To Avoid Snags'
date: '2025-06-03T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/06/03/start-sidecar-first/
post_kind: link
draft: false
tldr: 'From the Kubernetes Multicontainer Pods: An Overview blog post you know what
  their job is, what are the main architectural patterns, and how they are implemented
  in Kubernetes. The main thing I’ll cover in this article is how to ensure that your
  sidecar containers start before the main app.'
summary: 'From the Kubernetes Multicontainer Pods: An Overview blog post you know
  what their job is, what are the main architectural patterns, and how they are implemented
  in Kubernetes. The main thing I’ll cover in this article is how to ensure that your
  sidecar containers start before the main app. It’s more complicated than you might
  think! I''d just like to remind readers that the v1. 29. 0 release of Kubernetes
  added native support for sidecar containers , which can now be defined within the.
  spec. initContainers field, but with restartPolicy: Always. You can see that illustrated
  in the following example Pod manifest snippet: What are the specifics of defining
  sidecars with a. spec. initContainers block, rather than as a legacy multi-container
  pod with multiple. spec. containers ? Well, all.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/06/03/start-sidecar-first/
