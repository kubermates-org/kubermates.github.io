---
title: I made a policy engine think it was in production
date: '2026-07-22T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/07/22/i-made-a-policy-engine-think-it-was-in-production/
post_kind: link
draft: false
tldr: 'Week one: The Codebase wins Clearing the ground The disguise Foundation fixes
  New offline capabilities New CLI Flags and policy type support Documentation What
  I would tell someone starting out Posted on July 22, 2026 by Sargam Puram, Kyverno
  Project Maintainer CNCF projects highlighted in this post Kyverno is a Kubernetes-native
  policy engine that validates, mutates, and generates resources before workloads
  reach your cluster, enforcing security and compliance rules as code, without requiring
  a separate policy language. Enterprise teams running Kyverno policies in production
  face a specific, painful problem.'
summary: 'Week one: The Codebase wins Clearing the ground The disguise Foundation
  fixes New offline capabilities New CLI Flags and policy type support Documentation
  What I would tell someone starting out Posted on July 22, 2026 by Sargam Puram,
  Kyverno Project Maintainer CNCF projects highlighted in this post Kyverno is a Kubernetes-native
  policy engine that validates, mutates, and generates resources before workloads
  reach your cluster, enforcing security and compliance rules as code, without requiring
  a separate policy language. Enterprise teams running Kyverno policies in production
  face a specific, painful problem. Their policies use GlobalContextEntry references
  – at evaluation time, the engine looks up live Kubernetes resources to make decisions.
  In a real cluster, this works perfectly. In CI/CD, without a live API server, the
  CLI has nowhere to resolve those lookups. Tests panic. Rules are silently skipped.
  Policy reports show results that bear no relationship to what will actually happen
  in production. This was not a theoretical gap. It was the documented, open state
  of the Kyverno CLI at the start of 2026. And closing it was the problem I was handed
  as a Spring 2026 LFX Mentee. GlobalContextEntry I am a final-year Computer Engineering
  undergraduate.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/07/22/i-made-a-policy-engine-think-it-was-in-production/
