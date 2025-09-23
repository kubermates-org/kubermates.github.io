---
title: 'Kubernetes v1.34: Pod Level Resources Graduated to Beta'
date: '2025-09-22T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/09/22/kubernetes-v1-34-pod-level-resources/
post_kind: link
draft: false
tldr: 'Kubernetes v1.34: Pod Level Resources Graduated to Beta Pod-level specification
  for resources Why does Pod-level specification matter? How to specify resources
  for an entire Pod Example manifest Interaction with container-level resource requests
  or limits Limitations On behalf of the Kubernetes community, I am thrilled to announce
  that the Pod Level Resources feature has graduated to Beta in the Kubernetes v1.34
  release and is enabled by default! This significant milestone introduces a new layer
  of flexibility for defining and managing resource allocation for your Pods. This
  flexibility stems from the ability to specify CPU and memory resources for the Pod
  as a whole.'
summary: 'Kubernetes v1.34: Pod Level Resources Graduated to Beta Pod-level specification
  for resources Why does Pod-level specification matter? How to specify resources
  for an entire Pod Example manifest Interaction with container-level resource requests
  or limits Limitations On behalf of the Kubernetes community, I am thrilled to announce
  that the Pod Level Resources feature has graduated to Beta in the Kubernetes v1.34
  release and is enabled by default! This significant milestone introduces a new layer
  of flexibility for defining and managing resource allocation for your Pods. This
  flexibility stems from the ability to specify CPU and memory resources for the Pod
  as a whole. Pod level resources can be combined with the container-level specifications
  to express the exact resource requirements and limits your application needs. Until
  recently, resource specifications that applied to Pods were primarily defined at
  the individual container level. While effective, this approach sometimes required
  duplicating or meticulously calculating resource needs across multiple containers
  within a single Pod. As a beta feature, Kubernetes allows you to specify the CPU,
  memory and hugepages resources at the Pod-level. This means you can now define resource
  requests and limits for an entire Pod, enabling easier resource sharing without
  requiring granular, per-container management of these resources where it''s not
  needed. This feature enhances resource management in Kubernetes by offering flexible
  resource management at both the Pod and container levels. It provides a consolidated
  approach to resource declaration, reducing the need for meticulous, per-container
  management, especially for Pods with multiple containers. Pod-level resources enable
  containers within a pod to share unused resoures amongst themselves, promoting efficient
  utilization within the pod. For example, it prevents sidecar containers from becoming
  performance bottlenecks. Previously, a sidecar (e.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/09/22/kubernetes-v1-34-pod-level-resources/
