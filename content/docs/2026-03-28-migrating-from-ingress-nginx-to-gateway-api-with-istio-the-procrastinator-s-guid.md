---
title: Migrating from Ingress NGINX to Gateway API with Istio – The Procrastinator’s
  Guide
date: '2026-03-28T17:40:22+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/03/28/ingress-nginx-to-gateway-api-istio-vks-migration/
post_kind: link
draft: false
tldr: 'Why You’re Reading This (and Why It’s Not Too Late) What Changed Before: Ingress
  NGINX After: Gateway API + Istio TLS: Automatic with cert-manager The Helm Chart:
  Backward-Compatible Toggle Step by Step: How I Applied the Migration 1. Install
  Prerequisites 2.'
summary: 'Why You’re Reading This (and Why It’s Not Too Late) What Changed Before:
  Ingress NGINX After: Gateway API + Istio TLS: Automatic with cert-manager The Helm
  Chart: Backward-Compatible Toggle Step by Step: How I Applied the Migration 1. Install
  Prerequisites 2. Fix Pod Security Admission 3. Helm Upgrade (cluster-01) 4. ArgoCD
  Sync (cluster-02) 5. Update DNS The Result Gotchas and Lessons Learned (the Time-Savers)
  File Changes Summary The Bottom Line: Can You Really Do This in One Day? What’s
  Next Discover more from VMware Cloud Foundation (VCF) Blog Related Articles Applying
  GitOps Principles to Maintain Desired State Configuration using VMware vSphere Configuration
  Profile - Part 3 Accelerate Database as a Service with new VMware Data Services
  Manager Proof of Value Service from AxelCore Announcing the i7i. metal-24xl Instance
  for VMware Cloud on AWS The deadline: March 31, 2026 — three days from now. The
  situation: Ingress NGINX stops receiving security patches forever. The reality:
  You’re still running it in production. In November 2025, the Kubernetes project
  announced Ingress NGINX’s retirement. If you waited until the last minute, you’re
  not alone; migration activity spiked 300% in February-March 2026 as teams raced
  to beat the deadline. I migrated a multi-app demo suite (Bookstore, Reader, Chatbot)
  across two VMware vSphere Kubernetes Service (VKS) clusters with zero downtime in
  under 8 hours.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/03/28/ingress-nginx-to-gateway-api-istio-vks-migration/
