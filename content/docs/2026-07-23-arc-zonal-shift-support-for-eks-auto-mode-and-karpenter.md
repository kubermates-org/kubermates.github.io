---
title: ARC zonal shift support for EKS Auto Mode and Karpenter
date: '2026-07-23T16:53:34+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/arc-zonal-shift-support-for-eks-auto-mode-and-karpenter/
post_kind: link
draft: false
tldr: 'ARC zonal shift support for EKS Auto Mode and Karpenter How it works Best practices
  Knowing where you’re exposed Enabling Zonal Shift support (OSS Karpenter) Enabling
  Zonal Shift on Auto Mode clusters Running a test Prerequisites Step 1: Deploy a
  multi-AZ workload Step 2: Verify pre-shift state Step 3: Trigger a manual zonal
  shift Step 4: Observe zonal shift behavior Step 5: Cancel the shift and verify recovery
  Step 6: (Optional) Test with AWS Fault Injection Service Clean up Delete the sample
  workload (Optional) Disable zonal shift on the cluster Conclusion About the authors
  When an Availability Zone (AZ) experiences a failure, workloads running across multiple
  AZs need a fast, automated way to shift traffic and capacity away from the impaired
  zone. The AWS provider for Karpenter recently added support for Zonal Shift and
  Zonal Autoshift , features of Amazon Application Recovery Controller (ARC) designed
  to help you recover from these types of failures.'
summary: 'ARC zonal shift support for EKS Auto Mode and Karpenter How it works Best
  practices Knowing where you’re exposed Enabling Zonal Shift support (OSS Karpenter)
  Enabling Zonal Shift on Auto Mode clusters Running a test Prerequisites Step 1:
  Deploy a multi-AZ workload Step 2: Verify pre-shift state Step 3: Trigger a manual
  zonal shift Step 4: Observe zonal shift behavior Step 5: Cancel the shift and verify
  recovery Step 6: (Optional) Test with AWS Fault Injection Service Clean up Delete
  the sample workload (Optional) Disable zonal shift on the cluster Conclusion About
  the authors When an Availability Zone (AZ) experiences a failure, workloads running
  across multiple AZs need a fast, automated way to shift traffic and capacity away
  from the impaired zone. The AWS provider for Karpenter recently added support for
  Zonal Shift and Zonal Autoshift , features of Amazon Application Recovery Controller
  (ARC) designed to help you recover from these types of failures. In this post, we
  walk through how zonal shift integrates with Amazon Elastic Kubernetes Service (Amazon
  EKS) and what happens when a shift is triggered. We also show how to enable it on
  both self-managed Karpenter and EKS Auto Mode (EKS Auto) clusters. When Zonal Shift
  integration is enabled, it performs the following functions automatically: first,
  it cordons the worker nodes running in the affected zone, preventing new pods from
  being scheduled there. Second, it deregisters the IP addresses of pods running on
  worker nodes in the impaired zone from application and network load balancers. It
  also removes the endpoints of those pods from their corresponding endpoint slices.
  This effectively prevents those pods from receiving network traffic. Third, it temporarily
  prevents Managed Node Groups (MNG) , EKS Auto, and self-managed Karpenter from provisioning
  new capacity in the impaired zone. When using EKS Auto or self-managing Karpenter,
  voluntary disruptions (consolidation, drift, empty, and underutilized) are also
  temporarily suspended in the affected zone. Like MNGs, Karpenter avoids provisioning
  capacity in impaired zones. It detects the type of shift (manual or auto) and which
  zones are currently affected by polling the ARC GetManagedResources API every 30
  seconds.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/arc-zonal-shift-support-for-eks-auto-mode-and-karpenter/
