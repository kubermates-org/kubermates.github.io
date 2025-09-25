---
title: 'Kubernetes Observability: Your Q&A Guide to Calico Whisker'
date: '2025-09-24T20:45:51+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/kubernetes-observability-your-qa-guide-to-calico-whisker/
post_kind: link
draft: false
tldr: 'Frequently Asked Questions From The Community Do you have more questions? The
  Calico community is here to help! Calico Whisker is quickly becoming the go-to tool
  for teams that want granular, real-time visibility into their Kubernetes network
  traffic and security posture. It provides an intuitive, high-level view of your
  network, but as with any new tool, there are going to be questions: How does it
  handle manifest-based installations versus operator-based ones? Can it leverage
  eBPF for high-performance data collection? What’s the best way to export its rich
  flow logs to your existing SIEM or visualize traffic on a network map? Getting the
  most out of Whisker requires understanding its inner workings and this guide is
  designed to help you master this exciting tool with support from the Calico community.'
summary: 'Frequently Asked Questions From The Community Do you have more questions?
  The Calico community is here to help! Calico Whisker is quickly becoming the go-to
  tool for teams that want granular, real-time visibility into their Kubernetes network
  traffic and security posture. It provides an intuitive, high-level view of your
  network, but as with any new tool, there are going to be questions: How does it
  handle manifest-based installations versus operator-based ones? Can it leverage
  eBPF for high-performance data collection? What’s the best way to export its rich
  flow logs to your existing SIEM or visualize traffic on a network map? Getting the
  most out of Whisker requires understanding its inner workings and this guide is
  designed to help you master this exciting tool with support from the Calico community.
  We’ve compiled the most frequently asked questions from our community Slack , support
  conversations, and CalicoCon sessions. This Q&A covers everything from initial installation
  tips and version requirements to advanced topics like filtering flow logs and integrating
  with Goldmane, the powerful API that underpins Whisker. Whether you’re just beginning
  to evaluate Whisker or looking to extract more value from your current deployment,
  this guide provides clear, actionable answers to help you level up your Kubernetes
  observability game. Yes you can, noting that Calico Whisker requires Calico v3.30
  or higher. If you’re running an older version, you’ll need to upgrade your cluster
  first. To check your Calico version, run the following command: kubectl exec -it
  -n tigera-operator deployment/tigera-operator -- operator --version kubectl exec
  -it -n tigera-operator deployment/tigera-operator -- operator --version If your
  version is older than v3.30, follow the upgrade guide or 📹 watch the video below
  for a demonstration of how to upgrade Calico on Kubernetes: Yes! While we recommend
  upgrading to the operator-based installation for a smoother experience and easier
  lifecycle management, you can still use Whisker with a manifest-based installation.
  Check out this detailed installation guide for enabling Whisker manually. Whisker
  and Goldmane contain sensitive network and workload data and are secured via NetworkPolicies
  by default. We strongly recommend against exposing this data externally. If you
  absolutely must expose it, you can create a new ingress NetworkPolicy to allow external
  traffic.'
---
Open the original post ↗ https://www.tigera.io/blog/kubernetes-observability-your-qa-guide-to-calico-whisker/
