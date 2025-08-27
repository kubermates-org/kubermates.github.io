---
title: 'Blog: Spotlight on SIG API Machinery'
date: '2024-08-07T00:00:00+00:00'
tags:
- kubernetes
- community
source: Kubernetes.dev Blog
external_url: https://www.kubernetes.dev/blog/2024/08/07/sig-api-machinery-spotlight-2024/
post_kind: link
draft: false
tldr: 'We recently talked with Federico Bongiovanni (Google) and David Eads (Red Hat),
  Chairs of SIG API Machinery, to know a bit more about this Kubernetes Special Interest
  Group. Frederico (FSM): Hello, and thank your for your time.'
summary: 'We recently talked with Federico Bongiovanni (Google) and David Eads (Red
  Hat), Chairs of SIG API Machinery, to know a bit more about this Kubernetes Special
  Interest Group. Frederico (FSM): Hello, and thank your for your time. To start with,
  could you tell us about yourselves and how you got involved in Kubernetes? David
  : I started working on OpenShift (the Red Hat distribution of Kubernetes) in the
  fall of 2014 and got involved pretty quickly in API Machinery. My first PRs were
  fixing kube-apiserver error messages and from there I branched out to kubectl (
  kubeconfigs are my fault!), auth ( RBAC and *Review APIs are ports from OpenShift),
  apps ( workqueues and sharedinformers for example). Don’t tell the others, but API
  Machinery is still my favorite :) Federico : I was not as early in Kubernetes as
  David, but now it’s been more than six years. At my previous company we were starting
  to use Kubernetes for our own products, and when I came across the opportunity to
  work directly with Kubernetes I left everything and boarded the ship (no pun intended).
  I joined Google and Kubernetes in early 2018, and have been involved since. FSM:
  It only takes a quick look at the SIG API Machinery charter to see that it has quite
  a significant scope, nothing less than the Kubernetes control plane. Could you describe
  this scope in your own words? David : We own the kube-apiserver and how to efficiently
  use it. On the backend, that includes its contract with backend storage and how
  it allows API schema evolution over time. On the frontend, that includes schema
  best practices, serialization, client patterns, and controller patterns on top of
  all of it. Federico : Kubernetes has a lot of different components, but the control
  plane has a really critical mission: it’s your communication layer with the cluster
  and also owns all the extensibility mechanisms that make Kubernetes so powerful.'
---
Open the original post ↗ https://www.kubernetes.dev/blog/2024/08/07/sig-api-machinery-spotlight-2024/
