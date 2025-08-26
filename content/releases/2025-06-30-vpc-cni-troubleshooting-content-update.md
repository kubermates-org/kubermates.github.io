---
title: VPC CNI troubleshooting content update
date: '2025-06-30T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/network-policies-troubleshooting.html
post_kind: release
draft: false
tldr: Help improve this page To contribute to this user guide, choose the Edit this
  page on GitHub link that is located in the right pane of every page. This is the
  troubleshooting guide for network policy feature of the Amazon VPC CNI.
summary: 'Help improve this page To contribute to this user guide, choose the Edit
  this page on GitHub link that is located in the right pane of every page. This is
  the troubleshooting guide for network policy feature of the Amazon VPC CNI. This
  guide covers: Install information, CRD and RBAC permissions New policyendpoints
  CRD and permissions Logs to examine when diagnosing network policy problems Network
  policy logs Running the eBPF SDK collection of tools to troubleshoot Known issues
  and solutions Known issues and solutions Note that network policies are only applied
  to pods that are made by Kubernetes Deployments. For more limitations of the network
  policies in the VPC CNI, see Considerations. You can troubleshoot and investigate
  network connections that use network policies by reading the Network policy logs
  and by running tools from the eBPF SDK. CRD: policyendpoints. networking. k8s. aws
  Kubernetes API: apiservice called v1. networking. k8s. io Kubernetes resource: Kind:
  NetworkPolicy RBAC: ClusterRole called aws-node (VPC CNI), ClusterRole called eks:network-policy-controller
  (network policy controller in EKS cluster control plane) For network policy, the
  VPC CNI creates a new CustomResourceDefinition (CRD) called policyendpoints.'
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/network-policies-troubleshooting.html
