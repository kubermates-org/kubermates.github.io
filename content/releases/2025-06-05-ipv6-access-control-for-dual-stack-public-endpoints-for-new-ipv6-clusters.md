---
title: IPv6 access control for dual-stack public endpoints for new IPv6 clusters
date: '2025-06-05T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html
post_kind: release
draft: false
tldr: "Help improve this page To contribute to this user guide, choose the Edit this\
  \ page on GitHub link that is located in the right pane of every page. This topic\
  \ helps you to enable private access for your Amazon EKS clusterâ\x80\x99s Kubernetes\
  \ API server endpoint and limit, or completely disable, public access from the internet."
summary: "Help improve this page To contribute to this user guide, choose the Edit\
  \ this page on GitHub link that is located in the right pane of every page. This\
  \ topic helps you to enable private access for your Amazon EKS clusterâ\x80\x99\
  s Kubernetes API server endpoint and limit, or completely disable, public access\
  \ from the internet. When you create a new cluster, Amazon EKS creates an endpoint\
  \ for the managed Kubernetes API server that you use to communicate with your cluster\
  \ (using Kubernetes management tools such as kubectl ). By default, this API server\
  \ endpoint is public to the internet, and access to the API server is secured using\
  \ a combination of AWS Identity and Access Management (IAM) and native Kubernetes\
  \ Role Based Access Control (RBAC). This endpoint is known as the cluster public\
  \ endpoint. Also there is a cluster private endpoint. For more information about\
  \ the cluster private endpoint, see the following section Cluster private endpoint.\
  \ EKS creates a unique dual-stack endpoint in the following format for new IPv6\
  \ clusters that are made after October 2024. An IPv6 cluster is a cluster that you\
  \ select IPv6 in the IP family ( ipFamily ) setting of the cluster. EKS cluster\
  \ public/private endpoint: eks-cluster. region. api."
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html
