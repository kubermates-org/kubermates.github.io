---
title: Is a Pod the right deployment unit for an AI agent?
date: '2026-07-14T11:20:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/07/14/is-a-pod-the-right-deployment-unit-for-an-ai-agent/
post_kind: link
draft: false
tldr: The Pod as the Deployment Unit But Should Agents Be Best Represented as Pods?
  Enter Agent-substrate Challenging More Than Deployment Model Agent Identity Security
  and Policy Ownership and Multi-tenancy Observability Looking Ahead Posted on July
  14, 2026 by Lin Sun, Solo. io | CNCF Ambassador When we first started building kagent,
  we didn’t run every agent in its own Kubernetes Pod, Service, and ServiceAccount.
summary: 'The Pod as the Deployment Unit But Should Agents Be Best Represented as
  Pods? Enter Agent-substrate Challenging More Than Deployment Model Agent Identity
  Security and Policy Ownership and Multi-tenancy Observability Looking Ahead Posted
  on July 14, 2026 by Lin Sun, Solo. io | CNCF Ambassador When we first started building
  kagent, we didn’t run every agent in its own Kubernetes Pod, Service, and ServiceAccount.
  Instead, agents were simply executed inside the kagent runtime. It was the simplest
  architecture possible: one runtime hosting many agents. It worked well for demos
  and proofs of concept. As the number of agents grew, however, fundamental questions
  started to emerge. How do we isolate one agent from another? How does each agent
  get its own identity? How do we enforce access and network policies? How do we understand
  what an individual agent is doing? Who owns an agent, and how do we support multi-tenancy?
  These aren’t Kubernetes questions. They’re agent platform questions. Our first answer
  was straightforward: run every agent in its own Pod, Service, and ServiceAccount.
  That decision immediately solved many of our problems. A Pod provides process and
  container isolation. A ServiceAccount gives every agent its own Kubernetes identity,
  allowing us to integrate naturally with authentication and authorization mechanisms.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/07/14/is-a-pod-the-right-deployment-unit-for-an-ai-agent/
