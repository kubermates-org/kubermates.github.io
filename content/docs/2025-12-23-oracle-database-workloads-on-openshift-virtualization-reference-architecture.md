---
title: Oracle Database Workloads On OpenShift Virtualization Reference Architecture
date: '2025-12-23T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/Oracle-Database-Workloads-On-OpenShift-Virtualization-Reference-Architecture
post_kind: link
draft: false
tldr: 'Oracle Database Workloads On OpenShift Virtualization Reference Architecture
  Background OpenShift Virtualization architecture overview Oracle Database design
  principles Reference architecture Compute Network Storage Hardware configuration
  OpenShift Virtualization configuration Oracle Database configuration Oracle Database
  Single Instance Oracle RAC database Observability and monitoring System performance
  evaluation Test coverage summary Evaluation of impact of VM Live Migration Final
  thoughts Red Hat Learning Subscription | Product Trial About the authors Mikhail
  Mikhailitchenko Lokesh Rangineni Abdul Hameed Kamlesh Panchal More like this Red
  Hat OpenShift Virtualization: The strategic platform for virtualization customers
  Red Hat OpenShift Virtualization 4.20: Hybrid cloud-flexibility and enhanced VM
  management Keep exploring Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share This article details Red Hat''s engineering efforts to support running a Oracle
  Database 19c on Red Hat OpenShift Virtualization. It provides a comprehensive reference
  architecture, validation results covering functionality, performance, scalability,
  and live migration, along with links to testing artifacts hosted on GitHub.'
summary: 'Oracle Database Workloads On OpenShift Virtualization Reference Architecture
  Background OpenShift Virtualization architecture overview Oracle Database design
  principles Reference architecture Compute Network Storage Hardware configuration
  OpenShift Virtualization configuration Oracle Database configuration Oracle Database
  Single Instance Oracle RAC database Observability and monitoring System performance
  evaluation Test coverage summary Evaluation of impact of VM Live Migration Final
  thoughts Red Hat Learning Subscription | Product Trial About the authors Mikhail
  Mikhailitchenko Lokesh Rangineni Abdul Hameed Kamlesh Panchal More like this Red
  Hat OpenShift Virtualization: The strategic platform for virtualization customers
  Red Hat OpenShift Virtualization 4.20: Hybrid cloud-flexibility and enhanced VM
  management Keep exploring Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share This article details Red Hat''s engineering efforts to support running a Oracle
  Database 19c on Red Hat OpenShift Virtualization. It provides a comprehensive reference
  architecture, validation results covering functionality, performance, scalability,
  and live migration, along with links to testing artifacts hosted on GitHub. OpenShift
  Virtualization offers robust performance for demanding production workloads, such
  as Oracle databases, providing a viable virtualization alternative without sacrificing
  performance. This is especially for technology leaders, architects, engineering
  teams, and project managers involved in evaluating and adopting single-instance
  Oracle Database or Oracle RAC Database on OpenShift Virtualization. The architecture
  design principles focus on resource allocation, partitioning, and abstraction layer
  optimization for compute, network, and storage. Performance tests using HammerDB
  with the TPC-C benchmark prove that Oracle Database can successfully run on OpenShift
  Virtualization with different storage solutions including software defined Red Hat
  OpenShift Data Foundation or traditional SAN storage dynamically provisioned via
  Pure/Portworx CSI driver. This article will also highlight observability and monitoring,
  using Prometheus and Grafana for infrastructure and Oracle-specific insights. Many
  customers are seeking virtualization alternatives without sacrificing performance.
  OpenShift Virtualization provides robust performance for demanding production workloads,
  including enterprise databases. One of the most common components in traditional
  software architecture is the Oracle Database. To support customers interested in
  evaluating and adopting Oracle Database on OpenShift Virtualization, Red Hat has
  dedicated engineering resources to provide an optimized experience operating Oracle
  Database on OpenShift Virtualization. This article assumes readers have an understanding
  of Red Hat OpenShift Container Platform.'
---
Open the original post ↗ https://www.redhat.com/en/blog/Oracle-Database-Workloads-On-OpenShift-Virtualization-Reference-Architecture
