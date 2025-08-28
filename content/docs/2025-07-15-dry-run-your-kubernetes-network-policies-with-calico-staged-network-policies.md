---
title: 'Dry Run: Your Kubernetes network policies with Calico staged network policies'
date: '2025-07-15T14:01:01+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/dry-run-your-kubernetes-network-policies-with-calico-staged-network-policies/
post_kind: link
draft: false
tldr: Kubernetes Network Policies (KNP) are powerful resources that help secure and
  isolate workloads in a cluster. By defining what traffic is allowed to and from
  specific pods, KNPs provide the foundation for zero-trust networking and least-privilege
  access in cloud-native environments.
summary: 'Kubernetes Network Policies (KNP) are powerful resources that help secure
  and isolate workloads in a cluster. By defining what traffic is allowed to and from
  specific pods, KNPs provide the foundation for zero-trust networking and least-privilege
  access in cloud-native environments. But there’s a problem: KNPs are risky, and
  applying them without a clear game plan can be potentially disruptive. Without deep
  insight into existing traffic flows, applying a restrictive policy can instantly
  break connectivity killing live workloads, user sessions, or critical app dependencies.
  An even scarier scenario is when we implement policies that we think cover everything
  and workloads actually work, but after a restart or scaling operation we hit new
  problems. Kubernetes, with all of its features, has no built-in “dry run” mode for
  policies, and no first-class observability to show what would be blocked or allowed
  which is the right decision since Kubernetes is an orchestrator not an implementer.
  This forces platform teams into a difficult choice, deploy permissive or no policies
  and weaken security, or Risk service disruption while debugging restrictive ones.
  As a result, many teams delay implementing network policies entirely only to regret
  it after a zero-day exploit like Log4Shell, XZ backdoor, or other vulnerabilities
  that can impact production. The fear of breaking something becomes the top reason
  why Kubernetes environments go unsegmented. You can’t enforce what you can’t test
  safely. For instance, let’s say you want to secure a workload deployed by another
  team. You don’t control how it was configured.'
---
Open the original post ↗ https://www.tigera.io/blog/dry-run-your-kubernetes-network-policies-with-calico-staged-network-policies/
