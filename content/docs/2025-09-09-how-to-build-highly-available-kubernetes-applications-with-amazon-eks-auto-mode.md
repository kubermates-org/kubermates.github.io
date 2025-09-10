---
title: How to build highly available Kubernetes applications with Amazon EKS Auto
  Mode
date: '2025-09-09T17:49:16+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/how-to-build-highly-available-kubernetes-applications-with-amazon-eks-auto-mode/
post_kind: link
draft: false
tldr: How to build highly available Kubernetes applications with Amazon EKS Auto Mode
  Solution overview Test scenarios Pod fail scenario Node fail scenario AZ fail scenario
  Cluster version upgrade scenario Karpenter node disruption Conclusion About the
  authors As organizations scale their Kubernetes deployments, many find themselves
  facing critical operational challenges. Consider how DevOps teams spend countless
  hours planning and executing cluster upgrades, managing add-ons, and making sure
  that security patches are applied consistently.
summary: How to build highly available Kubernetes applications with Amazon EKS Auto
  Mode Solution overview Test scenarios Pod fail scenario Node fail scenario AZ fail
  scenario Cluster version upgrade scenario Karpenter node disruption Conclusion About
  the authors As organizations scale their Kubernetes deployments, many find themselves
  facing critical operational challenges. Consider how DevOps teams spend countless
  hours planning and executing cluster upgrades, managing add-ons, and making sure
  that security patches are applied consistently. There is a clear need for reliable,
  automated cluster lifecycle management with teams struggling to maintain consistent
  cluster configurations and security postures across environments. Amazon Elastic
  Kubernetes Service (Amazon EKS) Auto Mode addresses these challenges by automating
  control plane updates, streamlining add-on management, and making sure that clusters
  maintain current best practices. This post explores the capabilities of EKS Auto
  Mode in depth, subjecting it to a series of challenging scenarios such as failure
  simulations, node recycling, and cluster upgrades—all while maintaining uninterrupted
  service traffic. This guide delves into strategies for achieving high availability
  in the face of the dynamic nature of EKS Auto Mode by using a range of Kubernetes
  features to maximize uptime. The goal is to provide a comprehensive guide that shows
  how to harness the potential of EKS Auto Mode, thus making sure that your services
  remain robust and resilient in the demanding environments. Although there is a wealth
  of comprehensive literature on the broader subject of reliability in container ecosystems,
  this post specifically narrows its scope to the nuanced considerations of operating
  reliable workloads within EKS Auto Mode environments. Before delving into the specifics
  of Amazon EKS and its Auto Mode feature , you must understand key Kubernetes concepts
  that are instrumental in maximizing service uptime during different cluster events.
  These foundational elements form the bedrock of resilient application architectures
  in Kubernetes environments, regardless of the specific cloud provider or management
  mode. Mastering these concepts enables you to use EKS Auto Mode effectively and
  build highly available systems that withstand various operational challenges. In
  the rest of this section we explore these essential Kubernetes features that play
  a pivotal role in maintaining service continuity during both planned and unplanned
  events.
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/how-to-build-highly-available-kubernetes-applications-with-amazon-eks-auto-mode/
