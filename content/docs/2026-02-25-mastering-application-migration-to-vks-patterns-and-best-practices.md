---
title: 'Mastering Application Migration to VKS: Patterns and Best Practices'
date: '2026-02-25T20:38:18+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/02/25/mastering-application-migration-to-vks-patterns-and-best-practices/
post_kind: link
draft: false
tldr: 'Strategy 1: The “Lift and Shift” (Re-platforming) How it works The caveats
  Strategy 2: The “Pipeline Retargeting” (Re-deploy) How it works The “VCF native”
  evolution The Stateful Dilemma: Handling Persistent Data The solution Handling “The
  Big Version Jump” (Upgrades) Conclusion Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles Model Gallery: How to Use JupyterLab Notebooks to Simplify
  Model Deployment and Management Mastering Application Migration to VKS: Patterns
  and Best Practices Automic Automation: Application-Aware Automation for the Private
  Cloud Migrating applications to a modern platform like VMware vSphere Kubernetes
  Service (VKS) is rarely a “one-size-fits-all” operation. Whether you are moving
  from a generic Kubernetes provider (like OpenShift, EKS, or GKE), migrating from
  virtual machines, or repatriating cloud services, the strategy you choose depends
  heavily on your current automation maturity and workload requirements.'
summary: 'Strategy 1: The “Lift and Shift” (Re-platforming) How it works The caveats
  Strategy 2: The “Pipeline Retargeting” (Re-deploy) How it works The “VCF native”
  evolution The Stateful Dilemma: Handling Persistent Data The solution Handling “The
  Big Version Jump” (Upgrades) Conclusion Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles Model Gallery: How to Use JupyterLab Notebooks to Simplify
  Model Deployment and Management Mastering Application Migration to VKS: Patterns
  and Best Practices Automic Automation: Application-Aware Automation for the Private
  Cloud Migrating applications to a modern platform like VMware vSphere Kubernetes
  Service (VKS) is rarely a “one-size-fits-all” operation. Whether you are moving
  from a generic Kubernetes provider (like OpenShift, EKS, or GKE), migrating from
  virtual machines, or repatriating cloud services, the strategy you choose depends
  heavily on your current automation maturity and workload requirements. In this post,
  we discuss the primary migration patterns: re-platforming (“lift and shift”) versus
  re-deploying (pipeline-driven). The following guide can help you choose the right
  path for your organization. Best for: Organizations with little to no automation
  or deployment pipelines If your team is hand-deploying applications or lacks mature
  GitOps practices, the most viable path is often a “backup and restore” approach
  using tools like Velero. Backup source state: Velero queries the source Kubernetes
  API to grab all objects (deployments, secrets, config maps, services) and bundles
  them into an S3-compatible storage bucket. Restore to VKS: You install Velero on
  the destination VKS cluster and restore from that backup. Since VKS is CNCF-conformant,
  it replays the API details into the new cluster. Be selective: You cannot simply
  back up everything. You must avoid system namespaces (like kube-system) and target
  only specific application workloads using labels and selectors. Manual cleanup:
  This is a 1:1 state copy. If the destination environment requires different configurations
  (e.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/02/25/mastering-application-migration-to-vks-patterns-and-best-practices/
