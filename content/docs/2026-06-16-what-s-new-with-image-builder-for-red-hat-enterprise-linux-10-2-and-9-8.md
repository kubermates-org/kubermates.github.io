---
title: What's new with image builder for Red Hat Enterprise Linux 10.2 and 9.8
date: '2026-06-16T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/whats-new-image-builder-red-hat-enterprise-linux-102-and-98
post_kind: link
draft: false
tldr: What's new with image builder for Red Hat Enterprise Linux 10.2 and 9.8 What's
  new for the image builder command-line interface in RHEL 10.2 and 9.8? Build bootable
  image mode for RHEL images Build stateless or diskless (PXE) images Build network
  installer (boot ISO) images What's new for the image builder web console interface
  in RHEL 10.2? Build bootable image mode for RHEL images Build and launch a virtual
  machine Build security-hardened images Try Red Hat image builder today Red Hat Enterprise
  Linux | Product trial About the author Shane McDowell More like this Red Hat has
  updated the RISC-V Developer Preview Expiration of Secure Boot signing certificates
  in 2026 Infrastructure At The Edge | Compiler Operating System Management | Compiler
  Keep exploring Browse by channel Automation Artificial intelligence Open hybrid
  cloud Security Edge computing Infrastructure Applications Virtualization Share Image
  builder for Red Hat Enterprise Linux (RHEL) is a powerful tool for creating custom
  RHEL images with pre-installed software and configurations. It helps organizations
  standardize deployments, bring consistency, and reduce manual effort, generating
  ready-to-deploy images for virtual machines (VM), cloud, and bare metal.
summary: What's new with image builder for Red Hat Enterprise Linux 10.2 and 9.8 What's
  new for the image builder command-line interface in RHEL 10.2 and 9.8? Build bootable
  image mode for RHEL images Build stateless or diskless (PXE) images Build network
  installer (boot ISO) images What's new for the image builder web console interface
  in RHEL 10.2? Build bootable image mode for RHEL images Build and launch a virtual
  machine Build security-hardened images Try Red Hat image builder today Red Hat Enterprise
  Linux | Product trial About the author Shane McDowell More like this Red Hat has
  updated the RISC-V Developer Preview Expiration of Secure Boot signing certificates
  in 2026 Infrastructure At The Edge | Compiler Operating System Management | Compiler
  Keep exploring Browse by channel Automation Artificial intelligence Open hybrid
  cloud Security Edge computing Infrastructure Applications Virtualization Share Image
  builder for Red Hat Enterprise Linux (RHEL) is a powerful tool for creating custom
  RHEL images with pre-installed software and configurations. It helps organizations
  standardize deployments, bring consistency, and reduce manual effort, generating
  ready-to-deploy images for virtual machines (VM), cloud, and bare metal. Image builder
  for RHEL can be used as a hosted service on the Red Hat Hybrid Cloud Console or
  as an on-premise service from the RHEL command-line interface and the RHEL web console.
  The image-builder command is available as an RPM in the AppStream repository and
  as a container image in the Red Hat container registry. A similar containerized
  tool called bootc-image-builder is deprecated. image-builder To deploy an image
  mode for RHEL system, you create a bootable image from a container image. Previously,
  this was only possible by using bootc-image-builder as a standalone container or
  as an extension for Podman Desktop. With RHEL 10.2 and 9.8, you can build a bootable
  image mode for RHEL image using the image-builder command. image-builder For example,
  to create a bootable virtualization image (. qcow2 ) from the base image mode for
  RHEL container image, authenticate to registry. redhat. io and then run this command:.
---
Open the original post ↗ https://www.redhat.com/en/blog/whats-new-image-builder-red-hat-enterprise-linux-102-and-98
