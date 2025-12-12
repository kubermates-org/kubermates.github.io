---
title: Erasure Codes in VMware vSAN versus Storage Arrays
date: '2025-12-10T13:00:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/12/10/erasure-codes-in-vmware-vsan-versus-storage-arrays/
post_kind: link
draft: false
tldr: 'The Purpose of Erasure Coding Data Storage in vSAN versus a Storage Array Comparing
  Erasure Codes in vSAN versus Traditional Storage Storage Array vSAN Decoupling Cluster
  Size and Availability Summary Discover more from VMware Cloud Foundation (VCF) Blog
  Related Articles Erasure Codes in VMware vSAN versus Storage Arrays Integrating
  VMware Data Services Manager with Harbor for a Production-Ready Registry NVMe Memory
  Tiering Design and Sizing on VMware Cloud Foundation 9 Part 3: Sizing for Success
  Data availability is a core competency of enterprise storage systems. For decades,
  these systems have attempted to deliver high levels of data availability while ensuring
  that performance and space efficiency expectations are also met.'
summary: 'The Purpose of Erasure Coding Data Storage in vSAN versus a Storage Array
  Comparing Erasure Codes in vSAN versus Traditional Storage Storage Array vSAN Decoupling
  Cluster Size and Availability Summary Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles Erasure Codes in VMware vSAN versus Storage Arrays Integrating
  VMware Data Services Manager with Harbor for a Production-Ready Registry NVMe Memory
  Tiering Design and Sizing on VMware Cloud Foundation 9 Part 3: Sizing for Success
  Data availability is a core competency of enterprise storage systems. For decades,
  these systems have attempted to deliver high levels of data availability while ensuring
  that performance and space efficiency expectations are also met. Achieving all three
  at the same time is not easy. Erasure coding has played an important role in storing
  data in a resilient yet space-efficient way. This post will help you better understand
  how erasure coding is implemented in VMware vSAN, how it is different from what
  may be found in traditional storage arrays, and how best to interpret an erasure
  code’s capabilities with data availability. The primary responsibility of any storage
  system is to give back the bit of data that has been requested. To ensure it can
  do this reliably, storage systems must store that data in a resilient way. A simple
  form of data resilience would be through the use of multiple copies, or “mirrors”
  that would help maintain availability in the event of some type of discrete failure
  in the storage system, such as a disk in a storage array, or a host in a distributed
  storage system like vSAN. One of the challenges with this approach is storing full
  copies of data becomes very costly in terms of capacity consumption. An additional
  copy would double the amount of data stored, while two additional copies would triple
  the amount of data stored. Erasure codes are used to store data in a resilient way,
  but with much more space efficiency relative to traditional mirroring of data. It
  does not use the approach of copies.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/12/10/erasure-codes-in-vmware-vsan-versus-storage-arrays/
