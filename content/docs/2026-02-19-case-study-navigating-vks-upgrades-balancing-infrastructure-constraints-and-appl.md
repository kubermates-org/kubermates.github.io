---
title: 'Case Study: Navigating VKS Upgrades – Balancing Infrastructure Constraints
  and Application Reality'
date: '2026-02-19T18:04:09+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/02/19/case-study-navigating-vks-upgrades-balancing-infrastructure-constraints-and-application-reality/
post_kind: link
draft: false
tldr: 'Option 1: Sequential In-Place Upgrade Typical Flow Why Teams Like It The Operational
  Reality Application Considerations (Often the Deciding Factor) Option 2: Parallel
  / Blue-Green Upgrade High-Level Approach Why Teams Choose This Prerequisites for
  Success: The “Must-Haves” Decision Checklist Platform and Scale Application Readiness
  Operations and Governance Infrastructure Constraints How VMware Professional Services
  Accelerates the Upgrade 1. Assessment and Dependency Mapping 2.'
summary: 'Option 1: Sequential In-Place Upgrade Typical Flow Why Teams Like It The
  Operational Reality Application Considerations (Often the Deciding Factor) Option
  2: Parallel / Blue-Green Upgrade High-Level Approach Why Teams Choose This Prerequisites
  for Success: The “Must-Haves” Decision Checklist Platform and Scale Application
  Readiness Operations and Governance Infrastructure Constraints How VMware Professional
  Services Accelerates the Upgrade 1. Assessment and Dependency Mapping 2. Strategy
  Selection and Roadmap Design 3. Automation and Tooling 4. Operational Enablement
  Summary Discover more from VMware Cloud Foundation (VCF) Blog Related Articles Model
  Gallery: How to Use JupyterLab Notebooks to Simplify Model Deployment and Management
  Mastering Application Migration to VKS: Patterns and Best Practices Automic Automation:
  Application-Aware Automation for the Private Cloud Kubernetes upgrades are often
  presented as straightforward, linear progressions: move from one version to the
  next, validate, and repeat. This approach—commonly called the Sequential In-Place
  Upgrade—is proven, conservative, and widely adopted. However, in modern enterprise
  platforms, upgrades span much more than just the Kubernetes version number. They
  involve a complex interplay of: A management plane (Supervisor / platform services)
  Platform layers (VMware Kubernetes Service – VKS) Workload clusters Applications
  with varying levels of resilience and state Understanding both the technical requirements
  and the organizational realities is critical to helping teams choose the right upgrade
  model and avoid costly surprises. The in-place model upgrades existing components
  layer by layer, modifying the running infrastructure. Supervisor Cluster: 1.29 →
  1.30 VKS Service: Updated to support newer Kubernetes versions (e. g. , v3.1 → v3.5)
  Workload Clusters: 1.30 → 1.31 → 1.32 → 1.33 Reuses existing infrastructure: No
  need for massive spare capacity.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/02/19/case-study-navigating-vks-upgrades-balancing-infrastructure-constraints-and-application-reality/
