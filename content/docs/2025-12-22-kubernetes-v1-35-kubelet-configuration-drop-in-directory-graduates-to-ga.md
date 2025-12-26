---
title: 'Kubernetes v1.35: Kubelet Configuration Drop-in Directory Graduates to GA'
date: '2025-12-22T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/12/22/kubernetes-v1-35-kubelet-config-drop-in-directory-ga/
post_kind: link
draft: false
tldr: 'Kubernetes v1.35: Kubelet Configuration Drop-in Directory Graduates to GA The
  problem: managing kubelet configuration at scale Example use cases Managing heterogeneous
  node pools Gradual configuration rollouts Viewing the merged configuration Good
  practices Acknowledgments Get involved With the recent v1.35 release of Kubernetes,
  support for a kubelet configuration drop-in directory is generally available. The
  newly stable feature simplifies the management of kubelet configuration across large,
  heterogeneous clusters.'
summary: 'Kubernetes v1.35: Kubelet Configuration Drop-in Directory Graduates to GA
  The problem: managing kubelet configuration at scale Example use cases Managing
  heterogeneous node pools Gradual configuration rollouts Viewing the merged configuration
  Good practices Acknowledgments Get involved With the recent v1.35 release of Kubernetes,
  support for a kubelet configuration drop-in directory is generally available. The
  newly stable feature simplifies the management of kubelet configuration across large,
  heterogeneous clusters. With v1.35, the kubelet command line argument --config-dir
  is production-ready and fully supported, allowing you to specify a directory containing
  kubelet configuration drop-in files. All files in that directory will be automatically
  merged with your main kubelet configuration. This allows cluster administrators
  to maintain a cohesive base configuration for kubelets while enabling targeted customizations
  for different node groups or use cases, and without complex tooling or manual configuration
  management. --config-dir As Kubernetes clusters grow larger and more complex, they
  often include heterogeneous node pools with different hardware capabilities, workload
  requirements, and operational constraints. This diversity necessitates different
  kubelet configurations across node groups—yet managing these varied configurations
  at scale becomes increasingly challenging. Several pain points emerge: Configuration
  drift : Different nodes may have slightly different configurations, leading to inconsistent
  behavior Node group customization : GPU nodes, edge nodes, and standard compute
  nodes often require different kubelet settings Operational overhead : Maintaining
  separate, complete configuration files for each node type is error-prone and difficult
  to audit Change management : Rolling out configuration changes across heterogeneous
  node pools requires careful coordination Before this support was added to Kubernetes,
  cluster administrators had to choose between using a single monolithic configuration
  file for all nodes, manually maintaining multiple complete configuration files,
  or relying on separate tooling. Each approach had its own drawbacks. This graduation
  to stable gives cluster administrators a fully supported fourth way to solve that
  challenge. Consider a cluster with multiple node types: standard compute nodes,
  high-capacity nodes (such as those with GPUs or large amounts of memory), and edge
  nodes with specialized requirements. File: 00-base.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/12/22/kubernetes-v1-35-kubelet-config-drop-in-directory-ga/
