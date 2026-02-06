---
title: 'Modern Automation with VMware Cloud Foundation Part 1: Push-Button Infrastructure
  Provisioning'
date: '2026-02-03T11:11:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/02/03/modern-automation-with-vmware-cloud-foundation-part-1/
post_kind: link
draft: false
tldr: 'The Challenge of DIY Automation: “The Frankenstein Approach” Leveraging VCF
  to Automate This Process What Does an SDDC Look Like? Real-World Examples of VCF
  Infrastructure Automation Stay Tuned for Part 2: Leveraging the VCF API for Infrastructure
  Automation Discover more from VMware Cloud Foundation (VCF) Blog Related Articles
  Modernizing EDA Infrastructure: Lessons from Samsung’s VCF Deployment How to Converge
  a VMware vSphere Environment to VMware Cloud Foundation 9.0 VCF Breakroom Chats
  Episode 83 – Designing Developer-Loved Platforms: What is an IDP? In a former life,
  I successfully automated ESX rollouts, livestock-style in what we’d call a “vSphere
  only” environment. The project was to automate the process of ESX bare-metal host
  provisioning: storage zoning, bare metal installation, ESX configuration, vCenter
  import, post-vCenter configuration, iPAM/CMDB and monitoring registration, and so
  on.'
summary: 'The Challenge of DIY Automation: “The Frankenstein Approach” Leveraging
  VCF to Automate This Process What Does an SDDC Look Like? Real-World Examples of
  VCF Infrastructure Automation Stay Tuned for Part 2: Leveraging the VCF API for
  Infrastructure Automation Discover more from VMware Cloud Foundation (VCF) Blog
  Related Articles Modernizing EDA Infrastructure: Lessons from Samsung’s VCF Deployment
  How to Converge a VMware vSphere Environment to VMware Cloud Foundation 9.0 VCF
  Breakroom Chats Episode 83 – Designing Developer-Loved Platforms: What is an IDP?
  In a former life, I successfully automated ESX rollouts, livestock-style in what
  we’d call a “vSphere only” environment. The project was to automate the process
  of ESX bare-metal host provisioning: storage zoning, bare metal installation, ESX
  configuration, vCenter import, post-vCenter configuration, iPAM/CMDB and monitoring
  registration, and so on. Upon project completion, we could provision an ESX host
  into any cluster in 18 minutes, and ESX host decommission and re-provision took
  30 minutes. It was a powerful ESX-host-as-livestock approach: No need to do upgrades;
  every major update/upgrade was a new installation. No need to troubleshoot. Just
  roll out a new ESX host and decom the faulty one so you can troubleshoot it risk-free
  or delegate it to others, limiting the need for lengthy on-call events. Capacity
  planning became more flexible because we could pull any host from any lesser-utilized
  cluster and, within minutes, place it into a higher-utilized cluster. This saved
  tens of thousands of dollars every quarter since we didn’t have to plan for peak
  utilization. The project took months of iteration and no less than five platforms
  to get it all up and running. Why did it take so long, and why was it so complex?
  Because I had to learn and debug all five different platforms to get it all working;
  I had to make sure all five platforms worked together through my infrastructure
  pipeline. This is what we might call DIY automation; outside of REST APIs, I wasn’t
  really given an easy way to automate anything. I was mostly on my own.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/02/03/modern-automation-with-vmware-cloud-foundation-part-1/
