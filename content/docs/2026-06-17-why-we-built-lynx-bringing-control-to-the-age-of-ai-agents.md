---
title: 'Why We Built Lynx: Bringing Control to the Age of AI Agents'
date: '2026-06-17T13:00:22+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/why-we-built-lynx-bringing-control-to-the-age-of-ai-agents/
post_kind: link
draft: false
tldr: 'AI agents broke the assumptions security stacks were built on What Lynx does
  Security & visibility for Kubernetes-native AI For a decade, one idea has guided
  everything we’ve built at Tigera: How do you secure a dynamic system with a lot
  of moving parts that is changing rapidly, with a programmatic approach? Calico has
  applied that idea for Global 2000 companies running the largest Kubernetes platforms
  in the world, securing tens of millions of mission-critical transactions every day.
  Today I’m excited to announce the next chapter of that work: Lynx, a unified control
  plane for Kubernetes-native AI agents.'
summary: 'AI agents broke the assumptions security stacks were built on What Lynx
  does Security & visibility for Kubernetes-native AI For a decade, one idea has guided
  everything we’ve built at Tigera: How do you secure a dynamic system with a lot
  of moving parts that is changing rapidly, with a programmatic approach? Calico has
  applied that idea for Global 2000 companies running the largest Kubernetes platforms
  in the world, securing tens of millions of mission-critical transactions every day.
  Today I’m excited to announce the next chapter of that work: Lynx, a unified control
  plane for Kubernetes-native AI agents. This enables us to apply our deep knowledge
  of Kubernetes, eBPF, and our expertise in building scalable and highly performant
  systems to solve the security challenges that come with deploying AI Agents. Before
  I explain how Lynx addresses these challenges, it’s worth being clear about why
  AI agents are so hard to secure in the first place. The enterprise security tooling
  most organizations run was designed for workloads that are deterministic. A service
  does roughly the same thing today that it did yesterday. You can reason about its
  behavior, define what it’s allowed to touch, and trust that a valid credential maps
  to expected actions. AI agents don’t work that way. They’re autonomous and non-deterministic.
  An agent acts on behalf of a user, reaches for whatever tool, LLM, or other agent
  it needs, carries a delegation chain, and reads untrusted input as it goes. The
  same agent can take a different path every time it runs. A valid credential no longer
  guarantees good behavior, it just guarantees the door opens.'
---
Open the original post ↗ https://www.tigera.io/blog/why-we-built-lynx-bringing-control-to-the-age-of-ai-agents/
