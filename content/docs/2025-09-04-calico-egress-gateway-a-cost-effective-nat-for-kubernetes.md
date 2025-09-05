---
title: 'Calico Egress Gateway: A Cost-Effective NAT for Kubernetes'
date: '2025-09-04T20:51:58+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/calico-egress-gateway-a-cost-effective-nat-for-kubernetes/
post_kind: link
draft: false
tldr: 'The Need for a Kubernetes NAT Gateway The Challenge With Cloud NAT Gateways
  Calico’s Built-in NAT for Kubernetes Egress How Calico Egress Gateway works as a
  NAT gateway – a simple example: Advantages of Calico Egress Gateway Used as a NAT
  Use Cases for Calico Egress Gateway and NAT Examples of Calico Egress Gateway in
  Action Preventing Data Exfiltration with Firewalls Enabling Trusted Access to Databases
  Behind a Firewall The Bottom Line When Kubernetes workloads need to connect to the
  outside world, whether to access external APIs, integrate with external systems,
  or connect to partner networks, they often face a unique challenge. The problem?
  Pod IP addresses inside Kubernetes clusters are dynamic and non-routable.'
summary: 'The Need for a Kubernetes NAT Gateway The Challenge With Cloud NAT Gateways
  Calico’s Built-in NAT for Kubernetes Egress How Calico Egress Gateway works as a
  NAT gateway – a simple example: Advantages of Calico Egress Gateway Used as a NAT
  Use Cases for Calico Egress Gateway and NAT Examples of Calico Egress Gateway in
  Action Preventing Data Exfiltration with Firewalls Enabling Trusted Access to Databases
  Behind a Firewall The Bottom Line When Kubernetes workloads need to connect to the
  outside world, whether to access external APIs, integrate with external systems,
  or connect to partner networks, they often face a unique challenge. The problem?
  Pod IP addresses inside Kubernetes clusters are dynamic and non-routable. For external
  systems to recognize and trust this traffic, workloads need a consistent, dependable
  identity. This means outbound connections require fixed, routable IP addresses that
  external services can rely on. This is where Network Address Translation (NAT) becomes
  essential. It assigns Kubernetes pods with a static, consistent IP for all outbound
  traffic, ensuring those connections work properly. If you’re running Kubernetes
  in the cloud, a common solution is to use your cloud provider’s managed NAT gateway
  service. These are easy to use, but they can come at a cost. In AWS, Azure, and
  Google Cloud, cloud-managed NAT gateways charge both an hourly fee and a per-gigabyte
  data processing fee. For high-traffic deployments, those charges can quickly add
  up, sometimes even exceeding your compute costs. The good news: with Calico, you
  can handle NAT from inside your Kubernetes cluster, avoiding cloud NAT gateway fees
  and giving you more control over how egress works. Managed NAT gateways from cloud
  providers are designed for convenience, but they come with a few limitations: Ongoing
  hourly charges – even if you’re not sending much traffic.'
---
Open the original post ↗ https://www.tigera.io/blog/calico-egress-gateway-a-cost-effective-nat-for-kubernetes/
