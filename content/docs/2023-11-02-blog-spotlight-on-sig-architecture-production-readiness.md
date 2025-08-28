---
title: 'Blog: Spotlight on SIG Architecture: Production Readiness'
date: '2023-11-02T00:00:00+00:00'
tags:
- kubernetes
- community
source: Kubernetes.dev Blog
external_url: https://www.kubernetes.dev/blog/2023/11/02/sig-architecture-production-readiness-spotlight-2023/
post_kind: link
draft: false
tldr: 'Spotlight on SIG Architecture: Production Readiness About SIG Architecture
  and the Production Readiness subproject Production readiness and the Kubernetes
  project Helping with Production Readiness This is the second interview of a SIG
  Architecture Spotlight series that will cover the different subprojects. In this
  blog, we will cover the SIG Architecture: Production Readiness subproject.'
summary: 'Spotlight on SIG Architecture: Production Readiness About SIG Architecture
  and the Production Readiness subproject Production readiness and the Kubernetes
  project Helping with Production Readiness This is the second interview of a SIG
  Architecture Spotlight series that will cover the different subprojects. In this
  blog, we will cover the SIG Architecture: Production Readiness subproject. In this
  SIG Architecture spotlight, we talked with Wojciech Tyczynski (Google), lead of
  the Production Readiness subproject. Frederico (FSM) : Hello Wojciech, could you
  tell us a bit about yourself, your role and how you got involved in Kubernetes?
  Wojciech Tyczynski (WT) : I started contributing to Kubernetes in January 2015.
  At that time, Google (where I was and still am working) decided to start a Kubernetes
  team in the Warsaw office (in addition to already existing teams in California and
  Seattle). I was lucky enough to be one of the seeding engineers for that team. After
  two months of onboarding and helping with different tasks across the project towards
  1.0 launch, I took ownership of the scalability area and I was leading Kubernetes
  to support clusters with 5000 nodes. I’m still involved in SIG Scalability as its
  Technical Lead. That was the start of a journey since scalability is such a cross-cutting
  topic, and I started contributing to many other areas including, over time, to SIG
  Architecture. FSM : In SIG Architecture, why specifically the Production Readiness
  subproject? Was it something you had in mind from the start, or was it an unexpected
  consequence of your initial involvement in scalability? WT : After reaching that
  milestone of Kubernetes supporting 5000-node clusters , one of the goals was to
  ensure that Kubernetes would not degrade its scalability properties over time. While
  non-scalable implementation is always fixable, designing non-scalable APIs or contracts
  is problematic. I was looking for a way to ensure that people are thinking about
  scalability when they create new features and capabilities without introducing too
  much overhead.'
---
Open the original post ↗ https://www.kubernetes.dev/blog/2023/11/02/sig-architecture-production-readiness-spotlight-2023/
