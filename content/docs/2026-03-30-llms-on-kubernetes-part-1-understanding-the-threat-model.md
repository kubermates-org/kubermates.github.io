---
title: 'LLMs on Kubernetes Part 1: Understanding the threat model'
date: '2026-03-30T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/03/30/llms-on-kubernetes-part-1-understanding-the-threat-model/
post_kind: link
draft: false
tldr: 'Understanding what you’re actually running OWASP LLM Top 10: A framework for
  understanding risks Four risks that Kubernetes operators need to understand 1. Prompt
  Injection (LLM01) 2.'
summary: 'Understanding what you’re actually running OWASP LLM Top 10: A framework
  for understanding risks Four risks that Kubernetes operators need to understand
  1. Prompt Injection (LLM01) 2. Sensitive Information Disclosure (LLM02) 3. Supply
  Chain Risks (LLM03) 4. Excessive Agency (LLM06) Where these controls belong Choosing
  a policy layer Posted on March 30, 2026 by Nigel Douglas, CloudSmith CNCF projects
  highlighted in this post Let’s say you’ve got an LLM running on Kubernetes. Pods
  are healthy, logs are clean, users are chatting. Everything looks fine. But here’s
  the thing: Kubernetes is great at scheduling workloads and keeping them isolated.
  It has no idea what those workloads do. And an LLM isn’t just compute, it’s a system
  that takes untrusted input and decides what to do with it. That’s a different threat
  model. And it needs controls Kubernetes doesn’t provide.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/03/30/llms-on-kubernetes-part-1-understanding-the-threat-model/
