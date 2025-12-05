---
title: Red Hat OpenShift Service on AWS supports Capacity Reservations and Capacity
  Blocks for Machine Learning
date: '2025-12-03T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/red-hat-openshift-service-aws-rosa-now-supports-demand-capacity-reservations-ml-workloads
post_kind: link
draft: false
tldr: Red Hat OpenShift Service on AWS supports Capacity Reservations and Capacity
  Blocks for Machine Learning Red Hat OpenShift Container Platform | Product Trial
  About the authors Bala Chandrasekaran Brae Troutman More like this Optimize Cloud
  Costs with Red Hat OpenShift Virtualization and ROSA on AWS DxOperator from DH2i
  is now certified for Red Hat OpenShift 4.19 SREs on a plane | Technically Speaking
  Get started with ROSA Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share Red Hat OpenShift Service on AWS (ROSA) is a fully managed application platform
  that offers a more seamless experience for building, deploying, and scaling applications.
  For machine learning (ML) workloads, ROSA now supports On-Demand Capacity Reservations
  (ODCR) and Capacity Blocks for ML, allowing cloud architects and platform administrators
  to strategically utilize their existing AWS purchases to help deliver uninterrupted
  access to essential compute infrastructure.
summary: 'Red Hat OpenShift Service on AWS supports Capacity Reservations and Capacity
  Blocks for Machine Learning Red Hat OpenShift Container Platform | Product Trial
  About the authors Bala Chandrasekaran Brae Troutman More like this Optimize Cloud
  Costs with Red Hat OpenShift Virtualization and ROSA on AWS DxOperator from DH2i
  is now certified for Red Hat OpenShift 4.19 SREs on a plane | Technically Speaking
  Get started with ROSA Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share Red Hat OpenShift Service on AWS (ROSA) is a fully managed application platform
  that offers a more seamless experience for building, deploying, and scaling applications.
  For machine learning (ML) workloads, ROSA now supports On-Demand Capacity Reservations
  (ODCR) and Capacity Blocks for ML, allowing cloud architects and platform administrators
  to strategically utilize their existing AWS purchases to help deliver uninterrupted
  access to essential compute infrastructure. Today, ROSA is available in over 30
  regions and supports over 600 instance types, allowing customers to run diverse
  workloads according to their business needs. However, maintaining guaranteed or
  uninterrupted access to a specific infrastructure type in a particular availability
  zone (AZ) is important for several critical scenarios: GPU-based accelerated computing
  workloads: Gaining uninterrupted access to accelerated computing (GPU) instances
  is vital for AI/ML teams conducting training, fine-tuning, or inference workloads.
  Capacity reservation helps eliminate the risk of compute unavailability for these
  time-sensitive, resource-intensive tasks. Planned scaling events: Enabling infrastructure
  scaling events to confidently support planned business events—such as peak traffic
  seasons, major product launches, or scheduled batch processing—without provisioning
  delays. High availability and disaster recovery: Enhancing resiliency by guaranteeing
  capacity when deploying workloads across multiple AZs or executing disaster recovery
  protocols across regions. Amazon EC2 Capacity Reservations allow you to reserve
  compute capacity for your Amazon EC2 instances in a specific AZ for any duration.
  Capacity Blocks for ML allow you to reserve GPU-based accelerated computing instances
  on a future date to support your short duration ML workloads. With the support for
  Capacity Reservations for clusters with hosted control planes (HCP), platform administrators
  can now create ROSA machine pools in their cluster that directly consume the capacity
  already reserved with AWS. Key best practices for effectively leveraging Capacity
  Reservations with ROSA: Pre-planning of AZs, instance types, and capacity: Before
  creation, ensure a precise match between the reserved capacity and the ROSA machine
  pool attributes. This includes VPC subnets, the number of node replicas, and the
  instance type.'
---
Open the original post ↗ https://www.redhat.com/en/blog/red-hat-openshift-service-aws-rosa-now-supports-demand-capacity-reservations-ml-workloads
