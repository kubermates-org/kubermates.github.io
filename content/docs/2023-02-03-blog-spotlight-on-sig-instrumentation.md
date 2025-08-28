---
title: 'Blog: Spotlight on SIG Instrumentation'
date: '2023-02-03T00:00:00+00:00'
tags:
- kubernetes
- community
source: Kubernetes.dev Blog
external_url: https://www.kubernetes.dev/blog/2023/02/03/sig-instrumentation-spotlight-2023/
post_kind: link
draft: false
tldr: Spotlight on SIG Instrumentation About SIG Instrumentation Current status and
  ongoing challenges Community and contribution Observability requires the right data
  at the right time for the right consumer (human or piece of software) to make the
  right decision. In the context of Kubernetes, having best practices for cluster
  observability across all Kubernetes components is crucial.
summary: 'Spotlight on SIG Instrumentation About SIG Instrumentation Current status
  and ongoing challenges Community and contribution Observability requires the right
  data at the right time for the right consumer (human or piece of software) to make
  the right decision. In the context of Kubernetes, having best practices for cluster
  observability across all Kubernetes components is crucial. SIG Instrumentation helps
  to address this issue by providing best practices and tools that all other SIGs
  use to instrument Kubernetes components-like the API server , scheduler , kubelet
  and kube-controller-manager. In this SIG Instrumentation spotlight, Imran Noor Mohamed
  , SIG ContribEx-Comms tech lead talked with Elana Hashman , and Han Kang , chairs
  of SIG Instrumentation, on how the SIG is organized, what are the current challenges
  and how anyone can get involved and contribute. Imran (INM) : Hello, thank you for
  the opportunity of learning more about SIG Instrumentation. Could you tell us a
  bit about yourself, your role, and how you got involved in SIG Instrumentation?
  Han (HK) : I started in SIG Instrumentation in 2018, and became a chair in 2020.
  I primarily got involved with SIG instrumentation due to a number of upstream issues
  with metrics which ended up affecting GKE in bad ways. As a result, we ended up
  launching an initiative to stabilize our metrics and make metrics a proper API.
  Elana (EH) : I also joined SIG Instrumentation in 2018 and became a chair at the
  same time as Han. I was working as a site reliability engineer (SRE) on bare metal
  Kubernetes clusters and was working to build out our observability stack. I encountered
  some issues with label joins where Kubernetes metrics didn’t match kube-state-metrics
  ( KSM ) and started participating in SIG meetings to improve things. I helped test
  performance improvements to kube-state-metrics and ultimately coauthored a KEP for
  overhauling metrics in the 1.14 release to improve usability.'
---
Open the original post ↗ https://www.kubernetes.dev/blog/2023/02/03/sig-instrumentation-spotlight-2023/
