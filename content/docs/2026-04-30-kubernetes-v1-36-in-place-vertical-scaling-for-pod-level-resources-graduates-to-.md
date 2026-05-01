---
title: 'Kubernetes v1.36: In-Place Vertical Scaling for Pod-Level Resources Graduates
  to Beta'
date: '2026-04-30T10:35:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/04/30/kubernetes-v1-36-inplace-pod-level-resources-beta/
post_kind: link
draft: false
tldr: 'Kubernetes v1.36: In-Place Vertical Scaling for Pod-Level Resources Graduates
  to Beta Why Pod-level in-place resize? Resource inheritance and the resizePolicy
  Example: ccaling a shared resource pool 1. Initial Pod specification 2.'
summary: 'Kubernetes v1.36: In-Place Vertical Scaling for Pod-Level Resources Graduates
  to Beta Why Pod-level in-place resize? Resource inheritance and the resizePolicy
  Example: ccaling a shared resource pool 1. Initial Pod specification 2. The resize
  operation Node-Level reality: feasibility and safety 1. The feasibility check 2.
  Update sequencing Observability: tracking resize status Constraints and requirements
  What''s next? Getting started and providing feedback Following the graduation of
  Pod-Level Resources to Beta in v1.34 and the General Availability (GA) of In-Place
  Pod Vertical Scaling in v1.35, the Kubernetes community is thrilled to announce
  that In-Place Pod-Level Resources Vertical Scaling has graduated to Beta in v1.36!
  This feature is now enabled by default via the InPlacePodLevelResourcesVerticalScaling
  feature gate. It allows users to update the aggregate Pod resource budget (. spec.
  resources ) for a running Pod, often without requiring a container restart. InPlacePodLevelResourcesVerticalScaling.
  spec. resources The Pod-level resource model simplified management for complex Pods
  (such as those with sidecars) by allowing containers to share a collective pool
  of resources. In v1.36, you can now adjust this aggregate boundary on-the-fly.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/04/30/kubernetes-v1-36-inplace-pod-level-resources-beta/
