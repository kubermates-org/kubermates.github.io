---
title: Resizing VMware vCenter in VMware Cloud Foundation 9
date: '2026-05-12T12:41:46+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/05/12/resizing-vmware-vcenter/
post_kind: link
draft: false
tldr: Resize vCenter VCF 9.1 using API Resize vCenter 9.0 and earlier using reduced
  downtime upgrade Resize vCenter 9.0 and earlier using File-Based Backup Restore
  Discover more from VMware Cloud Foundation (VCF) Blog Related Articles What’s New
  with vSphere in VMware Cloud Foundation 9.1? Resizing VMware vCenter in VMware Cloud
  Foundation 9 Non-Disruptive VMware vCenter Patching in VMware Cloud Foundation 9.1
  When you deploy the VMware vCenter appliance, you select an appliance that is suitable
  for the size of your environment. The option that you select determines the number
  of CPUs, the amount of memory, and the size of the disks for the appliance.
summary: 'Resize vCenter VCF 9.1 using API Resize vCenter 9.0 and earlier using reduced
  downtime upgrade Resize vCenter 9.0 and earlier using File-Based Backup Restore
  Discover more from VMware Cloud Foundation (VCF) Blog Related Articles What’s New
  with vSphere in VMware Cloud Foundation 9.1? Resizing VMware vCenter in VMware Cloud
  Foundation 9 Non-Disruptive VMware vCenter Patching in VMware Cloud Foundation 9.1
  When you deploy the VMware vCenter appliance, you select an appliance that is suitable
  for the size of your environment. The option that you select determines the number
  of CPUs, the amount of memory, and the size of the disks for the appliance. We refer
  to these sizes as “t-shirt sizes” and they consist of tiny, small, medium, large,
  and extra-large. Disk size can use sizes default, large and extra-large. For more
  information on vCenter sizing, see the documentation System Requirements for the
  vCenter Appliance. Resizing CPU and memory is straightforward. Simply shut down
  the vCenter VM and increase the CPU and memory as desired and power it back on.
  Resizing the disks is a little more involved and you can learn more about that process
  in the Knowledge Base article Increasing the disk space for the vCenter Server Appliance.
  In this blog we explore options to automatically resize vCenter, including a new
  API introduced in VMware Cloud Foundation (VCF) 9.1. Using the new API is the preferred
  method once you are running vCenter version 9.1. Important: Resizing vCenter is
  a one-way process and is for sizing up only. Be sure to take appropriate backups
  before performing any resize operation.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/05/12/resizing-vmware-vcenter/
