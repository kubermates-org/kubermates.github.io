---
title: 'Kubernetes v1.36: Staleness Mitigation and Observability for Controllers'
date: '2026-04-28T10:35:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/04/28/kubernetes-v1-36-staleness-mitigation-for-controllers/
post_kind: link
draft: false
tldr: 'Kubernetes v1.36: Staleness Mitigation and Observability for Controllers What
  is staleness? Improvements in 1.36 client-go improvements kube-controller-manager
  improvements Use for informer authors Observability Metrics What''s next? Staleness
  in Kubernetes controllers is a problem that affects many controllers, and is something
  may affect controller behavior in subtle ways. It is usually not until it is too
  late, when a controller in production has already taken incorrect action, that staleness
  is found to be an issue due to some underlying assumption made by the controller
  author.'
summary: 'Kubernetes v1.36: Staleness Mitigation and Observability for Controllers
  What is staleness? Improvements in 1.36 client-go improvements kube-controller-manager
  improvements Use for informer authors Observability Metrics What''s next? Staleness
  in Kubernetes controllers is a problem that affects many controllers, and is something
  may affect controller behavior in subtle ways. It is usually not until it is too
  late, when a controller in production has already taken incorrect action, that staleness
  is found to be an issue due to some underlying assumption made by the controller
  author. Some issues caused by staleness include controllers taking incorrect actions,
  controllers not taking action when they should, and controllers taking too long
  to take action. I am excited to announce that Kubernetes v1.36 includes new features
  that help mitigate staleness in controllers and provide better observability into
  controller behavior. Staleness in controllers comes from an outdated view of the
  world inside of the controller cache. In order to provide a fast user experience,
  controllers typically maintain a local cache of the state of the cluster. This cache
  is populated by watching the Kubernetes API server for changes to objects that the
  controller cares about. When the controller needs to take action, it will first
  check its cache to see if it has the latest information. If it does not, it will
  then update its cache by watching the API server for changes to objects that the
  controller cares about. This process is known as reconciliation. However, there
  are some cases where the controller''s cache may be outdated. For example, if the
  controller is restarted, it will need to rebuild its cache by watching the API server
  for changes to objects that the controller cares about.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/04/28/kubernetes-v1-36-staleness-mitigation-for-controllers/
