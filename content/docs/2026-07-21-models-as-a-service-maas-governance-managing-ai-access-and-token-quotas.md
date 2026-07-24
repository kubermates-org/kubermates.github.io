---
title: 'Models-as-a-Service (MaaS) governance: Managing AI access and token quotas'
date: '2026-07-21T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/models-service-maas-governance-managing-ai-access-and-token-quotas
post_kind: link
draft: false
tldr: 'Models-as-a-Service (MaaS) governance: Managing AI access and token quotas
  Subscriptions: Quota-backed entitlements AuthPolicies: Access rules The 2-gate system
  Fitting MaaS to your organization How organizations map their structure to policy
  Going deeper The adaptable enterprise: Why AI readiness is disruption readiness
  About the author Chaitanya Kulkarni More like this Why single AI agents fail at
  scale: Building governed multi-agent networks Why prompt-level guardrails aren''t
  enough: The platform security layers production agents need Technically Speaking
  | Defining sovereign AI with open source Technically Speaking | Inside open source
  AI strategy Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share In our previous post , we talked about the API key lifecycle in MaaS. In this
  article, we''ll set up the governance layer those keys bind to, focusing on 2 core
  controls: managing token quotas (via MaaSSubscription ) and defining model access
  rules (via MaaSAuthPolicy ).'
summary: 'Models-as-a-Service (MaaS) governance: Managing AI access and token quotas
  Subscriptions: Quota-backed entitlements AuthPolicies: Access rules The 2-gate system
  Fitting MaaS to your organization How organizations map their structure to policy
  Going deeper The adaptable enterprise: Why AI readiness is disruption readiness
  About the author Chaitanya Kulkarni More like this Why single AI agents fail at
  scale: Building governed multi-agent networks Why prompt-level guardrails aren''t
  enough: The platform security layers production agents need Technically Speaking
  | Defining sovereign AI with open source Technically Speaking | Inside open source
  AI strategy Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share In our previous post , we talked about the API key lifecycle in MaaS. In this
  article, we''ll set up the governance layer those keys bind to, focusing on 2 core
  controls: managing token quotas (via MaaSSubscription ) and defining model access
  rules (via MaaSAuthPolicy ). Models-as-a-Service (MaaS), an integrated component
  of Red Hat Openshift AI , aims to give enterprises a flexible GitOps friendly way
  to set up their policy framework. Both attach to models through a MaaSModelRef :
  MaaSSubscription defines how much a user can consume in a given time window. MaaSAuthPolicy
  defines which models a user is permitted to call. A MaaSSubscription defines the
  quota. It declares an owner (groups or users) and defines how many tokens they can
  consume within a time window. When an application creates an API key, that key binds
  to a subscription. The bound subscription travels with every request the key makes.
  The platform enforces the limits continuously; administrators do not watch and adjust
  them by hand. A subscription can define a quota for a single model, or all the models
  across your enterprise. This gives enterprises flexibility in how they want to define
  the subscription and entitlement approach that maps people and workloads to specific
  models, instead of forcing a single "one size fits all" subscription shape.'
---
Open the original post ↗ https://www.redhat.com/en/blog/models-service-maas-governance-managing-ai-access-and-token-quotas
