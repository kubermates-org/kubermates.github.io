---
title: 'Making Harbor Production-Ready: Essential Considerations for Deployment'
date: '2025-12-02T11:58:04+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/12/02/making-harbor-production-ready-essential-considerations-for-deployment/
post_kind: link
draft: false
tldr: 1. High Availability (HA) and Scalability 2.
summary: '1. High Availability (HA) and Scalability 2. Security Best Practices 3.
  Storage Considerations 4. Monitoring and Alerting 5. Network Configuration Conclusion
  Discover more from VMware Cloud Foundation (VCF) Blog Related Articles VCF Breakroom
  Chats Episode 75 - Breaking the GitOps Barrier: Continuous Delivery for Modern Apps
  with VCF 9 What’s Next for Cloud Native: Highlights from KubeCon North America 2025
  NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation 9 Part 3: Sizing
  for Success Harbor is an open-source container registry that secures artifacts with
  policies and role-based access control, ensuring images are scanned for vulnerabilities
  and signed as trusted. To learn more about Harbor and how to deploy it on a Virtual
  Machine (VM) and in Kubernetes (K8s), refer to parts 1 and 2 of the series. While
  deploying Harbor is straightforward, making it production-ready requires careful
  consideration of several key aspects. This blog outlines critical factors to ensure
  your Harbor instance is robust, secure, and scalable for production environments.
  For this blog, we will focus on upstream Harbor (v 2.14) deployed on Kubernetes
  via Helm as our base and provide suggestions for this specific deployment. For a
  production environment, single points of failure are unacceptable. This is especially
  true for image registries that acts as a central repository for storing and pulling
  images and artifacts.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/12/02/making-harbor-production-ready-essential-considerations-for-deployment/
