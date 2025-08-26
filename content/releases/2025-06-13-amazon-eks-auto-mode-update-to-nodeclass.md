---
title: Amazon EKS Auto Mode update to NodeClass
date: '2025-06-13T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/create-node-class.html#auto-node-class-spec
post_kind: release
draft: false
tldr: Help improve this page To contribute to this user guide, choose the Edit this
  page on GitHub link that is located in the right pane of every page. Amazon EKS
  Node Classes are templates that offer granular control over the configuration of
  your EKS Auto Mode managed nodes.
summary: "Help improve this page To contribute to this user guide, choose the Edit\
  \ this page on GitHub link that is located in the right pane of every page. Amazon\
  \ EKS Node Classes are templates that offer granular control over the configuration\
  \ of your EKS Auto Mode managed nodes. A Node Class defines infrastructure-level\
  \ settings that apply to groups of nodes in your EKS cluster, including network\
  \ configuration, storage settings, and resource tagging. This topic explains how\
  \ to create and configure a Node Class to meet your specific operational requirements.\
  \ When you need to customize how EKS Auto Mode provisions and configures EC2 instances\
  \ beyond the default settings, creating a Node Class gives you precise control over\
  \ critical infrastructure parameters. For example, you can specify private subnet\
  \ placement for enhanced security, configure instance ephemeral storage for performance-sensitive\
  \ workloads, or apply custom tagging for cost allocation. To create a NodeClass\
  \ , follow these steps: Create a YAML file (for example, nodeclass. yaml ) with\
  \ your Node Class configuration Apply the configuration to your cluster using kubectl\
  \ Reference the Node Class in your Node Pool configuration. For more information,\
  \ see Create a Node Pool for EKS Auto Mode. You need kubectl installed and configured.\
  \ For more information, see Set up to use Amazon EKS. Hereâ\x80\x99s an example\
  \ Node Class: This NodeClass increases the amount of ephemeral storage on the node."
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/create-node-class.html#auto-node-class-spec
