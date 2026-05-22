---
title: Bringing Claude self-hosted sandboxes to OpenShell on Red Hat AI
date: '2026-05-20T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/bringing-claude-self-hosted-sandboxes-to-openshell-on-red-hat-ai
post_kind: link
draft: false
tldr: 'Bringing Claude self-hosted sandboxes to OpenShell on Red Hat AI Outsource
  the thinking, keep the doing Greater security posture for execution (the where)
  How it works together From laptop to cluster on the same architecture Why this matters
  What comes next The adaptable enterprise: Why AI readiness is disruption readiness
  About the authors Derek Carr Mrunal Patel Adel Zaalouk Joe Fernandes More like this
  What even is the harness in AI? Red Hat AI and OpenShell: Driving security-enhanced
  agent execution for enterprise AI Technically Speaking | Build a production-ready
  AI toolbox Technically Speaking | Platform engineering for AI agents Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share The promise of enterprise
  AI agents is straightforward: Let the model think, Let the code run, and keep everything
  under your control. Until now, this promise was hard to deliver.'
summary: 'Bringing Claude self-hosted sandboxes to OpenShell on Red Hat AI Outsource
  the thinking, keep the doing Greater security posture for execution (the where)
  How it works together From laptop to cluster on the same architecture Why this matters
  What comes next The adaptable enterprise: Why AI readiness is disruption readiness
  About the authors Derek Carr Mrunal Patel Adel Zaalouk Joe Fernandes More like this
  What even is the harness in AI? Red Hat AI and OpenShell: Driving security-enhanced
  agent execution for enterprise AI Technically Speaking | Build a production-ready
  AI toolbox Technically Speaking | Platform engineering for AI agents Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share The promise of enterprise
  AI agents is straightforward: Let the model think, Let the code run, and keep everything
  under your control. Until now, this promise was hard to deliver. If you wanted Claude
  to write and execute code for your team, you had 2 options: Run everything on the
  cloud and accept that your data, your code, and your execution environment live
  outside your perimeter. Build the entire orchestration stack yourself and lose the
  intelligence that makes managed agents valuable. Anthropic''s self-hosted sandboxes
  for Claude Managed Agents change that equation. Effectively, this capability outsources
  the “thinking” while keeping the “doing” on your own infrastructure. We tested this
  with OpenShell , an open source project started by NVIDIA where Red Hat is an active
  contributor. The integration works out of the box, on both a developer laptop with
  Podman and a Red Hat OpenShift AI cluster. Here is what we learned. Anthropic runs
  the orchestration layer , including the Claude model, conversation management, tool
  routing, and retry logic. You run the execution layer, an environment worker on
  your infrastructure that polls for tasks, executes them locally, and posts results
  back. Layer Where it runs Reasoning and orchestration Anthropic''s cloud Code execution
  and file access Your infrastructure Your data, your files, and your execution results
  stay on your infrastructure.'
---
Open the original post ↗ https://www.redhat.com/en/blog/bringing-claude-self-hosted-sandboxes-to-openshell-on-red-hat-ai
