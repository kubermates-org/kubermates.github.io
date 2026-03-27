---
title: Lift-and-Shift VMs to Kubernetes with Calico L2 Bridge Networks
date: '2026-03-21T06:12:02+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/lift-and-shift-vms-to-kubernetes-with-calico-l2-bridge-networks/
post_kind: link
draft: false
tldr: 'Why lift-and-shift migration is challenging Introducing Calico L2 Bridge Networks
  Why this matters Benefits After Migration Network Observability Calico Policy Enforcement
  Live Migration Conclusion Calico L2 bridge networking for virtual machines In a
  traditional hypervisor environment: A VM connects to a network the rest of the data
  center already understands. Its IP address is a first-class citizen of the network.'
summary: 'Why lift-and-shift migration is challenging Introducing Calico L2 Bridge
  Networks Why this matters Benefits After Migration Network Observability Calico
  Policy Enforcement Live Migration Conclusion Calico L2 bridge networking for virtual
  machines In a traditional hypervisor environment: A VM connects to a network the
  rest of the data center already understands. Its IP address is a first-class citizen
  of the network. Firewalls, routers, monitoring tools , and peer applications know
  how to reach it. Existing application dependencies are often built around that network
  identity. Default Kubernetes pod networking works very differently: Pod IPs usually
  come from a cluster-managed pod CIDR. Those IPs are mainly meaningful inside the
  Kubernetes cluster. The upstream network usually does not have direct visibility
  into pod networks. The original network segments from the VM world are not preserved
  by default. This creates a major problem for VM migration: The workload can no longer
  keep the same network presence it had before. Teams often need to introduce VIPs
  or reconfigure the networking settings of the VM. That adds more complexity since
  changing the IP of the VM also requires changes to network firewall and load balancer
  configuration. At scale, it can make migration slower, more expensive, and harder
  to justify.'
---
Open the original post ↗ https://www.tigera.io/blog/lift-and-shift-vms-to-kubernetes-with-calico-l2-bridge-networks/
