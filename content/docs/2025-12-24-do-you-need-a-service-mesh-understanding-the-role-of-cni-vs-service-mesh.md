---
title: Do You Need a Service Mesh? Understanding the Role of CNI vs. Service Mesh
date: '2025-12-24T17:58:09+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/do-you-need-a-service-mesh-understanding-the-role-of-cni-vs-service-mesh/
post_kind: link
draft: false
tldr: 'What a CNI Actually Does The CNI’s Core Responsibilities (and Their Limits)
  What a CNI Does Not Do What is a Service Mesh What a Service Mesh Adds Where CNI
  and Service Mesh Overlap So When Do You Need a Service Mesh? A Layered Model: Outer
  Perimeter and Inner Core Calico and Istio: A Combined Approach One Last Thing: Complexity
  and Tradeoffs Get Started with Calico and Istio Today The world of Kubernetes networking
  can sometimes be confusing. What’s a CNI? A service mesh? Do I need one? Both? And
  how do they interact in my cluster? The questions can go on and on.'
summary: 'What a CNI Actually Does The CNI’s Core Responsibilities (and Their Limits)
  What a CNI Does Not Do What is a Service Mesh What a Service Mesh Adds Where CNI
  and Service Mesh Overlap So When Do You Need a Service Mesh? A Layered Model: Outer
  Perimeter and Inner Core Calico and Istio: A Combined Approach One Last Thing: Complexity
  and Tradeoffs Get Started with Calico and Istio Today The world of Kubernetes networking
  can sometimes be confusing. What’s a CNI? A service mesh? Do I need one? Both? And
  how do they interact in my cluster? The questions can go on and on. Even for seasoned
  platform engineers, making sense of where these two components overlap and where
  the boundaries of responsibility end can be challenging. Seemingly bewildering obstacles
  can stand in the way of getting the most out of their complementary features. One
  way to cut through the confusion is to start by defining what each of them is, then
  look at their respective capabilities, and finally clarify where they intersect
  and how they can work together. This post will clarify: What a CNI is responsible
  for What a service mesh adds on top When you need one, the other, or both Container
  Network Interface (CNI) is a standard way to connect and manage networking for containers
  in Kubernetes. It is a set of standards defined by Kubernetes for configuring container
  network interfaces and maintaining connectivity between pods in a dynamic environment
  where network peers are constantly being created and destroyed. Those standards
  are implemented by CNI plugins. A CNI plugin is the concrete networking component
  that runs in your cluster and performs the actual networking tasks defined by the
  CNI specification. Calico is an example of a CNI plugin, implementing the CNI specification
  to deliver connectivity and policy enforcement for Kubernetes clusters. At a high
  level, a CNI plugin: Connects pods to the network Assigns IP addresses Routes traffic
  between pods and nodes Enforces Kubernetes NetworkPolicy All of this happens at
  the network and transport layers (L3/L4). The CNI doesn’t understand applications,
  it just ensures packets get from point A to point B efficiently and securely.'
---
Open the original post ↗ https://www.tigera.io/blog/do-you-need-a-service-mesh-understanding-the-role-of-cni-vs-service-mesh/
