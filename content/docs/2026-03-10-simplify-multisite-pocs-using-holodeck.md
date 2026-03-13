---
title: Simplify Multisite PoCs Using Holodeck
date: '2026-03-10T14:53:09+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/03/10/holodeck-multisite/
post_kind: link
draft: false
tldr: 'Architecture: The “Lab-in-a-Box” Framework Strategic Use Cases 1. Disaster
  Recovery 2.'
summary: 'Architecture: The “Lab-in-a-Box” Framework Strategic Use Cases 1. Disaster
  Recovery 2. NSX Federation and Global Policy Management Key Advantages of Holodeck
  Deployment Process Prerequisites: Deployment Steps: Conclusion Discover more from
  VMware Cloud Foundation (VCF) Blog Related Articles Simplify Multisite PoCs Using
  Holodeck VMware Cloud Foundation: Workaround for Quorum-Disk Failure Scenario in
  2-Node WSFC 2025 Configuration Building the Foundation for Private AI: Why Data
  Sovereignty Matters In the current enterprise landscape, the ability to validate
  high availability and disaster recovery (DR) architectures is a prerequisite for
  operational excellence. However, for proof of concepts (PoCs) and learning, the
  infrastructure required to stage these environments—traditionally necessitating
  two distinct physical footprints—often stalls innovation. The VMware Cloud Foundation
  (VCF) Holodeck toolkit has emerged as the suitable solution for this challenge.
  By leveraging nested virtualization, Holodeck enables the deployment of a fully
  functional, dual-site VCF environment on a comparatively smaller hardware footprint.
  This provides a sandbox environment to master complex multi-instance operations
  without the capital expenditure of a secondary data center. Holodeck’s dual-site
  capability is built on a sophisticated networking and automation stack designed
  to provide a nested enterprise private cloud. Holorouter Architecture: A specialized
  Photon OS appliance serves as the centralized network services hub. It provides
  BGP, DNS, DHCP, and NTP services. It also provides the routing service required
  to route traffic between “Site-a” and “Site-b” as if they were geographically separated.
  Automation Layer: The deployment process is entirely automated.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/03/10/holodeck-multisite/
