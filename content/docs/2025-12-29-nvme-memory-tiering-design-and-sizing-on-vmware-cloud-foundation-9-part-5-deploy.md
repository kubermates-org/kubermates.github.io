---
title: 'NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation 9 Part 5:
  Deployment Scenarios (Greenfield, Brownfield, Nested Lab)'
date: '2025-12-29T12:00:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/12/29/nvme-memory-tiering-design-and-sizing-on-vmware-cloud-foundation-9-part-5/
post_kind: link
draft: false
tldr: 'Greenfield Deployments Brownfield Deployments Lab Deployments Discover more
  from VMware Cloud Foundation (VCF) Blog Related Articles NVMe Memory Tiering Design
  and Sizing on VMware Cloud Foundation 9 Part 5: Deployment Scenarios (Greenfield,
  Brownfield, Nested Lab) NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation
  9 Part 4: vSAN Compatibility and Storage Considerations NVMe Memory Tiering Design
  and Sizing on VMware Cloud Foundation 9 Part 3: Sizing for Success In this part
  of the blog series, I want to provide some information about the differences when
  enabling Memory Tiering in different scenarios. Although the core process remains
  the same, there are things that may require extra attention and planning to save
  some time and effort.'
summary: 'Greenfield Deployments Brownfield Deployments Lab Deployments Discover more
  from VMware Cloud Foundation (VCF) Blog Related Articles NVMe Memory Tiering Design
  and Sizing on VMware Cloud Foundation 9 Part 5: Deployment Scenarios (Greenfield,
  Brownfield, Nested Lab) NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation
  9 Part 4: vSAN Compatibility and Storage Considerations NVMe Memory Tiering Design
  and Sizing on VMware Cloud Foundation 9 Part 3: Sizing for Success In this part
  of the blog series, I want to provide some information about the differences when
  enabling Memory Tiering in different scenarios. Although the core process remains
  the same, there are things that may require extra attention and planning to save
  some time and effort. When we talk about greenfield scenarios, we refer to brand
  new VMware Cloud Foundation (VCF) deployments including new hardware and new configuration
  for the whole stack. Brownfield scenarios will cover configuring Memory Tiering
  on an existing VCF environment. Lastly, I do want to include lab scenarios as I
  have seen mixed statements that this is not supported, but I will cover this at
  the end of this blog post. Let’s start with the configuration process of greenfield
  environments. In Part 4 , I covered how VMware vSAN and Memory Tiering are compatible
  and can co-exist in the same cluster. I’ve also highlighted something important
  that you should be aware of during greenfield deployments of VCF. As of VCF 9.0,
  enabling Memory Tiering is a “Day 2” operation, meaning that you first configure
  VCF and then you can configure Memory Tiering, but during the VCF deployment workflow,
  you will notice there is no option to enable Memory Tiering (yet), but you can enable
  vSAN. How you handle your NVMe device dedicated for Memory Tiering will dictate
  the steps necessary to get that device presented for its configuration. If all the
  NVMe devices for both vSAN and Memory Tiering are present during the VCF deployment,
  chances are vSAN may auto-claim all of the drives (including the NVMe device you
  have allocated for Memory Tiering). In this case you would have to remove the drive
  from vSAN post-configuration, erase partitions and then start your Memory Tiering
  configuration.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/12/29/nvme-memory-tiering-design-and-sizing-on-vmware-cloud-foundation-9-part-5/
