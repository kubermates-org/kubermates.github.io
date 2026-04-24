---
title: Policy-Driven Authorization for AI Agents with Kyverno and AWS AgentCore
date: '2026-04-08T17:06:58+00:00'
tags:
- nirmata
- kubernetes
source: Nirmata Blog
external_url: https://nirmata.com/2026/04/08/policy-driven-authorization-for-ai-agents-with-kyverno-and-aws-agentcore/?utm_source=rss&utm_medium=rss&utm_campaign=policy-driven-authorization-for-ai-agents-with-kyverno-and-aws-agentcore
post_kind: link
draft: false
tldr: 'Enforcing real-time, payload-aware governance for the agentic era Introduction:
  From Generation to Action The Need for Runtime Authorization Architecture: MCP Governance
  Gateway Request Flow Key Engineering Learnings 1. The “No VPC” Constraint 2.'
summary: 'Enforcing real-time, payload-aware governance for the agentic era Introduction:
  From Generation to Action The Need for Runtime Authorization Architecture: MCP Governance
  Gateway Request Flow Key Engineering Learnings 1. The “No VPC” Constraint 2. Interceptor
  Response Format is Strict 3. Policy-as-Code with Kyverno (HTTP Mode) Example: Blocking
  Destructive Operations in Production How This Works Getting Started Conclusion AI
  agents are no longer just generating responses, they’re taking actions. From invoking
  APIs to modifying infrastructure, agentic systems now operate directly on production
  environments. This raises a critical question: How do we control what an AI agent
  is allowed to do at runtime? Standard IAM roles are excellent for identity and access
  management, but they are often too coarse-grained to understand: The context of
  a natural language prompt The intent behind an action The specific parameters of
  a tool call What’s missing is a runtime authorization layer, one that evaluates
  every agent action dynamically before execution. AI agents operate in highly dynamic
  environments: A single prompt can trigger multiple tool calls Decisions are influenced
  by natural language input Actions may involve sensitive or destructive operations
  Without proper authorization controls, this can lead to: Unauthorized system access
  Destructive operations in production Data leakage Prompt injection–driven misuse
  Traditional IAM-based approaches are: Static Coarse-grained Not aware of request
  payloads What we need is policy-driven authorization (AuthZ) , evaluated in real
  time, based on context. This solution introduces a runtime authorization layer directly
  into the agent execution path using a reusable architecture pattern. At its core
  is the MCP Governance Gateway , which inserts a “security interceptor” between the
  agent and the tool it wants to execute. Agent initiates a tool call An MCP client
  or agent runtime using Amazon Bedrock AgentCore Gateway decides it needs to invoke
  a tool (for example, delete-pod ). Gateway interception The AgentCore Gateway receives
  the request and routes it through an interceptor Interceptor extracts context The
  Lambda interceptor captures: User identity Role Tool name Request parameters User
  identity Role Tool name Request parameters Kyverno policy evaluation The request
  is sent to Kyverno (running in HTTP/AuthZ mode) Policy decision Kyverno evaluates
  the request against policies Returns an authorization decision Kyverno evaluates
  the request against policies Returns an authorization decision Enforcement ✅ ALLOW
  → Gateway invokes the tool ❌ DENY → Gateway blocks execution and returns a 403 ✅
  ALLOW → Gateway invokes the tool ❌ DENY → Gateway blocks execution and returns a
  403 Audit logging Decisions are recorded for observability and compliance Decisions
  are recorded for observability and compliance Authorization is enforced before execution
  not after. Building this architecture uncovered several important real-world constraints.'
---
Open the original post ↗ https://nirmata.com/2026/04/08/policy-driven-authorization-for-ai-agents-with-kyverno-and-aws-agentcore/?utm_source=rss&utm_medium=rss&utm_campaign=policy-driven-authorization-for-ai-agents-with-kyverno-and-aws-agentcore
