---
title: Deploying Harbor Service in Air-Gapped VMware Cloud Foundation 9.0
date: '2026-04-21T10:45:33+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/04/21/deploying-harbor-service-in-air-gapped-vmware-cloud-foundation-9-0/
post_kind: link
draft: false
tldr: 'Understanding Air-Gapped Deployment Challenges Deployment Process Prerequisites
  Step 1: Bitnami Harbor OVA Deployment Step 2: Image Pre-Staging Step 3: Install
  Harbor Supervisor Service Conclusion Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles Harbor: Your Enterprise-Ready Container Registry for
  a Modern Private Cloud Reducing Harbor Deployment Complexity on Kubernetes Using
  Harbor as an AI Model Registry Modern private cloud infrastructure demands enterprise-grade
  container registry capabilities, particularly in environments where external internet
  connectivity is restricted or prohibited. Within VMware Cloud Foundation (VCF) 9.0,
  deploying Supervisor Services in air-gapped environments presents unique technical
  challenges that require careful planning and precise execution.'
summary: 'Understanding Air-Gapped Deployment Challenges Deployment Process Prerequisites
  Step 1: Bitnami Harbor OVA Deployment Step 2: Image Pre-Staging Step 3: Install
  Harbor Supervisor Service Conclusion Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles Harbor: Your Enterprise-Ready Container Registry for
  a Modern Private Cloud Reducing Harbor Deployment Complexity on Kubernetes Using
  Harbor as an AI Model Registry Modern private cloud infrastructure demands enterprise-grade
  container registry capabilities, particularly in environments where external internet
  connectivity is restricted or prohibited. Within VMware Cloud Foundation (VCF) 9.0,
  deploying Supervisor Services in air-gapped environments presents unique technical
  challenges that require careful planning and precise execution. This guide provides
  a systematic approach to deploying and managing Harbor as a Supervisor Service in
  air-gapped VCF deployments, enabling your organization to maintain container image
  availability while adhering to strict security and compliance requirements. The
  critical challenge in air-gapped environments is the “bootstrap problem. ” Harbor
  Supervisor Service requires container images to deploy, but in an air-gapped environment,
  you have no registry from which to pull those images. This guide addresses this
  challenge by demonstrating how to establish a bootstrap registry that enables Harbor
  Supervisor Service deployment, after which Harbor Supervisor Service can become
  your production container registry. An air-gapped environment is a network security
  measure that physically or logically isolates a computer network from unsecured
  networks, including the internet. For organizations operating in regulated industries
  such as financial services, government agencies, healthcare, and defense, air-gapped
  infrastructure is not optional; it is a regulatory requirement. Hence, we provide
  you here with a solution to deploying the Harbor Supervisor Service in an air-gapped
  setup that will then become your OCI registry for the air-gapped environment. For
  air-gapped VCF environments, we require a two-phased approach. Step 1: Bitnami Harbor
  OVA Deployment Deploy the Harbor Open Virtual Appliance (OVA) from Bitnami as a
  virtual machine as the bootstrap registry for storing the Harbor Supervisor Service
  images. This approach provides: Quick deployment through a preconfigured appliance
  Traditional VM-based management Suitable for initial testing or smaller deployments
  This bootstrap registry serves a critical purpose: it hosts the Harbor Supervisor
  Service container images that will be pulled during Harbor Supervisor Service deployment.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/04/21/deploying-harbor-service-in-air-gapped-vmware-cloud-foundation-9-0/
