---
title: How to Converge a VMware vSphere Environment to VMware Cloud Foundation 9.0
date: '2026-02-05T15:27:10+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/02/05/how-to-converge-a-vmware-vsphere-environment-to-vmware-cloud-foundation-9-0/
post_kind: link
draft: false
tldr: 'Path 1: Converting a vSphere instance Step 1: Assess, Check Prerequisites,
  and Remediate Core Components Step 2: Perform Upgrades to Appliances and ESX Hosts
  Step 3: Convert vSphere to VCF Path 2: Importing a vSphere instance into a VCF Fleet
  Step 1: Assess, Check Prerequisites, and Remediate Core Components Step 2: Remediate
  Any Errors Step 3: Import vSphere to VCF Need Help? Discover more from VMware Cloud
  Foundation (VCF) Blog Related Articles How to Converge a VMware vSphere Environment
  to VMware Cloud Foundation 9.0 VCF Breakroom Chats Episode 83 – Designing Developer-Loved
  Platforms: What is an IDP? A Perfect Match for Big Data: VMware vSphere Kubernetes
  Service and Tanzu Greenplum Converging your VMware vSphere environment into VMware
  Cloud Foundation (VCF) is a strategic move that shifts your infrastructure from
  a collection of managed silos to a unified private cloud. Depending on your current
  environment, there are two primary paths.'
summary: 'Path 1: Converting a vSphere instance Step 1: Assess, Check Prerequisites,
  and Remediate Core Components Step 2: Perform Upgrades to Appliances and ESX Hosts
  Step 3: Convert vSphere to VCF Path 2: Importing a vSphere instance into a VCF Fleet
  Step 1: Assess, Check Prerequisites, and Remediate Core Components Step 2: Remediate
  Any Errors Step 3: Import vSphere to VCF Need Help? Discover more from VMware Cloud
  Foundation (VCF) Blog Related Articles How to Converge a VMware vSphere Environment
  to VMware Cloud Foundation 9.0 VCF Breakroom Chats Episode 83 – Designing Developer-Loved
  Platforms: What is an IDP? A Perfect Match for Big Data: VMware vSphere Kubernetes
  Service and Tanzu Greenplum Converging your VMware vSphere environment into VMware
  Cloud Foundation (VCF) is a strategic move that shifts your infrastructure from
  a collection of managed silos to a unified private cloud. Depending on your current
  environment, there are two primary paths. Path 1: Convert your vSphere environment
  into a new VCF fleet using the VCF Installer. This approach is typically used if
  there is no VCF instance deployed already, but there are existing VMware Cloud Foundation
  Operations, VMware vCenter, and VMware NSX instances in the environment. These existing
  components are used to instantiate the VCF management domain, deploying any components
  which are missing. Path 2: Import your vSphere environment into an existing VCF
  fleet using VCF Operations. This approach is used when you already have a VCF instance
  deployed and want to manage a vSphere instance centrally as an additional VI workload
  domain in VCF. This will also deploy any missing components, such as NSX, if they
  have not been instantiated yet while the vSphere instance is being imported. The
  exact steps you need to take depend on the version of vSphere and/or VCF that is
  being used in the environment. Here are the typical processes VCF Professional Services
  uses to convert or import vSphere to VCF. This is the typical starting point for
  many vSphere customers who do not want to do a fresh deployment of VCF 9.0, where
  there is no existing VCF instance already deployed in the environment. This allows
  for the existing components in the environment to be used as starting blocks for
  a VCF management domain.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/02/05/how-to-converge-a-vmware-vsphere-environment-to-vmware-cloud-foundation-9-0/
