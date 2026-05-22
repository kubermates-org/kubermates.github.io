---
title: 'Kubernetes v1.36: Fine-Grained Kubelet API Authorization Graduates to GA'
date: '2026-04-24T10:35:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/04/24/kubernetes-v1-36-fine-grained-kubelet-authorization-ga/
post_kind: link
draft: false
tldr: 'Kubernetes v1.36: Fine-Grained Kubelet API Authorization Graduates to GA Motivation:
  the nodes/proxy problem What''s wrong with that? The nodes/proxy GET WebSocket RCE
  risk Fine-grained kubelet authorization: how it works What this means in practice
  Updated system:kubelet-api-admin ClusterRole Upgrade considerations Verifying the
  feature is enabled The journey from alpha to GA What''s next? Getting involved On
  behalf of Kubernetes SIG Auth and SIG Node, we are pleased to announce the graduation
  of fine-grained kubelet API authorization to General Availability (GA) in Kubernetes
  v1.36! kubelet The KubeletFineGrainedAuthz feature gate was introduced as an opt-in
  alpha feature in Kubernetes v1.32, then graduated to beta (enabled by default) in
  v1.33. Now, the feature is generally available and the feature gate is locked to
  enabled.'
summary: 'Kubernetes v1.36: Fine-Grained Kubelet API Authorization Graduates to GA
  Motivation: the nodes/proxy problem What''s wrong with that? The nodes/proxy GET
  WebSocket RCE risk Fine-grained kubelet authorization: how it works What this means
  in practice Updated system:kubelet-api-admin ClusterRole Upgrade considerations
  Verifying the feature is enabled The journey from alpha to GA What''s next? Getting
  involved On behalf of Kubernetes SIG Auth and SIG Node, we are pleased to announce
  the graduation of fine-grained kubelet API authorization to General Availability
  (GA) in Kubernetes v1.36! kubelet The KubeletFineGrainedAuthz feature gate was introduced
  as an opt-in alpha feature in Kubernetes v1.32, then graduated to beta (enabled
  by default) in v1.33. Now, the feature is generally available and the feature gate
  is locked to enabled. This feature enables more precise, least-privilege access
  control over the kubelet ''s HTTPS API, replacing the need to grant the overly broad
  nodes/proxy permission for common monitoring and observability use cases. KubeletFineGrainedAuthz
  kubelet nodes/proxy nodes/proxy The kubelet exposes an HTTPS endpoint with several
  APIs that give access to data of varying sensitivity, including pod listings, node
  metrics, container logs, and, critically, the ability to execute commands inside
  running containers. kubelet Prior to this feature, kubelet authorization used a
  coarse-grained model. When webhook authorization was enabled, almost all kubelet
  API paths were mapped to a single nodes/proxy subresource. This meant that any workload
  needing to read metrics or health status from the kubelet required nodes/proxy permission,
  the same permission that also grants the ability to execute arbitrary commands in
  any container running on the node. kubelet kubelet nodes/proxy kubelet nodes/proxy
  Granting nodes/proxy to monitoring agents, log collectors, or health-checking tools
  violates the principle of least privilege. If any of those workloads were compromised,
  an attacker would gain the ability to run commands in every container on the node.
  The nodes/proxy permission is effectively a node-level superuser capability, and
  granting it broadly dramatically increases the blast radius of a security incident.
  nodes/proxy nodes/proxy This problem has been well understood in the community for
  years (see kubernetes/kubernetes#83465 ), and was the driving motivation behind
  this enhancement KEP-2862. nodes/proxy GET The situation is more severe than it
  might appear at first glance.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/04/24/kubernetes-v1-36-fine-grained-kubelet-authorization-ga/
