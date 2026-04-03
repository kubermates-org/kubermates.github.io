---
title: How to Stub LLMs for AI Agent Security Testing and Governance
date: '2026-04-02T14:15:28+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/how-to-stub-llms-for-ai-agent-security-testing-and-governance/
post_kind: link
draft: false
tldr: 'The Core Concept: A “Malicious” Router for AI Agent Security Testing Python:
  Proving RBAC & Tool Governance Go: Validating OAuth & Identity Boundaries Why Security
  & Governance Teams Love This Architecture The Trade-Offs: What the Stub Model DOESN’T
  Test Beyond the Chatbot: Engineering for Agency Note: The core architecture for
  this pattern was introduced by Isaac Hawley from Tigera. If you are building an
  AI agent that relies on tool calling, complex routing, or the Model Context Protocol
  (MCP) , you’re not just building a chatbot anymore.'
summary: 'The Core Concept: A “Malicious” Router for AI Agent Security Testing Python:
  Proving RBAC & Tool Governance Go: Validating OAuth & Identity Boundaries Why Security
  & Governance Teams Love This Architecture The Trade-Offs: What the Stub Model DOESN’T
  Test Beyond the Chatbot: Engineering for Agency Note: The core architecture for
  this pattern was introduced by Isaac Hawley from Tigera. If you are building an
  AI agent that relies on tool calling, complex routing, or the Model Context Protocol
  (MCP) , you’re not just building a chatbot anymore. You are building an autonomous
  system with access to your internal APIs. With that power comes a massive security
  and governance headache, and AI agent security testing is where most teams hit a
  wall. How do you definitively prove that your agent’s identity and access management
  (IAM) actually works? The scale of the problem is hard to overstate. Microsoft’s
  telemetry shows that 80% of Fortune 500 companies now run active AI agents , yet
  only 47% have implemented specific AI security controls. Most teams are deploying
  agents faster than they can test them. If an agent is hijacked via prompt injection,
  or simply hallucinates a destructive action, does your governance layer stop it?
  Testing this usually forces engineers into a frustrating trade-off: Use the real
  API (Gemini, OpenAI): Real models are heavily RLHF’d to be safe and polite. It is
  incredibly difficult (and non-deterministic) to intentionally force a real model
  to “go rogue” and consistently output malicious tool calls so you can test your
  security boundaries. Mock the internal tools only: You test your Python or Go functions
  in isolation, but you never actually test the “Agent Loop”—meaning you aren’t testing
  if the harness correctly applies the user’s OAuth tokens or Role-Based Access Control
  (RBAC) to the LLM’s requested tool call. Recently, Isaac Hawley introduced a much
  better pattern: The Stub Model —a way to stub your LLM for testing that makes your
  security assertions completely deterministic. A Stub Model (or mock LLM) is a deterministic,
  non-AI replacement for a real language model that you inject into your agent harness
  during testing.'
---
Open the original post ↗ https://www.tigera.io/blog/how-to-stub-llms-for-ai-agent-security-testing-and-governance/
