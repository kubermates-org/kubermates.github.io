---
title: Solving Kubernetes Multi-tenancy Challenges with vCluster
date: '2025-09-23T16:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/09/23/solving-kubernetes-multi-tenancy-challenges-with-vcluster/
post_kind: link
draft: false
tldr: Understanding Multi-tenancy Multi-tenancy with native Kubernetes features Control
  Plane Isolation Data Plane Isolation vCluster Concept Hands-on Prerequisites Deploy
  a virtual cluster Deploy workload Deploy a CRD Hands-on summary Interaction with
  host applications Falco Kyverno Implications Summary Outlook References Posted on
  September 23, 2025 by Fabian Brundke, Senior Platform Engineer, Liquid Reply CNCF
  projects highlighted in this post When we are building Internal Developer Platforms
  (IDP) for our customers Kubernetes is often a solid choice as the robust core of
  this platform. This is due to its technical capabilities and the strong community
  that is constantly expanding the surrounding ecosystem.
summary: Understanding Multi-tenancy Multi-tenancy with native Kubernetes features
  Control Plane Isolation Data Plane Isolation vCluster Concept Hands-on Prerequisites
  Deploy a virtual cluster Deploy workload Deploy a CRD Hands-on summary Interaction
  with host applications Falco Kyverno Implications Summary Outlook References Posted
  on September 23, 2025 by Fabian Brundke, Senior Platform Engineer, Liquid Reply
  CNCF projects highlighted in this post When we are building Internal Developer Platforms
  (IDP) for our customers Kubernetes is often a solid choice as the robust core of
  this platform. This is due to its technical capabilities and the strong community
  that is constantly expanding the surrounding ecosystem. One common IDP use case
  is to support the software development lifecycle (SDLC) of multiple tenants (e.
  g. multiple applications or software engineering teams). Adopting Kubernetes helps
  to share resources among these different tenants and while this helps to – among
  other benefits – optimize costs and enforce standards, it also introduces the challenge
  of isolating workloads from each other. This is known as multi-tenancy and for an
  IDP we have to ensure that this isolation is fair and secure. Thankfully Kubernetes
  provides a few out-of-the-box features to support isolation in a multi-tenant setup.
  This isolation can happen for the control plane and data plane. Let’s briefly describe
  these features. Namespaces are used to group different resources for tenants into
  logical units. While this allows you to effectively apply e.
---
Open the original post ↗ https://www.cncf.io/blog/2025/09/23/solving-kubernetes-multi-tenancy-challenges-with-vcluster/
