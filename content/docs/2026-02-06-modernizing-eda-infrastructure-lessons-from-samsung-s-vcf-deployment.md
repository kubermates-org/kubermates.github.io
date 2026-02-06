---
title: 'Modernizing EDA Infrastructure: Lessons from Samsung’s VCF Deployment'
date: '2026-02-06T04:01:53+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/02/05/modernizing-eda-infrastructure-lessons-from-samsungs-vcf-deployment/
post_kind: link
draft: false
tldr: 'The Challenge: Memory Latency in Virtualization The Solution: Harnessing the
  Power of Huge Pages Performance Evaluation of Huge Pages Result Comparison Summary
  of Huge Page Settings Other Settings to Consider to Improve HPC Application Performance
  in VCF Determine When to Use Latency Sensitivity Mode Using High Speed Interconnect
  HCAs/NICs for MPI Workloads Maximum Memory Reservation for a User VM Reference Discover
  more from VMware Cloud Foundation (VCF) Blog Related Articles Modernizing EDA Infrastructure:
  Lessons from Samsung’s VCF Deployment How to Converge a VMware vSphere Environment
  to VMware Cloud Foundation 9.0 VCF Breakroom Chats Episode 83 – Designing Developer-Loved
  Platforms: What is an IDP? Authors: Yifan Hao, Yuankun Fu, Dongyun Heo, Jinsung
  Heo, Michael Furman, Rajesh Venkatasubramanian, Haoqiang Zheng, Kyung Min Park,
  Ramesh Radhakrishnan, Ashish Kaila, Yuichi Ui Samsung: Young-Jun Hong, Mokmin Park
  For organizations running Electronic Design Automation (EDA) workloads and High-Performance
  Computing (HPC) in virtualized environments, achieving near bare-metal performance
  is essential. One key challenge we identified is the performance impact caused by
  differences in memory access latency.'
summary: 'The Challenge: Memory Latency in Virtualization The Solution: Harnessing
  the Power of Huge Pages Performance Evaluation of Huge Pages Result Comparison Summary
  of Huge Page Settings Other Settings to Consider to Improve HPC Application Performance
  in VCF Determine When to Use Latency Sensitivity Mode Using High Speed Interconnect
  HCAs/NICs for MPI Workloads Maximum Memory Reservation for a User VM Reference Discover
  more from VMware Cloud Foundation (VCF) Blog Related Articles Modernizing EDA Infrastructure:
  Lessons from Samsung’s VCF Deployment How to Converge a VMware vSphere Environment
  to VMware Cloud Foundation 9.0 VCF Breakroom Chats Episode 83 – Designing Developer-Loved
  Platforms: What is an IDP? Authors: Yifan Hao, Yuankun Fu, Dongyun Heo, Jinsung
  Heo, Michael Furman, Rajesh Venkatasubramanian, Haoqiang Zheng, Kyung Min Park,
  Ramesh Radhakrishnan, Ashish Kaila, Yuichi Ui Samsung: Young-Jun Hong, Mokmin Park
  For organizations running Electronic Design Automation (EDA) workloads and High-Performance
  Computing (HPC) in virtualized environments, achieving near bare-metal performance
  is essential. One key challenge we identified is the performance impact caused by
  differences in memory access latency. In collaboration with Samsung, we have been
  investigating how to minimize this gap between bare-metal and virtualized platforms,
  particularly as observed with the memtest benchmark. Our analysis shows that the
  use of huge pages plays a crucial role in improving performance. In this blog, we
  share the progress made by the VCF engineering team in understanding memory access
  latency behavior and provide guidance on tuning systems to achieve optimal performance
  for HPC workloads. Our internal evaluation on Intel® Sapphire Rapids platforms shows
  that memory access latency can become noticeably higher in virtualized environments
  than on bare metal, particularly when the workload’s memory footprint grows beyond
  the coverage of the Translation Lookaside Buffer (TLB). In other words, as more
  memory pages are actively in use, the system experiences more frequent TLB misses,
  and the cost of handling those misses is amplified under virtualization. Why does
  this happen? When running inside a virtual machine, the translation from virtual
  memory to physical memory involves an additional level of indirection, requiring
  more page table state to be cached and managed. The hardware TLB, however, has a
  fixed capacity and can only cache a limited number of translations. Once the working
  set exceeds this capacity, the system must walk the page tables more often—and each
  page walk in a virtualized environment is more expensive than on bare metal. To
  illustrate the magnitude of this effect, our measurements show that memory access
  latency can increase by ~12% once the TLB is under pressure. The remainder of this
  blog explores why this happens in detail, and how tuning page sizes—especially through
  the use of huge pages—can dramatically reduce this overhead.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/02/05/modernizing-eda-infrastructure-lessons-from-samsungs-vcf-deployment/
