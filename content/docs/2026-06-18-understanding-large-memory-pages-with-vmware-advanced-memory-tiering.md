---
title: Understanding Large Memory Pages with VMware Advanced Memory Tiering
date: '2026-06-18T13:40:06+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/06/18/understanding-large-memory-pages-with-vmware-advanced-memory-tiering/
post_kind: link
draft: false
tldr: 'Let’s Set the Stage Memory Tiering Changes the Equation The Three Page Size
  Scenarios 4 KB Small Pages: Fully Optimized 2 MB Large Pages: Opt-In, with a Catch
  1 GB Pages: DRAM Only, No Exceptions The TPS Angle The Bottom Line Discover more
  from VMware Cloud Foundation (VCF) Blog Related Articles What a TAM Really Does:
  Three Stories from the Field Diagnostics Log Assist for Broadcom Cases PostgreSQL
  Diagnostic Superpowers: Deep Visibility with VMware Data Services Manager 9.1 If
  you’ve been setting up VMware Memory Tiering or thinking about it, you’ve probably
  asked yourself at some point: what happens to Memory Large Pages? It’s a great question,
  and I’m glad you’ve asked it, because the answer changes how you need to plan your
  capacity and configure your VMs. Let me walk you through it.'
summary: 'Let’s Set the Stage Memory Tiering Changes the Equation The Three Page Size
  Scenarios 4 KB Small Pages: Fully Optimized 2 MB Large Pages: Opt-In, with a Catch
  1 GB Pages: DRAM Only, No Exceptions The TPS Angle The Bottom Line Discover more
  from VMware Cloud Foundation (VCF) Blog Related Articles What a TAM Really Does:
  Three Stories from the Field Diagnostics Log Assist for Broadcom Cases PostgreSQL
  Diagnostic Superpowers: Deep Visibility with VMware Data Services Manager 9.1 If
  you’ve been setting up VMware Memory Tiering or thinking about it, you’ve probably
  asked yourself at some point: what happens to Memory Large Pages? It’s a great question,
  and I’m glad you’ve asked it, because the answer changes how you need to plan your
  capacity and configure your VMs. Let me walk you through it. Before we get into
  the tiering-specific behavior, let’s quickly recap what Large Pages are and why
  they matter. The x86 architecture supports three page sizes: 4 KB (small pages),
  2 MB, and 1 GB. The latter two are collectively called “Large Pages”. Think of page
  size like the denomination of bills in your wallet. Larger denominations are more
  efficient to carry around, but harder to make change with. Large pages work the
  same way; they reduce TLB (Translation Lookaside Buffer) pressure and cut the cost
  of page table walks, which translates to potential performance gains for memory-intensive
  workloads. ESX uses 2 MB pages to back guest virtual RAM by default, and for good
  reason: the performance benefit is well established. So when Memory Tiering enters
  the picture, you’d naturally assume large pages stay on. Here’s where things get
  interesting. When you enable Memory Tiering on a host, VMs are configured with Large
  Pages disabled from tiering by default.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/06/18/understanding-large-memory-pages-with-vmware-advanced-memory-tiering/
