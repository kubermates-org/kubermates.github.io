---
title: Replicating VMware vSphere Configuration Profile Desired State
date: '2026-04-29T18:03:11+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/04/29/replicating-vsphere-configuration-profile-desired-state/
post_kind: link
draft: false
tldr: About vSphere Configuration Profiles Replicating configuration to new clusters
  Export configuration from an existing cluster Edit vSphere Configuration Profile
  JSON file Import the updated configuration to the new cluster Summary Discover more
  from VMware Cloud Foundation (VCF) Blog Related Articles Replicating VMware vSphere
  Configuration Profile Desired State VMware Advanced Memory Tiering Tips for Success
  Applying GitOps Principles to Maintain Desired State Configuration using VMware
  vSphere Configuration Profile - Part 3 vSphere Configuration Profiles allows VMware
  Cloud Foundation (VCF) administrators to manage the ESX host configuration at a
  cluster level. In this article, we discuss how to easily replicate configuration
  from one cluster to another cluster.
summary: 'About vSphere Configuration Profiles Replicating configuration to new clusters
  Export configuration from an existing cluster Edit vSphere Configuration Profile
  JSON file Import the updated configuration to the new cluster Summary Discover more
  from VMware Cloud Foundation (VCF) Blog Related Articles Replicating VMware vSphere
  Configuration Profile Desired State VMware Advanced Memory Tiering Tips for Success
  Applying GitOps Principles to Maintain Desired State Configuration using VMware
  vSphere Configuration Profile - Part 3 vSphere Configuration Profiles allows VMware
  Cloud Foundation (VCF) administrators to manage the ESX host configuration at a
  cluster level. In this article, we discuss how to easily replicate configuration
  from one cluster to another cluster. Note: Screenshots and steps described are based
  on vSphere 9.0.2. Certain UI elements or verbiage may differ in earlier or later
  versions. vSphere Configuration Profiles is a new feature, first introduced in vSphere
  8.0, that is a successor to Host Profiles in its ability to manage ESX host configurations
  at scale. Host Profiles is made unwieldy by its requirement that the host configuration
  needs to be specified in its entirety. This places an undue burden on administrators,
  who may only be aware of the changes that they want to make to the configuration.
  vSphere Configuration Profiles, in contrast, only requires the admin to define the
  changes to the default configuration. This also makes the configuration document
  human-readable and much more manageable. A common use case when it comes to configuration
  management is that, in addition to maintaining consistent configuration within a
  vSphere cluster, we also may wish to maintain consistent configuration across multiple
  clusters. vSphere Configuration Profiles makes this very easy to do. If you have
  not yet transitioned a cluster to use vSphere Configuration Profiles, see the blog
  article Transitioning to VMware vSphere Configuration Profiles from Host Profiles.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/04/29/replicating-vsphere-configuration-profile-desired-state/
