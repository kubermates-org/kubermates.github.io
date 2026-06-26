---
title: 'How Lynx Works: A Technical Walkthrough'
date: '2026-06-18T17:19:30+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/how-lynx-works-a-technical-walkthrough/
post_kind: link
draft: false
tldr: 'The constraints we started from The data model Identity: reuse what you already
  trust One gateway for A2A, MCP, and LLM The data plane: drive the proxy, don’t fork
  it The decision point: policy in the path, credentials minted per hop Catching what
  routes around the gateway Agent sandboxing Tracing, audit, and compliance Driving
  Lynx: dashboard, CLI, and MCP Built on open standards How it installs We launched
  Lynx this week. Instead of restating the pitch, I want to explain how it’s built
  and why we made the architectural choices we did.'
summary: 'The constraints we started from The data model Identity: reuse what you
  already trust One gateway for A2A, MCP, and LLM The data plane: drive the proxy,
  don’t fork it The decision point: policy in the path, credentials minted per hop
  Catching what routes around the gateway Agent sandboxing Tracing, audit, and compliance
  Driving Lynx: dashboard, CLI, and MCP Built on open standards How it installs We
  launched Lynx this week. Instead of restating the pitch, I want to explain how it’s
  built and why we made the architectural choices we did. If you run Kubernetes and
  you’re starting to put AI agents on it, this is roughly the system you’d end up
  designing yourself. Lynx is a control and data plane for all agentic AI traffic,
  providing a registry, gateway, audit, authentication with token exchange, policy
  enforcement, agent sandboxing, shadow agent discovery, and advanced AI capabilities
  such as red team agent and a guardian supervising agent to keep your agents on track.
  Lynx is single control point in the path of every agent call – agent-to-agent, agent-to-MCP,
  agent-to-LLM. Every call is authenticated, authorized against policy, and recorded,
  with no changes to agent code. Four principles shaped the design: No agent code
  changes. Governance has to be applied by the platform, not adopted as a library.
  If it requires a code change, it won’t land uniformly – and uniformity is the entire
  point. No new database in the control plane. The source of truth is the Kubernetes
  API server and the data model is custom resources – there’s no separate datastore
  to run, back up, and secure. (Telemetry is the one thing that needs a column store
  at scale; that’s kept separate and is bring-your-own.'
---
Open the original post ↗ https://www.tigera.io/blog/how-lynx-works-a-technical-walkthrough/
