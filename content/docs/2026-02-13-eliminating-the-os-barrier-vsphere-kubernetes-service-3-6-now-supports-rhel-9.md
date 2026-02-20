---
title: 'Eliminating the OS Barrier: vSphere Kubernetes Service 3.6 Now Supports RHEL
  9'
date: '2026-02-13T19:00:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/02/13/vsphere-kubernetes-service-3-6-rhel-support/
post_kind: link
draft: false
tldr: 'The “UBI Tax” and Why the OS Matters How It Works: The Image Baker Workflow
  Step 1: Define the Image Spec Step 2: Set Credentials and Bake Deploying RHEL Clusters:
  Zero Friction Advanced Flexibility: Mixed Clusters and Upgrades Meeting You Where
  You Are Discover more from VMware Cloud Foundation (VCF) Blog Related Articles VMware
  vSphere Kubernetes Service 3.6: Making Enterprise Kubernetes Safer, More Flexible,
  and Easier to Operate Case Study: Navigating VKS Upgrades – Balancing Infrastructure
  Constraints and Application Reality Platform Engineering Needs a Cloud Engine For
  many enterprise platform teams, adoption isn’t blocked by Kubernetes features—it’s
  blocked by the operating system (OS). You might want the automated lifecycle management
  of vSphere Kubernetes Service (VKS), but you cannot abandon the Red Hat Enterprise
  Linux (RHEL) standards that underpin your security compliance, licensing models,
  and operational toolchains.'
summary: 'The “UBI Tax” and Why the OS Matters How It Works: The Image Baker Workflow
  Step 1: Define the Image Spec Step 2: Set Credentials and Bake Deploying RHEL Clusters:
  Zero Friction Advanced Flexibility: Mixed Clusters and Upgrades Meeting You Where
  You Are Discover more from VMware Cloud Foundation (VCF) Blog Related Articles VMware
  vSphere Kubernetes Service 3.6: Making Enterprise Kubernetes Safer, More Flexible,
  and Easier to Operate Case Study: Navigating VKS Upgrades – Balancing Infrastructure
  Constraints and Application Reality Platform Engineering Needs a Cloud Engine For
  many enterprise platform teams, adoption isn’t blocked by Kubernetes features—it’s
  blocked by the operating system (OS). You might want the automated lifecycle management
  of vSphere Kubernetes Service (VKS), but you cannot abandon the Red Hat Enterprise
  Linux (RHEL) standards that underpin your security compliance, licensing models,
  and operational toolchains. Historically, this forced a difficult choice: adopt
  a managed platform and rebuild your entire operational stack on a new OS (like Ubuntu
  or Photon), or stay on legacy infrastructure just to keep your OS. With the release
  of VKS 3.6 , we are removing that friction. We are excited to announce Build Your
  Own Image (BYOI) support for RHEL 9. This isn’t just about adding another option
  to the menu; it’s about acknowledging that the best platform is one that fits seamlessly
  into your existing environment, without forcing you to rebuild your foundation.
  Why is the underlying node OS such a dealbreaker? For many, it comes down to support
  and licensing efficiency. When organizations build their application stack on Red
  Hat Universal Base Images (UBI) and these UBI containers run on a RHEL host, they
  automatically inherit the host’s support status. This provides end-to-end support
  from Red Hat for the entire stack. VKS 3.6 allows you to keep this end-to-end support
  from Red Hat by bringing RHEL 9 nodes directly into the VKS lifecycle management,
  preserving your support chain and compliance posture without sacrificing modern
  platform automation. We didn’t just want to support RHEL; we wanted to give you
  control over how it’s built. VKS 3.6 introduces the Image Baker tool through the
  VCF CLI.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/02/13/vsphere-kubernetes-service-3-6-rhel-support/
