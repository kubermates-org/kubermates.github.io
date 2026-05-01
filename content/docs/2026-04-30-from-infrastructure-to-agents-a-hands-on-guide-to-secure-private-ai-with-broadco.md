---
title: 'From Infrastructure to Agents: A Hands-On Guide to Secure Private AI with
  Broadcom – Part 2'
date: '2026-04-30T13:25:05+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/04/30/guide-to-secure-private-ai-with-broadcom-part-2/
post_kind: link
draft: false
tldr: 'Part 2 of 4: Securing GPU-Accelerated AI Workloads with VMware vDefend on VMware
  Private AI Foundation with NVIDIA From Catalog to Cluster: Provisioning AI Infrastructure
  The NIM RAG Blueprint: A Hybrid Architecture with External Elasticsearch The Security
  Problem: A Flat Network and an External Dependency vDefend: Zero-Trust Microsegmentation
  for AI Components From NSX Manager to Antrea: The Policy Pipeline Security Groups
  Based on Workload Identity The Firewall Rules: Ingress, Egress, and Default Deny
  Microsegmentation as Code with Terraform Extending Zero Trust to the Network Boundary:
  Antrea Egress with NSX VPC How It Works: From Pod to Public Subnet Defense in Depth:
  Two Independent Enforcement Points Proving It Works: Antrea Traceflow Blocked Path:
  Frontend to Elasticsearch (Infrastructure Layer DFW) The Complete Picture: Private
  AI with Lateral Security Conclusion Discover more from VMware Cloud Foundation (VCF)
  Blog Related Articles From Infrastructure to Agents: A Hands-On Guide to Secure
  Private AI with Broadcom - Part 2 The New Frontier: Leading the Cloud-Native Evolution
  Webinar Recap: Design and Architecture Considerations for VMware vSphere Kubernetes
  Service on VMware Cloud Foundation In Part 1 of this series , we laid the hardware
  and network groundwork for a secure Private AI architecture. We walked through how
  to enforce deep GPU tenancy, physically and logically isolating compute resources
  from the organizational level down to the silicon.'
summary: 'Part 2 of 4: Securing GPU-Accelerated AI Workloads with VMware vDefend on
  VMware Private AI Foundation with NVIDIA From Catalog to Cluster: Provisioning AI
  Infrastructure The NIM RAG Blueprint: A Hybrid Architecture with External Elasticsearch
  The Security Problem: A Flat Network and an External Dependency vDefend: Zero-Trust
  Microsegmentation for AI Components From NSX Manager to Antrea: The Policy Pipeline
  Security Groups Based on Workload Identity The Firewall Rules: Ingress, Egress,
  and Default Deny Microsegmentation as Code with Terraform Extending Zero Trust to
  the Network Boundary: Antrea Egress with NSX VPC How It Works: From Pod to Public
  Subnet Defense in Depth: Two Independent Enforcement Points Proving It Works: Antrea
  Traceflow Blocked Path: Frontend to Elasticsearch (Infrastructure Layer DFW) The
  Complete Picture: Private AI with Lateral Security Conclusion Discover more from
  VMware Cloud Foundation (VCF) Blog Related Articles From Infrastructure to Agents:
  A Hands-On Guide to Secure Private AI with Broadcom - Part 2 The New Frontier: Leading
  the Cloud-Native Evolution Webinar Recap: Design and Architecture Considerations
  for VMware vSphere Kubernetes Service on VMware Cloud Foundation In Part 1 of this
  series , we laid the hardware and network groundwork for a secure Private AI architecture.
  We walked through how to enforce deep GPU tenancy, physically and logically isolating
  compute resources from the organizational level down to the silicon. We also established
  our foundational routing, demonstrating how to deploy dedicated Virtual Private
  Clouds (VPCs) and even fully airgapped environments to dictate strict network topologies
  for different business units. We did this because enterprises are deploying AI workloads
  to private cloud infrastructure for compelling reasons: data sovereignty, regulatory
  compliance, intellectual property protection, and the assurance that proprietary
  documents, model weights, and inference data never leave the organization’s control.
  VMware Private AI Foundation with NVIDIA delivers on this promise, providing a turnkey
  platform on VMware Cloud Foundation (VCF) for deploying GPU-accelerated AI pipelines,
  from inference and embedding to full retrieval-augmented generation (RAG) workflows,
  all within the enterprise data center. But bringing AI workloads on-premises solves
  only half of the security equation: Private AI protects data from leaving the organization.
  Even with robust VPCs and dedicated hardware slices, we still have to answer a critical
  question: What protects the AI components from each other? In a typical Kubernetes
  deployment, once traffic is inside the cluster, every pod can reach every other
  pod. A compromised component, whether through a supply chain vulnerability in a
  model dependency, a prompt injection exploit, or a container escape, has a flat
  network path to the most sensitive assets in the pipeline: the language model serving
  proprietary inferences, the vector database holding your corporate knowledge base,
  and the orchestration layer controlling all of it. This is the lateral security
  gap, and for AI workloads, the stakes are uniquely high. Before we dive in, note
  that we’ve included a full, real-time demo video at the very end of this post showing
  exactly how we close this gap in action. But don’t skip ahead just yet as the video
  only scratches the surface. The post serves as your comprehensive lab notes, going
  into much greater depth with extensive architecture breakdowns, under-the-hood configurations,
  and the exact Terraform code snippets you won’t see in the recording.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/04/30/guide-to-secure-private-ai-with-broadcom-part-2/
