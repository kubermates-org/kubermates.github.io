---
title: EFA support for static capacity in EKS Auto Mode
date: '2026-07-21T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/create-node-class.html#static-network-interfaces
post_kind: release
draft: false
tldr: 'Create a Node Class for Amazon EKS Create a Node Class Basic Node Class Example
  Create node class access entry Create access entry with CLI Create access entry
  with CloudFormation Node Class Specification Considerations Separate subnets and
  security groups for Pods How it works Use cases Example configuration Considerations
  for separate Pod subnets and security groups Secondary IP Mode for Pods Use cases
  Example configuration Considerations for secondary IP mode Disable IPv4 egress from
  IPv6 pods in IPv6 clusters. Use cases Example configuration Considerations for disabling
  enableV4Egress Static Network Interface Configuration How it works Considerations
  Example: EFA-only interfaces for GPU training View a markdown version of this page
  Help improve this page To contribute to this user guide, choose the Edit this page
  on GitHub link that is located in the right pane of every page.'
summary: 'Create a Node Class for Amazon EKS Create a Node Class Basic Node Class
  Example Create node class access entry Create access entry with CLI Create access
  entry with CloudFormation Node Class Specification Considerations Separate subnets
  and security groups for Pods How it works Use cases Example configuration Considerations
  for separate Pod subnets and security groups Secondary IP Mode for Pods Use cases
  Example configuration Considerations for secondary IP mode Disable IPv4 egress from
  IPv6 pods in IPv6 clusters. Use cases Example configuration Considerations for disabling
  enableV4Egress Static Network Interface Configuration How it works Considerations
  Example: EFA-only interfaces for GPU training View a markdown version of this page
  Help improve this page To contribute to this user guide, choose the Edit this page
  on GitHub link that is located in the right pane of every page. Amazon EKS Node
  Classes are templates that offer granular control over the configuration of your
  EKS Auto Mode managed nodes. A Node Class defines infrastructure-level settings
  that apply to groups of nodes in your EKS cluster, including network configuration,
  storage settings, and resource tagging. This topic explains how to create and configure
  a Node Class to meet your specific operational requirements. When you need to customize
  how EKS Auto Mode provisions and configures EC2 instances beyond the default settings,
  creating a Node Class gives you precise control over critical infrastructure parameters.
  For example, you can specify private subnet placement for enhanced security, configure
  instance ephemeral storage for performance-sensitive workloads, or apply custom
  tagging for cost allocation. To create a NodeClass , follow these steps: NodeClass
  Create a YAML file (for example, nodeclass. yaml ) with your Node Class configuration
  Create a YAML file (for example, nodeclass. yaml ) with your Node Class configuration
  nodeclass. yaml Apply the configuration to your cluster using kubectl Apply the
  configuration to your cluster using kubectl kubectl Reference the Node Class in
  your Node Pool configuration. For more information, see Create a Node Pool for EKS
  Auto Mode.'
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/create-node-class.html#static-network-interfaces
