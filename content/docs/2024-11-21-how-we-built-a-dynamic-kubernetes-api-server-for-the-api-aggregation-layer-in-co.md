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
tldr: How we built a dynamic Kubernetes API Server for the API Aggregation Layer in
  Cozystack What Is the API Aggregation Layer? When to use the API Aggregation Layer
  Imperative Logic and Subresources You're not tied to use etcd One-Time resources
  Full control over conversion, validation, and output formatting Dynamic resource
  registration When not to use the API Aggregation Layer Unstable backend Slow requests
  Why we needed it in Cozystack Limitations of the RBAC model Need for a public API
  Two-Way conversion Implementation Disable etcd support Generate a common resource
  kind Configure configuration loading Implement our own registry What did we achieve?
  Next Steps Conclusion Hi there! I'm Andrei Kvapil, but you might know me as @kvaps
  in communities dedicated to Kubernetes and cloud-native tools. In this article,
  I want to share how we implemented our own extension api-server in the open-source
  PaaS platform, Cozystack.
summary: How we built a dynamic Kubernetes API Server for the API Aggregation Layer
  in Cozystack What Is the API Aggregation Layer? When to use the API Aggregation
  Layer Imperative Logic and Subresources You're not tied to use etcd One-Time resources
  Full control over conversion, validation, and output formatting Dynamic resource
  registration When not to use the API Aggregation Layer Unstable backend Slow requests
  Why we needed it in Cozystack Limitations of the RBAC model Need for a public API
  Two-Way conversion Implementation Disable etcd support Generate a common resource
  kind Configure configuration loading Implement our own registry What did we achieve?
  Next Steps Conclusion Hi there! I'm Andrei Kvapil, but you might know me as @kvaps
  in communities dedicated to Kubernetes and cloud-native tools. In this article,
  I want to share how we implemented our own extension api-server in the open-source
  PaaS platform, Cozystack. Kubernetes truly amazes me with its powerful extensibility
  features. You're probably already familiar with the controller concept and frameworks
  like kubebuilder and operator-sdk that help you implement it. In a nutshell, they
  allow you to extend your Kubernetes cluster by defining custom resources (CRDs)
  and writing additional controllers that handle your business logic for reconciling
  and managing these kinds of resources. This approach is well-documented, with a
  wealth of information available online on how to develop your own operators. However,
  this is not the only way to extend the Kubernetes API. For more complex scenarios
  such as implementing imperative logic, managing subresources, and dynamically generating
  responses—the Kubernetes API aggregation layer provides an effective alternative.
  Through the aggregation layer, you can develop a custom extension API server and
  seamlessly integrate it within the broader Kubernetes API framework. In this article,
  I will explore the API aggregation layer, the types of challenges it is well-suited
  to address, cases where it may be less appropriate, and how we utilized this model
  to implement our own extension API server in Cozystack. First, let's get definitions
  straight to avoid any confusion down the road. The API aggregation layer is a feature
  in Kubernetes, while an extension api-server is a specific implementation of an
  API server for the aggregation layer.
---
Open the original post ↗ https://kubernetes.io/blog/2024/11/21/dynamic-kubernetes-api-server-for-cozystack/
