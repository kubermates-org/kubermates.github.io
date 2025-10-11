---
title: A blueprint for zero-trust AI on Kubernetes
date: '2025-10-10T14:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/10/10/a-blueprint-for-zero-trust-ai-on-kubernetes/
post_kind: link
draft: false
tldr: Are these AI security challenges unique? A blueprint for securing AI on Kubernetes
  Securing ingress to your endpoints (secure the front door) Control the traffic (Sorry
  this cluster is RSVP only) Observability (What is actually happening inside the
  house) The bottom line Posted on October 10, 2025 by Tigera CNCF projects highlighted
  in this post LLMs and AI are everywhere these days. Everyone wants to build the
  next big thing, ship it fast, and maybe even cash out and chill for the rest of
  their lives.
summary: 'Are these AI security challenges unique? A blueprint for securing AI on
  Kubernetes Securing ingress to your endpoints (secure the front door) Control the
  traffic (Sorry this cluster is RSVP only) Observability (What is actually happening
  inside the house) The bottom line Posted on October 10, 2025 by Tigera CNCF projects
  highlighted in this post LLMs and AI are everywhere these days. Everyone wants to
  build the next big thing, ship it fast, and maybe even cash out and chill for the
  rest of their lives. The problem? Most open source AI projects are shared as is.
  They’re created with the best intentions, but their developers aren’t losing sleep
  over things like security guardrails or production hardening, that part is left
  for you to figure out. If that sounds like the boat you’re in, you’re in the right
  place. In this blog, we’ll look at how running AI on Kubernetes introduces some
  very real networking and security challenges, and what you can do about them before
  your experiment turns into a liability. Because here’s the thing: AI systems are
  complicated, sometimes even the people building them admit they don’t fully know
  why a model makes the decision it does. But at the end of the day, it’s still just
  bits moving around computers and network cables, and securing those bits, whether
  they’re API keys, training data, or model endpoints, is easier than you might think
  if you know the right patterns. Yes and no. On the one hand, the issues AI workloads
  face, unrestricted network traffic, exposed endpoints, leaked credentials, are the
  same classic security problems we’ve been wrestling with in IT for decades. On the
  other hand, they don’t just move data around, they handle sensitive training datasets,
  expensive inference workloads, and powerful APIs that can be abused in seconds.
  A stolen API key doesn’t just mean a small breach; it could mean thousands of dollars
  in cloud bills or a model that starts spilling the beans for the wrong confidant.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/10/10/a-blueprint-for-zero-trust-ai-on-kubernetes/
