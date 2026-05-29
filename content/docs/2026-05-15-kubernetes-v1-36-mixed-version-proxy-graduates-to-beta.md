---
title: 'Kubernetes v1.36: Mixed Version Proxy Graduates to Beta'
date: '2026-05-15T10:00:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/05/15/kubernetes-1-36-feature-mixed-version-proxy-beta/
post_kind: link
draft: false
tldr: 'Kubernetes v1.36: Mixed Version Proxy Graduates to Beta What problem are we
  solving? How has it evolved since 1.28 Required configuration Configuring with kubeadm
  Call to action Back in Kubernetes 1.28, we introduced the Mixed Version Proxy (MVP)
  as an Alpha feature (under the feature gate UnknownVersionInteroperabilityProxy
  ) in a previous blog post. The goal was simple but critical: make cluster upgrades
  safer by ensuring that requests for resources not yet known to an older API server
  are correctly routed to a newer peer API server, instead of returning an incorrect
  404 Not Found.'
summary: 'Kubernetes v1.36: Mixed Version Proxy Graduates to Beta What problem are
  we solving? How has it evolved since 1.28 Required configuration Configuring with
  kubeadm Call to action Back in Kubernetes 1.28, we introduced the Mixed Version
  Proxy (MVP) as an Alpha feature (under the feature gate UnknownVersionInteroperabilityProxy
  ) in a previous blog post. The goal was simple but critical: make cluster upgrades
  safer by ensuring that requests for resources not yet known to an older API server
  are correctly routed to a newer peer API server, instead of returning an incorrect
  404 Not Found. Mixed Version Proxy (MVP) UnknownVersionInteroperabilityProxy 404
  Not Found We are excited to announce that the Mixed Version Proxy is moving to Beta
  in Kubernetes 1.36 and will be enabled by default! The feature has evolved significantly
  since its initial release, addressing key gaps and modernizing its architecture.
  Here is a look at how the feature has evolved and what you need to know to leverage
  it in your clusters. In a highly available control plane undergoing an upgrade,
  you often have API servers running different versions. These servers might serve
  different sets of APIs (Groups, Versions, Resources). Without MVP, if a client request
  lands on an API server that does not serve the requested resource (e. g. , a new
  API version introduced in the upgrade), that server returns a 404 Not Found. This
  is technically incorrect because the resource is available in the cluster, just
  not on that specific server. This can lead to serious side effects, such as mistaken
  garbage collection or blocked namespace deletions. MVP solves this by proxying the
  request to a peer API server that can serve it.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/05/15/kubernetes-1-36-feature-mixed-version-proxy-beta/
