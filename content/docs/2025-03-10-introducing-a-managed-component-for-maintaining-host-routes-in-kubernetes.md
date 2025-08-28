---
title: Introducing a Managed Component for Maintaining Host Routes in Kubernetes
date: '2025-03-10T19:39:28.335000+00:00'
tags:
- kubernetes
source: Digital Ocean
external_url: https://www.digitalocean.com/blog/introducing-doks-routing-agent
post_kind: link
draft: false
tldr: Introducing a Managed Component for Maintaining Host Routes in Kubernetes Key
  Features of the DOKS Routing Agent 1. Static Route Management via Custom Resources
  2.
summary: "Introducing a Managed Component for Maintaining Host Routes in Kubernetes\
  \ Key Features of the DOKS Routing Agent 1. Static Route Management via Custom Resources\
  \ 2. Support for Multiple Gateways and ECMP 3. Overriding Default Routes 4. Node\
  \ Selection for Routes Enabling the DOKS Routing Agent Example Commands: Usage for\
  \ Static Egress IP Why This Matters: Coming Soon: Fully Managed NAT Gateway Simplify\
  \ Static Route Management Get started today About the author Try DigitalOcean for\
  \ free Related Articles Stop Building SaaS from Scratch: Meet the SeaNotes Starter\
  \ Kit Announcing OpenAI gpt-oss Models on the DigitalOcean Gradientâ\x84¢ AI Platform\
  \ Introducing langchain-gradient: Seamless LangChain Integration with DigitalOcean\
  \ Gradientâ\x84¢ AI Platform By Marco Jantke Published: March 10, 2025 3 min read\
  \ Our new DOKS routing agent is a managed component for configuring static routes\
  \ on Kubernetes worker nodes. It is a direct response to user feedback on its predecessor,\
  \ the static route operator, and introduces new features to enhance routing flexibility.\
  \ Despite being a managed component, the DOKS routing agent is included at no additional\
  \ cost for users. The DOKS routing agent enables users to configure IP routes on\
  \ their Kubernetes worker nodes using a dedicated Kubernetes Custom Resource. This\
  \ is particularly useful for VPN setups or tunneling egress traffic through specific\
  \ gateway nodes. apiVersion : networking. doks. digitalocean."
---
Open the original post ↗ https://www.digitalocean.com/blog/introducing-doks-routing-agent
