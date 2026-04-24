---
title: 'Shadow AI Is the New Shadow IT: Governing AI Agents from Code to Runtime'
date: '2026-04-06T01:36:18+00:00'
tags:
- nirmata
- kubernetes
source: Nirmata Blog
external_url: https://nirmata.com/2026/04/05/governing-ai-agents-from-code-to-runtime/?utm_source=rss&utm_medium=rss&utm_campaign=governing-ai-agents-from-code-to-runtime
post_kind: link
draft: false
tldr: 'The problem with discovering agents after they’re already running What an AIBOM
  is, and why it’s not an SBOM Attesting the AIBOM to the image digest Kyverno admission
  enforcement Policy 1: require-aibom-attestation Policy 2: enforce-aibom-constraints
  What this unlocks: the agent registry as a byproduct Getting started AIBOM Attestation
  and Kyverno at Admission Control A developer adds an agent to a microservice. It
  has access to a database tool, a code-execution tool, and calls Claude.'
summary: 'The problem with discovering agents after they’re already running What an
  AIBOM is, and why it’s not an SBOM Attesting the AIBOM to the image digest Kyverno
  admission enforcement Policy 1: require-aibom-attestation Policy 2: enforce-aibom-constraints
  What this unlocks: the agent registry as a byproduct Getting started AIBOM Attestation
  and Kyverno at Admission Control A developer adds an agent to a microservice. It
  has access to a database tool, a code-execution tool, and calls Claude. Nobody in
  security, compliance, or platform engineering knows it exists — until it causes
  an incident. This is shadow AI : unauthorized or uncontrolled AI usage that is invisible
  to the teams responsible for governing it. It is the AI equivalent of shadow IT,
  and it is happening at scale across every organization adopting LLMs. The root cause
  is a gap in the governance stack. Traditional tools — SBOMs, CSPM, vulnerability
  scanners— were built for deterministic software. They do not understand agent frameworks,
  tool declarations, model identifiers, or the relationships between them. The standard
  response is discovery: scan what’s running, map the tools, build a dashboard. But
  discovery after deployment has already lost the race. By the time you’ve mapped
  an agent’s tools and model, it has already handled requests, accumulated permissions,
  and potentially taken irreversible actions. Discovery is useful for understanding.'
---
Open the original post ↗ https://nirmata.com/2026/04/05/governing-ai-agents-from-code-to-runtime/?utm_source=rss&utm_medium=rss&utm_campaign=governing-ai-agents-from-code-to-runtime
