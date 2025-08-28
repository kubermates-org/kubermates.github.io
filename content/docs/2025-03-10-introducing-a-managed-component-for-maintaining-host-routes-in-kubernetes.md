---
title: Introducing a Managed Component for Maintaining Host Routes in Kubernetes
date: '2025-03-10T19:39:28.335000+00:00'
tags:
- kubernetes
source: Digital Ocean
external_url: https://www.digitalocean.com/blog/introducing-doks-routing-agent
post_kind: link
draft: false
tldr: By Marco Jantke Our new DOKS routing agent is a managed component for configuring
  static routes on Kubernetes worker nodes. It is a direct response to user feedback
  on its predecessor, the static route operator, and introduces new features to enhance
  routing flexibility.
summary: "By Marco Jantke Our new DOKS routing agent is a managed component for configuring\
  \ static routes on Kubernetes worker nodes. It is a direct response to user feedback\
  \ on its predecessor, the static route operator, and introduces new features to\
  \ enhance routing flexibility. Despite being a managed component, the DOKS routing\
  \ agent is included at no additional cost for users. The DOKS routing agent enables\
  \ users to configure IP routes on their Kubernetes worker nodes using a dedicated\
  \ Kubernetes Custom Resource. This is particularly useful for VPN setups or tunneling\
  \ egress traffic through specific gateway nodes. The routing agent supports multiple\
  \ gateways and automatically configures ECMP (Equal-Cost Multi-Path) routing to\
  \ distribute traffic across them. How ECMP Works: The routing agent allows users\
  \ to override default routes without disrupting cluster connectivityâ\x80\x94one\
  \ of the most requested features. To prevent issues with Kubernetes components,\
  \ the routing agent ensures that essential control plane endpoints, metadata services,\
  \ and DNS servers maintain direct connectivity through the worker node Dropletâ\x80\
  \x99s default gateway. Routes can be applied to specific nodes using Kubernetes\
  \ label selectors, allowing for fine-grained control over network configurations.\
  \ The routing agent can be enabled or disabled using doctl or the DigitalOcean API.\
  \ For API users, the field structure is: With the DOKS routing agent and a self-managed\
  \ VPC gateway Droplet, users can configure static egress IPs, ensuring outbound\
  \ traffic from Kubernetes workloads originates from a predictable IP address. Weâ\x80\
  \x99re also working on a fully managed NAT gateway , which will offer a simpler\
  \ solution for achieving static egress IPs."
---
Open the original post ↗ https://www.digitalocean.com/blog/introducing-doks-routing-agent
