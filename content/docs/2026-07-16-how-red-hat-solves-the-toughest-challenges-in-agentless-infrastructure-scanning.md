---
title: How Red Hat solves the toughest challenges in agentless infrastructure scanning
date: '2026-07-16T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/how-red-hat-solves-toughest-challenges-agentless-infrastructure-scanning
post_kind: link
draft: false
tldr: 'How Red Hat solves the toughest challenges in agentless infrastructure scanning
  What your security team needs to know about discovery Core security architecture
  Network footprint Anatomy of a discovery scan from start to finish Phase 1: Setup
  and definition Phase 2: Connection Phase 3: Interrogation Phase 4: Assembly and
  deduplication Phase 5: Results and action How Red Hat implemented agentless scanning
  at scale Next steps Red Hat Enterprise Linux | Product trial About the author Justin
  Kreft More like this Red Hat Enterprise Linux Long-Life Add-On: Your path to RHEL
  with no pre-determined end date Satellite 6.19 delivers Red Hat Lightspeed on premise
  security monitoring Infrastructure At The Edge | Compiler Operating System Management
  | Compiler Keep exploring Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share Enterprises want absolute clarity on their IT footprint: they want to know
  exactly what software is running, where it’s running, and how those deployments
  align with subscription entitlements. For many organizations, Red Hat Hybrid Cloud
  Console and subscription watch provide that visibility.'
summary: 'How Red Hat solves the toughest challenges in agentless infrastructure scanning
  What your security team needs to know about discovery Core security architecture
  Network footprint Anatomy of a discovery scan from start to finish Phase 1: Setup
  and definition Phase 2: Connection Phase 3: Interrogation Phase 4: Assembly and
  deduplication Phase 5: Results and action How Red Hat implemented agentless scanning
  at scale Next steps Red Hat Enterprise Linux | Product trial About the author Justin
  Kreft More like this Red Hat Enterprise Linux Long-Life Add-On: Your path to RHEL
  with no pre-determined end date Satellite 6.19 delivers Red Hat Lightspeed on premise
  security monitoring Infrastructure At The Edge | Compiler Operating System Management
  | Compiler Keep exploring Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share Enterprises want absolute clarity on their IT footprint: they want to know
  exactly what software is running, where it’s running, and how those deployments
  align with subscription entitlements. For many organizations, Red Hat Hybrid Cloud
  Console and subscription watch provide that visibility. But what happens when your
  infrastructure can''t (or shouldn''t) phone home? Air-gapped networks, government
  systems, manufacturing floors, and sovereign clouds all require a completely disconnected
  approach. That is exactly why we built discovery , an open source, agentless scanning
  tool that is a component of Red Hat Lightspeed and is designed to run entirely within
  your infrastructure. It scans your network environments, including IP ranges, hostnames,
  vCenter connections, and Red Hat Satellite servers to identify exactly which Red
  Hat products are deployed, including Red Hat Enterprise Linux (RHEL), Red Hat OpenShift
  Container Platform, Red Hat Ansible Automation Platform, or JBoss. Discovery can
  also determine the version numbers and infrastructure footprint for all these products.
  It is entirely configurable by you. This blog post will look under the hood of discovery,
  covering what your security team needs to know, how a scan executes from start to
  finish, and how we are solving the hardest engineering problems in enterprise-scale
  agentless scanning. Any tool that requires network access and credentials deserves
  rigorous scrutiny, and discovery is engineered to make that security review as straightforward
  as possible. Completely agentless: Discovery leaves no footprint on your target
  systems. There are no persistent agents to maintain, no background daemons to patch,
  and no software left behind. Strictly read-only: Once connected, discovery only
  reads system metadata, configuration files, and package registries.'
---
Open the original post ↗ https://www.redhat.com/en/blog/how-red-hat-solves-toughest-challenges-agentless-infrastructure-scanning
