---
title: How we built a dynamic Kubernetes API Server for the API Aggregation Layer
  in Cozystack
date: '2024-11-21T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2024/11/21/dynamic-kubernetes-api-server-for-cozystack/
post_kind: link
draft: false
tldr: Hi there! I'm Andrei Kvapil, but you might know me as @kvaps in communities
  dedicated to Kubernetes and cloud-native tools.
summary: Hi there! I'm Andrei Kvapil, but you might know me as @kvaps in communities
  dedicated to Kubernetes and cloud-native tools. In this article, I want to share
  how we implemented our own extension api-server in the open-source PaaS platform,
  Cozystack. Kubernetes truly amazes me with its powerful extensibility features.
  You're probably already familiar with the controller concept and frameworks like
  kubebuilder and operator-sdk that help you implement it. In a nutshell, they allow
  you to extend your Kubernetes cluster by defining custom resources (CRDs) and writing
  additional controllers that handle your business logic for reconciling and managing
  these kinds of resources. This approach is w...
---
Open the original post ↗ https://kubernetes.io/blog/2024/11/21/dynamic-kubernetes-api-server-for-cozystack/
