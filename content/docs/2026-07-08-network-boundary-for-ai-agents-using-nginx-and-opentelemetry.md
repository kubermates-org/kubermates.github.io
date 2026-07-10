---
title: Network boundary for AI agents using NGINX and OpenTelemetry
date: '2026-07-08T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/07/08/network-boundary-for-ai-agents-using-nginx-and-opentelemetry/
post_kind: link
draft: false
tldr: Validating the Idea Why This Matters Now Limitations and Future Work Posted
  on July 8, 2026 by Marko Sluga, F5 CNCF projects highlighted in this post I recently
  had an interesting conversation at a KCD about OpenClaw with one of the attendees,
  and they remarked that they wouldn’t put an agent in their network, because “we
  don’t know what that thing really does”. That got me thinking; agentic autonomy
  has huge potential to automate tasks previously needing humans, but at the same
  time, that capability introduces new operational and security challenges.
summary: 'Validating the Idea Why This Matters Now Limitations and Future Work Posted
  on July 8, 2026 by Marko Sluga, F5 CNCF projects highlighted in this post I recently
  had an interesting conversation at a KCD about OpenClaw with one of the attendees,
  and they remarked that they wouldn’t put an agent in their network, because “we
  don’t know what that thing really does”. That got me thinking; agentic autonomy
  has huge potential to automate tasks previously needing humans, but at the same
  time, that capability introduces new operational and security challenges. This inspired
  me to start a passion project to create a network boundary for AI agents. You might
  be thinking, that’s why we have guardrails! While it’s important to understand agentic
  intent to influence generation, it’s also necessary to control network access for
  agentic tools. Enforcing network traffic security is fundamental, and there are
  already many solutions available for that purpose. How about if we built a network
  boundary that was both enforced and observable at the same time, without needing
  to introduce entirely new infrastructure? The answer turned out to be surprisingly
  simple. Use two mature open source components that are already common in cloud native
  environments: NGINX as the traffic control plane and OpenTelemetry as the audit
  plane. They allow us to gain observability and create an efficient boundary where
  we can implement fine-grained, application-aware traffic shaping rules. Image: Request
  flow diagram Because NGINX sits on both sides of the flow, it performs the reverse
  proxy role for inbound traffic, terminates TLS, and forwards requests for the agent.
  For outbound traffic, the same instance acts as a forward proxy through which every
  agent request must pass. We can control the flow with iptables rules that drop all
  other egress traffic, so there is no second path. That makes the boundary a property
  of the architecture, not a policy we hope the application respects.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/07/08/network-boundary-for-ai-agents-using-nginx-and-opentelemetry/
