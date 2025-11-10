---
title: 'Safely managing Cilium network policies in Kubernetes: Testing and simulation
  techniques'
date: '2025-11-06T15:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/11/06/safely-managing-cilium-network-policies-in-kubernetes-testing-and-simulation-techniques/
post_kind: link
draft: false
tldr: 'How do Cilium network policy operations and enforcement modes work? Test environment
  setup Scenario 1: Applying the first default-deny policy Solution 1. a: Endpoint
  audit mode Solution 1.'
summary: 'How do Cilium network policy operations and enforcement modes work? Test
  environment setup Scenario 1: Applying the first default-deny policy Solution 1.
  a: Endpoint audit mode Solution 1. b: Policy default-deny mode Scenario 2: Making
  changes to the existing policies Solution 2. a: L7 allow-all Summary & next steps
  Posted on November 6, 2025 by Dean Lewis, Isovalent CNCF projects highlighted in
  this post Network policy changes are among the most frequent operations in a Kubernetes
  cluster. They are also among the most delicate, as even a small mistake can lead
  to widespread traffic disruption. This tutorial walks through several methods to
  make policy management safer, especially in day-2 operations or brownfield deployments
  where clusters already run critical workloads. It shows how to test and validate
  changes before enforcing them, helping teams adopt a more reliable approach to policy
  rollout. By following these steps, you can build confidence in your network policy
  lifecycle and reduce the likelihood of accidental outages. Cilium network policies
  build upon Kubernetes NetworkPolicy, extending it with deeper visibility and more
  flexible rule types. Policies are used to allow or deny traffic based on defined
  rules, which can apply to ingress, egress, or both. These rules are evaluated at
  the datapath level, meaning enforcement can take place directly in the kernel through
  eBPF. Every Cilium-managed endpoint operates under a policy enforcement mode, which
  defines the default network behavior before and after a policy is applied: Default:
  All traffic is allowed until an endpoint is selected by a policy.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/11/06/safely-managing-cilium-network-policies-in-kubernetes-testing-and-simulation-techniques/
