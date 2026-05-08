---
title: More Capacity with VMware vSAN Compression and Global Deduplication in VCF
  9.1
date: '2026-05-07T13:00:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/05/07/vsan-compression-and-global-deduplication-in-vcf-9-1/
post_kind: link
draft: false
tldr: 'New Data Compression: Always on, Always Efficient vSAN Global Deduplication
  Summary Discover more from VMware Cloud Foundation (VCF) Blog Related Articles Introducing
  VMmark 4.1: Enhanced Power Efficiency Benchmarking for Private Cloud Infrastructure
  Cost-Efficient VMware vSAN ReadyNodes Certified for Cyber Recovery Deployments More
  Capacity with VMware vSAN Compression and Global Deduplication in VCF 9.1 Driving
  down the cost of storage is the motivation behind our ongoing work to improve efficiency
  in vSAN. When you can store more data on the same physical hardware through software
  enhancements, everybody wins.'
summary: 'New Data Compression: Always on, Always Efficient vSAN Global Deduplication
  Summary Discover more from VMware Cloud Foundation (VCF) Blog Related Articles Introducing
  VMmark 4.1: Enhanced Power Efficiency Benchmarking for Private Cloud Infrastructure
  Cost-Efficient VMware vSAN ReadyNodes Certified for Cyber Recovery Deployments More
  Capacity with VMware vSAN Compression and Global Deduplication in VCF 9.1 Driving
  down the cost of storage is the motivation behind our ongoing work to improve efficiency
  in vSAN. When you can store more data on the same physical hardware through software
  enhancements, everybody wins. vSAN in VMware Cloud Foundation (VCF) 9.1 delivers
  two new enhancements that improve storage efficiency: new data compression capabilities
  and the general availability of vSAN global deduplication. These cluster-based features
  that make it possible, and they are the focus of this post. Data compression in
  vSAN has historically been achieved through the LZ4 compression algorithm. It is
  commonly used in all types of systems and processes that are latency-sensitive,
  as it emphasizes performance and low computational overhead over absolute space
  efficiency. Even with the introduction of vSAN Express Storage Architecture (ESA)
  in 2022, we continued to use LZ4, but designed ESA to adapt to other algorithms
  if needed. For vSAN ESA in VCF 9.1, we employ the use of another compression algorithm.
  zStandard (ZSTD) is a highly versatile and efficient compression algorithm originally
  developed by Meta. It has unique capabilities that can offer noticeably higher compression
  ratios than LZ4 while maintaining good performance and modest CPU overhead. Perhaps
  most intriguing is that it is adjustable, and has been carefully tuned for vSAN’s
  storage stack to offer the best balance of space efficiency with minimal resource
  overhead. This fine-tuning sets the stage for even more innovation to come in future
  editions of vSAN.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/05/07/vsan-compression-and-global-deduplication-in-vcf-9-1/
