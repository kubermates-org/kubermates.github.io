---
title: Building a cloud native platform from the ground up with Kairos, k0rdent, and
  bindy
date: '2026-05-13T11:30:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/05/13/building-a-cloud-native-platform-from-the-ground-up-with-kairos-k0rdent-and-bindy/
post_kind: link
draft: false
tldr: 'The challenge: Platform engineering at scale in a regulated environment Kairos:
  Immutable OS for nodes you can trust A CI/CD pipeline for operating system images
  Kubernetes-native VM provisioning with VirtRigaud k0rdent: Cluster lifecycle management
  as a platform bindy: Kubernetes-native DNS operations How the three fit together
  Challenges and lessons learned Looking ahead Posted on May 13, 2026 by Erick Bourgeois,
  Director & Head of Kubernetes Platform Engineering, RBC Capital Markets CNCF projects
  highlighted in this post As we shared in our earlier post on FluxCD , RBC Capital
  Markets has been on a deliberate journey to modernize our Kubernetes platform. GitOps
  with FluxCD gave us a solid deployment foundation.'
summary: 'The challenge: Platform engineering at scale in a regulated environment
  Kairos: Immutable OS for nodes you can trust A CI/CD pipeline for operating system
  images Kubernetes-native VM provisioning with VirtRigaud k0rdent: Cluster lifecycle
  management as a platform bindy: Kubernetes-native DNS operations How the three fit
  together Challenges and lessons learned Looking ahead Posted on May 13, 2026 by
  Erick Bourgeois, Director & Head of Kubernetes Platform Engineering, RBC Capital
  Markets CNCF projects highlighted in this post As we shared in our earlier post
  on FluxCD , RBC Capital Markets has been on a deliberate journey to modernize our
  Kubernetes platform. GitOps with FluxCD gave us a solid deployment foundation. But
  as our platform grew, today we operate over 50 clusters spanning on-premises VMware
  environments and multiple clouds, we hit a set of problems that no single off-the-shelf
  tool was designed to solve together: How do you manage the lifecycle of the clusters
  themselves? How do you ensure every node is reproducible and tamper-evident at boot?
  And how do you integrate Kubernetes service discovery with enterprise DNS infrastructure
  without every record change going through a ticket queue? This post is about the
  several projects that answered those questions for us, and what we learned building
  with them inside a regulated financial institution. Managing 50+ Kubernetes clusters
  across hybrid infrastructure is not just an operational challenge, in capital markets
  it is also a compliance challenge. SOX, PCI-DSS, and Basel III create real requirements
  around auditability, configuration drift prevention, and network segmentation. Our
  platform teams cannot afford to have snowflake nodes, undocumented cluster state,
  or manual DNS records that accumulate over years. When we stepped back and looked
  at what we were spending engineering effort on, three gaps stood out: Node configuration
  drift: VM-based nodes that had been patched and mutated over time were becoming
  impossible to reason about. Cluster provisioning: spinning up new clusters for trading
  desks or risk teams was a multi-day manual exercise with no single source of truth.
  DNS integration: every new service or ingress endpoint required a manual ticket
  to our network team, creating a bottleneck and an audit trail that lived outside
  our GitOps workflow. We decided to solve each of these from the ground up, using
  cloud-native projects where they existed and building our own where they did not.
  The first piece of the puzzle was node immutability. We evaluated several approaches,
  but Kairos , a CNCF Sandbox project, aligned most directly with what we needed:
  a Linux distribution designed from first principles to be immutable, declaratively
  configured, and reproducible.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/05/13/building-a-cloud-native-platform-from-the-ground-up-with-kairos-k0rdent-and-bindy/
