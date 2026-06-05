---
title: 'KubeVirt Live Migration Done Right: What it Takes to Run VMs on Kubernetes'
date: '2026-05-14T20:53:44+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/kubevirt-live-migration-done-right-what-it-takes-to-run-vms-on-kubernetes/
post_kind: link
draft: false
tldr: 'Kubernetes Networking Wasn’t Built for VMs Two Networking Modes, Two Different
  Problems Live Migration in Bridge Mode: What Happens Under the Hood The Core Challenge
  IP Persistence: IPAM That Understands VMs Route Convergence: The GARP Handover Policy
  continuity Portability and Standardization for VMs Running VMs in Kubernetes sounds
  like a crazy workaround for avoiding vendor lock-in, and standardizing legacy applications
  and newer containerized workloads on one control plane with one set of security
  policies to govern them all. It is, however, a rapidly growing pattern, and KubeVirt
  live migration — moving running VMs between nodes without downtime — is increasingly
  central to platform engineering use cases that require full VMs, like on-demand
  CI/CD pipelines.'
summary: 'Kubernetes Networking Wasn’t Built for VMs Two Networking Modes, Two Different
  Problems Live Migration in Bridge Mode: What Happens Under the Hood The Core Challenge
  IP Persistence: IPAM That Understands VMs Route Convergence: The GARP Handover Policy
  continuity Portability and Standardization for VMs Running VMs in Kubernetes sounds
  like a crazy workaround for avoiding vendor lock-in, and standardizing legacy applications
  and newer containerized workloads on one control plane with one set of security
  policies to govern them all. It is, however, a rapidly growing pattern, and KubeVirt
  live migration — moving running VMs between nodes without downtime — is increasingly
  central to platform engineering use cases that require full VMs, like on-demand
  CI/CD pipelines. KubeVirt is gaining traction as a way to bring VMs into Kubernetes
  as first-class workloads, managed with the same tools and primitives that platform
  teams already use for containers. It has, however, introduced some unique challenges.
  Here’s the uncomfortable truth about that migration: compute and storage are the
  easy parts. Networking is where migrations stall, roadblock multiple, and platform
  teams start questioning whether KubeVirt was the right call in the first place.
  If your VMs have no fixed IP dependencies, no VLAN memberships, and no upstream
  firewall rules scoped to specific subnets, you can migrate them into Kubernetes
  without losing sleep over the networking layer. If you’re running hundreds or thousands
  of VMs with IP addresses hardcoded into application configs, DNS entries, and firewall
  ACLs — and you need to move those VMs to Kubernetes without rewriting any of it
  — then your networking layer is about to become the most important decision in your
  migration. What follows is a technical walk-through of the L2 plumbing that keeps
  KubeVirt VMs connected when they move between nodes in a production cluster and
  how it eliminates the need to update your complicated network infrastructure. In
  a traditional hypervisor environment — vSphere, Hyper-V, Nutanix — VMs sit on VLANs
  and have fixed IPs. Upstream firewalls, load balancers, and DNS records all reference
  those IPs. A security team owns the VLAN segmentation while the network team owns
  the routing.'
---
Open the original post ↗ https://www.tigera.io/blog/kubevirt-live-migration-done-right-what-it-takes-to-run-vms-on-kubernetes/
