---
title: 'Sidecarless mTLS in Kubernetes: How Istio Ambient Mesh and ztunnel Enable
  Zero Trust'
date: '2026-01-06T21:52:44+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/sidecarless-mtls-in-kubernetes-how-istio-ambient-mesh-and-ztunnel-enable-zero-trust/
post_kind: link
draft: false
tldr: Delivering Cluster-Wide mTLS Without Sidecars What is ztunnel? Joining Workloads
  to the Mesh Identity and Authentication Without Sidecars HBONE and the Transport
  Layer The mTLS Flow in Ambient Mode Separating Layer 4 Security From Layer 7 Processing
  Ambient Mesh and Calico Network Policy Operational Impact A Shift in How mTLS Is
  Delivered Encrypting internal traffic and enforcing mutual (mTLS), a form of TLS
  in which both the client and server authenticate each other using X. 509 certificates.
summary: 'Delivering Cluster-Wide mTLS Without Sidecars What is ztunnel? Joining Workloads
  to the Mesh Identity and Authentication Without Sidecars HBONE and the Transport
  Layer The mTLS Flow in Ambient Mode Separating Layer 4 Security From Layer 7 Processing
  Ambient Mesh and Calico Network Policy Operational Impact A Shift in How mTLS Is
  Delivered Encrypting internal traffic and enforcing mutual (mTLS), a form of TLS
  in which both the client and server authenticate each other using X. 509 certificates.
  , has transitioned from a “nice-to-have” to a hard requirement, especially in Kubernetes
  environments where everything can talk to everything else by default. Whether your
  objectives are regulatory compliance, or simply aligning to the principles of Zero
  Trust, the goal is the same: to ensure every connection is encrypted, authenticated,
  and authorized. The word ‘service mesh’ is bandied about as the ideal solution for
  implementing zero-trust security but it comes at a price often too high for organizations
  to accept. In addition to a steep learning curve, deploying a service mesh with
  a sidecar proxy in every pod scales poorly, driving up CPU and memory consumption
  and creating ongoing maintenance challenges for cluster operators. Istio Ambient
  Mode addresses these pain points by decoupling the mesh from the application and
  splitting the service mesh into two distinct layers: mTLS and L7 traffic management,
  neither of which needs to run as a sidecar on a pod. By separating these domains,
  Istio allows platform engineers to implement mTLS cluster-wide without the complexity
  of L7 processing for every single connection. Ambient Mode recognizes that mTLS
  is a foundational infrastructure requirement, while L7 traffic management is a specific
  application requirement. With this separation, Istio moves mTLS to the ztunnel,
  making encryption a transparent part of the platform. In this context, this post
  explores how Istio Ambient Mesh delivers mTLS as a platform capability without sidecars
  using ztunnel, and how this approach fits into a broader zero trust strategy when
  combined with Calico network policy. Next, we’ll focus on ztunnel and how it secures
  pod to pod traffic with mTLS.'
---
Open the original post ↗ https://www.tigera.io/blog/sidecarless-mtls-in-kubernetes-how-istio-ambient-mesh-and-ztunnel-enable-zero-trust/
