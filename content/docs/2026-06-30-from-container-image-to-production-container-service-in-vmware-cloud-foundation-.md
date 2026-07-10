---
title: 'From Container Image to Production: Container Service in VMware Cloud Foundation
  9.1'
date: '2026-06-30T14:34:43+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/06/30/from-container-image-to-production-container-service-in-vmware-cloud-foundation-9-1/
post_kind: link
draft: false
tldr: 'Introduction Demo Technical Overview Deploying a container was never this easy!
  Scaling Workloads Conclusion Discover more from VMware Cloud Foundation (VCF) Blog
  Related Articles Beyond Benchmarks: Engineering a Science-Grounded Validation for
  the Envoy AI Gateway Announcing the General Availability of Holodeck 9.1 Faster
  Security Patching with Fewer Disruptions in VCF 9.1 The new Container Service in
  VMware Cloud Foundation (VCF) offers an easy-to-start on-ramp to Kubernetes (K8s)
  consumption for your business, without requiring Kubernetes expertise. We have heard
  from many organizations that sometimes they “just want to run a container,” or they
  can’t hire the talent they would like to run workloads on Kubernetes, or they’re
  just starting their application modernization journey – taking those old.'
summary: 'Introduction Demo Technical Overview Deploying a container was never this
  easy! Scaling Workloads Conclusion Discover more from VMware Cloud Foundation (VCF)
  Blog Related Articles Beyond Benchmarks: Engineering a Science-Grounded Validation
  for the Envoy AI Gateway Announcing the General Availability of Holodeck 9.1 Faster
  Security Patching with Fewer Disruptions in VCF 9.1 The new Container Service in
  VMware Cloud Foundation (VCF) offers an easy-to-start on-ramp to Kubernetes (K8s)
  consumption for your business, without requiring Kubernetes expertise. We have heard
  from many organizations that sometimes they “just want to run a container,” or they
  can’t hire the talent they would like to run workloads on Kubernetes, or they’re
  just starting their application modernization journey – taking those old. Net Framework
  apps, refactoring onto. Net Core, and beginning to containerize. Typically when
  you want to run simple container apps, the workflow has been: Set up a host OS Install
  and configure a container runtime Configure registry authentication Pull and run
  the container image That is to say nothing of the lifecycle management, OS patching,
  runtime upgrades, security hardening, etc. required to operate such a system over
  time. Whatever the reason, we have heard loud and clear that customers want a simple,
  managed experience that allows them to get the benefits of Kubernetes, without the
  toil or internal expertise. As such we’ve built the new Container Service into VCF
  Automation (and the Local Consumption Interface if you don’t have VCF Automation)
  to get you up and running with pre-built containers easily. Let’s take a look at
  how it works, what it does, and how you might use it today! The VCF Container Service
  is an easy-to-use wrapper around our Supervisor cluster’s concept of vSphere Pods.
  vSphere Pods allow you to run containers as VMs for a number of reasons; whether
  you require a hard kernel boundary between containers, you don’t want the overhead
  of having dedicated K8s control planes, or you just don’t want to manage and lifecycle
  K8s clusters. This wrapper exposes almost everything you can expect to do with a
  container workload on K8s, we will even make intelligent decisions based on the
  workload specifications you put into the Container Service whether that application
  should run as a K8s Deployment or StatefulSet for example. StatefulSet Getting started
  is simple; just give the Container Service an OCI-compliant image and it will run
  it for you.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/06/30/from-container-image-to-production-container-service-in-vmware-cloud-foundation-9-1/
