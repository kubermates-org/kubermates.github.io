---
title: Streamlining CI/CD and GitOps on VMware vSphere Kubernetes Service with Harness,
  Wiz, and Dynatrace
date: '2026-06-16T11:54:43+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/06/16/streamlining-ci-cd-and-gitops-on-vmware-vsphere-kubernetes-service-with-harness-wiz-and-dynatrace/
post_kind: link
draft: false
tldr: 'The Architecture: A Unified Consumption Model Implementing GitOps for VKS Shifting
  Left with Integrated Security and Observability Security Scanning with Wiz Performance
  Insights with Dynatrace Getting Started with the VKS Consumption Model Discover
  more from VMware Cloud Foundation (VCF) Blog Related Articles How to Upgrade to
  VMware Cloud Foundation 9.1 Understanding Large Memory Pages with VMware Advanced
  Memory Tiering VCF Breakroom Chats Episode 88 – Unpacking the Latest AI Advancements
  in the VCF 9.1 Release- 1 With VMware Cloud Foundation (VCF) 9, the focus for platform
  teams has shifted from simply providing infrastructure to enabling seamless, secure
  application delivery. As organizations scale their containerized workloads, the
  challenge lies in balancing developer velocity with operational guardrails.'
summary: 'The Architecture: A Unified Consumption Model Implementing GitOps for VKS
  Shifting Left with Integrated Security and Observability Security Scanning with
  Wiz Performance Insights with Dynatrace Getting Started with the VKS Consumption
  Model Discover more from VMware Cloud Foundation (VCF) Blog Related Articles How
  to Upgrade to VMware Cloud Foundation 9.1 Understanding Large Memory Pages with
  VMware Advanced Memory Tiering VCF Breakroom Chats Episode 88 – Unpacking the Latest
  AI Advancements in the VCF 9.1 Release- 1 With VMware Cloud Foundation (VCF) 9,
  the focus for platform teams has shifted from simply providing infrastructure to
  enabling seamless, secure application delivery. As organizations scale their containerized
  workloads, the challenge lies in balancing developer velocity with operational guardrails.
  In this article, we are diving into how you can build a robust, enterprise-grade
  delivery pipeline using VMware vSphere Kubernetes Service (VKS) integrated with
  Harness for CI/CD, Wiz for security, and Dynatrace for observability. To simplify
  the deployment of modern applications, we’ve introduced a structured VKS Consumption
  Model. This model provides a blueprint for using Infrastructure as Code and Helm
  to bootstrap VKS clusters and connect them to a centralized delivery plane. At the
  heart of this design is the Harness Delegate. Running within your VCF environment,
  the Delegate acts as the bridge between the Harness SaaS manager and your private
  VKS clusters. This ensures that your sensitive credentials and cluster endpoints
  never leave your secure environment while still benefiting from a powerful, cloud-native
  orchestration platform. GitOps has become the gold standard for Kubernetes operations,
  and for good reason. By treating your Git repository as the single source of truth,
  you ensure that the state of your VKS cluster always matches your desired configuration.
  Using Harness GitOps , platform teams can manage the lifecycle of VKS clusters and
  applications with ease: State Reconciliation: Automatically detect and correct configuration
  drift between Git and your live VKS environment. Version Control: Every change to
  your infrastructure or application is audited and reversible through Git commits.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/06/16/streamlining-ci-cd-and-gitops-on-vmware-vsphere-kubernetes-service-with-harness-wiz-and-dynatrace/
