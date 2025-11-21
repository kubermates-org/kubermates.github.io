---
title: Monitoring network performance on Amazon EKS using AWS Managed Open-Source
  Services
date: '2025-11-20T18:48:46+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/monitoring-network-performance-on-amazon-eks-using-aws-managed-open-source-services/
post_kind: link
draft: false
tldr: 'Monitoring network performance on Amazon EKS using AWS Managed Open-Source
  Services Architecture diagram Walkthrough Prerequisites Setup Network performance
  testing and visualization: Key considerations Managing dashboards and data sources
  with Grafana Operator Using ADOT for telemetry collection Cleanup Conclusion About
  the authors As organizations scale their microservices architectures on Amazon Elastic
  Kubernetes Service (Amazon EKS) , platform and development teams face mounting challenges
  in monitoring network performance across distributed workloads. While VPC Flow Logs
  provide visibility into IP traffic, they lack the Kubernetes context needed to correlate
  network flows to specific pods, services, and namespaces.'
summary: 'Monitoring network performance on Amazon EKS using AWS Managed Open-Source
  Services Architecture diagram Walkthrough Prerequisites Setup Network performance
  testing and visualization: Key considerations Managing dashboards and data sources
  with Grafana Operator Using ADOT for telemetry collection Cleanup Conclusion About
  the authors As organizations scale their microservices architectures on Amazon Elastic
  Kubernetes Service (Amazon EKS) , platform and development teams face mounting challenges
  in monitoring network performance across distributed workloads. While VPC Flow Logs
  provide visibility into IP traffic, they lack the Kubernetes context needed to correlate
  network flows to specific pods, services, and namespaces. This makes it difficult
  to diagnose connectivity issues, identify packet drops, or investigate security
  incidents. Platform teams struggle to answer critical questions such as: “ Which
  services are communicating with each other? Where are the latency bottlenecks? Are
  there any security policy violations?” Without Kubernetes-enriched network telemetry
  integrated into their observability and Security information and event management
  (SIEM) systems, teams spend excessive time troubleshooting network-related issues
  and lack the real-time visibility needed to ensure optimal performance and security
  across their EKS environments. In this post, we will discuss how to monitor the
  network performance of your workloads running in Amazon EKS clusters using new advanced
  network observability features which are a part of Container Network Observability
  in EKS. This includes capturing network performance metrics and exporting them to
  AWS Managed Open-Source services such as Amazon Managed Service for Prometheus ,
  Amazon Managed Grafana , etc. You can leverage the same approach to integrate with
  third-party observability solutions such as Datadog, New Relic, etc. , or self-managed
  open-source tools like Prometheus. Amazon EKS introduced new advanced network observability
  features that give you the ability to dynamically visualize and quickly understand
  the landscape, performance and security of the network environment of your Kubernetes
  clusters. At a cluster level, it provides you with a Service Map that depicts end-to-end
  visibility of network traffic flows for workloads in the cluster (east ↔ west traffic).
  Alongside this, you can access Network Flow Analysis which provide more granular
  information around application network activity and the network security posture
  for your workloads. Additionally, you can export Kubernetes-enriched network performance
  metrics from all your EKS clusters to be analyzed in your preferred monitoring solution
  or SIEM.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/monitoring-network-performance-on-amazon-eks-using-aws-managed-open-source-services/
