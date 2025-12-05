---
title: Amazon EKS introduces Provisioned Control Plane
date: '2025-11-27T00:32:32+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/amazon-eks-introduces-provisioned-control-plane/
post_kind: link
draft: false
tldr: Amazon EKS introduces Provisioned Control Plane Delivering predictable and high
  performance at scale How did we unlock this? Getting started with Provisioned Control
  Plane Creating a cluster with Provisioned Control Plane Updating control plane scaling
  tier Monitoring control plane scaling tier utilization Benchmarking with Provisioned
  Control Plane Conclusion About the authors Amazon Elastic Kubernetes Service (Amazon
  EKS) powers tens of millions of clusters annually, with an architecture refined
  by years of real-world insights from thousands of customers running diverse workloads.
  EKS automatically scales your cluster’s control plane to meet your workload demands.
summary: 'Amazon EKS introduces Provisioned Control Plane Delivering predictable and
  high performance at scale How did we unlock this? Getting started with Provisioned
  Control Plane Creating a cluster with Provisioned Control Plane Updating control
  plane scaling tier Monitoring control plane scaling tier utilization Benchmarking
  with Provisioned Control Plane Conclusion About the authors Amazon Elastic Kubernetes
  Service (Amazon EKS) powers tens of millions of clusters annually, with an architecture
  refined by years of real-world insights from thousands of customers running diverse
  workloads. EKS automatically scales your cluster’s control plane to meet your workload
  demands. This dynamic, intelligent scaling powers most use cases, handling everything
  from startup applications to enterprise platforms to mission critical workloads.
  Building on this proven architecture, we’re introducing capabilities designed for
  next-generation workloads with specialized requirements. When you’re running AI
  training or inference workloads at ultra scale, running multi-tenant SaaS platforms,
  or running mission-critical web applications where every second matters, you need
  absolute predictability – the ability to guarantee control plane responsiveness
  before peak demand arrives. To meet these advanced requirements, we’re introducing
  EKS Provisioned Control Plane, an enhanced option that complements the Standard
  Control Plane capabilities. Amazon EKS Provisioned Control Plane gives you the ability
  to pre-allocate control plane capacity from a set of new scaling tiers, ensuring
  predictable and high performance for your most demanding workloads. By provisioning
  capacity ahead of time, your cluster handles instantaneous traffic bursts without
  the need for control plane scaling, which is crucial for serving traffic during
  high-demand events or sudden workload spikes. These new scaling tiers unlock significantly
  higher control plane performance and scalability required for emerging workload
  patterns like ultra scale AI training/inference, high performance computing, or
  large-scale data processing. Provisioned Control Plane allows you to choose from
  multiple control plane scaling tiers (XL, 2XL, 4XL) with each tier offering well
  defined performance on these Kubernetes attributes: API request concurrency – the
  volume of requests processed by the Kubernetes API servers concurrently Pod scheduling
  rate – the throughput at which the Kubernetes default scheduler assigns pods to
  nodes Cluster database size – the storage space allocated to etcd, the database
  that holds the cluster state/metadata Once you designate a scaling tier to your
  cluster, EKS ensures sufficient capacity is always available to the control plane
  to meet the attribute values for that tier. You also get comprehensive visibility
  into your tier utilization through granular metrics for each attribute, available
  through both the EKS Prometheus metrics endpoint and Amazon CloudWatch metrics vended
  to your account. As your workload demands evolve, you can switch between scaling
  tiers or go back to the standard control plane at any time.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/amazon-eks-introduces-provisioned-control-plane/
