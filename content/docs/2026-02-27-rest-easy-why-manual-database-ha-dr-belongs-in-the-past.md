---
title: 'Rest Easy: Why Manual Database HA/DR Belongs in the Past'
date: '2026-02-27T17:34:10+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/02/27/rest-easy-why-manual-database-ha-dr-belongs-in-the-past/
post_kind: link
draft: false
tldr: 'The “Manual Tax” vs. The DSM Advantage Moving from “One-Off” Scripts to Policy-Based
  Governance The “Oops” Button: Point-in-Time Recovery (PITR) The Bottom Line: No
  Specialist Required Discover more from VMware Cloud Foundation (VCF) Blog Related
  Articles Building the Foundation for Private AI: Why Data Sovereignty Matters Day
  2 Operations for AI Blueprints in VCF Automation Announcing the General Availability
  of Holodeck 9.0.2 If you’ve spent your career managing open-source databases, you
  know the challenge.'
summary: 'The “Manual Tax” vs. The DSM Advantage Moving from “One-Off” Scripts to
  Policy-Based Governance The “Oops” Button: Point-in-Time Recovery (PITR) The Bottom
  Line: No Specialist Required Discover more from VMware Cloud Foundation (VCF) Blog
  Related Articles Building the Foundation for Private AI: Why Data Sovereignty Matters
  Day 2 Operations for AI Blueprints in VCF Automation Announcing the General Availability
  of Holodeck 9.0.2 If you’ve spent your career managing open-source databases, you
  know the challenge. Setting up high availability (HA) or disaster recovery (DR)
  often involves a “Frankenstein” mix of heartbeat scripts, manually tuned configuration
  files, and a prayer that your documentation is up to date when the primary node
  finally fails. You know the benefits of managing your important private cloud infrastructure
  from a central place with VMware Cloud Foundation. So, why are you managing your
  important databases manually? Here is how VMware Data Services Manager (DSM) replaces
  manual complexity with policy-driven automation for database management in a modern
  private cloud built on VMware Cloud Foundation (VCF) 9.0. Most DBAs spend a vast
  amount of their time on “keep the lights on” tasks. DSM is designed to give that
  time back by automating the high-stakes operations that usually require deep, platform-specific
  expertise. The real power of DSM isn’t just that it can do DR—it’s that it ensures
  DR is never forgotten. By using Infrastructure Policies, a VCF Admin can pre-define
  what “Mission-Critical” looks like. Instead of a DBA manually configuring every
  new instance, for example, they can simply select a policy: “Gold Tier” policy :
  Automatically deploys a 3-node HA cluster with cross-cluster replication to a secondary
  site and 15-minute PITR windows. “Dev Tier” policy: Single instance, daily backups,
  no replication. This ensures that every database deployed—whether by a DBA or a
  developer via self-service — inherits the correct protection levels without a single
  manual configuration step.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/02/27/rest-easy-why-manual-database-ha-dr-belongs-in-the-past/
