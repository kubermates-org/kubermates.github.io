---
title: Why sandboxing your agent is not enough
date: '2026-07-07T11:30:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/07/07/why-sandboxing-your-agent-is-not-enough/
post_kind: link
draft: false
tldr: 'What Are the Differences Between the Two Projects? Agent-sandbox Agent-substrate
  Do We Need Agent-substrate When We Already Have Agent -sandbox? Agent-substrate
  Integration with kagent Final Thoughts Additional Resources: Posted on July 7, 2026
  by Lin Sun (Solo. io) | CNCF Ambassador CNCF projects highlighted in this post The
  agentic AI space is moving incredibly fast.'
summary: 'What Are the Differences Between the Two Projects? Agent-sandbox Agent-substrate
  Do We Need Agent-substrate When We Already Have Agent -sandbox? Agent-substrate
  Integration with kagent Final Thoughts Additional Resources: Posted on July 7, 2026
  by Lin Sun (Solo. io) | CNCF Ambassador CNCF projects highlighted in this post The
  agentic AI space is moving incredibly fast. Not long ago, I learned about a cool
  project called agent-sandbox , which provides a sandboxed environment for AI agents
  by leveraging many of the building blocks we have already developed for Kubernetes
  pods, such as identities, storage and networking. If you’ve ever read the horror
  stories about AI coding agents or followed projects like OpenClaw & NemoClaw, you
  know how important it is to provide a secure and isolated environment for your agents.
  Without proper isolation, agents can surprise you by doing things you never intended,
  such as deleting family photos or modifying critical files. Just a few weeks ago
  at Open Source Summit North America in Minneapolis, while chatting with Bob Killen
  in the hallway track, I learned about a new project called agent-substrate. What
  immediately caught my attention was its ability to dynamically wake up agents based
  on invocation, thus allowing more agents on the same infrastructure resources while
  still providing the security benefits of sandboxed execution. Naturally, the first
  thing I did was discuss with our team how we could integrate it with kagent and
  agentgateway. The agent-sandbox project provides a Sandbox Custom Resource Definition
  (CRD) and controller for Kubernetes under the umbrella of Kubernetes SIG Apps. Its
  primary focus is on providing: Strong identities for agents Persistent storage that
  survives restarts Lifecycle management of sandboxed pods Security and isolation
  through the Sandbox controller In short, agent-sandbox focuses on making agent execution
  secure, manageable, and Kubernetes-native. The agent-substrate project is currently
  a standalone project and is not part of any Kubernetes SIG or other cloud native
  foundation project, though that may change in the future. Built on top of Kubernetes,
  agent-substrate aims to go beyond sandboxing by focusing on: Higher scale Better
  resource efficiency Lower latency execution More dynamic lifecycle management for
  agents My understanding is that agent-substrate provides the runtime building blocks
  needed to run AI agents securely at very high scale.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/07/07/why-sandboxing-your-agent-is-not-enough/
