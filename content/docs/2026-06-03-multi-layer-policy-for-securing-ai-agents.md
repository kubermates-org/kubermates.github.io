---
title: Multi-Layer Policy for Securing AI Agents
date: '2026-06-03T18:58:09+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/multi-layer-policy-for-securing-ai-agents/
post_kind: link
draft: false
tldr: 'Policy at the gateway: enforcing agent intent Policy at the kernel: constraining
  agent behaviour The dual-layer architecture Why single-layer policy isn’t enough
  for AI agent security Going deeper As part of our work at Tigera building products
  that create secure runtime environments for enterprise agents at scale in the real
  world, one small part of this puzzle I think about a lot is policy, and runtime
  enforcement of policy, and how to create a comprehensive secure runtime, configured
  from one place. The more companies we talk to trying to lock down and secure these
  platforms at runtime, the more I believe AI Agent security needs policy in multiple
  places, not just one (e.'
summary: 'Policy at the gateway: enforcing agent intent Policy at the kernel: constraining
  agent behaviour The dual-layer architecture Why single-layer policy isn’t enough
  for AI agent security Going deeper As part of our work at Tigera building products
  that create secure runtime environments for enterprise agents at scale in the real
  world, one small part of this puzzle I think about a lot is policy, and runtime
  enforcement of policy, and how to create a comprehensive secure runtime, configured
  from one place. The more companies we talk to trying to lock down and secure these
  platforms at runtime, the more I believe AI Agent security needs policy in multiple
  places, not just one (e. g. , not just at the gateway layer), and ideally expressed
  in the same policy language. At the L7 gateway layer, every agent call is observable:
  who is calling, what they are calling, what attributes both sides carry, what the
  requested action is. This is where you decide whether an agent should be permitted
  to talk to a particular MCP server, invoke a particular tool, delegate to another
  agent, or call a particular LLM. The atoms of policy here are identity, action,
  resource, and context. At the agent runtime layer, or kernel layer in a container,
  what the agent does inside its own runtime is observable: syscalls, file access,
  library loads, network connections that bypass the brokered channel. This is where
  you decide whether the agent can read a file, open a socket, spawn a subprocess,
  or load a library. The atoms of policy here are processes, paths, file descriptors,
  and system calls. Both layers are necessary. The gateway alone cannot constrain
  what an agent does inside its runtime once it holds a token.'
---
Open the original post ↗ https://www.tigera.io/blog/multi-layer-policy-for-securing-ai-agents/
