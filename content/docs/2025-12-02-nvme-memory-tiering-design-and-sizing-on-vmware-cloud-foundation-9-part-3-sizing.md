---
title: 'NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation 9 Part 3:
  Sizing for Success'
date: '2025-12-02T12:00:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/12/02/nvme-memory-tiering-design-and-sizing-on-vmware-cloud-foundation-9-part-3/
post_kind: link
draft: false
tldr: 'Discover more from VMware Cloud Foundation (VCF) Blog Related Articles NVMe
  Memory Tiering Design and Sizing on VMware Cloud Foundation 9 Part 3: Sizing for
  Success Making Harbor Production-Ready: Essential Considerations for Deployment
  Reducing Harbor Deployment Complexity on Kubernetes So far in this blog series,
  we have highlighted the value that NVMe Memory Tiering delivers to our customers
  and how this is driving adoption. Who doesn’t want to reduce their cost by ~40%
  just by adopting VMware Cloud Foundation 9?! We’ve also touched on pre-requisites,
  and hardware in Part 1 , and design in Part 2 ; so, let’s now talk about properly
  sizing your environment so you can maximize your investment while reducing your
  cost.'
summary: 'Discover more from VMware Cloud Foundation (VCF) Blog Related Articles NVMe
  Memory Tiering Design and Sizing on VMware Cloud Foundation 9 Part 3: Sizing for
  Success Making Harbor Production-Ready: Essential Considerations for Deployment
  Reducing Harbor Deployment Complexity on Kubernetes So far in this blog series,
  we have highlighted the value that NVMe Memory Tiering delivers to our customers
  and how this is driving adoption. Who doesn’t want to reduce their cost by ~40%
  just by adopting VMware Cloud Foundation 9?! We’ve also touched on pre-requisites,
  and hardware in Part 1 , and design in Part 2 ; so, let’s now talk about properly
  sizing your environment so you can maximize your investment while reducing your
  cost. Proper sizing for NVMe Memory Tiering is mainly on the hardware side, but
  there are two possible ways to look at this; greenfield and brownfield deployments.
  Let’s start with brownfield deployments, which is adopting Memory Tiering on existing
  infrastructure. You’ve came to the realization that VCF 9 is truly an integrated
  product delivering a cohesive cloud like solution and decided to deploy it but just
  learned about Memory Tiering. Don’t worry, you can still introduce NVMe memory Tiering
  after deployment of VCF 9. After reading Part 1 and Part 2, we’ve learned the importance
  of the NVMe performance and endurance classes as well as the understanding the 50%
  active memory requirement. This means that we need to think about purchasing an
  NVMe device that is at least the same size of our DRAM, since we will double our
  memory capacity. So, if each of your hosts have 1TB of DRAM we should at least have
  1TB NVMe devices, easy enough. However, we can go bigger and still be cheaper than
  buying more DIMMS, let me explain. I’ve made it a point to say “buy an NVMe device
  to be at least the same size of DRAM”, and this is because we use a DRAM:NVMe ratio
  of 1:1 by default, so half of the memory comes from DRAM and half comes from NVMe.
  Now, there are workloads that may not be doing a whole lot as far as memory activity,
  think some VDI workloads.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/12/02/nvme-memory-tiering-design-and-sizing-on-vmware-cloud-foundation-9-part-3/
