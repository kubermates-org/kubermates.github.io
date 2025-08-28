---
title: Kubernetes Is Powerful, But Not Secure (at least not by default)
date: '2025-07-24T19:38:47+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/kubernetes-is-powerful-but-not-secure-at-least-not-by-default/
post_kind: link
draft: false
tldr: Kubernetes has transformed how we deploy and manage applications. It gives us
  the ability to spin up a virtual data center in minutes, scaling infrastructure
  with ease.
summary: Kubernetes has transformed how we deploy and manage applications. It gives
  us the ability to spin up a virtual data center in minutes, scaling infrastructure
  with ease. But with great power comes great complexities, and in the case of Kubernetes,
  that complexity is security. By default, Kubernetes permits all traffic between
  workloads in a cluster. This “allow by default” stance is convenient during development,
  and testing but it’s dangerous in production. It’s up to DevOps, DevSecOps, and
  cloud platform teams to lock things down. To improve the security posture of a Kubernetes
  cluster, we can use microsegmentation , a practice that limits each workload’s network
  reach so it can only talk to the specific resources it needs. This is an essential
  security method in today’s cloud-native environments. We all understand that network
  policies can achieve microsegmentation; or in other words, it can divide our Kubernetes
  network model into isolated pieces. This is important since Kubernetes is usually
  used to provide multiple teams with their infrastructural needs or host multiple
  workloads for different tenants. With that, you would think network policies are
  first citizens of clusters. However, when we dig into implementing them, three operational
  challenges make most practitioners reluctant about implementing policies.
---
Open the original post ↗ https://www.tigera.io/blog/kubernetes-is-powerful-but-not-secure-at-least-not-by-default/
