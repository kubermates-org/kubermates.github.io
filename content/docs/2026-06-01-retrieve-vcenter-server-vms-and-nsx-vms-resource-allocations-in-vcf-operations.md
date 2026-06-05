---
title: Retrieve vCenter Server VMs and NSX VMs resource allocations in VCF Operations
date: '2026-06-01T22:29:55+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/06/01/retrieve-vcenter-server-vms-and-nsx-vms-resource-allocations-in-vcf-operations/
post_kind: link
draft: false
tldr: 'Overview Get allocated system resources for vCenter Server VMs Get allocated
  system resources for NSX Manager VMs Credits Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles Retrieve vCenter Server VMs and NSX VMs resource allocations
  in VCF Operations Diagnostics for VMware Cloud Foundation (VCF) 9.1 with Old Versions
  of VCF Components VCF 9.1 Licensing: Programmatic, Centralized, and Built to Scale
  In VMware Cloud Foundation (VCF) environments, vCenter Server and NSX management
  components are deployed as virtual machines. Administrators often require a streamlined
  method to monitor the resource allocations—specifically CPU, memory, and storage
  capacity—of these underlying vCenter Server and NSX management VMs in their entire
  infrastructure.'
summary: 'Overview Get allocated system resources for vCenter Server VMs Get allocated
  system resources for NSX Manager VMs Credits Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles Retrieve vCenter Server VMs and NSX VMs resource allocations
  in VCF Operations Diagnostics for VMware Cloud Foundation (VCF) 9.1 with Old Versions
  of VCF Components VCF 9.1 Licensing: Programmatic, Centralized, and Built to Scale
  In VMware Cloud Foundation (VCF) environments, vCenter Server and NSX management
  components are deployed as virtual machines. Administrators often require a streamlined
  method to monitor the resource allocations—specifically CPU, memory, and storage
  capacity—of these underlying vCenter Server and NSX management VMs in their entire
  infrastructure. Within VCF Operations, these configuration details can be efficiently
  extracted by utilizing the VMware Infrastructure Health (VIH) Adapter objects. To
  get allocated system resources for VMs underpinning vCenter Server application for
  your entire infrastructure, follow these steps: Login to the VCF operations user
  interface with an admin account or with an account that has sufficient privileges
  to create a view Create a new List view In the “Name and Configuration” section,
  name the list view as “vCenter Server VM – System Resources”. Retain the other default
  configurations in this section. In the “data” settings, add the subject “vCenter
  -> Virtual Machine” and Group by “VMware Infrastructure Health -> vCenter App”.
  In the “data” settings, add the following properties: The following screenshot shows
  the “data” settings of the view: In the “data” settings, select the preview as “vSphere
  World”. Retain the default configurations for the Time, Filter, and Summary settings.
  Click “Create” to create the new view. Go to the view results page, ensuring “vSphere
  World” is set as the preview source. Once the data has loaded, select “Export as
  csv” from the toolbar. Open the exported file and remove all entries starting from
  the “No Group” row through to the end.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/06/01/retrieve-vcenter-server-vms-and-nsx-vms-resource-allocations-in-vcf-operations/
