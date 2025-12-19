---
title: 'NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation 9 Part 4:
  vSAN Compatibility and Storage Considerations'
date: '2025-12-16T12:00:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/12/16/nvme-memory-tiering-design-and-sizing-on-vmware-cloud-foundation-9-part-4/
post_kind: link
draft: false
tldr: 'Storage Considerations Discover more from VMware Cloud Foundation (VCF) Blog
  Related Articles NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation
  9 Part 4: vSAN Compatibility and Storage Considerations Using Harbor as a Proxy
  Cache for Cloud-Based Registries What to Look for in Network Switches for VMware
  vSAN We’ve covered a lot of ground in the first 3 parts of this series: PART 1:
  Prerequisites and Hardware Compatibility PART 2: Design for Security, Redundancy,
  and Scalability PART 3: Sizing for Success But there is a lot more to learn about
  Memory Tiering. In fact, vSAN often comes up in conversations about Memory Tiering
  given its similarities, but also due to compatibility inquiries, so let’s dive in.'
summary: 'Storage Considerations Discover more from VMware Cloud Foundation (VCF)
  Blog Related Articles NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation
  9 Part 4: vSAN Compatibility and Storage Considerations Using Harbor as a Proxy
  Cache for Cloud-Based Registries What to Look for in Network Switches for VMware
  vSAN We’ve covered a lot of ground in the first 3 parts of this series: PART 1:
  Prerequisites and Hardware Compatibility PART 2: Design for Security, Redundancy,
  and Scalability PART 3: Sizing for Success But there is a lot more to learn about
  Memory Tiering. In fact, vSAN often comes up in conversations about Memory Tiering
  given its similarities, but also due to compatibility inquiries, so let’s dive in.
  When we first started working with Memory Tiering, the similarities between Memory
  Tiering and vSAN OSA were quite evident. Both have a multi-tier approach where active
  data is on fast devices and dormant data is on less expensive devices, thereby helping
  reduce TCO and the need for expensive devices for dormant data. They are also both
  deeply integrated into vSphere and are easy to implement. But aside from similarities,
  there was initially some confusion about compatibility, integration, and having
  both features enabled at the same time. So, let me answer those questions. Yes,
  you can have vSAN and Memory Tiering enabled on the same clusters at the same time.
  The confusion that exists is more around vSAN providing storage to Memory Tiering
  which is definitely not supported. I’ve covered this before, but I want to reiterate
  that although both solutions may be using NVMe devices, it does not mean they can
  share resources. Memory Tiering requires its own physical or logical device strictly
  for memory allocation. We do not want to share this physical/logical device with
  anything else including vSAN or other datastores.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/12/16/nvme-memory-tiering-design-and-sizing-on-vmware-cloud-foundation-9-part-4/
