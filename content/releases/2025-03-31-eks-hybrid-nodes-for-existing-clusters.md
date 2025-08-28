---
title: EKS Hybrid Nodes for existing clusters
date: '2025-03-31T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-cluster-update.html
post_kind: release
draft: false
tldr: Enable hybrid nodes on an existing Amazon EKS cluster or modify configuration
  Prerequisites Considerations Enable hybrid nodes on an existing cluster Enable EKS
  Hybrid Nodes in an existing cluster - AWS CloudFormation Enable EKS Hybrid Nodes
  in an existing cluster - AWS CLI Enable EKS Hybrid Nodes in an existing cluster
  - AWS Management Console Update hybrid nodes configuration in an existing cluster
  Update hybrid configuration in an existing cluster - AWS CloudFormation Update hybrid
  configuration in an existing cluster - AWS CLI Update hybrid configuration in an
  existing cluster - AWS Management Console Disable Hybrid nodes in an existing cluster
  Disable EKS Hybrid Nodes in an existing cluster - AWS CloudFormation Disable EKS
  Hybrid Nodes in an existing cluster - AWS CLI Disable EKS Hybrid Nodes in an existing
  cluster - AWS Management Console Help improve this page To contribute to this user
  guide, choose the Edit this page on GitHub link that is located in the right pane
  of every page. This topic provides an overview of the available options and describes
  what to consider when you add, change, or remove the hybrid nodes configuration
  for an Amazon EKS cluster.
summary: 'Enable hybrid nodes on an existing Amazon EKS cluster or modify configuration
  Prerequisites Considerations Enable hybrid nodes on an existing cluster Enable EKS
  Hybrid Nodes in an existing cluster - AWS CloudFormation Enable EKS Hybrid Nodes
  in an existing cluster - AWS CLI Enable EKS Hybrid Nodes in an existing cluster
  - AWS Management Console Update hybrid nodes configuration in an existing cluster
  Update hybrid configuration in an existing cluster - AWS CloudFormation Update hybrid
  configuration in an existing cluster - AWS CLI Update hybrid configuration in an
  existing cluster - AWS Management Console Disable Hybrid nodes in an existing cluster
  Disable EKS Hybrid Nodes in an existing cluster - AWS CloudFormation Disable EKS
  Hybrid Nodes in an existing cluster - AWS CLI Disable EKS Hybrid Nodes in an existing
  cluster - AWS Management Console Help improve this page To contribute to this user
  guide, choose the Edit this page on GitHub link that is located in the right pane
  of every page. This topic provides an overview of the available options and describes
  what to consider when you add, change, or remove the hybrid nodes configuration
  for an Amazon EKS cluster. To enable an Amazon EKS cluster to use hybrid nodes,
  add the IP address CIDR ranges of your on-premises node and optionally pod network
  in the RemoteNetworkConfig configuration. EKS uses this list of CIDRs to enable
  connectivity between the cluster and your on-premises networks. For a full list
  of options when updating your cluster configuration, see the UpdateClusterConfig
  in the Amazon EKS API Reference. RemoteNetworkConfig You can do any of the following
  actions to the EKS Hybrid Nodes networking configuration in a cluster: Add remote
  network configuration to enable EKS Hybrid Nodes in an existing cluster. Add remote
  network configuration to enable EKS Hybrid Nodes in an existing cluster. Add, change,
  or remove the remote node networks or the remote pod networks in an existing cluster.
  Remove all remote node network CIDR ranges to disable EKS Hybrid Nodes in an existing
  cluster. Before enabling your Amazon EKS cluster for hybrid nodes, ensure your environment
  meets the requirements outlined at Prerequisite setup for hybrid nodes , and detailed
  at Prepare networking for hybrid nodes , Prepare operating system for hybrid nodes
  , and Prepare credentials for hybrid nodes. Your cluster must use IPv4 address family.
  Your cluster must use either API or API_AND_CONFIG_MAP for the cluster authentication
  mode.'
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-cluster-update.html
