---
title: Non-Disruptive VMware vCenter Patching in VMware Cloud Foundation 9.1
date: '2026-05-12T12:18:45+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/05/12/vcenter-quick-patch/
post_kind: link
draft: false
tldr: Summary Discover more from VMware Cloud Foundation (VCF) Blog Related Articles
  What’s New with vSphere in VMware Cloud Foundation 9.1? Resizing VMware vCenter
  in VMware Cloud Foundation 9 Non-Disruptive VMware vCenter Patching in VMware Cloud
  Foundation 9.1 VMware vCenter is a critical component of the VMware Cloud Foundation
  (VCF) stack, helping administrators juggle service uptime with important maintenance
  and patching cycles. Traditional in-place vCenter patches can result in downtime
  of up to an hour or more.
summary: 'Summary Discover more from VMware Cloud Foundation (VCF) Blog Related Articles
  What’s New with vSphere in VMware Cloud Foundation 9.1? Resizing VMware vCenter
  in VMware Cloud Foundation 9 Non-Disruptive VMware vCenter Patching in VMware Cloud
  Foundation 9.1 VMware vCenter is a critical component of the VMware Cloud Foundation
  (VCF) stack, helping administrators juggle service uptime with important maintenance
  and patching cycles. Traditional in-place vCenter patches can result in downtime
  of up to an hour or more. VMware Cloud Foundation 9.1 introduces vCenter quick patch,
  taking vCenter patching to the next level. vCenter quick patch allows for rapid
  patching of vCenter with minimal, sometimes zero, downtime. The level of downtime
  depends on the service(s) being patched. vCenter quick patch targets rapid deployment
  of important security fixes for vCenter. Important: Similar to ESX live patch, not
  every vCenter patch is quick-patch compatible; it depends on the patch payload.
  vCenter release notes and the patch details in-product will highlight if a patch
  is quick-patch compatible. The scope for vCenter quick patch is security patches.
  Traditional in-place patching updates every RPM on the vCenter, regardless if that
  service or component has had a code change. vCenter quick patch changes only those
  specific RPMs or binaries that have a code change in the patch payload. This method
  dramatically reduces the overall maintenance window and reduces the vCenter downtime
  to under 1 minute and, in some cases, reduces the downtime to zero.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/05/12/vcenter-quick-patch/
