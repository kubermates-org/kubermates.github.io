---
title: Integrating VMware Data Services Manager with Harbor for a Production-Ready
  Registry
date: '2025-12-09T07:37:13+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/12/08/integrating-vmware-data-services-manager-with-harbor-for-a-production-ready-registry/
post_kind: link
draft: false
tldr: 'The Solution: Leveraging VMware Data Services Manager with Harbor Prerequisites
  Step 1: Provisioning PostgreSQL with VMware DSM Step 2: Preparing the Harbor Helm
  Chart Configuration Step 3: Deploying Harbor on Kubernetes Step 4: Verification
  and Maintenance Conclusion Discover more from VMware Cloud Foundation (VCF) Blog
  Related Articles VCF Breakroom Chats Episode 78: Build, Deploy, and Scale with vSphere
  Kubernetes Service 3.5 Unlocking Innovation on the Factory Floor: How VMware VCF
  Edge Empowers OT Citizen Developers Erasure Codes in VMware vSAN versus Storage
  Arrays Harbor is a widely adopted, open-source registry that secures artifacts with
  role-based access control, scans images for vulnerabilities, and ensures images
  are replicated and trusted. As a cloud-native registry, it is a critical component
  for any organization leveraging Kubernetes and containerization.'
summary: 'The Solution: Leveraging VMware Data Services Manager with Harbor Prerequisites
  Step 1: Provisioning PostgreSQL with VMware DSM Step 2: Preparing the Harbor Helm
  Chart Configuration Step 3: Deploying Harbor on Kubernetes Step 4: Verification
  and Maintenance Conclusion Discover more from VMware Cloud Foundation (VCF) Blog
  Related Articles VCF Breakroom Chats Episode 78: Build, Deploy, and Scale with vSphere
  Kubernetes Service 3.5 Unlocking Innovation on the Factory Floor: How VMware VCF
  Edge Empowers OT Citizen Developers Erasure Codes in VMware vSAN versus Storage
  Arrays Harbor is a widely adopted, open-source registry that secures artifacts with
  role-based access control, scans images for vulnerabilities, and ensures images
  are replicated and trusted. As a cloud-native registry, it is a critical component
  for any organization leveraging Kubernetes and containerization. In our previous
  blog , we established that while Harbor includes a built-in PostgreSQL database,
  this setup is generally not recommended for production use. Deploying a resilient,
  highly available container registry requires separating the application and database
  lifecycle to ensure operational excellence. Here are the key reasons why a dedicated,
  external database is critical for production Harbor deployments: Lack of High Availability
  (HA): The default internal PostgreSQL setup is typically a single instance, creating
  a single point of failure. A database pod failure means your entire Harbor instance
  becomes unavailable. Limited Scalability: An embedded database is not designed for
  independent scaling. Database performance bottlenecks that arise from growth can
  be difficult to address without disrupting Harbor itself. Complex Lifecycle Management:
  Managing critical database operations such as backups, point-in-time recovery, patching,
  and upgrades directly within an application’s Helm chart is significantly more complex
  and error-prone than with dedicated database solutions. To address these challenges,
  we need a highly available PostgreSQL cluster. This is where VMware Data Services
  Manager (DSM) comes in. VMware Cloud Foundation (VCF) is the private cloud platform
  that delivers on-premises security, resilience, and performance, providing the underlying
  infrastructure for modern private cloud environments, including the Kubernetes clusters
  where applications like Harbor are deployed.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/12/08/integrating-vmware-data-services-manager-with-harbor-for-a-production-ready-registry/
