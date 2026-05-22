---
title: VMware vSAN Protection and Recovery Enhancements for VCF 9.1
date: '2026-05-14T12:00:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/05/14/vmware-vsan-protection-and-recovery-enhancements-for-vcf-9-1/
post_kind: link
draft: false
tldr: 'Multi-Source Replication On-Premises Cyber Recovery: Your Private Clean Room
  Scaling Operations: Retention, Tags, and Seeding Hierarchical Snapshot Retention
  Protection Group Memberships using vSphere Tags Manual Replica Seeding Summary Discover
  more from VMware Cloud Foundation (VCF) Blog Related Articles Encrypted vMotion
  Offload to Intel QAT in VMware Cloud Foundation 9.1 Increase Deployment Flexibility
  with VCF Edge Automation 1.0.3 More Memory, Less Effort: Configuring Memory Tiering
  in VCF 9.1 With the release of VMware Cloud Foundation (VCF) 9.1, we are introducing
  significant enhancements to vSAN Protection and Recovery (formerly known as vSAN
  Data Protection). These updates focus on three core areas of the solution: architectural
  flexibility, sovereign cyber resilience, and operational scale.'
summary: 'Multi-Source Replication On-Premises Cyber Recovery: Your Private Clean
  Room Scaling Operations: Retention, Tags, and Seeding Hierarchical Snapshot Retention
  Protection Group Memberships using vSphere Tags Manual Replica Seeding Summary Discover
  more from VMware Cloud Foundation (VCF) Blog Related Articles Encrypted vMotion
  Offload to Intel QAT in VMware Cloud Foundation 9.1 Increase Deployment Flexibility
  with VCF Edge Automation 1.0.3 More Memory, Less Effort: Configuring Memory Tiering
  in VCF 9.1 With the release of VMware Cloud Foundation (VCF) 9.1, we are introducing
  significant enhancements to vSAN Protection and Recovery (formerly known as vSAN
  Data Protection). These updates focus on three core areas of the solution: architectural
  flexibility, sovereign cyber resilience, and operational scale. In VCF 9.0, we introduced
  vSAN-to-vSAN replication. It was the first logical step in providing remote protection
  for workloads running on vSAN. While powerful, many of our customers operate heterogeneous
  environments where data resides on a mix of storage platforms. VCF 9.1 breaks these
  silos by introducing multi-source replication capabilities. What does this mean?
  You can now protect VMs from multiple types of storage, including vSAN, VMFS and
  NFS datastores to a vSAN ESA cluster as the target. Not only does it provide the
  ability to have multiple sources, but it also allows for a “fan-in” architecture
  that gives you the ability to protect multiple source clusters to a single, centralized
  recovery site. Figure 1. Multi-source replication to a shared recovery site in vSAN
  Protection and Recovery. In this type of topology, both the source site and the
  shared recovery site must have their own respective vCenter Server, as well as a
  Protection and Recovery appliance. The relationship between the two sites is established
  by site pairing.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/05/14/vmware-vsan-protection-and-recovery-enhancements-for-vcf-9-1/
