---
title: What’s New in Calico v3.32
date: '2026-05-13T22:23:05+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/whats-new-in-calico-v3-32/
post_kind: link
draft: false
tldr: 🚨 Breaking Changes & Deprecations 🚀 Key Feature Updates 1. KubeVirt VM Live
  Migration Support 2.
summary: '🚨 Breaking Changes & Deprecations 🚀 Key Feature Updates 1. KubeVirt VM Live
  Migration Support 2. Sidecarless mTLS (Istio Ambient Mode) 3. Maglev Consistent-Hash
  Load Balancing 4. Whisker Policy Filtering (Tech Preview) Kubernetes ClusterNetworkPolicy
  (Alpha2) 🚨Breaking change🚨 Native v3 CRDs (Tech Preview) KubeVirt Virtual Machine
  (VM) Live Migration mTLS encryption without compromise – Istio Ambient Mode (Tech
  Preview) Maglev Consistent-Hash Load Balancing Whisker Policy Filtering (Tech Preview)
  We’re excited to announce the release of Calico Open Source v3.32! 🎉 This release
  corresponds with Kubernetes v1.36 (Codename Haru) and it goes beyond just sharing
  a cat as the mascot of the release, it actually extends capabilities and features
  of Kubernetes to keep you up to date with the latest innovations of the cloud. This
  release brings some of the most significant architectural changes in Calico, from
  live-migrating KubeVirt VMs to eBPF based Maglev load balancer. Here’s a quick look
  at everything that’s new: ClusterNetworkPolicy (Alpha2) replaces Admin and Baseline
  Admin Network Policies: AdminNetworkPolicy and BaselineAdminNetworkPolicy have been
  removed. You must migrate to ClusterNetworkPolicy before upgrading to v3.32, as
  Calico will no longer enforce the old resources. AdminNetworkPolicy BaselineAdminNetworkPolicy
  ClusterNetworkPolicy calico-apiserver Deprecated: The aggregated API server is deprecated
  and will be removed in a future release. It is being replaced by Native v3 CRDs.
  (Requires MutatingAdmissionPolicy feature gate, Kubernetes 1.30+). calico-apiserver
  What it does: Allows live-migrating KubeVirt VMs between nodes without dropping
  TCP connections.'
---
Open the original post ↗ https://www.tigera.io/blog/whats-new-in-calico-v3-32/
