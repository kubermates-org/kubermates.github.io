---
title: 'VMware Cloud on AWS: What’s New (December 2025)'
date: '2025-12-02T18:58:50+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/12/02/vmware-cloud-on-aws-whats-new-december-2025/
post_kind: link
draft: false
tldr: 'Optimize Your SDDC Deployments: Stretched Cluster Enhancements Non-Stretched
  Secondary Clusters in Stretched SDDCs Some key benefits include: Improved Scale-Down
  Options for Stretched Clusters Key use cases: Take Control of Your Data: New Host
  Usage Report API Product Enhancement: HCX version 4.11.3 Now Available for VMC What’s
  New in HCX 4.11.3? Improved Experience: Redesigned VMware Cloud on AWS UI Improved
  Sizing Recommendations: VMC Sizer & Cluster Conversion Updates What’s New for VMC
  Cluster Conversion estimates? Stay Tuned for Future Updates Discover more from VMware
  Cloud Foundation (VCF) Blog Related Articles VMware Cloud on AWS: What''s New (December
  2025) The Great Cloud Charade: Why "Data Residency" Isn''t "Data Sovereignty" VMware
  Cloud on AWS: VMC Console UI Migration to Broadcom Updated: 12/02/2025 At Broadcom,
  we are focused on helping customers modernize their infrastructure, improve resiliency,
  and simplify operations – without adding complexity for their teams to manage. Over
  the past few months, we’ve released several updates to make VMware Cloud on AWS
  (VMC) more flexible and easier to use.'
summary: 'Optimize Your SDDC Deployments: Stretched Cluster Enhancements Non-Stretched
  Secondary Clusters in Stretched SDDCs Some key benefits include: Improved Scale-Down
  Options for Stretched Clusters Key use cases: Take Control of Your Data: New Host
  Usage Report API Product Enhancement: HCX version 4.11.3 Now Available for VMC What’s
  New in HCX 4.11.3? Improved Experience: Redesigned VMware Cloud on AWS UI Improved
  Sizing Recommendations: VMC Sizer & Cluster Conversion Updates What’s New for VMC
  Cluster Conversion estimates? Stay Tuned for Future Updates Discover more from VMware
  Cloud Foundation (VCF) Blog Related Articles VMware Cloud on AWS: What''s New (December
  2025) The Great Cloud Charade: Why "Data Residency" Isn''t "Data Sovereignty" VMware
  Cloud on AWS: VMC Console UI Migration to Broadcom Updated: 12/02/2025 At Broadcom,
  we are focused on helping customers modernize their infrastructure, improve resiliency,
  and simplify operations – without adding complexity for their teams to manage. Over
  the past few months, we’ve released several updates to make VMware Cloud on AWS
  (VMC) more flexible and easier to use. It’s easy to miss the latest updates on our
  release notes , so we want to use this opportunity to highlight some of the most
  recent feature releases. Our latest features provide enterprise customers more cost-efficient
  resilience with non-stretched secondary clusters and improved scale-down, clearer
  operational insights via a redesigned user interface, an improved VMC Sizer, and
  new Host Usage APIs, and continued product enhancements through HCX 4.11.3. Here’s
  a look at what’s new. When you deploy a Software Defined Datacenter (SDDC) in VMC,
  you are given the choice of either a standard or a stretched SDDC deployment. While
  a standard cluster is deployed in a single AWS availability zone (AZ), a stretched
  cluster offers improved availability by deploying the SDDC across three AWS availability
  zones. Two of the availability zones are selected for the instance deployments and
  the third hosts the vSAN witness component. Because SDDCs in stretched clusters
  deploy hosts in two AWS availability zones, they require customers to size at two
  to one for their resource needs. This can be cost prohibitive for workloads that
  don’t require high availability. Additionally, once stretched clusters have been
  scaled beyond six hosts, they were previously unable to scale back down. To improve
  both of these experiences, the VMC team has introduced Non-Stretched Secondary Clusters
  in Stretched Cluster SDDCs and Improved Scale-Down Options for Stretched Clusters.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/12/02/vmware-cloud-on-aws-whats-new-december-2025/
