---
title: Simplify network connectivity using Tailscale with Amazon EKS Hybrid Nodes
date: '2025-08-06T22:12:21+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/simplify-network-connectivity-using-tailscale-with-amazon-eks-hybrid-nodes/
post_kind: link
draft: false
tldr: This post was co-authored with Lee Briggs, Director of Solutions Engineering
  at Tailscale. In this post, we guide you through integrating Tailscale with your
  Amazon Elastic Kubernetes Service (EKS) Hybrid Nodes environment.
summary: This post was co-authored with Lee Briggs, Director of Solutions Engineering
  at Tailscale. In this post, we guide you through integrating Tailscale with your
  Amazon Elastic Kubernetes Service (EKS) Hybrid Nodes environment. Amazon EKS Hybrid
  Nodes is a feature of Amazon EKS that enables you to streamline your Kubernetes
  management by connecting on-premises and edge infrastructure to an EKS cluster running
  in Amazon Web Services (AWS). This unified approach allows AWS to manage the Kubernetes
  control plane in the cloud while you maintain your hybrid nodes in on-premises or
  edge locations. We demonstrate how to configure a remote pod network and node address
  space. Install Tailscale on your hybrid nodes, set up a subnet router within your
  Amazon Virtual Private Cloud (Amazon VPC) , and update your AWS routes accordingly.
  This integration provides direct, encrypted connections that streamline the network
  architecture needed for EKS Hybrid Nodes. Although EKS Hybrid Nodes streamlines
  the Kubernetes management challenge, network connectivity between your on-premises
  infrastructure and AWS remains a critical requirement. Tailscale can help streamline
  this network connectivity between your EKS Hybrid Nodes data plane and Amazon EKS
  Kubernetes control plane. Unlike traditional VPNs, which tunnel all network traffic
  through a central gateway server, Tailscale creates a peer-to-peer mesh network
  (known as a tailnet ). It enables encrypted point-to-point connections using the
  open source WireGuard protocol, connecting devices and services across different
  networks with enhanced security features. However, you can still use Tailscale like
  a traditional VPN.
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/simplify-network-connectivity-using-tailscale-with-amazon-eks-hybrid-nodes/
