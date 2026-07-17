---
title: Operating OpenTelemetry at scale with OpAMP
date: '2026-07-13T11:30:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/07/13/operating-opentelemetry-at-scale-with-opamp/
post_kind: link
draft: false
tldr: 'Why OpAMP: The management challenge at scale Scale and variety of OTel Collector
  deployments What is the Open Agent Management Protocol (OpAMP) OpAMP protocol and
  components Beyond OTel Collector: OpAMP for Kubernetes, SDKs and more Hot off the
  press: OpAMP Gateway Extension OpAMP roadmap Posted on July 13, 2026 by Dotan Horovits,
  CNCF Ambassador CNCF projects highlighted in this post As more organizations move
  to use OpenTelemetry in production at scale, with multiple Collectors across heterogeneous
  environments, a new challenge arises: how to remotely manage, configure, and update
  this agent fleet in a consistent and secure way? This is where Open Agent Management
  Protocol (OpAMP) comes into the picture: it provides a standardized protocol that
  lets a central backend automatically configure agents, push updates, monitor their
  health, and collect status information. In a recent episode of OpenObservability
  Talks, I sat down with Andy Keller, OpAMP maintainer and Principal Engineer at BindPlane,
  to hear what OpAMP is and how it makes large-scale observability deployments much
  easier to operate and control.'
summary: 'Why OpAMP: The management challenge at scale Scale and variety of OTel Collector
  deployments What is the Open Agent Management Protocol (OpAMP) OpAMP protocol and
  components Beyond OTel Collector: OpAMP for Kubernetes, SDKs and more Hot off the
  press: OpAMP Gateway Extension OpAMP roadmap Posted on July 13, 2026 by Dotan Horovits,
  CNCF Ambassador CNCF projects highlighted in this post As more organizations move
  to use OpenTelemetry in production at scale, with multiple Collectors across heterogeneous
  environments, a new challenge arises: how to remotely manage, configure, and update
  this agent fleet in a consistent and secure way? This is where Open Agent Management
  Protocol (OpAMP) comes into the picture: it provides a standardized protocol that
  lets a central backend automatically configure agents, push updates, monitor their
  health, and collect status information. In a recent episode of OpenObservability
  Talks, I sat down with Andy Keller, OpAMP maintainer and Principal Engineer at BindPlane,
  to hear what OpAMP is and how it makes large-scale observability deployments much
  easier to operate and control. We also covered project status and roadmap, including
  a hot KubeCon update you don’t want to miss. OpenObservability Talks: Operating
  OpenTelemetry at Scale with OpAMP As OpenTelemetry adoption has exploded, organizations
  are finding themselves managing increasingly complex collector deployments. Before
  OpAMP, the landscape was fragmented and challenging. Andy shared their journey:
  “We probably developed in-house three, four, maybe five different agent management
  protocols. Some were HTTP-based, long polling. We used WebSockets. We used protobufs.
  We used JSON. ” The problem becomes acute when you consider the scale and variety
  of deployments. We’re not just talking about a handful of collectors — organizations
  are deploying collectors everywhere from massive gateways to embedded devices.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/07/13/operating-opentelemetry-at-scale-with-opamp/
