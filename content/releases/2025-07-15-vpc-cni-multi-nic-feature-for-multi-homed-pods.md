---
title: VPC CNI Multi-NIC feature for multi-homed pods
date: '2025-07-15T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/pod-multiple-network-interfaces.html
post_kind: release
draft: false
tldr: Help improve this page To contribute to this user guide, choose the Edit this
  page on GitHub link that is located in the right pane of every page. By default,
  the Amazon VPC CNI plugin assigns one IP address to each pod.
summary: "Help improve this page To contribute to this user guide, choose the Edit\
  \ this page on GitHub link that is located in the right pane of every page. By default,\
  \ the Amazon VPC CNI plugin assigns one IP address to each pod. This IP address\
  \ is attached to an elastic network interface that handles all incoming and outgoing\
  \ traffic for the pod. To increase the bandwidth and packet per second rate performance,\
  \ you can use the Multi-NIC feature of the VPC CNI to configure a multi-homed pod.\
  \ A multi-homed pod is a single Kubernetes pod that uses multiple network interfaces\
  \ (and multiple IP addresses). By running a multi-homed pod, you can spread its\
  \ application traffic across multiple network interfaces by using concurrent connections.\
  \ This is especially useful for Artificial Intelligence (AI), Machine Learning (ML),\
  \ and High Performance Computing (HPC) use cases. The following diagram shows a\
  \ multi-homed pod running on a worker node with multiple network interface cards\
  \ (NICs) in use. On Amazon EC2, an elastic network interface is a logical networking\
  \ component in a VPC that represents a virtual network card. For many EC2 instance\
  \ types, the network interfaces share a single network interface card (NIC) in hardware.\
  \ This single NIC has a maximum bandwidth and packet per second rate. If the multi-NIC\
  \ feature is enabled, the VPC CNI doesnâ\x80\x99t assign IP addresses in bulk, which\
  \ it does by default."
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/pod-multiple-network-interfaces.html
