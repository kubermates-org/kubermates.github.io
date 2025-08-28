---
title: 'Kubernetes v1.33: User Namespaces enabled by default!'
date: '2025-04-25T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/04/25/userns-enabled-by-default/
post_kind: link
draft: false
tldr: 'Kubernetes v1. 33: User Namespaces enabled by default! What is a user namespace?
  Demos Everything you wanted to know about user namespaces in Kubernetes Conclusions
  How do I get involved? In Kubernetes v1.'
summary: 'Kubernetes v1. 33: User Namespaces enabled by default! What is a user namespace?
  Demos Everything you wanted to know about user namespaces in Kubernetes Conclusions
  How do I get involved? In Kubernetes v1. 33 support for user namespaces is enabled
  by default. This means that, when the stack requirements are met, pods can opt-in
  to use user namespaces. To use the feature there is no need to enable any Kubernetes
  feature flag anymore! In this blog post we answer some common questions about user
  namespaces. But, before we dive into that, let''s recap what user namespaces are
  and why they are important. Note: Linux user namespaces are a different concept
  from Kubernetes namespaces. The former is a Linux kernel feature; the latter is
  a Kubernetes feature. Linux provides different namespaces to isolate processes from
  each other. For example, a typical Kubernetes pod runs within a network namespace
  to isolate the network identity and a PID namespace to isolate the processes. One
  Linux namespace that was left behind is the user namespace. It isolates the UIDs
  and GIDs of the containers from the ones on the host.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/04/25/userns-enabled-by-default/
