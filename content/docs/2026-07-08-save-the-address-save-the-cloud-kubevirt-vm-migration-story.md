---
title: Save the Address, Save the Cloud (KubeVirt VM Migration Story)
date: '2026-07-08T20:45:58+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/save-the-address-save-the-cloud-kubevirt-vm-migration-story/
post_kind: link
draft: false
tldr: 'There Is Something About KubeVirt CPU Memory Networking How local live migration
  actually works The hard part: the VM has to keep its IP Bridge mode is non-negotiable
  VM IP address persistence Don’t NAT the VM on the way out Switching the traffic
  with BGP route priority Policy must land before the switch Wrapping up Kubernetes
  is built for containers, and it’s been doing that since it used to run docker as
  an engine for its containers. But what if you want to add VMs to the mix? After
  all, containers are ephemeral and don’t require fixed IPs as they shift the identity
  toward labels, but VMs on the other hand are tied to IP addresses and in some cases
  MAC addresses.'
summary: 'There Is Something About KubeVirt CPU Memory Networking How local live migration
  actually works The hard part: the VM has to keep its IP Bridge mode is non-negotiable
  VM IP address persistence Don’t NAT the VM on the way out Switching the traffic
  with BGP route priority Policy must land before the switch Wrapping up Kubernetes
  is built for containers, and it’s been doing that since it used to run docker as
  an engine for its containers. But what if you want to add VMs to the mix? After
  all, containers are ephemeral and don’t require fixed IPs as they shift the identity
  toward labels, but VMs on the other hand are tied to IP addresses and in some cases
  MAC addresses. This brings us to this blog about VM migration and IP preservation.
  Unlike a pod that can be part of a deployment and run in a swarm of stateless endpoints,
  a VM is a stateful machine run by hypervisor like QEMU and extended to Kubernetes
  via KubeVirt Custom Resource Definitions (CRDs). KubeVirt is an abstraction layer
  between the underlying hypervisor (QEMU) on your machine and Kubernetes. Its job
  is to manage a VM’s lifecycle and provide the necessary requirements for a VM to
  be a native resident in Kubernetes. These requirements are CPU, Memory, Networking,
  etc. KubeVirt does this by wrapping each VM in an ordinary Kubernetes pod called
  virt-launcher. Inside that pod, KubeVirt runs libvirt and QEMU, and the “VM” is
  really just a process scheduled, networked, and accounted for like any other pod.
  That detail matters a lot once we get to migration: when a VM moves to another node,
  what Kubernetes actually does is create a brand-new virt-launcher pod on the destination
  and tear down the old one. Everything hard about live migration comes from making
  that pod swap invisible to the workload running inside. virt-launcher libvirt virt-launcher
  CPU is the part that does the actual work, every instruction the guest operating
  system and its applications execute runs on a virtual CPU that KubeVirt maps onto
  real cores of the host node.'
---
Open the original post ↗ https://www.tigera.io/blog/save-the-address-save-the-cloud-kubevirt-vm-migration-story/
