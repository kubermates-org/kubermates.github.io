---
title: Application Versus Infrastructure-Level High Availability with vSAN in VMware
  Cloud Foundation
date: '2025-10-28T16:00:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/10/28/application-versus-infrastructure-level-high-availability-with-vsan-in-vmware-cloud-foundation/
post_kind: link
draft: false
tldr: 'Accommodating for Failure Availability and Recovery of Applications and Data
  The Evolution of Options in High Availability Application-Level High Availability
  for Apps and Data Infrastructure-Level High Availability for Apps and Data Different
  Approaches to Achieve Data Consistency Differences in Recovery Time Objectives (RTO)
  Which One is Right for You? Summary Discover more from VMware Cloud Foundation (VCF)
  Blog Related Articles Government-Ready NVIDIA AI Enterprise Containers Now Available
  for Customers of VMware Private AI Foundation with NVIDIA Application Versus Infrastructure-Level
  High Availability with vSAN in VMware Cloud Foundation The FinOps Journey: From
  Visibility to Business Value Maintaining availability of data and the applications
  that produce or consume that data might be the most important responsibility of
  data center administrators. Capabilities like high performance or special data services
  mean very little if the applications and the data they produce or consume is not
  readily available.'
summary: 'Accommodating for Failure Availability and Recovery of Applications and
  Data The Evolution of Options in High Availability Application-Level High Availability
  for Apps and Data Infrastructure-Level High Availability for Apps and Data Different
  Approaches to Achieve Data Consistency Differences in Recovery Time Objectives (RTO)
  Which One is Right for You? Summary Discover more from VMware Cloud Foundation (VCF)
  Blog Related Articles Government-Ready NVIDIA AI Enterprise Containers Now Available
  for Customers of VMware Private AI Foundation with NVIDIA Application Versus Infrastructure-Level
  High Availability with vSAN in VMware Cloud Foundation The FinOps Journey: From
  Visibility to Business Value Maintaining availability of data and the applications
  that produce or consume that data might be the most important responsibility of
  data center administrators. Capabilities like high performance or special data services
  mean very little if the applications and the data they produce or consume is not
  readily available. Ensuring availability is a complex topic, as application availability
  and data availability use different techniques to achieve the desired result. Sometimes
  availability requirements are achieved using infrastructure-level mechanisms, while
  others may use application-centric solutions. What is best for your environment
  depends heavily on the requirements and capabilities of your infrastructure. While
  VMware Cloud Foundation (VCF) can deliver high levels of data and application availability
  in a simple way , this post will look at the differences in providing high availability
  of applications and data using application-level technologies versus inherent infrastructure-level
  technologies in VCF. We will also look at how VMware Data Services Manager (DSM)
  can play a part in simplifying some of these decisions. Protecting applications
  and data require an understanding of what typical failures look like, and what a
  system can do to accommodate for failure. For example, failures in a physical infrastructure
  may include: Centralized storage solutions like storage arrays Discrete storage
  devices in distributed solutions Hosts Network interface cards (NICs) Network switching
  fabrics, causing partitions Site/zone-level failures Failures like these noted above
  could impact the data, the applications, or both. Failures come in a variety of
  ways, with some explicitly identified, while others only through absence. Some failures
  are temporary, while others permanent. Solutions must be sophisticated enough to
  automatically handle these failure and recovery scenarios.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/10/28/application-versus-infrastructure-level-high-availability-with-vsan-in-vmware-cloud-foundation/
