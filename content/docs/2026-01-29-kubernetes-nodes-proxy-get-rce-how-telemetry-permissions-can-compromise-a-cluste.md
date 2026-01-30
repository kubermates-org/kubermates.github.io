---
title: 'Kubernetes nodes/proxy GET → RCE: how “telemetry” permissions can compromise
  a cluster'
date: '2026-01-29T19:01:56+00:00'
tags:
- nirmata
- kubernetes
source: Nirmata Blog
external_url: https://nirmata.com/2026/01/29/kubernetes-nodes-proxy-get-rce/?utm_source=rss&utm_medium=rss&utm_campaign=kubernetes-nodes-proxy-get-rce
post_kind: link
draft: false
tldr: 'Kubernetes nodes/proxy GET → RCE: how “telemetry” permissions can compromise
  a cluster References What’s happening (in plain English) The key idea Why nodes/proxy
  is especially risky Why platform teams should care: observability is a common blast-radius
  multiplier Prevention with Kyverno: make “dangerous RBAC” unshippable Policy 1:
  Block nodes/proxy (and nodes/* ) when verbs include get or * Defense-in-depth best
  practices (don’t skip these) 1) Inventory who already has nodes/proxy 2) Prefer
  Metrics API and fine-grained subresources 3) Network containment: reduce kubelet
  reachability 4) Audit logging (know what your audit can see) 5) Keep privileged
  landing zones small A short “how-to” using nctl ai : generate the Kyverno policy
  + tests, then iterate fast Step 1: Generate policy + tests with one prompt Step
  2: Save files into a tiny test harness Step 3: Run tests locally Step 4: Iterate
  using real RBAC from your cluster Step 5: Roll out safely (Audit → Enforce) Conclusion
  A subtle (and frankly surprising) Kubernetes authorization behavior has resurfaced
  as a practical cluster-compromise path : an identity granted nodes/proxy with get
  can be leveraged to execute commands in Pods across the cluster—effectively turning
  what many teams treat as “read-only node telemetry access” into remote code execution
  (RCE). This isn’t being treated like a traditional CVE you can patch away.'
summary: 'Kubernetes nodes/proxy GET → RCE: how “telemetry” permissions can compromise
  a cluster References What’s happening (in plain English) The key idea Why nodes/proxy
  is especially risky Why platform teams should care: observability is a common blast-radius
  multiplier Prevention with Kyverno: make “dangerous RBAC” unshippable Policy 1:
  Block nodes/proxy (and nodes/* ) when verbs include get or * Defense-in-depth best
  practices (don’t skip these) 1) Inventory who already has nodes/proxy 2) Prefer
  Metrics API and fine-grained subresources 3) Network containment: reduce kubelet
  reachability 4) Audit logging (know what your audit can see) 5) Keep privileged
  landing zones small A short “how-to” using nctl ai : generate the Kyverno policy
  + tests, then iterate fast Step 1: Generate policy + tests with one prompt Step
  2: Save files into a tiny test harness Step 3: Run tests locally Step 4: Iterate
  using real RBAC from your cluster Step 5: Roll out safely (Audit → Enforce) Conclusion
  A subtle (and frankly surprising) Kubernetes authorization behavior has resurfaced
  as a practical cluster-compromise path : an identity granted nodes/proxy with get
  can be leveraged to execute commands in Pods across the cluster—effectively turning
  what many teams treat as “read-only node telemetry access” into remote code execution
  (RCE). This isn’t being treated like a traditional CVE you can patch away. The recommended
  long-term direction is fine-grained kubelet authorization (KEP-2862 / KubeletFineGrainedAuthz),
  with upstream commentary pointing to future releases to make broad nodes/proxy less
  necessary. The New Stack: https://thenewstack. io/kubernetes-telemetry-feature-fully-compromises-clusters/
  Technical deep dives : https://grahamhelton. com/blog/nodes-proxy-rce https://labs.
  iximiuz. com/tutorials/nodes-proxy-rce-c9e436a9 Kubernetes exposes a “node proxy”
  capability: API server proxying to kubelet endpoints on nodes. Some of those proxied
  endpoints involve WebSockets (which start as an HTTP GET handshake). In this scenario,
  authorization ends up effectively being evaluated against the handshake method rather
  than the real operation that follows—allowing a token with nodes/proxy + get to
  do much more than teams assume. Kubernetes’ kubelet auth mapping makes this clearer:
  Many kubelet paths map cleanly to subresources like nodes/metrics , nodes/stats
  , nodes/log Anything else tends to fall into the coarse bucket: nodes/proxy ( Kubernetes
  ) In other words, nodes/proxy is the “catch-all,” which is exactly what you don’t
  want floating around in widely-used ServiceAccounts. This is not an “edge-case permission.'
---
Open the original post ↗ https://nirmata.com/2026/01/29/kubernetes-nodes-proxy-get-rce/?utm_source=rss&utm_medium=rss&utm_campaign=kubernetes-nodes-proxy-get-rce
