---
title: 'Kubernetes v1.34: Service Account Token Integration for Image Pulls Graduates
  to Beta'
date: '2025-09-03T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/09/03/kubernetes-v1-34-sa-tokens-image-pulls-beta/
post_kind: link
draft: false
tldr: 'Kubernetes v1.34: Service Account Token Integration for Image Pulls Graduates
  to Beta What''s new in beta? Required cacheType field Isolated image pull credentials
  How it works Configuration Image pull flow Audience restriction Getting started
  with beta Prerequisites Migration from alpha Example setup What''s next? Call to
  action How to get involved The Kubernetes community continues to advance security
  best practices by reducing reliance on long-lived credentials. Following the successful
  alpha release in Kubernetes v1.33 , Service Account Token Integration for Kubelet
  Credential Providers has now graduated to beta in Kubernetes v1.34, bringing us
  closer to eliminating long-lived image pull secrets from Kubernetes clusters.'
summary: 'Kubernetes v1.34: Service Account Token Integration for Image Pulls Graduates
  to Beta What''s new in beta? Required cacheType field Isolated image pull credentials
  How it works Configuration Image pull flow Audience restriction Getting started
  with beta Prerequisites Migration from alpha Example setup What''s next? Call to
  action How to get involved The Kubernetes community continues to advance security
  best practices by reducing reliance on long-lived credentials. Following the successful
  alpha release in Kubernetes v1.33 , Service Account Token Integration for Kubelet
  Credential Providers has now graduated to beta in Kubernetes v1.34, bringing us
  closer to eliminating long-lived image pull secrets from Kubernetes clusters. This
  enhancement allows credential providers to use workload-specific service account
  tokens to obtain registry credentials, providing a secure, ephemeral alternative
  to traditional image pull secrets. The beta graduation brings several important
  changes that make the feature more robust and production-ready: cacheType Breaking
  change from alpha : The cacheType field is required in the credential provider configuration
  when using service account tokens. This field is new in beta and must be specified
  to ensure proper caching behavior. cacheType # CAUTION: this is not a complete configuration
  example, just a reference for the ''tokenAttributes. cacheType'' field. tokenAttributes
  : serviceAccountTokenAudience : "my-registry-audience" cacheType : "ServiceAccount"
  # Required field in beta requireServiceAccount : true # CAUTION: this is not a complete
  configuration example, just a reference for the ''tokenAttributes. cacheType'' field.
  tokenAttributes : serviceAccountTokenAudience : "my-registry-audience" cacheType
  : "ServiceAccount" # Required field in beta requireServiceAccount : true Choose
  between two caching strategies: Token : Cache credentials per service account token
  (use when credential lifetime is tied to the token). This is useful when the credential
  provider transforms the service account token into registry credentials with the
  same lifetime as the token, or when registries support Kubernetes service account
  tokens directly. Note: The kubelet cannot send service account tokens directly to
  registries; credential provider plugins are needed to transform tokens into the
  username/password format expected by registries.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/09/03/kubernetes-v1-34-sa-tokens-image-pulls-beta/
