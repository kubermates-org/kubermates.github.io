---
title: Expand Shared VMDKs with Clustered Applications in VMware vSAN for VCF 9.1
date: '2026-05-15T12:00:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/05/15/expand-shared-vmdks-in-vmware-vsan-for-vcf-9-1/
post_kind: link
draft: false
tldr: 'Solving the Disk Expansion Maintenance Window Improved Deployment Flexibility
  Summary Discover more from VMware Cloud Foundation (VCF) Blog Related Articles Encrypted
  vMotion Offload to Intel QAT in VMware Cloud Foundation 9.1 Increase Deployment
  Flexibility with VCF Edge Automation 1.0.3 More Memory, Less Effort: Configuring
  Memory Tiering in VCF 9.1 While VMware vSphere and vSAN provide a common and consistent
  way of delivering high availability of your applications and data through virtualization,
  it is not uncommon to see customers using application-level clustering capabilities
  in a virtualized environment. In vSAN for VMware Cloud Foundation (VCF) 9.1, we’ve
  made the management of these clustered applications much easier.'
summary: 'Solving the Disk Expansion Maintenance Window Improved Deployment Flexibility
  Summary Discover more from VMware Cloud Foundation (VCF) Blog Related Articles Encrypted
  vMotion Offload to Intel QAT in VMware Cloud Foundation 9.1 Increase Deployment
  Flexibility with VCF Edge Automation 1.0.3 More Memory, Less Effort: Configuring
  Memory Tiering in VCF 9.1 While VMware vSphere and vSAN provide a common and consistent
  way of delivering high availability of your applications and data through virtualization,
  it is not uncommon to see customers using application-level clustering capabilities
  in a virtualized environment. In vSAN for VMware Cloud Foundation (VCF) 9.1, we’ve
  made the management of these clustered applications much easier. Let’s look at how
  provisioning and capacity management for clustered applications like Oracle RAC
  and Microsoft Windows Server Failover Clusters (WSFC) are integrated into the latest
  version of VCF. Applications that deliver high levels of availability using their
  own techniques typically consist of two or more application instances running in
  their own respective VMs, and one additional location to help determine quorum under
  various potential failure conditions. This additional location is typically a shared
  virtual disk or VMDK which requires each application to be able to read and write
  to that shared VMDK. For more information, see the post: “ Application Versus Infrastructure-Level
  High Availability with vSAN in VMware Cloud Foundation. ” VMDKs that have been configured
  to be accessed concurrently are intended only for these types of clustered applications
  that must be able to write data to the same block volume at the same time. The sharing
  of a VMDK can be achieved in one of two ways: Multiwriter flag. This setting will
  toggle off vSphere’s locking mechanism that assures a VMDK can be accessed by one
  VM/App instance. This is used with the assumption that a clustered application has
  its own logic in place (e. g. locking mechanisms, write ordering, etc.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/05/15/expand-shared-vmdks-in-vmware-vsan-for-vcf-9-1/
