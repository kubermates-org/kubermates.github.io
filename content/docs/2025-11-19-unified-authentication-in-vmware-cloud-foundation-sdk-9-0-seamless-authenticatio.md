---
title: 'Unified Authentication in VMware Cloud Foundation SDK 9.0: Seamless authentication
  across vSphere and vSAN APIs'
date: '2025-11-19T09:54:31+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/11/19/unified-authentication-in-vmware-cloud-foundation-sdk-9-0-seamless-authentication-across-vsphere-and-vsan-apis/
post_kind: link
draft: false
tldr: 'Authentication dilemma with vSphere APIs The unified authentication Sample
  Code What is happening behind the scenes? Resources Discover more from VMware Cloud
  Foundation (VCF) Blog Related Articles Upgrading VMware Cloud Foundation 5.2 to
  9.0: Webinar Takeaways Mapping VLAN Tags to Virtual Private Cloud Subnets VMware
  Cloud Foundation is the Gold Standard for Virtual Desktop Infrastructure VMware
  Cloud Foundation (VCF) 9 introduces a Unified VCF Software Development Kit (SDK)
  for Python and Java. The key highlight of this release was the unification of all
  the major components into a single deliverable package to deliver simple, extensible,
  and consistent automation experience across the stack.'
summary: 'Authentication dilemma with vSphere APIs The unified authentication Sample
  Code What is happening behind the scenes? Resources Discover more from VMware Cloud
  Foundation (VCF) Blog Related Articles Upgrading VMware Cloud Foundation 5.2 to
  9.0: Webinar Takeaways Mapping VLAN Tags to Virtual Private Cloud Subnets VMware
  Cloud Foundation is the Gold Standard for Virtual Desktop Infrastructure VMware
  Cloud Foundation (VCF) 9 introduces a Unified VCF Software Development Kit (SDK)
  for Python and Java. The key highlight of this release was the unification of all
  the major components into a single deliverable package to deliver simple, extensible,
  and consistent automation experience across the stack. Currently, the following
  VCF components are included as a part of the unified VCF SDK and rest of the components
  will be made available very soon- VMware vSphere VMware vSAN VMware vSAN Data Protection
  VMware SDDC Manager If you are reading the term Unified VCF SDK for the first time,
  do not worry about it. You can visit some of the existing content such as the announcement
  blog post or visit the VMware Explore Las Vegas 2025 session to get yourself up
  to speed with all the enhancements introduced with VCF APIs and the VCF SDK. In
  this blog post I will focus on a small yet very effective enhancement to our vSphere
  API authentication and explain its usage across the vSphere and vSAN APIs. For context,
  VMware vSphere exposes two major categories of APIs: vSphere Web Services APIs and
  vSphere Automation APIs. The primary difference between the two lies in their underlying
  communication protocol. vSphere Web Services APIs use the Simple Object Access Protocol
  (SOAP) protocol. vSphere Automation APIs use Representational State Transfer (REST).
  If you have ever explored the Managed Object Browser (MOB) from the vSphere Client,
  you were interacting with the Web Services (SOAP) APIs. In contrast, the API Explorer
  in the Developer Center exposes the vSphere Automation (REST) APIs. For building
  complete solutions, developers often need to work with both sets of APIs.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/11/19/unified-authentication-in-vmware-cloud-foundation-sdk-9-0-seamless-authentication-across-vsphere-and-vsan-apis/
