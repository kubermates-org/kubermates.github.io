---
title: Using Harbor as a Proxy Cache for Cloud-Based Registries
date: '2025-12-16T11:26:21+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/12/16/using-harbor-as-a-proxy-cache-for-cloud-based-registries/
post_kind: link
draft: false
tldr: 'The Problem: Public Registry Challenges Why Use a Proxy Cache? How it works:
  The Benefits: Setting Up Harbor as a Proxy Cache Step 1: Deploy and Access Harbor
  Step 2: Configure the Proxy Target (External Registry) Step 3: Create a New Project
  for the Proxy Using the Proxy Cache How it Works in Practice What happens behind
  the scenes: Visual Walkthrough Cache Invalidation and Retention Other Supported
  Registries Conclusion Discover more from VMware Cloud Foundation (VCF) Blog Related
  Articles Deploy VCF Private AI Services in Minimal VMware Cloud Foundation Environments
  NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation 9 Part 4: vSAN
  Compatibility and Storage Considerations Using Harbor as a Proxy Cache for Cloud-Based
  Registries In the world of containerization, pulling images from public registries
  is a daily task for development teams, CI/CD pipelines, and production deployments.
  But what happens when your team scales? What starts as a simple docker pull nginx
  command can quickly become a bottleneck.'
summary: 'The Problem: Public Registry Challenges Why Use a Proxy Cache? How it works:
  The Benefits: Setting Up Harbor as a Proxy Cache Step 1: Deploy and Access Harbor
  Step 2: Configure the Proxy Target (External Registry) Step 3: Create a New Project
  for the Proxy Using the Proxy Cache How it Works in Practice What happens behind
  the scenes: Visual Walkthrough Cache Invalidation and Retention Other Supported
  Registries Conclusion Discover more from VMware Cloud Foundation (VCF) Blog Related
  Articles Deploy VCF Private AI Services in Minimal VMware Cloud Foundation Environments
  NVMe Memory Tiering Design and Sizing on VMware Cloud Foundation 9 Part 4: vSAN
  Compatibility and Storage Considerations Using Harbor as a Proxy Cache for Cloud-Based
  Registries In the world of containerization, pulling images from public registries
  is a daily task for development teams, CI/CD pipelines, and production deployments.
  But what happens when your team scales? What starts as a simple docker pull nginx
  command can quickly become a bottleneck. docker pull nginx Picture this scenario:
  Your organization has 50 developers, each running builds multiple times a day. Your
  CI/CD system spins up fresh containers for every pipeline run. Each environment
  such as development, staging, and production pulls the same base images repeatedly.
  All of these pulls hit the public registry directly. Soon, you start experiencing:
  Rate Limiting Issues: Some public registries limit anonymous users to a specific
  number pulls per hour. With multiple teams and automated systems, you’ll hit these
  limits quickly, causing builds to fail with cryptic “too many requests” errors.
  Slow Build Times: Every pull traverses the internet, adding latency. A 500MB image
  that could be retrieved from your local network in seconds takes minutes from a
  public registry. Network Costs: Cloud providers charge for egress traffic. Repeatedly
  pulling multi-gigabyte images from external registries can result in significant
  monthly bills.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/12/16/using-harbor-as-a-proxy-cache-for-cloud-based-registries/
