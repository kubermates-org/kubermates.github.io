---
title: Red Hat OpenShift sandboxed containers 1.12 and Red Hat build of Trustee 1.1
  bring confidential computing to bare metal and AI workloads
date: '2026-04-13T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/red-hat-openshift-sandboxed-containers-112-and-red-hat-build-trustee-11-bring-confidential-computing-bare-metal-and-ai-workloads
post_kind: link
draft: false
tldr: 'Red Hat OpenShift sandboxed containers 1.12 and Red Hat build of Trustee 1.1
  bring confidential computing to bare metal and AI workloads OpenShift sandboxed
  containers 1.12: Enterprise-grade confidential computing everywhere Confidential
  containers on bare metal: Now generally available Confidential containers for AI
  workloads with confidential GPU accelerators: Technology Preview How it works Red
  Hat build of Trustee 1.1: Extending attestation across environments Real-world impact:
  Protecting the workloads that matter most See it in action: Protecting your model
  IP end-to-end Get started with confidential containers on Red Hat OpenShift today
  Red Hat OpenShift Container Platform | Product Trial About the authors Marcos Entenza
  Ariel Adam Jens Freimann Renjish Kumar More like this AI optimization: 7 powerful
  techniques you can use today! 233% 3-year return on investment and 13 months to
  payback with Red Hat AI Technically Speaking | Build a production-ready AI toolbox
  Technically Speaking | Platform engineering for AI agents Keep exploring Browse
  by channel Automation Artificial intelligence Open hybrid cloud Security Edge computing
  Infrastructure Applications Virtualization Share Red Hat is excited to announce
  the release of Red Hat OpenShift sandboxed containers 1.12 and Red Hat build of
  Trustee 1.1, marking a major leap forward in our confidential computing journey.
  These releases graduate confidential containers on bare metal from Technology Preview
  to General Availability (GA), delivering production-ready, hardware-based memory
  encryption and attestation for on-premise and hybrid cloud infrastructure, We are
  also introducing Technology Preview support for confidential containers with NVIDIA
  Confidential Computing , paving the way for digital sovereignty, hardened environments
  for AI, and machine learning workloads at scale.'
summary: 'Red Hat OpenShift sandboxed containers 1.12 and Red Hat build of Trustee
  1.1 bring confidential computing to bare metal and AI workloads OpenShift sandboxed
  containers 1.12: Enterprise-grade confidential computing everywhere Confidential
  containers on bare metal: Now generally available Confidential containers for AI
  workloads with confidential GPU accelerators: Technology Preview How it works Red
  Hat build of Trustee 1.1: Extending attestation across environments Real-world impact:
  Protecting the workloads that matter most See it in action: Protecting your model
  IP end-to-end Get started with confidential containers on Red Hat OpenShift today
  Red Hat OpenShift Container Platform | Product Trial About the authors Marcos Entenza
  Ariel Adam Jens Freimann Renjish Kumar More like this AI optimization: 7 powerful
  techniques you can use today! 233% 3-year return on investment and 13 months to
  payback with Red Hat AI Technically Speaking | Build a production-ready AI toolbox
  Technically Speaking | Platform engineering for AI agents Keep exploring Browse
  by channel Automation Artificial intelligence Open hybrid cloud Security Edge computing
  Infrastructure Applications Virtualization Share Red Hat is excited to announce
  the release of Red Hat OpenShift sandboxed containers 1.12 and Red Hat build of
  Trustee 1.1, marking a major leap forward in our confidential computing journey.
  These releases graduate confidential containers on bare metal from Technology Preview
  to General Availability (GA), delivering production-ready, hardware-based memory
  encryption and attestation for on-premise and hybrid cloud infrastructure, We are
  also introducing Technology Preview support for confidential containers with NVIDIA
  Confidential Computing , paving the way for digital sovereignty, hardened environments
  for AI, and machine learning workloads at scale. Together, these milestones provide
  organizations with a holistic approach for protecting their most sensitive workloads
  on any deployment. This was already possible in the cloud, and is now also available
  for on-premise hardware with a confidential computing platform built on Red Hat
  OpenShift, providing the level of consistency and support that enterprises expect.
  OpenShift sandboxed containers 1.12 builds on the strong foundation established
  in previous releases, extending confidential computing capabilities to bare-metal
  environments and confidential GPU-accelerated workloads. It further hardens the
  platform''s security posture and usability across cloud and on-premises deployments.
  Feature highlights include: Persistent volume support with encrypted block storage
  for confidential workloads Sealed secrets for protected provisioning of sensitive
  data to confidential workloads Automated hardware node discovery and RuntimeClass
  management for NVIDIA accelerated computing and confidential GPU workloads Assisted
  installer enhancements for simplified confidential container deployment One of the
  capabilities that our customers and partners have requested most often is the ability
  to run confidential containers directly on their own physical infrastructure. With
  OpenShift sandboxed containers 1.12, confidential containers on bare metal graduates
  from Technology Preview to General Availability, providing full production support
  with enterprise-grade reliability and Red Hat service-level agreement (SLA) commitments.
  This GA release supports the following trusted execution environment (TEE) hardware:
  Intel Trust Domain Extensions (TDX) : On compatible Intel bare-metal hardware AMD
  Secure Nested Paging (SEV-SNP) : On compatible AMD hardware IBM Secure Execution
  for Linux (SEL) : Telum processor support for IBM LinuxONE environments The GA release
  delivers the automation, stability, and supportability that production environments
  demand. The OpenShift sandboxed containers operator now automatically handles the
  full lifecycle of the confidential computing stack on bare-metal nodes: Detecting
  TEE hardware : The operator automatically detects and labels nodes for AMD SEV-SNP,
  Intel TDX, and IBM SEL, eliminating the need for manual hardware discovery. Creating
  runtimes : It dynamically provisions the kata-cc RuntimeClass, making confidential
  workloads immediately schedulable on TEE-capable nodes. Configuring the host : It
  manages CRI-O configuration via MachineConfigs to activate the runtime class, ensuring
  consistent and reproducible cluster configuration.'
---
Open the original post ↗ https://www.redhat.com/en/blog/red-hat-openshift-sandboxed-containers-112-and-red-hat-build-trustee-11-bring-confidential-computing-bare-metal-and-ai-workloads
