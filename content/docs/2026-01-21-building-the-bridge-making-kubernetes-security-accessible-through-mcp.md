---
title: 'Building the Bridge: Making Kubernetes Security Accessible Through MCP'
date: '2026-01-21T15:25:21+00:00'
tags:
- nirmata
- kubernetes
source: Nirmata Blog
external_url: https://nirmata.com/2026/01/21/building-the-bridge-making-kubernetes-security-accessible-through-mcp/?utm_source=rss&utm_medium=rss&utm_campaign=building-the-bridge-making-kubernetes-security-accessible-through-mcp
post_kind: link
draft: false
tldr: 'Building the Bridge: Making Kubernetes Security Accessible Through MCP Why
  Kubernetes Security Needed a Bridge Why We Built an MCP Server How the Nirmata MCP
  Server Works Embedded Policies for Instant Security Overcoming Key Technical Challenges
  Multi-Transport Flexibility Namespace Filtering User-Centric Error Handling Real-World
  Use Cases Performance and Security Built-In Performance Security The Bigger Picture:
  AI Meets Cloud-Native Governance Getting Started What We Learned Learn More Kubernetes
  security is powerful—but notoriously complex. At Nirmata , we saw teams struggling
  to implement proper security governance because doing so requires deep expertise
  in Kubernetes internals and policy management.'
summary: 'Building the Bridge: Making Kubernetes Security Accessible Through MCP Why
  Kubernetes Security Needed a Bridge Why We Built an MCP Server How the Nirmata MCP
  Server Works Embedded Policies for Instant Security Overcoming Key Technical Challenges
  Multi-Transport Flexibility Namespace Filtering User-Centric Error Handling Real-World
  Use Cases Performance and Security Built-In Performance Security The Bigger Picture:
  AI Meets Cloud-Native Governance Getting Started What We Learned Learn More Kubernetes
  security is powerful—but notoriously complex. At Nirmata , we saw teams struggling
  to implement proper security governance because doing so requires deep expertise
  in Kubernetes internals and policy management. That expertise gap introduces real
  risk. So, we asked a simple question: How do we preserve Kyverno’s precision while
  making it accessible to non-experts? The answer wasn’t simplifying Kyverno itself—it
  was transforming how people interact with it. The Model Context Protocol (MCP) changed
  the game. MCP provides a standardized way for AI assistants to interact with systems
  like Kubernetes and Kyverno. By building a Kyverno MCP Server , we created one interface
  that works with any AI assistant that speaks MCP—whether that’s ChatGPT , Claude
  , or a custom-built internal assistant. This means anyone can query their cluster
  through natural language , asking questions such as: “Does my cluster follow pod
  security standards?” “Does my cluster follow pod security standards?” “Show me RBAC
  violations in production. ” “Show me RBAC violations in production. ” “Which policies
  am I failing, and why?” “Which policies am I failing, and why?” The MCP server translates
  those plain-language questions into Kyverno operations, runs the evaluations, and
  returns the results conversationally—bridging the gap between human understanding
  and machine precision. We exposed five key capabilities through the MCP interface:
  Cluster Discovery – View available Kubernetes environments Cluster Discovery – View
  available Kubernetes environments Context Switching – Seamlessly move between clusters
  in one conversation Context Switching – Seamlessly move between clusters in one
  conversation Policy Application – Scan resources against policies for compliance
  insights Policy Application – Scan resources against policies for compliance insights
  Violation Reporting – Identify issues and explain why they matter Violation Reporting
  – Identify issues and explain why they matter Interactive Help – Guide users on
  what’s possible through MCP Interactive Help – Guide users on what’s possible through
  MCP Each capability is implemented as a modular Go component, designed for extensibility
  as Kyverno and Kubernetes evolve. The data flow is straightforward but powerful:
  The AI assistant sends a question through MCP The AI assistant sends a question
  through MCP The server translates it into precise Kyverno operations The server
  translates it into precise Kyverno operations Kyverno evaluates the cluster Kyverno
  evaluates the cluster Results return enriched with context and explanations Results
  return enriched with context and explanations This cycle allows natural, ongoing
  dialogue—turning traditional command-line operations into conversational experiences.'
---
Open the original post ↗ https://nirmata.com/2026/01/21/building-the-bridge-making-kubernetes-security-accessible-through-mcp/?utm_source=rss&utm_medium=rss&utm_campaign=building-the-bridge-making-kubernetes-security-accessible-through-mcp
