---
title: 'Why cloud native belongs at the heart of agentic AI: Lessons from building
  a multi-agent security platform on Kubernetes'
date: '2026-06-17T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/06/17/why-cloud-native-belongs-at-the-heart-of-agentic-ai-lessons-from-building-a-multi-agent-security-platform-on-kubernetes/
post_kind: link
draft: false
tldr: 1. Each agent is a Kubernetes workload, not an in-process module 2.
summary: '1. Each agent is a Kubernetes workload, not an in-process module 2. Inter-agent
  traffic needs mTLS, not a service mesh 3. Agent safety constraints are policy-as-code,
  not LLM prompt reasoning 4. Observability rides the A2A trace_id, GitOps owns the
  configuration 5. Gate the LLM with a classical anomaly model Keep the human in the
  loop, by protocol, not by culture How development and rollout actually go How the
  work is organised across teams and the community Why this stack About the author
  Posted on June 17, 2026 by Willem Berroubache, Lead Security Architect (Orange Innovation)
  and CNCF Golden Kubestronaut. In March, I gave a talk at KubeCon + CloudNativeCon
  Europe 2026 in Amsterdam. After the session, the same questions kept coming up on
  the CNCF Slack and in person: why build agentic AI on cloud native foundations at
  all? Which CNCF projects actually do the heavy lifting? Where does the human sit,
  and how do you organise the teams around it? What follows is the short answer, drawn
  from a system we are currently developing and rolling out at Orange Innovation.
  The context: an internal real-time security-operations platform protecting a regulated
  production environment, currently in active development with a rollout underway.
  A2A protocol for inter-agent coordination (open-sourced in 2025, now under the Linux
  Foundation). MCP for environment integration (hosted under the Agentic AI Foundation,
  an LF project). Falco with eBPF intercepts every syscall on the workloads we monitor;
  events flow through Kafka into an Isolation Forest classical anomaly model that
  pre-filters in front of the LLM-driven agents.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/06/17/why-cloud-native-belongs-at-the-heart-of-agentic-ai-lessons-from-building-a-multi-agent-security-platform-on-kubernetes/
