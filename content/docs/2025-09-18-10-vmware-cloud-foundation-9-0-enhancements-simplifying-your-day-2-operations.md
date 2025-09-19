---
title: '10 VMware Cloud Foundation 9.0 Enhancements: Simplifying Your Day 2 Operations'
date: '2025-09-18T14:52:48+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/09/18/10-vmware-cloud-foundation-9-enhancements-simplifying-your-day-2-operations/
post_kind: link
draft: false
tldr: 'Enhancement 1: Network Pool Creation/Expansion/Deletion Enhancement 2: Host
  Commissioning and Decommissioning for Existing or New Workload Domains Enhancement
  3: Workload Domain Deployment Enhancement 4: Cluster Creation and Expansion Enhancement
  5: VCF Backup Configuration Enhancement 6: Network Settings Configuration (DNS/NTP)
  Enhancement 7: Certificate Authority Configuration Enhancement 8: Certificate Management
  Enhancement 9: Password Management Enhancement 10: Deploying NSX Edge Cluster The
  Evolution of VCF 9.0 Continues Related Related Articles VCF Breakroom Chats Episode
  57: Behind the Code – A Journey from Customer Pain to VCF 9.0 10 VMware Cloud Foundation
  9.0 Enhancements: Simplifying Your Day 2 Operations Deploy Distributed LLM Inference
  with GPUDirect RDMA over InfiniBand in VMware Private AI As organizations prepare
  to upgrade to VMware Cloud Foundation (VCF) 9.0, understanding Day 2 operational
  changes becomes critical for a successful transition. In previous versions such
  as VCF 5.2, many administrative tasks—such as network pool creation, host commissioning,
  and workload domain deployments—were tightly coupled with SDDC Manager and performing
  them outside of it often led to issues.'
summary: 'Enhancement 1: Network Pool Creation/Expansion/Deletion Enhancement 2: Host
  Commissioning and Decommissioning for Existing or New Workload Domains Enhancement
  3: Workload Domain Deployment Enhancement 4: Cluster Creation and Expansion Enhancement
  5: VCF Backup Configuration Enhancement 6: Network Settings Configuration (DNS/NTP)
  Enhancement 7: Certificate Authority Configuration Enhancement 8: Certificate Management
  Enhancement 9: Password Management Enhancement 10: Deploying NSX Edge Cluster The
  Evolution of VCF 9.0 Continues Related Related Articles VCF Breakroom Chats Episode
  57: Behind the Code – A Journey from Customer Pain to VCF 9.0 10 VMware Cloud Foundation
  9.0 Enhancements: Simplifying Your Day 2 Operations Deploy Distributed LLM Inference
  with GPUDirect RDMA over InfiniBand in VMware Private AI As organizations prepare
  to upgrade to VMware Cloud Foundation (VCF) 9.0, understanding Day 2 operational
  changes becomes critical for a successful transition. In previous versions such
  as VCF 5.2, many administrative tasks—such as network pool creation, host commissioning,
  and workload domain deployments—were tightly coupled with SDDC Manager and performing
  them outside of it often led to issues. VCF 9.0 introduces significant enhancements
  in Day 2 operations, offering greater flexibility by shifting many of these tasks
  to more familiar tools such as VMware vCenter and VCF Operations. This evolution
  not only streamlines workflows but also empowers administrators with more direct
  control. This post highlights 10 key operational changes that organizations should
  consider when planning and executing an upgrade to VCF 9.0. While not an exhaustive
  list, these insights are based on recurring themes in customer conversations and
  real-world upgrade experiences. In VCF 5.2, network pool creation, expansion, and
  deletion are performed in SDDC Manager. Administration -> Network Settings -> Network
  Pool In VCF 9.0, these tasks are performed through vCenter. You do not need any
  additional configuration to act on the Management Domain networks, however you must
  be using VCF SSO and vCenter Server Linking for Workload Domains. Global Inventory
  List -> Hosts -> Network Pools In VCF 5.2, host commissioning/decommissioning for
  existing or new workload domains are done in SDDC Manager. Inventory -> Hosts In
  VCF 9.0, these tasks are performed through vCenter. Global Inventory List -> Hosts
  -> Unassigned Hosts In VCF 5.2, Workload Domain deployment is done in SDDC Manager.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/09/18/10-vmware-cloud-foundation-9-enhancements-simplifying-your-day-2-operations/
