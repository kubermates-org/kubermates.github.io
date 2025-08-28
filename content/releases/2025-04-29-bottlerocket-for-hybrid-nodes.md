---
title: Bottlerocket for hybrid nodes
date: '2025-04-29T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-bottlerocket.html
post_kind: release
draft: false
tldr: 'Connect hybrid nodes with Bottlerocket Prerequisites Step 1: Create the Bottlerocket
  settings TOML file SSM IAM Roles Anywhere Step 2: Provision the Bottlerocket vSphere
  VM with user data Creating VM for the first time Updating user data for an existing
  VM Step 3: Verify the hybrid node connection Step 4: Configure a CNI for hybrid
  nodes Help improve this page To contribute to this user guide, choose the Edit this
  page on GitHub link that is located in the right pane of every page. This topic
  describes how to connect hybrid nodes running Bottlerocket to an Amazon EKS cluster.'
summary: 'Connect hybrid nodes with Bottlerocket Prerequisites Step 1: Create the
  Bottlerocket settings TOML file SSM IAM Roles Anywhere Step 2: Provision the Bottlerocket
  vSphere VM with user data Creating VM for the first time Updating user data for
  an existing VM Step 3: Verify the hybrid node connection Step 4: Configure a CNI
  for hybrid nodes Help improve this page To contribute to this user guide, choose
  the Edit this page on GitHub link that is located in the right pane of every page.
  This topic describes how to connect hybrid nodes running Bottlerocket to an Amazon
  EKS cluster. Bottlerocket is an open source Linux distribution that is sponsored
  and supported by AWS. Bottlerocket is purpose-built for hosting container workloads.
  With Bottlerocket, you can improve the availability of containerized deployments
  and reduce operational costs by automating updates to your container infrastructure.
  Bottlerocket includes only the essential software to run containers, which improves
  resource usage, reduces security threats, and lowers management overhead. Only VMware
  variants of Bottlerocket version v1.37.0 and above are supported with EKS Hybrid
  Nodes. VMware variants of Bottlerocket are available for Kubernetes versions v1.28
  and above. The OS images for these variants include the kubelet, containerd, aws-iam-authenticator
  and other software prerequisites for EKS Hybrid Nodes. You can configure these components
  using a Bottlerocket settings file that includes base64 encoded user-data for the
  Bottlerocket bootstrap and admin containers. Configuring these settings enables
  Bottlerocket to use your hybrid nodes credentials provider to authenticate hybrid
  nodes to your cluster. After your hybrid nodes join the cluster, they will appear
  with status Not Ready in the Amazon EKS console and in Kubernetes-compatible tooling
  such as kubectl.'
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-bottlerocket.html
