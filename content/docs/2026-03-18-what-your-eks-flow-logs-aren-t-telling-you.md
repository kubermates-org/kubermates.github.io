---
title: What Your EKS Flow Logs Aren’t Telling You
date: '2026-03-18T21:06:48+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/what-your-eks-flow-logs-arent-telling-you/
post_kind: link
draft: false
tldr: 'What EKS Gives You Out of the Box What EKS Native Observability Doesn’t Tell
  You What Calico Adds: Goldmane and Whisker Goldmane: Flow Logs That Speak Kubernetes
  Security Whisker: Real-Time Policy Visibility Without Additional Infrastructure
  Going Further: Calico Cloud Free Tier A Quick Comparison Sign up for the free tier
  Conclusion If you’re running workloads on Amazon EKS, there’s a good chance you
  already have some form of network observability in place. VPC Flow Logs have been
  a staple of AWS networking for years, and AWS has since introduced Container Network
  Observability, a newer set of capabilities built on Amazon CloudWatch Network Flow
  Monitor, that adds pod-level visibility and a service map directly in the EKS console.'
summary: 'What EKS Gives You Out of the Box What EKS Native Observability Doesn’t
  Tell You What Calico Adds: Goldmane and Whisker Goldmane: Flow Logs That Speak Kubernetes
  Security Whisker: Real-Time Policy Visibility Without Additional Infrastructure
  Going Further: Calico Cloud Free Tier A Quick Comparison Sign up for the free tier
  Conclusion If you’re running workloads on Amazon EKS, there’s a good chance you
  already have some form of network observability in place. VPC Flow Logs have been
  a staple of AWS networking for years, and AWS has since introduced Container Network
  Observability, a newer set of capabilities built on Amazon CloudWatch Network Flow
  Monitor, that adds pod-level visibility and a service map directly in the EKS console.
  It’s a reasonable assumption that between these tools, you have solid visibility
  into what’s happening on your cluster’s network. But for teams focused on Kubernetes
  security and policy enforcement , there’s a significant gap — and it’s not the one
  you might expect. In this post, we’ll break down exactly what EKS native observability
  gives you, where it falls short for security-focused use cases, and what Calico’s
  observability tools, Goldmane and Whisker, provide that you simply cannot get from
  AWS alone. AWS offers two main sources of network observability for EKS clusters:
  VPC Flow Logs capture IP traffic at the network interface level across your VPC.
  For each flow, you get source and destination IP addresses, ports, protocol, and
  whether traffic was accepted or rejected at the VPC level, by security groups and
  network ACLs. Useful for infrastructure-level visibility, but with no awareness
  of the Kubernetes layer. Container Network Observability, introduced more recently
  and powered by Amazon CloudWatch Network Flow Monitor, goes meaningfully further.
  Once you’ve installed the NFM agent as a DaemonSet and configured the required IAM
  permissions, Scope, and Monitor resources, you get access to: Performance metrics
  — pod and node-level metrics including ingress/egress flow counts, packet counts,
  bytes transferred, and bandwidth limit events, exposed in OpenMetrics format and
  scrapable by Prometheus A service map — a visualization of traffic between pods
  and deployments in the EKS console, showing retransmissions, retransmission timeouts,
  and data transferred between communicating workloads A flow table — a breakdown
  of top-talking workloads across three views: within the cluster (east-west), to
  AWS services (S3, DynamoDB), and to external destinations This is a genuinely capable
  performance observability tool. If your primary concern is understanding network
  throughput, identifying bandwidth hotspots, tracking cross-AZ traffic costs, or
  detecting retransmission anomalies, Container Network Observability gives you a
  solid foundation. But if your primary concern is Kubernetes network security , specifically
  understanding policy behavior, debugging denied connections, and moving toward a
  least-privilege posture, it leaves critical gaps.'
---
Open the original post ↗ https://www.tigera.io/blog/what-your-eks-flow-logs-arent-telling-you/
