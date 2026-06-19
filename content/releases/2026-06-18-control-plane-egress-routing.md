---
title: Control plane egress routing
date: '2026-06-18T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/control-plane-egress.html
post_kind: release
draft: false
tldr: Configuring control plane egress routing Egress routing modes Prerequisites
  Create a cluster with customer-routed egress Update an existing cluster IPv6 considerations
  Considerations IAM condition key OIDC provider configuration Verify connectivity
  View a markdown version of this page Help improve this page To contribute to this
  user guide, choose the Edit this page on GitHub link that is located in the right
  pane of every page. By default, Amazon EKS manages the egress networking from the
  Kubernetes control plane to resources in your VPC.
summary: "Configuring control plane egress routing Egress routing modes Prerequisites\
  \ Create a cluster with customer-routed egress Update an existing cluster IPv6 considerations\
  \ Considerations IAM condition key OIDC provider configuration Verify connectivity\
  \ View a markdown version of this page Help improve this page To contribute to this\
  \ user guide, choose the Edit this page on GitHub link that is located in the right\
  \ pane of every page. By default, Amazon EKS manages the egress networking from\
  \ the Kubernetes control plane to resources in your VPC. Use control plane egress\
  \ routing to change this behavior and manage the network path yourself. This gives\
  \ you full control over how traffic from the control plane elastic network interfaces\
  \ (ENIs) reaches your VPC resources. You can route through your own NAT gateways,\
  \ firewalls, or inspection appliances. Amazon EKS supports the following control\
  \ plane egress routing modes: AWS_MANAGED AWS_MANAGED Default behavior. Amazon EKS\
  \ manages the egress path from the control plane ENIs. You donâ\x80\x99t need to\
  \ configure NAT gateways or other routing infrastructure for control plane traffic.\
  \ CUSTOMER_ROUTED CUSTOMER_ROUTED You manage the egress path from the control plane\
  \ in your VPC subnets. You are responsible for ensuring that the control plane can\
  \ reach required endpoints (such as webhook servers, OIDC providers, and other resources).\
  \ You provide an egress path, such as a NAT gateway, NAT instance, transit gateway,\
  \ or firewall appliance. You also configure the route table, network ACL, and security\
  \ group rules that allow this traffic."
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/control-plane-egress.html
