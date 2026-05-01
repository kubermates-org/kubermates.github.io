---
title: 'From Infrastructure to Agents: A Hands-On Guide to Secure Private AI with
  Broadcom – Part 1'
date: '2026-04-27T12:32:53+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/04/27/guide-to-secure-private-ai-with-broadcom-part-1/
post_kind: link
draft: false
tldr: 'Part 1 of 4: Setting the Infrastructure – Networking and Deep Tenancy Architecting
  Deep GPU Tenancy: Slicing the Compute from the Org to the Silicon Strong Network
  Control: From Airgapped AI to Dynamic VPCs Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles How Many Users Can Your LLM Server Really Handle? From
  Infrastructure to Agents: A Hands-On Guide to Secure Private AI with Broadcom -
  Part 2 The New Frontier: Leading the Cloud-Native Evolution As enterprises rush
  to integrate AI into their workflows, moving from experimentation to production
  is often stalled by a critical hurdle: risk around security, privacy, and compliance.
  De-risking the AI enterprise requires more than just deploying a model behind a
  corporate firewall.'
summary: 'Part 1 of 4: Setting the Infrastructure – Networking and Deep Tenancy Architecting
  Deep GPU Tenancy: Slicing the Compute from the Org to the Silicon Strong Network
  Control: From Airgapped AI to Dynamic VPCs Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles How Many Users Can Your LLM Server Really Handle? From
  Infrastructure to Agents: A Hands-On Guide to Secure Private AI with Broadcom -
  Part 2 The New Frontier: Leading the Cloud-Native Evolution As enterprises rush
  to integrate AI into their workflows, moving from experimentation to production
  is often stalled by a critical hurdle: risk around security, privacy, and compliance.
  De-risking the AI enterprise requires more than just deploying a model behind a
  corporate firewall. It means ensuring strict tenant privacy, rigorously scanning
  containerized models for vulnerabilities before they are ever deployed , securing
  those models in production against prompt injections and data poisoning, and applying
  robust governance to autonomous AI agents. While the industry discusses these security
  concepts at length, practical, engineering-focused guidance remains scarce. In this
  blog series, we are moving past high-level architecture to share our lab notes on
  securing a complete private AI stack. We aren’t starting from bare metal architecture
  though. For architecture build, we have deployed VMware Private AI Foundation with
  NVIDIA, which means VMware Private AI Services, VMware Cloud Foundation (VCF), and
  VMware vSphere Kubernetes Services (VKS) were deployed. With the infrastructure
  already stood up, we shift the deployment into a fortified, enterprise-grade AI
  environment. Whether you are a network engineer, a security architect, or a platform
  operator, this series provides a security blueprint for using VMware Private AI
  Services, vDefend, Avi, Istio, admission controllers, and the Tanzu platform to
  effectively protect your AI workloads from privacy, security and compliance risks.
  To provide a clear, actionable path, we have structured this blog series into four
  blogs: Part 1: Setting the infrastructure – Networking and Deep Tenancy Building
  on our existing VCF, VKS, and a private AI deployment, this post details how we
  construct a secure AI environment. We cover the configuration of L3 networking and
  the establishment of deep GPU tenancy to isolate workloads before we even look at
  a firewall rule. Part 2: Securing GPU-Accelerated AI Workloads with VMware vDefend
  on VMware Private AI Foundation with NVIDIA With the infrastructure deployed, our
  second post dives into deploying vDefend to enforce L3 firewalling across the VMs
  and pods alike.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/04/27/guide-to-secure-private-ai-with-broadcom-part-1/
