---
title: 'Deploying VMware Cloud Foundation Private AI Services: Navigating Supervisor
  Architectures With and Without NSX'
date: '2026-06-11T15:42:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/06/11/deploying-vmware-cloud-foundation-private-ai-services-navigating-supervisor-architectures-with-and-without-nsx/
post_kind: link
draft: false
tldr: 'The Role of the vSphere Supervisor in VCF Private AI Services Supervisor Networking
  Models: NSX vs. Foundation Load Balancer The Consumption Layer: VCF Automation and
  Multi-Tenancy Architectural Considerations: Pros and Cons Planning for the Future:
  Evolving Your Network Architecture Conclusion Useful Links Discover more from VMware
  Cloud Foundation (VCF) Blog Related Articles VCF Breakroom Chats Episode 87 – Governing
  the AI Private Cloud: Deep Dive into VCF 9.1 Infrastructure Placement Policies Deploying
  VMware Cloud Foundation Private AI Services: Navigating Supervisor Architectures
  With and Without NSX Modern Automation with VMware Cloud Foundation Part 2: Modern
  Infrastructure as Code with VCF To help businesses develop generative AI applications
  securely within their private data centers, VCF Private AI Services is built directly
  into VMware Cloud Foundation (VCF).'
summary: 'The Role of the vSphere Supervisor in VCF Private AI Services Supervisor
  Networking Models: NSX vs. Foundation Load Balancer The Consumption Layer: VCF Automation
  and Multi-Tenancy Architectural Considerations: Pros and Cons Planning for the Future:
  Evolving Your Network Architecture Conclusion Useful Links Discover more from VMware
  Cloud Foundation (VCF) Blog Related Articles VCF Breakroom Chats Episode 87 – Governing
  the AI Private Cloud: Deep Dive into VCF 9.1 Infrastructure Placement Policies Deploying
  VMware Cloud Foundation Private AI Services: Navigating Supervisor Architectures
  With and Without NSX Modern Automation with VMware Cloud Foundation Part 2: Modern
  Infrastructure as Code with VCF To help businesses develop generative AI applications
  securely within their private data centers, VCF Private AI Services is built directly
  into VMware Cloud Foundation (VCF). This embedded suite of services abstracts away
  the complexity of AI infrastructure, providing an end-to-end platform that includes
  a Model Gallery, Model Runtime, Agent Builder, and Data Indexing capabilities for
  Retrieval-Augmented Generation (RAG), API Gateway, and MCP Tools Registry. The architectural
  foundation that powers this platform is the vSphere Supervisor. When configuring
  the Supervisor for your AI workloads, VCF 9 offers the flexibility of two distinct
  networking architectures: a VMware NSX-backed model and a vSphere Distributed Switch
  (VDS)-backed model. Both approaches provide a robust foundation for VCF Private
  AI Services, allowing organizations to align their infrastructure with their specific
  operational readiness. Whether your objective is to launch a streamlined, rapid
  proof-of-concept or to establish a fully automated, multi-tenant AI cloud for your
  developers, your networking choice will shape the consumption and scalability of
  your environment. Let’s explore how the Supervisor enables VCF Private AI Services
  and the architectural considerations of deploying with and without NSX. At a technical
  level, VCF Private AI Services utilizes the vSphere Supervisor to transform your
  ESXi hypervisors into a native Kubernetes control plane. Activating the Supervisor
  provides the essential API and resource management layer required to seamlessly
  install and run your VCF Private AI Services. (Note: When sizing your Supervisor
  control plane VMs for Small, Medium, or Large, plan your capacity carefully, as
  you can only scale the control plane up, never down). As shown in the architecture
  diagram above, VCF Private AI Services operates through a declarative Kubernetes
  model utilizing two key components: Kubenertes Operator for the VCF Private AI Services
  (Supervisor Level) : In standard Kubernetes architecture, an “Operator” is a specialized
  software controller that knows how to manage a complex application.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/06/11/deploying-vmware-cloud-foundation-private-ai-services-navigating-supervisor-architectures-with-and-without-nsx/
