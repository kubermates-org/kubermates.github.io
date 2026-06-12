---
title: 'Architecting VMware vSphere Kubernetes Service on VCF: Top Webinar and Field
  Questions Answered'
date: '2026-06-09T14:37:49+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/06/09/architecting-vmware-vsphere-kubernetes-service-on-vcf-top-webinar-and-field-questions-answered/
post_kind: link
draft: false
tldr: 'Architecture, Availability Zones, and Deployments VMware Cloud Foundation Automation
  Integration Networking, Container Network Interface (CNI), and Load Balancing Storage,
  Persistent Volume Claims (PVCs), and Container Storage Interface (CSI) Backup, DR,
  and Lifecycle Management Need help? Discover more from VMware Cloud Foundation (VCF)
  Blog Related Articles Architecting VMware vSphere Kubernetes Service on VCF: Top
  Webinar and Field Questions Answered Modernizing the Private Cloud: Why VCF 9.1
  Lifecycle Management is a Game Changer Webinar Recap: Design and Architecture Considerations
  for VMware vSphere Kubernetes Service on VMware Cloud Foundation If you missed our
  recent webinar on VMware vSphere Kubernetes Service (VKS) on VMware Cloud Foundation
  , don’t worry—we’ve got you covered. Caleb Washburn (Momentum AI, CIO) and I teamed
  up to talk about architecture and design, while our Principal Architect for VCF
  Professional Services, Libby Shen , tackled lots of great questions from the audience.'
summary: 'Architecture, Availability Zones, and Deployments VMware Cloud Foundation
  Automation Integration Networking, Container Network Interface (CNI), and Load Balancing
  Storage, Persistent Volume Claims (PVCs), and Container Storage Interface (CSI)
  Backup, DR, and Lifecycle Management Need help? Discover more from VMware Cloud
  Foundation (VCF) Blog Related Articles Architecting VMware vSphere Kubernetes Service
  on VCF: Top Webinar and Field Questions Answered Modernizing the Private Cloud:
  Why VCF 9.1 Lifecycle Management is a Game Changer Webinar Recap: Design and Architecture
  Considerations for VMware vSphere Kubernetes Service on VMware Cloud Foundation
  If you missed our recent webinar on VMware vSphere Kubernetes Service (VKS) on VMware
  Cloud Foundation , don’t worry—we’ve got you covered. Caleb Washburn (Momentum AI,
  CIO) and I teamed up to talk about architecture and design, while our Principal
  Architect for VCF Professional Services, Libby Shen , tackled lots of great questions
  from the audience. In this post, we’re bringing those answers directly to you, combining
  the best Q&A from the live session with the top questions we hear every day while
  working on customer engagements. Q: What is the minimum number of VMware ESX hosts
  required to set up a VMware vSphere Supervisor, VKS cluster, and an Availability
  Zone (AZ)? A: The standard minimum requirement for an ESX host cluster to support
  VMware vSAN and HA is three hosts. An AZ in VCF represents a logical construct of
  an independent physical failure domain, which typically means a minimum of three
  hosts per zone to maintain quorum and availability. Q: Why not use a single stretched
  ESX metro cluster across two data centers for the management control plane? Is that
  supported? A: Stretched clusters are fully supported for both the Management Domain
  and Workload Domains in VCF 9. x. However, VCF 9.1 heavily promotes the 3-Zone Deployment
  Model as the modern standard for native Kubernetes HA, as it provides better fault
  tolerance without the split-brain risks sometimes associated with 2-site metro clusters.
  Q: If worker nodes sit in ESX hosts, where do the vSphere Supervisor control plane
  VMs and workload cluster control plane VMs sit? A: In VKS both the vSphere Supervisor
  control plane and the workload cluster nodes ultimately run on ESX. The vSphere
  Supervisor control plane VMs are deployed onto the vSphere Supervisor-enabled vSphere
  cluster and managed by vCenter/VCF. When a workload cluster is created, its Kubernetes
  control plane nodes and worker nodes are also provisioned as VMs on the ESX hosts,
  typically spread by DRS/HA according to placement and availability rules. So ESX
  is the common substrate; the distinction is whether a VM belongs to the vSphere
  Supervisor platform control plane or to a tenant/workload Kubernetes cluster.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/06/09/architecting-vmware-vsphere-kubernetes-service-on-vcf-top-webinar-and-field-questions-answered/
