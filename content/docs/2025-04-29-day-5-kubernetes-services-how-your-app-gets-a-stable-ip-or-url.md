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
tldr: 'Let’s Start With What You Might Know What Is a Kubernetes Service? How It Works
  Example Types of Services (Simplified) Real-World Analogy Try It Out Quick Summary
  Coming Up. Exploring System Architecture for DevOps Engineers Why KubeCon India
  2025 Meant More to KodeKloud Linux: List Disks Linux: "cat" Command Linux Made Easy
  for DevOps Beginners From CFP to Stage: Win Your Tech Talk Slot MCP Explained Simply:
  How AI Can Actually Do Things Now Still Not Job-Ready After Learning DevOps? What
  Is Kubernetes? Finally, a Simple Explanation! But here’s the next problem: You try
  running: kubectl get pods -o wide kubectl get pods -o wide And you see something
  like: NAME READY STATUS IP NODE myapp-xyz 1/1 Running 10.'
summary: 'Let’s Start With What You Might Know What Is a Kubernetes Service? How It
  Works Example Types of Services (Simplified) Real-World Analogy Try It Out Quick
  Summary Coming Up. Exploring System Architecture for DevOps Engineers Why KubeCon
  India 2025 Meant More to KodeKloud Linux: List Disks Linux: "cat" Command Linux
  Made Easy for DevOps Beginners From CFP to Stage: Win Your Tech Talk Slot MCP Explained
  Simply: How AI Can Actually Do Things Now Still Not Job-Ready After Learning DevOps?
  What Is Kubernetes? Finally, a Simple Explanation! But here’s the next problem:
  You try running: kubectl get pods -o wide kubectl get pods -o wide And you see something
  like: NAME READY STATUS IP NODE myapp-xyz 1/1 Running 10. 244. 1. 5 worker-node-1
  NAME READY STATUS IP NODE myapp-xyz 1/1 Running 10. 244. 1. 5 worker-node-1 Great
  — but: That Pod IP is internal It changes if the Pod dies and restarts And if you
  have 3 replicas… which IP do you even hit? That’s where Services come in. You can
  think of it as: A permanent IP address or DNS name inside the cluster A load balancer
  that routes traffic to the right Pods A gateway between your app and the outside
  world (if needed) You attach a Service to a set of Pods using labels The Service
  tracks the matching Pods — even as Pods come and go Kubernetes uses something called
  kube-proxy to route traffic to the correct Pod behind the scenes So even if Pods
  restart, the Service endpoint never changes. Let’s say you run 3 Pods of a web app
  with the label: app: myapp app: myapp You create a Service like this: selector:
  app: myapp selector: app: myapp Now, when someone accesses the Service: Kubernetes
  forwards the request to any of the healthy Pods It’s automatic, balanced, and reliable
  Imagine your app’s Pods are like food trucks moving around a festival ground. A
  Service is like the signpost that says: You don’t care where the trucks are parked
  — you just follow the sign. Kubernetes routes you to the right place, even if trucks
  come and go.'
---
Open the original post ↗ https://kodekloud.com/blog/day-5-kubernetes-services-how-your-app-gets-a-stable-ip-or-url/
