---
title: 'Introducing the Nirmata Cloud Controller: Preventive Cloud Governance at Scale'
date: '2026-02-20T19:27:40+00:00'
tags:
- nirmata
- kubernetes
source: Nirmata Blog
external_url: https://nirmata.com/2026/02/20/introducing-the-nirmata-cloud-controller-preventive-cloud-governance-at-scale/?utm_source=rss&utm_medium=rss&utm_campaign=introducing-the-nirmata-cloud-controller-preventive-cloud-governance-at-scale
post_kind: link
draft: false
tldr: What Is the Nirmata Cloud Controller? Stop Risky Cloud Changes The Moment They
  Happen Cloud Admission Controller How the Cloud Controller Works 1. Inline Enforcement
  (Admission Control) 2.
summary: 'What Is the Nirmata Cloud Controller? Stop Risky Cloud Changes The Moment
  They Happen Cloud Admission Controller How the Cloud Controller Works 1. Inline
  Enforcement (Admission Control) 2. Continuous Scanning (Drift & Legacy Detection)
  Continuous Compliance When Reality Drifts from IaC Cloud Scanner Flow Kyverno-Style
  Policies Extended Beyond Kubernetes Unified Governance Model Built for Large AWS
  Organizations Enterprise Discovery Model Standardized Policy Reporting for Platform
  Teams Unified Governance Across Pipelines, Clusters, and Cloud Unified Governance
  View How is Cloud Controller Different from CSPM and CNAPP? Key Differences How
  to Get Started with Nirmata Cloud Controller Cloud governance has a timing problem.
  Most organizations discover cloud misconfigurations after they happen, through CSPM
  dashboards, CNAPP alerts, or tickets that arrive long after the risky change is
  already live. By then, platform teams are stuck reacting instead of preventing.
  The Nirmata Cloud Controller (NCC) changes that model by bringing preventive, policy-as-code
  governance directly to the cloud API layer , while still providing continuous compliance
  and visibility as environments evolve. For platform engineers, Cloud Controller
  acts as a central control plane for governing cloud actions, cloud drift, and cloud
  posture, using the same Kyverno-style policies and reporting models they already
  trust in Kubernetes. The Nirmata Cloud Controller is a preventive cloud governance
  platform that enforces policy-as-code on AWS API requests in real time while continuously
  scanning cloud environments for drift and compliance gaps. Unlike traditional CSPM
  or CNAPP tools that detect issues after deployment, Cloud Controller can block non-compliant
  cloud changes before they are applied. The defining capability of the Nirmata Cloud
  Controller is admission-style control for cloud APIs. Instead of only scanning for
  issues later, Cloud Controller can intercept AWS API requests in real-time , evaluate
  them against policy, and decide whether they should be allowed at all. CLI / SDK
  / Automation | v Nirmata Cloud Admission Controller | Kyverno Policy Evaluation
  | Allow ✅ Deny ❌ | v AWS APIs This applies to: AWS CLI commands Automation and pipelines
  Scripts and tooling Any direct API-driven cloud change This is true preventive governance,
  not just visibility after the fact.'
---
Open the original post ↗ https://nirmata.com/2026/02/20/introducing-the-nirmata-cloud-controller-preventive-cloud-governance-at-scale/?utm_source=rss&utm_medium=rss&utm_campaign=introducing-the-nirmata-cloud-controller-preventive-cloud-governance-at-scale
