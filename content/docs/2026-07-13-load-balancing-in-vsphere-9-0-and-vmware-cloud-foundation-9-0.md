---
title: Load Balancing in vSphere 9.0+ and VMware Cloud Foundation 9.0+
date: '2026-07-13T22:48:52+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/07/13/choosing-the-right-load-balancer-for-vsphere-supervisor-in-vsphere-9-0-and-vmware-cloud-foundation-9-0/
post_kind: link
draft: false
tldr: 'The Three Core Platform Load Balancer Options 1. Foundation Load Balancer and
  NSX Load Balancer: Out-of-the-Box Layer 4 Connectivity 2.'
summary: 'The Three Core Platform Load Balancer Options 1. Foundation Load Balancer
  and NSX Load Balancer: Out-of-the-Box Layer 4 Connectivity 2. Avi Load Balancer:
  Enterprise-Grade Advanced Traffic Management Choosing a Platform Load Balancer by
  Workload Network Flexibility at the VKS Cluster Level At-a-Glance: Platform Load
  Balancer Comparison Final Thoughts Discover more from VMware Cloud Foundation (VCF)
  Blog Related Articles VCF Breakroom Chats | Episode 91 Spotting Infra Issues Instantly
  with VCF 9.1 We Asked an Independent Lab to Time Us. Here''s What They Found. Simplified
  Identity Management with Authentik for Holodeck 9.1 If you’re managing Kubernetes
  alongside traditional virtual machines, vSphere Supervisor in vSphere 9.0+ and VMware
  Cloud Foundation (VCF) 9.0+ serves as your unified control plane. But when it comes
  to setting up the infrastructure, one question always comes up from teams designing
  these environments: “Which load balancers are supported, and how do I choose the
  right one for my vSphere Supervisor?” The answer depends entirely on your existing
  networking architecture, your licensing, and how much traffic management control
  you want to hand off to the platform versus the development teams. Let’s break down
  the supported platform load balancers in vSphere 9+ and VCF 9+, look at how they
  map to your network topology, and explore where you can still leverage application-specific
  flexibility. vSphere Supervisor supports three platform load balancer options. Your
  choice determines how core infrastructure services – including VM Service virtual
  machines, native vSphere Pods, and VMware vSphere Kubernetes Service (VKS) cluster
  control planes – receive Layer 4 connectivity. Each option is designed for a different
  networking architecture and operational model. If you need integrated Layer 4 (IP:Port)
  load balancing out of the box, Foundation Load Balancer (FLB) and NSX Load Balancer
  (NSX-LB) are the primary platform load balancer options. Both provide native Layer
  4 connectivity for Supervisor-managed workloads.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/07/13/choosing-the-right-load-balancer-for-vsphere-supervisor-in-vsphere-9-0-and-vmware-cloud-foundation-9-0/
