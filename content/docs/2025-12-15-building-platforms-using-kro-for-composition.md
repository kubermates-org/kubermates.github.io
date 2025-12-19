---
title: Building platforms using kro for composition
date: '2025-12-15T12:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/12/15/building-platforms-using-kro-for-composition/
post_kind: link
draft: false
tldr: The rise of Kubernetes-native composition Where kro fits in platform design
  Where platforms need more than kro Looking ahead at a growing ecosystem Posted on
  December 15, 2025 by Abby Bangser, CNCF Ambassador CNCF projects highlighted in
  this post Recent industry developments, such as Amazon’s announcement of the new
  EKS capabilities, highlight a trend toward supporting platforms with managed GitOps,
  cloud resource operators, and composition tooling. In particular, the involvement
  of Kube Resource Orchestrator (kro) —a young, cross-cloud initiative—reflects growing
  ecosystem interest in simplifying Kubernetes-native resource grouping.
summary: The rise of Kubernetes-native composition Where kro fits in platform design
  Where platforms need more than kro Looking ahead at a growing ecosystem Posted on
  December 15, 2025 by Abby Bangser, CNCF Ambassador CNCF projects highlighted in
  this post Recent industry developments, such as Amazon’s announcement of the new
  EKS capabilities, highlight a trend toward supporting platforms with managed GitOps,
  cloud resource operators, and composition tooling. In particular, the involvement
  of Kube Resource Orchestrator (kro) —a young, cross-cloud initiative—reflects growing
  ecosystem interest in simplifying Kubernetes-native resource grouping. Its inclusion
  in the capabilities package signals that major cloud providers recognize the value
  of the SIG Cloud Provider –maintained project and its potential role in future platform-engineering
  workflows. This is a win for platform engineers. The composition of Kubernetes resources
  is becoming increasingly important as declarative Infrastructure as Code (IaC) tooling
  expands the number of objects we manage. For example, CNCF graduated project Crossplane
  , and the cloud-specific alternatives, such as AWS Controller for Kubernetes (ACK),
  which is packaged with EKS Capabilities both can add hundreds or even thousands
  of new CRDs to a cluster. With composition available as a managed service, platform
  teams can focus on their mission to build what is unique to their business but common
  to their teams. They achieve this by combining composition with encapsulation of
  all associated processes and decoupled delivery across any target environment. The
  core value of kro lies in the idea of a ResourceGraphDefinition. Each definition
  abstracts many Kubernetes objects behind a single API. This API specifies what users
  may configure when requesting an instance, which resources are created per request,
  how those sub-resources depend on each other, and what status should be exposed
  back to the users and dependent resources. kro then acts as a controller that responds
  to these definitions by creating a new user-facing CRD and managing requests against
  it through an optimized resource DAG.
---
Open the original post ↗ https://www.cncf.io/blog/2025/12/15/building-platforms-using-kro-for-composition/
