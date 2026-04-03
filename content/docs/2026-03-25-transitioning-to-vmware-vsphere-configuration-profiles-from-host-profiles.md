---
title: Transitioning to VMware vSphere Configuration Profiles from Host Profiles
date: '2026-03-25T12:53:53+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/03/25/transitioning-to-vmware-vsphere-configuration-profiles/
post_kind: link
draft: false
tldr: 'About vSphere Configuration Profiles Transitioning from Host Profiles Manage
  Configuration at Cluster Level Create Configuration Pre-check and Apply Summary
  Discover more from VMware Cloud Foundation (VCF) Blog Related Articles Applying
  GitOps Principles to Maintain Desired State Configuration using VMware vSphere Configuration
  Profile - Part 3 Transitioning to VMware vSphere Configuration Profiles from Host
  Profiles Unlocking VMware Cloud Foundation Enterprise Value: Cloud Field Day 25
  vSphere Configuration Profiles, first introduced in VMware vSphere 8.0, allows VMware
  Cloud Foundation administrators to manage the ESX host configuration at a cluster
  level. In this article, we will discuss how this feature compares to Host Profiles,
  and how to transition from Host Profiles to vSphere Configuration Profiles in vSphere
  9.'
summary: 'About vSphere Configuration Profiles Transitioning from Host Profiles Manage
  Configuration at Cluster Level Create Configuration Pre-check and Apply Summary
  Discover more from VMware Cloud Foundation (VCF) Blog Related Articles Applying
  GitOps Principles to Maintain Desired State Configuration using VMware vSphere Configuration
  Profile - Part 3 Transitioning to VMware vSphere Configuration Profiles from Host
  Profiles Unlocking VMware Cloud Foundation Enterprise Value: Cloud Field Day 25
  vSphere Configuration Profiles, first introduced in VMware vSphere 8.0, allows VMware
  Cloud Foundation administrators to manage the ESX host configuration at a cluster
  level. In this article, we will discuss how this feature compares to Host Profiles,
  and how to transition from Host Profiles to vSphere Configuration Profiles in vSphere
  9. Note: Screenshots and steps described are based on vSphere 9.0.2. Certain UI
  elements or verbiage may differ in earlier or later versions. vSphere Configuration
  Profiles is a new feature, first introduced in vSphere 8.0, that is a successor
  to Host Profiles, in its ability to manage ESX host configurations at scale. Host
  Profiles is made unwieldy by its requirement that the host configuration needs to
  be specified in its entirety. This places an undue burden on administrators, who
  may only be aware of the changes that they want to make to the configuration. vSphere
  Configuration Profiles, in contrast, only requires the admin to define the changes
  to the default configuration. This also makes the configuration document human-readable
  and much more manageable. Administrators currently managing ESX host configurations
  using Host Profiles on a cluster whose lifecycle is managed by vSphere Lifecycle
  Manager images, can transition their clusters to use vSphere Configuration Profiles.
  Note: Using vSphere Configuration Profiles with baseline managed clusters are supported
  in vSphere 8 U3. However, baseline managed clusters are no longer supported in vSphere
  9 and Host Profiles are deprecated, but still supported, in vSphere 9.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/03/25/transitioning-to-vmware-vsphere-configuration-profiles/
