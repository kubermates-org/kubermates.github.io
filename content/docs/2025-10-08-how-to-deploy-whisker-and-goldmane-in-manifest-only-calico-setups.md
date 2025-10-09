---
title: How to Deploy Whisker and Goldmane in Manifest Only Calico Setups
date: '2025-10-08T19:29:00+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/how-to-deploy-whisker-and-goldmane-in-manifest-only-calico-setups/
post_kind: link
draft: false
tldr: Your Step-by-Step to Observability Without the Operator Why Whisker and Goldmane
  Matter Installing Whisker and Goldmane Manually Requirements Generating Certificates
  and Certificate Authority (CA) Tuning Typha to use certificates Fixing DNS Issues
  Deploying Goldmane Tuning Goldmane Deployment Deploying Whisker UI Observability
  Unlocked (and Why the Operator Helps) Final Thoughts For Calico users who install
  using manifests, enabling the new observability features Whisker and Goldmane from
  version 3.30 has been a challenge. While these tools offer powerful insights into
  Kubernetes network flows and policy decisions, previous documentation was only for
  users who deployed with the Tigera operator.
summary: 'Your Step-by-Step to Observability Without the Operator Why Whisker and
  Goldmane Matter Installing Whisker and Goldmane Manually Requirements Generating
  Certificates and Certificate Authority (CA) Tuning Typha to use certificates Fixing
  DNS Issues Deploying Goldmane Tuning Goldmane Deployment Deploying Whisker UI Observability
  Unlocked (and Why the Operator Helps) Final Thoughts For Calico users who install
  using manifests, enabling the new observability features Whisker and Goldmane from
  version 3.30 has been a challenge. While these tools offer powerful insights into
  Kubernetes network flows and policy decisions, previous documentation was only for
  users who deployed with the Tigera operator. The operator automates several advanced,
  security-focused steps required to safely deploy Goldmane, which is why manifest
  users have had a more difficult time. These steps are crucial for protecting sensitive
  information. We’ve heard from many of you in the Calico Slack community: you’re
  eager to try out Whisker and Goldmane but aren’t sure how to set them up without
  Helm or the operator. For anyone who’s up for a challenge, this blog post provides
  a step-by-step guide on how to get everything wired up the hard way. However, even
  if you already use the operator, keep reading! We’re going to pull back the curtain
  on the magic it performs behind the scenes. Understanding these mechanics will help
  you troubleshoot, customize, and better appreciate a managed approach, whether you’re
  an SRE, platform engineer, or a curious cluster admin. What you will achieve at
  the end of this blog: You will learn how to get up and running with Whisker and
  Goldmane in a manifest based installation. You will learn why a Helm chart or the
  Tigera operator is our recommendation to manage your Kubernetes workloads at scale.
  You will have some hands on experience on what to look for when things are deployed
  in a real life scenario. Without Goldmane and tools, you’re essentially flying blind
  and you: Can’t easily debug why traffic is dropped Can’t visualize how policies
  affect flows Can’t trace service-to-service communication paths This leads to increased
  time-to-resolution for network bugs, frustration from teams consuming the platform,
  limited audit capabilities for security teams For manifest-only users, the lack
  of clear installation steps means many miss out on these benefits and as a developer
  advocate.'
---
Open the original post ↗ https://www.tigera.io/blog/how-to-deploy-whisker-and-goldmane-in-manifest-only-calico-setups/
