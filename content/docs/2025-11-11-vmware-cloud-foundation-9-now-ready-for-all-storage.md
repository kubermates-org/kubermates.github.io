---
title: 'VMware Cloud Foundation 9: Now Ready For All Storage'
date: '2025-11-11T19:12:46+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/11/11/vmware-cloud-foundation-9-now-ready-for-all-storage/
post_kind: link
draft: false
tldr: 'VCF 9 is Ready for All vSphere-supported External Storage What about iSCSI,
  NFS v4.1, and NVMe over Fabrics? Documentation of Support Statement What’s the simplest
  way to adopt, run and manage storage for VCF? Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles VMware Cloud Foundation 9: Now Ready For All Storage
  From Tickets to Clicks: Driving Real Consumption in Your Self‑Service Private Cloud
  Analyst Insight Series: Virtualization virtue #3: Supporting application modernization
  Building a private cloud on VMware Cloud Foundation™ (VCF) 9 necessitates careful
  consideration of storage options. Customers must weigh the benefits of each storage
  option based on their specific needs and existing investments to optimize their
  vSphere environments.'
summary: 'VCF 9 is Ready for All vSphere-supported External Storage What about iSCSI,
  NFS v4.1, and NVMe over Fabrics? Documentation of Support Statement What’s the simplest
  way to adopt, run and manage storage for VCF? Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles VMware Cloud Foundation 9: Now Ready For All Storage
  From Tickets to Clicks: Driving Real Consumption in Your Self‑Service Private Cloud
  Analyst Insight Series: Virtualization virtue #3: Supporting application modernization
  Building a private cloud on VMware Cloud Foundation™ (VCF) 9 necessitates careful
  consideration of storage options. Customers must weigh the benefits of each storage
  option based on their specific needs and existing investments to optimize their
  vSphere environments. Customers looking to rapidly adopt VCF 9 have asked for workflows
  to support all existing supported vSphere storage types, so in our latest version,
  Broadcom has significantly expanded storage options, now allowing the use of NFSv3
  or Fibre Channel VMFS datastores as principal storage for the management workload
  domain during greenfield deployments. This enhancement builds upon the robust, automated
  VMware vSAN deployment capabilities already in place. VMware Cloud Foundation (VCF)
  9 supports a variety of storage types as principal storage (see Storage Models in
  the product documentation for more details). Typically, principal storage is configured
  during creation of the management or workload domains or when adding new clusters
  to an existing workload domain. These scenarios are referred to as greenfield deployments.
  Additional principal storage types such as iSCSI, NFS v4.1, and NVMe over Fabrics
  (FC or TCP), which are not currently available in a greenfield deployment, can now
  be configured as principal storage for VCF 9 by converging an existing vSphere environment
  or by using VCF import. If the default cluster includes multiple datastore types,
  VCF determines the primary datastore using the following priority: vSAN NFS v3 VMFS
  NFS 4.1 iSCSI This process is documented in KB 416270​​. This is also detailed in
  the techdocs under converging an existing vSphere environment into a VCF instance.
  Specifically “Any supported vSphere storage type” is supported. For a list of supported
  vSphere 9 supported storage platforms see the Broadcom compatibility guide.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/11/11/vmware-cloud-foundation-9-now-ready-for-all-storage/
