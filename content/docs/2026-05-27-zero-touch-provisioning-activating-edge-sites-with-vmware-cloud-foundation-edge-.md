---
title: 'Zero Touch Provisioning: Activating Edge Sites with VMware Cloud Foundation
  Edge 9.1'
date: '2026-05-27T08:35:28+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/05/27/zero-touch-provisioning-activating-edge-sites-with-vmware-cloud-foundation-edge-9-1/
post_kind: link
draft: false
tldr: What Is Zero Touch Provisioning? Bringing up a new VMware Cloud Foundation (VCF)
  Edge site traditionally required manual, onsite configuration, a process that does
  not scale across dozens or hundreds of remote locations. With VCF Edge 9.1, Broadcom
  delivers Zero Touch Provisioning (ZTP) or vSphere Elastic Provisioning, a capability
  that automates bare-metal host boot, ESX installation, and cluster registration
  over the network, eliminating the need for local expertise at the edge.
summary: 'What Is Zero Touch Provisioning? Bringing up a new VMware Cloud Foundation
  (VCF) Edge site traditionally required manual, onsite configuration, a process that
  does not scale across dozens or hundreds of remote locations. With VCF Edge 9.1,
  Broadcom delivers Zero Touch Provisioning (ZTP) or vSphere Elastic Provisioning,
  a capability that automates bare-metal host boot, ESX installation, and cluster
  registration over the network, eliminating the need for local expertise at the edge.
  This blog walks through the complete workflow: creating a ZTP-enabled cluster in
  vCenter, configuring Auto Deploy and Deploy Rules, booting an edge host via UEFI
  HTTPS, and then using the open-source VcfEdgeAtScale PowerShell module to configure
  the fully-registered host into a production-ready edge site cluster, all without
  anyone touching a keyboard at the remote site. Zero Touch Provisioning is the capability
  within VMware Cloud Foundation that orchestrates fully unattended ESX host deployment
  at remote sites. A bare-metal server arrives at the edge site directly from the
  OEM vendor. Once connected to the network and powered on, the host broadcasts a
  DHCP request. In response, a configured DHCP server at the primary data center responds
  with the address of a UEFI HTTPS Boot URL, served by the vCenter Auto Deploy service.
  The host downloads the ESX installer image over HTTPS, auto-provisions, and then
  registers itself with vCenter, placing itself into the designated cluster as specified
  by the matching Deploy Rule. The result is a host that goes from bare metal to a
  fully registered vCenter cluster member with zero on-site human interaction. Paired
  with the VcfEdgeAtScale PowerShell module , subsequent configuration of the vSphere
  Supervisor, networking, storage, and Supervisor Services (Harbor and Argo CD) is
  equally automated. The following components must be in place before starting the
  ZTP workflow: The first action is to create a cluster that will serve as the landing
  zone for ZTP-provisioned edge hosts. In vCenter, right-click the target datacenter
  and select New Cluster.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/05/27/zero-touch-provisioning-activating-edge-sites-with-vmware-cloud-foundation-edge-9-1/
