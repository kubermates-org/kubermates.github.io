---
title: 'KubeVirt Networking: How to Preserve VM IP Addresses During Migration'
date: '2026-04-21T20:55:58+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/kubevirt-networking-how-to-preserve-vm-ip-addresses-during-migration/
post_kind: link
draft: false
tldr: Introducing KubeVirt The network is a different story Why default KubeVirt networking
  breaks VM migrations A lift-and-shift becomes a multi-team project How to preserve
  VM IP addresses and VLANs in Kubernetes Why a secondary interface and not the primary?
  How Calico sets it up What you gain after the migration Network visibility Security
  policy you can actually version control Live migration that doesn’t touch the network
  Making VM migration to Kubernetes practical Organisations are re-evaluating their
  VM infrastructure. The economics have shifted, the tooling has matured, and the
  case for running two separate platforms, one for containers, one for VMs, is getting
  harder to justify.
summary: 'Introducing KubeVirt The network is a different story Why default KubeVirt
  networking breaks VM migrations A lift-and-shift becomes a multi-team project How
  to preserve VM IP addresses and VLANs in Kubernetes Why a secondary interface and
  not the primary? How Calico sets it up What you gain after the migration Network
  visibility Security policy you can actually version control Live migration that
  doesn’t touch the network Making VM migration to Kubernetes practical Organisations
  are re-evaluating their VM infrastructure. The economics have shifted, the tooling
  has matured, and the case for running two separate platforms, one for containers,
  one for VMs, is getting harder to justify. Platform teams that spent years managing
  hypervisor infrastructure are being asked to consolidate, and most are landing on
  the same answer: Kubernetes. KubeVirt makes running VMs on Kubernetes possible.
  But KubeVirt networking – what happens to a VM’s IP address, VLAN, and security
  posture when it lands in a cluster – is where most migration plans hit a wall. The
  reasons go beyond cost: Most enterprises already run Kubernetes. Containers are
  already there. Adding VMs to the same platform consolidates tooling, lifecycle management,
  networking models, and security policy into a single operational model. Two platforms
  means double the overhead. Separate infrastructure means separate upgrade cycles,
  separate monitoring, separate network configuration, and separate on-call runbooks.
  Platform consolidation has direct operational value. Kubernetes is mature enough.'
---
Open the original post ↗ https://www.tigera.io/blog/kubevirt-networking-how-to-preserve-vm-ip-addresses-during-migration/
