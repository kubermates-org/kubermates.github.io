---
title: 'Securing the Node: A Primer on Cilium’s Host Firewall'
date: '2025-09-03T14:02:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/09/03/securing-the-node-a-primer-on-ciliums-host-firewall/
post_kind: link
draft: false
tldr: 'The Node as a Blind Spot How Cilium’s Host Firewall Works Enabling Host Firewall
  Audit Mode Observe Network Traffic with Hubble Writing Host Network Policies Enforcing
  the Policy Best Practices and Troubleshooting Tips Conclusion Additional Resources:
  Posted on September 3, 2025 by Paul Arah, Isovalent @ Cisco When discussing Kubernetes
  network security, much of the attention focuses on pod-to-pod traffic, ingress controllers,
  and service meshes. But what about the underlying nodes themselves, the very foundation
  on which our workloads run? The attack surface that Kubernetes nodes expose is vast
  and, if left unprotected, can become a golden ticket for malicious actors.'
summary: 'The Node as a Blind Spot How Cilium’s Host Firewall Works Enabling Host
  Firewall Audit Mode Observe Network Traffic with Hubble Writing Host Network Policies
  Enforcing the Policy Best Practices and Troubleshooting Tips Conclusion Additional
  Resources: Posted on September 3, 2025 by Paul Arah, Isovalent @ Cisco When discussing
  Kubernetes network security, much of the attention focuses on pod-to-pod traffic,
  ingress controllers, and service meshes. But what about the underlying nodes themselves,
  the very foundation on which our workloads run? The attack surface that Kubernetes
  nodes expose is vast and, if left unprotected, can become a golden ticket for malicious
  actors. Cilium host firewall is built to lock down the host network namespace with
  precision, visibility, and control, extending the same familiar declarative Kubernetes
  network policy model to the underlying host. In this blog post, we’ll explore what
  Cilium Host Firewall is, how it works, and why it should be a core part of your
  Kubernetes security. Kubernetes native network policies don’t apply to host-level
  traffic. This means any communication that enters or leaves the host directly (for
  example, SSH, kubelet, or external monitoring agents) is largely invisible to traditional
  Kubernetes policy enforcement. While some firewalling is possible via firewalld
  or external systems, managing those rules is brittle and lacks integration with
  Kubernetes. At its core, this is the problem Cilium Host Firewall solves. Leveraging
  eBPF, Cilium introduces host firewalling directly into the fabric of the cluster.
  Cilium treats the node as a special type of endpoint with the label reserved:host.
  This lets us apply policies just like we would for pods, except these apply to traffic
  to and from the node(s) themselves. Cilium host firewall operates at the interface
  level.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/09/03/securing-the-node-a-primer-on-ciliums-host-firewall/
