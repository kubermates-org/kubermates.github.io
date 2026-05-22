---
title: What even is the harness in AI?
date: '2026-05-21T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/what-even-harness-ai
post_kind: link
draft: false
tldr: 'What even is the harness in AI? The conversation so far 5 layers, outside-in
  Layer 1: Infrastructure Layer 2: Sandbox Layer 3: Agent harness Layer 4: Agent runtime
  Layer 5: Model and inference endpoint Subtractive versus additive Get started with
  AI for enterprise organizations: A beginner’s guide About the author Ralph Bean
  More like this Building trust through AI red teaming: Red Hat''s approach to testing
  model safety Bringing Claude self-hosted sandboxes to OpenShell on Red Hat AI Technically
  Speaking | Build a production-ready AI toolbox Technically Speaking | Platform engineering
  for AI agents Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share I recently saw OpenClaw referred to as a harness. I thought, “That’s interesting.'
summary: 'What even is the harness in AI? The conversation so far 5 layers, outside-in
  Layer 1: Infrastructure Layer 2: Sandbox Layer 3: Agent harness Layer 4: Agent runtime
  Layer 5: Model and inference endpoint Subtractive versus additive Get started with
  AI for enterprise organizations: A beginner’s guide About the author Ralph Bean
  More like this Building trust through AI red teaming: Red Hat''s approach to testing
  model safety Bringing Claude self-hosted sandboxes to OpenShell on Red Hat AI Technically
  Speaking | Build a production-ready AI toolbox Technically Speaking | Platform engineering
  for AI agents Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share I recently saw OpenClaw referred to as a harness. I thought, “That’s interesting.
  OpenClaw isn’t a harness. It’s an agent runtime—it drives the agent loop. ” So,
  what does the word "harness" even mean? The structural baseline for the concept
  comes from Birgitta Böckeler''s April 2026 article , which elegantly defines an
  agent as model + harness = agent. She bifurcated the stack into a builder harness
  (the inner runtime shipped with the tool) and a user harness (the developer''s custom
  context). This definition built on a wave of discussion from February 2026, which
  included Mitchell Hashimoto''s pragmatic approach to engineering AGENTS. md contexts,
  OpenAI''s overview of internal harness engineering for automated deployment, and
  Böckeler''s original summary memo. model + harness = agent AGENTS. md I think there’s
  more to an agent than model + harness. For me, this starts with the observation
  that we just can’t trust the agent runtime. In order to get some certainty about
  the software supply chain security of code produced by an agent factory, we need
  a distinct sandbox layer that we can use to capture provenance information and limit
  the possible impact of an agent off the rails.'
---
Open the original post ↗ https://www.redhat.com/en/blog/what-even-harness-ai
