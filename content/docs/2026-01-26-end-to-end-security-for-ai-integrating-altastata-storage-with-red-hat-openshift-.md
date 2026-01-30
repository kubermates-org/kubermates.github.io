---
title: 'End-to-end security for AI: Integrating AltaStata Storage with Red Hat OpenShift
  confidential containers'
date: '2026-01-26T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/end-end-security-ai-integrating-altastata-storage-red-hat-openshift-confidential-containers
post_kind: link
draft: false
tldr: 'End-to-end security for AI: Integrating AltaStata Storage with Red Hat OpenShift
  confidential containers The challenge: Storage in confidential computing AI-specific
  storage security challenges A. Training: Dataset poisoning attack B.'
summary: 'End-to-end security for AI: Integrating AltaStata Storage with Red Hat OpenShift
  confidential containers The challenge: Storage in confidential computing AI-specific
  storage security challenges A. Training: Dataset poisoning attack B. Compromising
  model storage: AI model replacement attack C. Inference: RAG documents poisoning
  attack Three approaches to storage security 1. Cloud server-side encryption (not
  end-to-end) 2. Master key end-to-end encryption 3. AltaStata enterprise solution
  Performance optimizations Multicloud storage support for confidential containers
  AltaStata key advantages Security comparison Integration with confidential containers
  AltaStata and confidential containers for AI workloads Real-world examples Securing
  PyTorch model training example Protecting RAG pipeline example Conclusion Red Hat
  Product Security About the authors Serge Vilvovsky Ariel Adam Pradipta Banerjee
  Kevin Cattell Axel Saß Matt Smith More like this Introducing OpenShift Service Mesh
  3.2 with Istio’s ambient mode From if to how: A year of post-quantum reality Data
  Security 101 | Compiler AI Is Changing The Threat Landscape | Compiler Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share Confidential computing
  represents the next frontier in hybrid and multicloud security, offering hardware-level
  memory protection (data in use) through technologies such as AMD SEV and Intel TDX.
  However, implementing storage solutions in these environments presents unique challenges
  that traditional approaches can''t address. In this article, we''ll explore different
  approaches to adding storage to Red Hat OpenShift confidential container environments,
  what to watch out for, and how AltaStata —a Red Hat partner —simplifies the process
  with encryption and protection for AI. Confidential containers (CoCo) protect the
  workload’s data in use, but some workloads also require storage for persistence.
  When adding storage to confidential containers, we need to address a number of security
  challenges on top of data in use, which confidential computing protects against:
  Data at rest : Files stored in cloud-encrypted storage remain accessible to anyone
  with bucket access Data in transit : Network communications need end-to-end encryption
  Compliance : GDPR, HIPAA, SOC 2, NIST RMF, AI Act, and CCPA require audit trails
  and version control Multicloud : Organizations need to maintain consistent security
  across diverse cloud environments and hybrid data centers Confidential containers
  are emerging as a tool to protect AI models, weights, and data, especially when
  performing inferencing. For additional information on confidential containers for
  AI use cases, we recommend reading this article about the power of confidential
  containers on Red Hat OpenShift with NVIDIA GPUs.'
---
Open the original post ↗ https://www.redhat.com/en/blog/end-end-security-ai-integrating-altastata-storage-red-hat-openshift-confidential-containers
