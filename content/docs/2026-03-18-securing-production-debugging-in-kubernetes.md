---
title: Securing Production Debugging in Kubernetes
date: '2026-03-18T10:00:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/03/18/securing-production-debugging-in-kubernetes/
post_kind: link
draft: false
tldr: 'Securing Production Debugging in Kubernetes 1) Using an access broker on top
  of Kubernetes RBAC Example: a namespaced on-call debug Role 2) Short-lived, identity-bound
  credentials Option A: short-lived OIDC tokens Option B: Short-lived client certificates
  (X. 509) 3) Use a just-in-time access gateway to run debugging commands Example:
  Namespace-scoped role bindings Example: Cluster-scoped role binding References During
  production debugging, the fastest route is often broad access such as cluster-admin
  (a ClusterRole that grants administrator-level access), shared bastions/jump boxes,
  or long-lived SSH keys.'
summary: 'Securing Production Debugging in Kubernetes 1) Using an access broker on
  top of Kubernetes RBAC Example: a namespaced on-call debug Role 2) Short-lived,
  identity-bound credentials Option A: short-lived OIDC tokens Option B: Short-lived
  client certificates (X. 509) 3) Use a just-in-time access gateway to run debugging
  commands Example: Namespace-scoped role bindings Example: Cluster-scoped role binding
  References During production debugging, the fastest route is often broad access
  such as cluster-admin (a ClusterRole that grants administrator-level access), shared
  bastions/jump boxes, or long-lived SSH keys. It works in the moment, but it comes
  with two common problems: auditing becomes difficult, and temporary exceptions have
  a way of becoming routine. cluster-admin This post offers my recommendations for
  good practices applicable to existing Kubernetes environments with minimal tooling
  changes: Least privilege with RBAC Short-lived, identity-bound credentials An SSH-style
  handshake model for cloud native debugging A good architecture for securing production
  debugging workflows is to use a just-in-time secure shell gateway (often deployed
  as an on demand pod in the cluster). It acts as an SSH-style “front door” that makes
  temporary access actually temporary. You can authenticate with short-lived, identity-bound
  credentials, establish a session to the gateway, and the gateway uses the Kubernetes
  API and RBAC to control what they can do, such as pods/log , pods/exec , and pods/portforward.
  Sessions expire automatically, and both the gateway logs and Kubernetes audit logs
  capture who accessed what and when without shared bastion accounts or long-lived
  keys. pods/log pods/exec pods/portforward RBAC controls who can do what in Kubernetes.
  Many Kubernetes environments rely primarily on RBAC for authorization, although
  Kubernetes also supports other authorization modes such as Webhook authorization.
  You can enforce access directly with Kubernetes RBAC, or put an access broker in
  front of the cluster that still relies on Kubernetes permissions under the hood.
  In either model, Kubernetes RBAC remains the source of truth for what the Kubernetes
  API allows and at what scope. An access broker adds controls that RBAC does not
  cover well.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/03/18/securing-production-debugging-in-kubernetes/
