---
title: 'Red Hat AI and OpenShell: Driving security-enhanced agent execution for enterprise
  AI'
date: '2026-05-20T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/red-hat-ai-and-openshell-driving-security-enhanced-agent-execution-for-enterprise-ai
post_kind: link
draft: false
tldr: 'Red Hat AI and OpenShell: Driving security-enhanced agent execution for enterprise
  AI 3 ways to sandbox an agent OpenShell: kernel-enforced agent sandboxing Putting
  it to the test: OpenShell across agent platforms, frameworks, and agentic APIs Anthropic
  self-hosted sandboxes (Mode 2) Responses API with the Containers API (Mode 2) OpenAI
  Agents SDK sandbox extensions (Mode 3) Mode 1: Already works out of the box The
  next step for taking agents to production What comes next The adaptable enterprise:
  Why AI readiness is disruption readiness About the authors Adel Zaalouk Derek Carr
  Mrunal Patel Joe Fernandes More like this What even is the harness in AI? Bringing
  Claude self-hosted sandboxes to OpenShell on Red Hat AI Technically Speaking | Build
  a production-ready AI toolbox Technically Speaking | Platform engineering for AI
  agents Keep exploring Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share AI agents are no longer passive assistants. They write code, call APIs, install
  packages, and interact with production systems.'
summary: 'Red Hat AI and OpenShell: Driving security-enhanced agent execution for
  enterprise AI 3 ways to sandbox an agent OpenShell: kernel-enforced agent sandboxing
  Putting it to the test: OpenShell across agent platforms, frameworks, and agentic
  APIs Anthropic self-hosted sandboxes (Mode 2) Responses API with the Containers
  API (Mode 2) OpenAI Agents SDK sandbox extensions (Mode 3) Mode 1: Already works
  out of the box The next step for taking agents to production What comes next The
  adaptable enterprise: Why AI readiness is disruption readiness About the authors
  Adel Zaalouk Derek Carr Mrunal Patel Joe Fernandes More like this What even is the
  harness in AI? Bringing Claude self-hosted sandboxes to OpenShell on Red Hat AI
  Technically Speaking | Build a production-ready AI toolbox Technically Speaking
  | Platform engineering for AI agents Keep exploring Browse by channel Automation
  Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share AI agents are no longer passive assistants. They
  write code, call APIs, install packages, and interact with production systems. This
  shift from passive to active changes not only the usefulness of agents, but also
  the security question around their activities entirely. When an agent can only generate
  text, the worst outcome is a bad answer. When an agent can execute code, the worst
  outcome is a deleted production database. That happened last month. 9 seconds, no
  rollback,no recovery. The question every enterprise team hits sooner or later: how
  do you safely allow AI agents to execute code and interact with enterprise systems?
  In a recent post , we outlined a 6-layer defense-in-depth framework for enhancing
  the security posture of AI agents on Red Hat AI. This post goes deeper into one
  of those layers: secure sandboxed execution, and how we validated it across various
  agent frameworks, APIs, and platforms. Running agent-generated code directly on
  developer laptops, shared infrastructure, or unrestricted runtime environments introduces
  real risk. Enterprises need isolation boundaries, policy enforcement, credential
  protection, and runtime audit controls before these systems can be trusted in production.
  At Red Hat, we have been working on bringing secure sandboxed execution into Red
  Hat AI through a collaboration with NVIDIA on OpenShell.'
---
Open the original post ↗ https://www.redhat.com/en/blog/red-hat-ai-and-openshell-driving-security-enhanced-agent-execution-for-enterprise-ai
