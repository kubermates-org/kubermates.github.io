---
title: Network observability
date: '2025-11-19T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/network-observability.html
post_kind: release
draft: false
tldr: Monitor Kubernetes workload traffic with Container Network Observability Use
  cases Measure network performance to detect anomalies Leverage console visualizations
  for more precise troubleshooting Track top-talkers in your Amazon EKS environment
  Features Get started Prerequisites and important notes Required IAM permissions
  Using Infrastructure as Code (IaC) Terraform How does it work? Performance metrics
  Service map and flow table Considerations and limitations Help improve this page
  To contribute to this user guide, choose the Edit this page on GitHub link that
  is located in the right pane of every page. Amazon EKS provides enhanced network
  observability features that provide deeper insights into your container networking
  environment.
summary: "Monitor Kubernetes workload traffic with Container Network Observability\
  \ Use cases Measure network performance to detect anomalies Leverage console visualizations\
  \ for more precise troubleshooting Track top-talkers in your Amazon EKS environment\
  \ Features Get started Prerequisites and important notes Required IAM permissions\
  \ Using Infrastructure as Code (IaC) Terraform How does it work? Performance metrics\
  \ Service map and flow table Considerations and limitations Help improve this page\
  \ To contribute to this user guide, choose the Edit this page on GitHub link that\
  \ is located in the right pane of every page. Amazon EKS provides enhanced network\
  \ observability features that provide deeper insights into your container networking\
  \ environment. These capabilities help you better understand, monitor, and troubleshoot\
  \ your Kubernetes network landscape in AWS. With enhanced container network observability,\
  \ you can leverage granular, network-related metrics for better proactive anomaly\
  \ detection across cluster traffic, cross-AZ flows, and AWS services. Using these\
  \ metrics, you can measure system performance and visualize the underlying metrics\
  \ using your preferred observability stack. In addition, Amazon EKS now provides\
  \ network monitoring visualizations in the AWS console that accelerate and enhance\
  \ precise troubleshooting for faster root cause analysis. You can also leverage\
  \ these visual capabilities to pinpoint top-talkers and network flows causing retransmissions\
  \ and retransmission timeouts, eliminating blind spots during incidents. These capabilities\
  \ are enabled by Amazon CloudWatch Network Flow Monitor. Several teams standardize\
  \ on an observability stack that allows them to measure their systemâ\x80\x99s performance,\
  \ visualize system metrics and be alarmed in the event that a specific threshold\
  \ is breached. Container network observability in EKS aligns with this by exposing\
  \ key system metrics that you can scrape to broaden observability of your systemâ\x80\
  \x99s network performance at the pod and worker node level. In the event of an alarm\
  \ from your monitoring system, you may want to hone in on the cluster and workload\
  \ where an issue originated from. To support this, you can leverage visualizations\
  \ in the EKS console that narrow the scope of investigation at a cluster level,\
  \ and accelerate the disclosure of the network flows responsible for the most retransmissions,\
  \ retransmission timeouts, and the volume of data transferred."
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/network-observability.html
