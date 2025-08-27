---
title: 'Day 6: ConfigMaps & Secrets — Managing App Settings and Sensitive Data in
  Kubernetes'
date: '2025-05-01T18:11:50+00:00'
tags:
- kodekloud
- kubernetes
source: KodeKloud Blog (Kubernetes)
external_url: https://kodekloud.com/blog/day-6-configmaps-and-secrets/
post_kind: link
draft: false
tldr: 'In traditional apps — whether Node. js, Python, Java, or others — you’ve probably
  done this before: And sometimes… you (accidentally or lazily) hardcode passwords
  into the code itself.'
summary: 'In traditional apps — whether Node. js, Python, Java, or others — you’ve
  probably done this before: And sometimes… you (accidentally or lazily) hardcode
  passwords into the code itself. 😬 But in Kubernetes, there’s a better and safer
  way to do this. Enter: ConfigMaps and Secrets It keeps your app configs separate
  from your app code and container image — which is great for flexibility and security.
  Secrets are base64-encoded and can be managed with tighter access controls in Kubernetes.
  You: And a Secret: Then, in your Pod spec (simplified YAML): 👉 Use the KodeKloud
  Kubernetes Playground 1 - Create a Secret: 2 - Create a Pod using that secret: Apply
  it with: You’ll see the password securely injected. Imagine you’re deploying an
  app on a shared team server. 📅 Day 7: Your Kubernetes Learning Roadmap — What’s
  Next After the Basics? You’ll get: New here? Start from Day 1 and catch up on the
  series: Day 1: What Is Kubernetes & Why Should You Care? Discover why Kubernetes
  matters and how it changes the game. Day 2: What Are Pods in Kubernetes? Understand
  the smallest deployable unit in Kubernetes. Day 3: Understanding Nodes, Clusters
  & the Kubernetes Control Plane See how all the pieces connect behind the scenes.
  Day 4: Deployments & ReplicaSets — How Kubernetes Runs and Manages Your App ⚙Learn
  how Kubernetes keeps your apps running smoothly. Day 5: Kubernetes Services — How
  Your App Gets a Stable IP or URL Discover how Services expose and connect your app
  reliably.'
---
Open the original post ↗ https://kodekloud.com/blog/day-6-configmaps-and-secrets/
