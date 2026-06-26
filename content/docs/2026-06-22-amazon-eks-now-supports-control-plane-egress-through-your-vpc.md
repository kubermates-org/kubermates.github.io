---
title: Amazon EKS now supports control plane egress through your VPC
date: '2026-06-22T16:20:28+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc/
post_kind: link
draft: false
tldr: 'Amazon EKS now supports control plane egress through your VPC Who this is for
  and why it matters How it works Layering with private cluster endpoints Getting
  started with Amazon EKS customer-routed control plane egress Enforcing customer-routed
  control plane egress across your organization Example scenarios Scenario 1: Routing
  admission webhook traffic through your VPC Scenario 2: Private reachability for
  an external OIDC identity provider Considerations Now available About the authors
  Today, we’re announcing customer-routed control plane egress , a new capability
  that you can use to route Kubernetes control plane traffic through your own Amazon
  Virtual Private Cloud (Amazon VPC). This includes admission webhook callbacks, OpenID
  Connect (OIDC) provider lookups, and aggregate API server requests.'
summary: 'Amazon EKS now supports control plane egress through your VPC Who this is
  for and why it matters How it works Layering with private cluster endpoints Getting
  started with Amazon EKS customer-routed control plane egress Enforcing customer-routed
  control plane egress across your organization Example scenarios Scenario 1: Routing
  admission webhook traffic through your VPC Scenario 2: Private reachability for
  an external OIDC identity provider Considerations Now available About the authors
  Today, we’re announcing customer-routed control plane egress , a new capability
  that you can use to route Kubernetes control plane traffic through your own Amazon
  Virtual Private Cloud (Amazon VPC). This includes admission webhook callbacks, OpenID
  Connect (OIDC) provider lookups, and aggregate API server requests. With this feature,
  you can apply the same VPC routing, security group, endpoint policy, and AWS Network
  Firewall controls that you use for your data plane to the Kubernetes API Server’s
  customer-controllable outbound traffic on Amazon Elastic Kubernetes Service (Amazon
  EKS) clusters. By default, traffic from the Kubernetes API Server leaves the cluster
  through that EKS-managed Control Plane. That traffic includes calls to validating
  and mutating admission webhooks, fetches of OIDC discovery documents, and proxied
  requests to aggregate API servers. Customers in regulated industries asked for a
  way to apply their own VPC egress controls to that path, so the policies that govern
  their workloads also govern the traffic that Kubernetes API Server initiates. Customer-routed
  control plane egress gives you that control. When you create or update an existing
  cluster with this feature enabled, the Kubernetes API Server’s egress flows through
  an Elastic Network Interface (ENI) in your VPC. You configure how that traffic reaches
  its destination using the routing, security groups, VPC endpoints, and AWS PrivateLink
  connections you already manage. Customer-routed control plane egress is built for
  organizations that need verifiable controls over how customer-driven control plane
  traffic routes through their network. This includes government agencies operating
  in regulated environments and highly regulated commercial organizations, such as
  financial services firms, healthcare providers, and enterprises that must demonstrate
  where their Kubernetes control plane traffic goes. During early development, customers
  told us they value two things most: complete control over where customer-driven
  Kubernetes control plane traffic routes through their VPC, and the ability to enforce
  that routing organization-wide through AWS Organizations Service Control Policies.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc/
