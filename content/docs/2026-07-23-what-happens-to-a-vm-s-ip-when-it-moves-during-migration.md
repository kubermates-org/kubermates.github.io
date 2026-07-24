---
title: What Happens to a VM’s IP When It Moves During Migration?
date: '2026-07-23T13:10:45+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/what-happens-to-a-vms-ip-when-it-moves-during-migration/
post_kind: link
draft: false
tldr: 'Why VM IP identity needs handling on Kubernetes How Calico keeps the IP The
  handover window Why policy survives the move Routing: native BGP and fast convergence
  Prove it in the scenarios that matter What you gain once your VMs are Kubernetes-native
  Where this leaves you A KubeVirt VM runs inside a pod. That is the trick that lets
  Kubernetes schedule a VM like any other workload.'
summary: 'Why VM IP identity needs handling on Kubernetes How Calico keeps the IP
  The handover window Why policy survives the move Routing: native BGP and fast convergence
  Prove it in the scenarios that matter What you gain once your VMs are Kubernetes-native
  Where this leaves you A KubeVirt VM runs inside a pod. That is the trick that lets
  Kubernetes schedule a VM like any other workload. It also means the VM and the pod
  have different lifecycles. The VM is long-lived and has a stable identity. The pod
  is disposable. When the VM reboots, gets evicted, or live-migrates, the pod underneath
  is destroyed and a new one is created. That matters because a VM’s IP is load-bearing.
  Firewall rules, load balancer entries, and DNS records all point at it. On Kubernetes,
  standard pod IPAM ties the address to the pod, so a new pod would mean a new IP,
  and a changed IP is what breaks those dependencies. KubeVirt on its own does not
  carry the IP across a migration. Its issue tracker has a user reporting exactly
  this, with a maintainer confirming sticky IPs were never built into the project.
  The network identity needs something to carry it.'
---
Open the original post ↗ https://www.tigera.io/blog/what-happens-to-a-vms-ip-when-it-moves-during-migration/
