---
title: Announcing Gateway API Support for DigitalOcean Kubernetes
date: '2025-09-09T21:28:56.259000+00:00'
tags:
- kubernetes
source: Digital Ocean
external_url: https://www.digitalocean.com/blog/introducing-managed-gateway-api
post_kind: link
draft: false
tldr: "Announcing Gateway API Support for DigitalOcean Kubernetes Key Benefits Why\
  \ Move Beyond Ingress? The Gateway API Advantage The DigitalOcean Difference: Performance\
  \ Powered by Cilium and eBPF Pricing Try the Gateway API on DOKS About the author\
  \ Try DigitalOcean for free Related Articles What's New on DigitalOcean App Platform\
  \ Single Sign-On is Now Available, Strengthening Security and Simplifying Authentication\
  \ Announcing OpenAI gpt-oss Models on the DigitalOcean Gradientâ\x84¢ AI Platform\
  \ By Kang Xie Senior Product Manager Published: September 9, 2025 3 min read Managing\
  \ traffic into a DigitalOcean Kubernetes cluster has long been the domain of the\
  \ Ingress. While functional, it comes with limitations in flexibility, role separation,\
  \ and advanced routing."
summary: "Announcing Gateway API Support for DigitalOcean Kubernetes Key Benefits\
  \ Why Move Beyond Ingress? The Gateway API Advantage The DigitalOcean Difference:\
  \ Performance Powered by Cilium and eBPF Pricing Try the Gateway API on DOKS About\
  \ the author Try DigitalOcean for free Related Articles What's New on DigitalOcean\
  \ App Platform Single Sign-On is Now Available, Strengthening Security and Simplifying\
  \ Authentication Announcing OpenAI gpt-oss Models on the DigitalOcean Gradientâ\x84\
  ¢ AI Platform By Kang Xie Senior Product Manager Published: September 9, 2025 3\
  \ min read Managing traffic into a DigitalOcean Kubernetes cluster has long been\
  \ the domain of the Ingress. While functional, it comes with limitations in flexibility,\
  \ role separation, and advanced routing. Today, weâ\x80\x99re excited to change\
  \ that. We are thrilled to announce that the Kubernetes Gateway API, as a managed\
  \ service, is pre-installed in all DigitalOcean Kubernetes (DOKS) clusters and ready\
  \ to use at no additional cost. This next-generation traffic management solution\
  \ is more expressive, extensible, and powerful than Ingress. Best of all, itâ\x80\
  \x99s powered by Ciliumâ\x80\x99s high-performance eBPF implementation, offering\
  \ superior performance and advanced routing capabilities without the overhead of\
  \ traditional proxy-based solutions. Zero Configuration Required : Gateway API support\
  \ comes pre-installed via Cilium in all DOKS clusters Zero Configuration Required\
  \ : Gateway API support comes pre-installed via Cilium in all DOKS clusters Advanced\
  \ Traffic Management : Support for header-based routing, traffic splitting, and\
  \ canary deployments Advanced Traffic Management : Support for header-based routing,\
  \ traffic splitting, and canary deployments Superior Performance : Ciliumâ\x80\x99\
  s eBPF implementation operates in kernel space, eliminating proxy overhead Superior\
  \ Performance : Ciliumâ\x80\x99s eBPF implementation operates in kernel space, eliminating\
  \ proxy overhead Native Load Balancer Integration : Seamless integration with DigitalOcean\
  \ Network Load Balancers Native Load Balancer Integration : Seamless integration\
  \ with DigitalOcean Network Load Balancers Multi-tenant Ready : Built-in support\
  \ for cross-namespace resource sharing with secure RBAC Multi-tenant Ready : Built-in\
  \ support for cross-namespace resource sharing with secure RBAC Future-Proof API\
  \ : Active development and standardization by the Kubernetes community Future-Proof\
  \ API : Active development and standardization by the Kubernetes community The Gateway\
  \ API was designed by the Kubernetes community to address the fundamental limitations\
  \ of the Ingress API. It achieves this through a role-oriented resource model that\
  \ separates infrastructure concerns from application routing. Cluster Operators\
  \ manage Gateway resources, defining where and how traffic enters the cluster (e.\
  \ g. , provisioning a DigitalOcean Load Balancer). Application Developers manage\
  \ Route resources (like HTTPRoute), defining how traffic is routed to their specific\
  \ applications."
---
Open the original post ↗ https://www.digitalocean.com/blog/introducing-managed-gateway-api
