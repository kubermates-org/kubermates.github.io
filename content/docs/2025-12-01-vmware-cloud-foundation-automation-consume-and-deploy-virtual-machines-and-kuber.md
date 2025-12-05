---
title: VMware Cloud Foundation Automation – Consume and Deploy Virtual Machines and
  Kubernetes Clusters
date: '2025-12-01T16:00:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/12/01/vmware-cloud-foundation-automation-consume-and-deploy-virtual-machines-and-kubernetes-clusters/
post_kind: link
draft: false
tldr: 'Virtual Machine Service vSphere Kubernetes Service Summary Discover more from
  VMware Cloud Foundation (VCF) Blog Related Articles VCF Breakroom Chats Episode
  75 - Breaking the GitOps Barrier: Continuous Delivery for Modern Apps with VCF 9
  VMware Cloud Foundation Automation – Consume and Deploy Virtual Machines and Kubernetes
  Clusters VCF Breakroom Chats Episode 74 - From VI Admin to Private Cloud Architect:
  New VCAP & VCDX Certification Explained In our previous blog , we talked about how
  an organization admin leveraging VMware Cloud Foundation Automation enables their
  organization to be effectively ready for application teams to self-serve and provision
  infrastructure and applications. In this blog, we are going to shed light on two
  foundational infrastructure services that are enabled and available out of the box
  when configuring the tenant organization that leverages the K8S Style API: the Virtual
  Machine Service and the vSphere Kubernetes Service.'
summary: 'Virtual Machine Service vSphere Kubernetes Service Summary Discover more
  from VMware Cloud Foundation (VCF) Blog Related Articles VCF Breakroom Chats Episode
  75 - Breaking the GitOps Barrier: Continuous Delivery for Modern Apps with VCF 9
  VMware Cloud Foundation Automation – Consume and Deploy Virtual Machines and Kubernetes
  Clusters VCF Breakroom Chats Episode 74 - From VI Admin to Private Cloud Architect:
  New VCAP & VCDX Certification Explained In our previous blog , we talked about how
  an organization admin leveraging VMware Cloud Foundation Automation enables their
  organization to be effectively ready for application teams to self-serve and provision
  infrastructure and applications. In this blog, we are going to shed light on two
  foundational infrastructure services that are enabled and available out of the box
  when configuring the tenant organization that leverages the K8S Style API: the Virtual
  Machine Service and the vSphere Kubernetes Service. The Kubernetes declarative API
  model has already transformed the way organizations build and operate modern applications.
  But in recent years, the same Kubernetes model has been extended beyond containerized
  workloads into the world of infrastructure itself. What started with kubectl apply
  for Pods and Deployments has evolved into using Kubernetes APIs to provision and
  manage virtual machines, K8S clusters, networking, storage, load balancers, and
  even databases. Kubernetes is no longer “just the platform for cloud-native apps.
  ” It’s steadily becoming the universal control plane for both applications and infrastructure.
  kubectl apply The Virtual Machine (VM) Service in VMware Cloud Foundation 9.0 provides
  a unified, Kubernetes-native interface for provisioning and managing VMs directly
  through namespaces. By exposing VM classes, images, storage policies, and networking
  configurations as declarative Kubernetes resources, the VM Service enables platform
  and application teams to consume vSphere-backed compute using familiar Kubernetes
  tooling. This service ensures consistent governance and lifecycle management by
  enforcing the policies defined at the organization, region, and project levels in
  VCF Automation, while leveraging vSphere’s mature virtualization capabilities underneath.
  Below is a detailed walkthrough of the VM provisioning workflow experience in VMware
  Cloud Foundation Automation. The vSphere Kubernetes Service (VKS) in VMware Cloud
  Foundation 9.0 delivers a fully integrated, upstream-compatible Kubernetes control
  plane that runs natively on vSphere.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/12/01/vmware-cloud-foundation-automation-consume-and-deploy-virtual-machines-and-kubernetes-clusters/
