---
title: Registry mirror authentication with Kubernetes secrets
date: '2026-03-09T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/03/09/registry-mirror-authentication-with-kubernetes-secrets/
post_kind: link
draft: false
tldr: 'The problem with node-level credentials The solution: Kubelet credential provider
  plugins Kubelet configuration requirements How the CRI-O Credential Provider Works
  Simplified workflow Complete workflow with component interactions A real world example
  Configure RBAC Running the example Security considerations Conclusion Posted on
  March 9, 2026 by Sascha Grunert, Red Hat CNCF projects highlighted in this post
  Part I: Architecture and Implementation In production Kubernetes clusters, pulling
  container images from private registries happens thousands of times per day. Kubernetes
  distributions from major cloud vendors provide credential providers for their respective
  registries like AWS ECR, Google GCR, and Azure ACR.'
summary: 'The problem with node-level credentials The solution: Kubelet credential
  provider plugins Kubelet configuration requirements How the CRI-O Credential Provider
  Works Simplified workflow Complete workflow with component interactions A real world
  example Configure RBAC Running the example Security considerations Conclusion Posted
  on March 9, 2026 by Sascha Grunert, Red Hat CNCF projects highlighted in this post
  Part I: Architecture and Implementation In production Kubernetes clusters, pulling
  container images from private registries happens thousands of times per day. Kubernetes
  distributions from major cloud vendors provide credential providers for their respective
  registries like AWS ECR, Google GCR, and Azure ACR. However, the problem emerges
  when you need to authenticate to private registry mirrors or pull-through caches.
  This is particularly common in air-gapped environments where organizations run their
  own mirror registries to reduce egress costs, improve performance, or meet compliance
  requirements. Traditional approaches to mirror authentication require node-level
  configuration and direct access to nodes. This means credentials must be configured
  globally at the node level, shared across all namespaces. This breaks tenant isolation
  and violates the principle of least privilege. The CRI-O project provides a credential
  provider that solves this problem by enabling authentication for registry mirrors
  using standard Kubernetes Secrets. This approach maintains security boundaries while
  preserving the performance benefits of registry mirrors. Prerequisites Kubernetes
  1.33 or later CRI-O 1.34 or later KubeletServiceAccountTokenForCredentialProviders
  feature gate enabled KubeletServiceAccountTokenForCredentialProviders The credential
  provider binary installed on all nodes Traditional container registry authentication
  in Kubernetes has a fundamental limitation when working with private registry mirrors.
  The kubelet itself has no knowledge of mirror configuration. Mirrors are configured
  at the container runtime level through files like /etc/containers/registries.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/03/09/registry-mirror-authentication-with-kubernetes-secrets/
