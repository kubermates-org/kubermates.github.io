---
title: Running containerized hybrid nodes with Amazon Elastic Kubernetes Service
date: '2026-02-24T16:50:36+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/running-containerized-hybrid-nodes-with-amazon-elastic-kubernetes-service/
post_kind: link
draft: false
tldr: Running containerized hybrid nodes with Amazon Elastic Kubernetes Service Prerequisites
  Bootstrapping the container entrypoint. sh and hybrid-node-setup.
summary: Running containerized hybrid nodes with Amazon Elastic Kubernetes Service
  Prerequisites Bootstrapping the container entrypoint. sh and hybrid-node-setup.
  sh scripts Establishing network connectivity with Tailscale Setting up the Tailscale
  VPN Installing and configuring the Cilium CNI Configuring the EKS remote network
  Configuring a containerized hybrid node Docker setup Example application Troubleshooting
  Additional troubleshooting steps Cleanup Summary About the authors EKS hybrid nodes
  is a feature of Amazon Elastic Kubernetes Service (EKS) that allows you to use an
  EKS managed control plane with worker nodes that reside outside of the AWS cloud.
  Starting a small Proof of Concept (PoC) with hybrid nodes can be challenging because
  hybrid nodes require network connectivity between the remote network (where you’re
  deploying your worker nodes) and the cluster Virtual Private Cloud (VPC). Additionally,
  you may have trouble finding enough physical hardware or virtual machines to adequately
  test hybrid nodes. To address these challenges, we created the containerized hybrid
  nodes project. The project is a proof of concept that allows you to quickly run
  a hybrid node as a container on a modestly equipped laptop. Connectivity between
  the remote network, i. e. your laptop, and the cluster VPC is established through
  a Tailscale network. For now, think of the Tailscale network as an encrypted peer
  to peer mesh network. Once network connectivity is established, you can run a containerized
  hybrid node and begin scheduling workloads onto it.
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/running-containerized-hybrid-nodes-with-amazon-elastic-kubernetes-service/
