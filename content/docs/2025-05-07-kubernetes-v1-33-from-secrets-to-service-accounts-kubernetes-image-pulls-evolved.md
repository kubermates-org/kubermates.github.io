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
tldr: 'Kubernetes v1.33: From Secrets to Service Accounts: Kubernetes Image Pulls
  Evolved The problem with image pull secrets The solution: Service Account token
  integration for Kubelet credential providers How it works 1. Service Account tokens
  for credential providers 2.'
summary: 'Kubernetes v1.33: From Secrets to Service Accounts: Kubernetes Image Pulls
  Evolved The problem with image pull secrets The solution: Service Account token
  integration for Kubelet credential providers How it works 1. Service Account tokens
  for credential providers 2. Image registry authentication flow Benefits of this
  approach What''s next? Try it out How to get involved Kubernetes has steadily evolved
  to reduce reliance on long-lived credentials stored in the API. A prime example
  of this shift is the transition of Kubernetes Service Account (KSA) tokens from
  long-lived, static tokens to ephemeral, automatically rotated tokens with OpenID
  Connect (OIDC)-compliant semantics. This advancement enables workloads to securely
  authenticate with external services without needing persistent secrets. However,
  one major gap remains: image pull authentication. Today, Kubernetes clusters rely
  on image pull secrets stored in the API, which are long-lived and difficult to rotate,
  or on node-level kubelet credential providers, which allow any pod running on a
  node to access the same credentials. This presents security and operational challenges.
  To address this, Kubernetes is introducing Service Account Token Integration for
  Kubelet Credential Providers , now available in alpha. This enhancement allows credential
  providers to use pod-specific service account tokens to obtain registry credentials,
  which kubelet can then use for image pulls — eliminating the need for long-lived
  image pull secrets. Currently, Kubernetes administrators have two primary options
  for handling private container image pulls: Image pull secrets stored in the Kubernetes
  API These secrets are often long-lived because they are hard to rotate. They must
  be explicitly attached to a service account or pod.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/07/kubernetes-v1-33-wi-for-image-pulls/
