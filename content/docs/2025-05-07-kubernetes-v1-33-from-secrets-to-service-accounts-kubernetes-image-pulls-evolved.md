---
title: 'Kubernetes v1.33: From Secrets to Service Accounts: Kubernetes Image Pulls
  Evolved'
date: '2025-05-07T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/05/07/kubernetes-v1-33-wi-for-image-pulls/
post_kind: link
draft: false
tldr: Kubernetes has steadily evolved to reduce reliance on long-lived credentials
  stored in the API. A prime example of this shift is the transition of Kubernetes
  Service Account (KSA) tokens from long-lived, static tokens to ephemeral, automatically
  rotated tokens with OpenID Connect (OIDC)-compliant semantics.
summary: 'Kubernetes has steadily evolved to reduce reliance on long-lived credentials
  stored in the API. A prime example of this shift is the transition of Kubernetes
  Service Account (KSA) tokens from long-lived, static tokens to ephemeral, automatically
  rotated tokens with OpenID Connect (OIDC)-compliant semantics. This advancement
  enables workloads to securely authenticate with external services without needing
  persistent secrets. However, one major gap remains: image pull authentication. Today,
  Kubernetes clusters rely on image pull secrets stored in the API, which are long-lived
  and difficult to rotate, or on node-level kubelet credential providers, which allow
  any pod running on a node to access the same credentials. This presents security
  and operational challenges. To address this, Kubernetes is introducing Service Account
  Token Integration for Kubelet Credential Providers , now available in alpha. This
  enhancement allows credential providers to use pod-specific service account tokens
  to obtain registry credentials, which kubelet can then use for image pulls — eliminating
  the need for long-lived image pull secrets. Currently, Kubernetes administrators
  have two primary options for handling private container image pulls: Image pull
  secrets stored in the Kubernetes API Kubelet credential providers Neither approach
  aligns with the principles of least privilege or ephemeral authentication , leaving
  Kubernetes with a security gap. This new enhancement enables kubelet credential
  providers to use workload identity when fetching image registry credentials. Instead
  of relying on long-lived secrets, credential providers can use service account tokens
  to request short-lived credentials tied to a specific pod’s identity. This approach
  provides: Kubelet generates short-lived, automatically rotated tokens for service
  accounts if the credential provider it communicates with has opted into receiving
  a service account token for image pulls.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/07/kubernetes-v1-33-wi-for-image-pulls/
