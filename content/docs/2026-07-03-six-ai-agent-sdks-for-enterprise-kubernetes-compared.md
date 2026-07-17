---
title: Six AI agent SDKs for enterprise Kubernetes, compared
date: '2026-07-03T20:44:49+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/six-ai-agent-sdks-for-enterprise-kubernetes-compared/
post_kind: link
draft: false
tldr: The six SDKs most people are actually using LangGraph CrewAI Google ADK Microsoft
  Agent Framework OpenAI Agents SDK Anthropic Claude Agent SDK The comparison at a
  glance Picking one (or, realistically, several) Governing the fleet you’ll actually
  have There’s a question we hear constantly from platform and engineering leaders
  right now, “which agent SDK should we standardize on for our Kubernetes clusters?”
  The honest answer is that the question is slightly wrong, and the rest of this post
  explains why. But it’s a fair question, so let’s compare the contenders first.
summary: 'The six SDKs most people are actually using LangGraph CrewAI Google ADK
  Microsoft Agent Framework OpenAI Agents SDK Anthropic Claude Agent SDK The comparison
  at a glance Picking one (or, realistically, several) Governing the fleet you’ll
  actually have There’s a question we hear constantly from platform and engineering
  leaders right now, “which agent SDK should we standardize on for our Kubernetes
  clusters?” The honest answer is that the question is slightly wrong, and the rest
  of this post explains why. But it’s a fair question, so let’s compare the contenders
  first. If you’re an enterprise running on-premise or in your own VPC, the SDK you
  pick has to do two things most of the “build an agent in 20 lines” tutorials skip
  over. It has to run in a container you control, and it has to talk to a model you
  can host yourself. That second one rules out a surprising amount. These are the
  ones with the most mindshare in mid-2026. There are others, but these are the names
  that come up in every conversation. They sit on a rough spectrum of model freedom:
  most will happily run against a model you host yourself, the OpenAI SDK will too
  but treats that as a side path, and one of them (Anthropic’s) is tied to a single
  vendor’s models. I’ve ordered them with the most flexible first. LangChain’s lower-level
  library. You model your agent as a directed graph: nodes do work, edges decide what
  happens next, and the whole thing checkpoints its state so a long-running agent
  can pause, resume, and even rewind. If your problem is “this workflow is genuinely
  complicated and has to survive restarts,” LangGraph is the one built for that.'
---
Open the original post ↗ https://www.tigera.io/blog/six-ai-agent-sdks-for-enterprise-kubernetes-compared/
