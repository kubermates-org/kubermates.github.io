---
title: 'Day 5: Kubernetes Services — How Your App Gets a Stable IP or URL'
date: '2025-04-29T17:26:00+00:00'
tags:
- kodekloud
- kubernetes
source: KodeKloud Blog (Kubernetes)
external_url: https://kodekloud.com/blog/day-5-kubernetes-services-how-your-app-gets-a-stable-ip-or-url/
post_kind: link
draft: false
tldr: 'By now, you’ve launched a container, wrapped it in a Pod, deployed it using
  a Deployment, and scaled it up to multiple Pods. But here’s the next problem: You
  try running: And you see something like: Great — but: That’s where Services come
  in.'
summary: 'By now, you’ve launched a container, wrapped it in a Pod, deployed it using
  a Deployment, and scaled it up to multiple Pods. But here’s the next problem: You
  try running: And you see something like: Great — but: That’s where Services come
  in. You can think of it as: So even if Pods restart, the Service endpoint never
  changes. Let’s say you run 3 Pods of a web app with the label: You create a Service
  like this: Now, when someone accesses the Service: Imagine your app’s Pods are like
  food trucks moving around a festival ground. A Service is like the signpost that
  says: You don’t care where the trucks are parked — you just follow the sign. Kubernetes
  routes you to the right place, even if trucks come and go. Use the Kubernetes Playground:
  👉 KodeKloud Kubernetes Playground Create a deployment: Now run: Look for the NodePort
  (e. g. , 30123 ) and try opening: You’re now accessing your app through a Kubernetes
  Service! 📅 Day 6: ConfigMaps & Secrets — Managing App Settings and Sensitive Data
  You’ll learn: New here? Start from Day 1 and catch up on the series: Day 1: What
  Is Kubernetes & Why Should You Care? Discover why Kubernetes matters and how it
  changes the game. Day 2: What Are Pods in Kubernetes? Understand the smallest deployable
  unit in Kubernetes. Day 3: Understanding Nodes, Clusters & the Kubernetes Control
  Plane See how all the pieces connect behind the scenes. Day 4: Deployments & ReplicaSets
  — How Kubernetes Runs and Manages Your App Learn how Kubernetes keeps your apps
  running smoothly.'
---
Open the original post ↗ https://kodekloud.com/blog/day-5-kubernetes-services-how-your-app-gets-a-stable-ip-or-url/
