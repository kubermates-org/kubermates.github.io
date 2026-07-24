---
title: NVIDIA OpenShell Secures the Agent. Who Governs the Fleet?
date: '2026-07-15T14:41:56+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/nvidia-openshell-secures-the-agent-who-governs-the-fleet/
post_kind: link
draft: false
tldr: 'What OpenShell actually does Where OpenShell stops, on purpose Closing the
  gap: three integration patterns Pattern 1: One road out of the sandbox Pattern 2:
  The API key never enters the sandbox Pattern 3: Identity from birth Same policy
  idea, from laptop to cluster The other half In short: At GTC 2026, NVIDIA released
  OpenShell, an open source runtime that sandboxes autonomous AI agents with kernel-level
  policy: what files they can touch, what processes they can spawn, where their traffic
  can go. It is a serious piece of engineering and it validates something we have
  argued all year: agent security belongs in the environment, not in the prompt.'
summary: 'What OpenShell actually does Where OpenShell stops, on purpose Closing the
  gap: three integration patterns Pattern 1: One road out of the sandbox Pattern 2:
  The API key never enters the sandbox Pattern 3: Identity from birth Same policy
  idea, from laptop to cluster The other half In short: At GTC 2026, NVIDIA released
  OpenShell, an open source runtime that sandboxes autonomous AI agents with kernel-level
  policy: what files they can touch, what processes they can spawn, where their traffic
  can go. It is a serious piece of engineering and it validates something we have
  argued all year: agent security belongs in the environment, not in the prompt. But
  agent identity, agent-to-agent governance, and cross-sandbox communication all sit
  outside its scope today. This post covers what OpenShell does, where it stops by
  design, and three integration patterns that close the gap with Tigera Lynx. Most
  attempts to control AI agents work at the model layer (alignment, system prompts)
  or the application layer (guardrail libraries, output filters). Both share a flaw:
  the thing being secured is also the thing doing the securing. A sufficiently confused
  or sufficiently compromised agent can talk its way past its own instructions. OpenShell
  takes a different position, and it is the right one. Put the controls in the environment,
  where the agent cannot negotiate with them. An agent inside an OpenShell sandbox
  cannot leak a credential it never received, and cannot call an endpoint the kernel
  refuses to route. If that argument sounds familiar, it should. It is the same case
  we made in Why We Built Lynx and throughout the AI agent accountability series :
  controls the agent can override are not controls.'
---
Open the original post ↗ https://www.tigera.io/blog/nvidia-openshell-secures-the-agent-who-governs-the-fleet/
