---
title: How to get started with Calico Observability features
date: '2025-04-15T15:37:28+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/how-to-get-started-with-calico-observability-features/
post_kind: link
draft: false
tldr: Kubernetes, by default, adopts a permissive networking model where all pods
  can freely communicate unless explicitly restricted using network policies. While
  this simplifies application deployment, it introduces significant security risks.
summary: 'Kubernetes, by default, adopts a permissive networking model where all pods
  can freely communicate unless explicitly restricted using network policies. While
  this simplifies application deployment, it introduces significant security risks.
  Unrestricted network traffic allows workloads to interact with unauthorized destinations,
  increasing the potential for cyberattacks such as Remote Code Execution (RCE), DNS
  spoofing, and privilege escalation. To better understand these problems, let’s examine
  a sample Kubernetes application: ANP Demo App. This application comprises a deployment
  that spawns pods and a service that exposes them to external users in a similar
  situation like any real word workload which you will encounter in your environment.
  If you open the application service before implementing any policies, the application
  reports the following messages: In this blog post we are going through a scenario
  to secure our cluster by preventing our workloads from accessing the external resources.
  Number 1 and 3 from the previous list. In Kubernetes, the default permissive networking
  model, where all pods can freely communicate, poses a significant security challenge.
  While network policies are crucial for enforcing a Zero Trust security model, identifying
  the necessary network flows for an application to function correctly can be difficult.
  Using CLI tools to inspect network traffic and deduce the required policies can
  be a complex and time-consuming task. It often involves sifting through large amounts
  of data and requires a deep understanding of network protocols and Kubernetes internals.
  Even for experienced administrators, accurately capturing all necessary flows without
  disrupting application functionality is a challenge.'
---
Open the original post ↗ https://www.tigera.io/blog/how-to-get-started-with-calico-observability-features/
