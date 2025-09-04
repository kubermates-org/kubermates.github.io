---
title: Dynamic Kubernetes request right sizing with Kubecost
date: '2025-09-03T18:52:27+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/dynamic-kubernetes-request-right-sizing-with-kubecost/
post_kind: link
draft: false
tldr: Dynamic Kubernetes request right sizing with Kubecost What are container requests?
  Kubecost savings insights Customizing recommendations Acting on Kubecost recommendations
  One-time resizing Scheduled right sizing Automating resizing with Helm Conclusion
  About the authors This post was co-written with Kai Wombacher, Founding Product
  Manager at Kubecost. In this post we show you how to use the Kubecost Amazon Elastic
  Kubernetes Service (Amazon EKS) add-on to lower infrastructure costs and boost Kubernetes
  efficiency.
summary: Dynamic Kubernetes request right sizing with Kubecost What are container
  requests? Kubecost savings insights Customizing recommendations Acting on Kubecost
  recommendations One-time resizing Scheduled right sizing Automating resizing with
  Helm Conclusion About the authors This post was co-written with Kai Wombacher, Founding
  Product Manager at Kubecost. In this post we show you how to use the Kubecost Amazon
  Elastic Kubernetes Service (Amazon EKS) add-on to lower infrastructure costs and
  boost Kubernetes efficiency. The Container Request Right Sizing feature allows you
  to find how container requests are configured, look for inefficiencies, and fix
  them either manually or through automated remediation. Specifically, we cover how
  to review Kubecost’s right sizing recommendations and take action on them using
  one-time updates or scheduled, automated resizing within your Amazon EKS environment
  to continuously optimize resource usage. Over-requested containers are one of the
  most common sources of cloud resource waste in Kubernetes environments. Without
  visibility and automation, development teams can request far more resources than
  their applications use, which leads to overprovisioned nodes and higher costs. In
  Kubernetes, a container request is a declared amount of CPU and memory that a workload
  needs. It plays a crucial role in how workloads are scheduled and how nodes are
  used. When a container specifies a CPU or memory request, the scheduler looks for
  a node that has at least that amount of unallocated capacity. When a pod is placed
  on a node, the requested resources are essentially reserved, regardless of whether
  the container uses them in practice. Although this reservation behavior makes sure
  that workloads have access to the resources they need, it can also lead to inefficient
  resource usage if requests are set too high. For example, if a container requests
  1 CPU but only uses 200 millicores (0.2 CPU), then that added 0.8 CPU goes unused,
  yet the node capacity is still reserved and charged for.
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/dynamic-kubernetes-request-right-sizing-with-kubecost/
