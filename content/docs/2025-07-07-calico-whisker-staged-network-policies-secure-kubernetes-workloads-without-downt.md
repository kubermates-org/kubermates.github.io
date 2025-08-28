---
title: 'Calico Whisker & Staged Network Policies: Secure Kubernetes Workloads Without
  Downtime'
date: '2025-07-07T20:00:17+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/calico-whisker-staged-network-policies-secure-kubernetes-workloads-without-downtime/
post_kind: link
draft: false
tldr: Rolling out network policies in a live Kubernetes cluster can feel like swapping
  wings mid-flight—one typo or overly broad rule and critical traffic is grounded.
  Calico’s Staged Network Policies remove the turbulence by letting you deploy policies
  in staged mode, so you can observe their impact before enforcing anything.
summary: Rolling out network policies in a live Kubernetes cluster can feel like swapping
  wings mid-flight—one typo or overly broad rule and critical traffic is grounded.
  Calico’s Staged Network Policies remove the turbulence by letting you deploy policies
  in staged mode, so you can observe their impact before enforcing anything. Add Whisker
  , the open-source policy enforcement and testing tool (introduced as part of Calico
  Open Source 3. 30 ) that captures every flow and tags it with a policy verdict,
  and you’ve got a safety harness that proves your change is sound long before you
  flip the switch. In this post, we’ll walk you through how you can leverage these
  capabilities to tighten security, validate intent, and ship changes confidently—without
  a single packet of downtime. Calico for Policy is a CNI agnostic tool. Refer to
  the Calico Open Source docs for a list of supported CNIs. The git repository for
  this blog post can be found here. For this post, let’s deploy a simple AKS cluster
  with Azure CNI. Now that our cluster is deployed. Let’s provision a demo application.
  For this post, we will deploy a three-tier web application called “yet-another-bank”
  (yaobank).
---
Open the original post ↗ https://www.tigera.io/blog/calico-whisker-staged-network-policies-secure-kubernetes-workloads-without-downtime/
