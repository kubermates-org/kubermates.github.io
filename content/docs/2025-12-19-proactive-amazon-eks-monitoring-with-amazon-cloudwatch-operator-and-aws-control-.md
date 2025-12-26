---
title: Proactive Amazon EKS monitoring with Amazon CloudWatch Operator and AWS Control
  Plane metrics
date: '2025-12-19T18:30:39+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/proactive-amazon-eks-monitoring-with-amazon-cloudwatch-operator-and-aws-control-plane-metrics/
post_kind: link
draft: false
tldr: Proactive Amazon EKS monitoring with Amazon CloudWatch Operator and AWS Control
  Plane metrics Understanding basic CloudWatch metrics Enhanced monitoring with CloudWatch
  Observability Operator Prerequisites Walkthrough Setup Installing and configuring
  the CloudWatch Observability Operator Basic CloudWatch metrics CloudWatch Container
  Insights CloudWatch Application Signals Create anomaly detection alerts for cluster
  Real-world monitoring scenarios Detecting scheduling issues Tracking API server
  performance Monitoring admission webhook health etcd storage monitoring Cleaning
  up Conclusion About the authors Organizations running Kubernetes workloads on Amazon
  Elastic Kubernetes Service (Amazon EKS) need comprehensive monitoring for optimal
  cluster performance and reliability. Although Amazon EKS manages the control plane,
  maintaining workload health requires monitoring capabilities.
summary: 'Proactive Amazon EKS monitoring with Amazon CloudWatch Operator and AWS
  Control Plane metrics Understanding basic CloudWatch metrics Enhanced monitoring
  with CloudWatch Observability Operator Prerequisites Walkthrough Setup Installing
  and configuring the CloudWatch Observability Operator Basic CloudWatch metrics CloudWatch
  Container Insights CloudWatch Application Signals Create anomaly detection alerts
  for cluster Real-world monitoring scenarios Detecting scheduling issues Tracking
  API server performance Monitoring admission webhook health etcd storage monitoring
  Cleaning up Conclusion About the authors Organizations running Kubernetes workloads
  on Amazon Elastic Kubernetes Service (Amazon EKS) need comprehensive monitoring
  for optimal cluster performance and reliability. Although Amazon EKS manages the
  control plane, maintaining workload health requires monitoring capabilities. This
  post explores using the Amazon CloudWatch monitoring, including new Amazon EKS metrics
  and the CloudWatch Observability Operator, to gain deeper visibility into cluster
  operations, detect issues, understand bottlenecks, and maintain healthy EKS clusters.
  Before Amazon EKS 1.28, control plane metrics were available only through the Kubernetes
  API server’s /metrics endpoint (Prometheus format). Amazon EKS 1.28+ automatically
  sends core Kubernetes control plane metrics to CloudWatch in the AWS/EKS namespace
  at no extra cost. These metrics are accessible through Amazon EKS console dashboards
  and CloudWatch. Key metric categories include the following: /metrics AWS/EKS API
  server metrics : Monitor API server health through total requests, HTTP 4XX/5XX
  errors, and throttling to detect bottlenecks or performance degradation. Scheduler
  metrics : Monitor pod scheduling attempts and pending pods ( active/backoff/gated/unschedulable
  queues) to detect scheduling bottlenecks, such as under-resourced worker nodes.
  active/backoff/gated/unschedulable etcd metrics : Monitor database size and performance
  to maintain a healthy etcd cluster. The following figure shows the architecture
  for viewing application and cluster metrics through CloudWatch Container Insights
  and the Amazon EKS console pre-built dashboards. Figure1: Architecture showing enhanced
  monitoring with CloudWatch Observability Operator for EKS clusters CloudWatch monitors
  cloud resources and applications. The CloudWatch Observability Operator, when added
  to Amazon EKS as an Amazon EKS add-on , automatically instruments applications using
  CloudWatch Application Signals and Container Insights.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/proactive-amazon-eks-monitoring-with-amazon-cloudwatch-operator-and-aws-control-plane-metrics/
