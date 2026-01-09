---
title: 'Kubernetes v1.35: A Better Way to Pass Service Account Tokens to CSI Drivers'
date: '2026-01-07T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/01/07/kubernetes-v1-35-csi-sa-tokens-secrets-field-beta/
post_kind: link
draft: false
tldr: 'Kubernetes v1.35: A Better Way to Pass Service Account Tokens to CSI Drivers
  Understanding the existing approach How the opt-in mechanism works About the beta
  release Guide for CSI driver authors Adding fallback logic Rollout sequence Important
  constraints Why this matters Call to action If you maintain a CSI driver that uses
  service account tokens, Kubernetes v1.35 brings a refinement you''ll want to know
  about. Since the introduction of the TokenRequests feature , service account tokens
  requested by CSI drivers have been passed to them through the volume_context field.'
summary: 'Kubernetes v1.35: A Better Way to Pass Service Account Tokens to CSI Drivers
  Understanding the existing approach How the opt-in mechanism works About the beta
  release Guide for CSI driver authors Adding fallback logic Rollout sequence Important
  constraints Why this matters Call to action If you maintain a CSI driver that uses
  service account tokens, Kubernetes v1.35 brings a refinement you''ll want to know
  about. Since the introduction of the TokenRequests feature , service account tokens
  requested by CSI drivers have been passed to them through the volume_context field.
  While this has worked, it''s not the ideal place for sensitive information, and
  we''ve seen instances where tokens were accidentally logged in CSI drivers. volume_context
  Kubernetes v1.35 introduces a beta solution to address this: CSI Driver Opt-in for
  Service Account Tokens via Secrets Field. This allows CSI drivers to receive service
  account tokens through the secrets field in NodePublishVolumeRequest , which is
  the appropriate place for sensitive data in the CSI specification. secrets NodePublishVolumeRequest
  When CSI drivers use the TokenRequests feature , they can request service account
  tokens for workload identity by configuring the TokenRequests field in the CSIDriver
  spec. These tokens are passed to drivers as part of the volume attributes map, using
  the key csi. storage. k8s. io/serviceAccount. tokens. TokenRequests csi.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/01/07/kubernetes-v1-35-csi-sa-tokens-secrets-field-beta/
