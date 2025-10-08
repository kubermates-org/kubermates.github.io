---
title: Red Hat OpenStack VMware Migration toolkit deep-dive
date: '2025-10-07T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/red-hat-openstack-vmware-migration-toolkit-deep-dive
post_kind: link
draft: false
tldr: Red Hat OpenStack VMware Migration toolkit deep-dive Highlights Ansible Integration
  with Ansible Automation Platform OpenStack APIs and Changed Block Tracking (CBT)
  for Warm Migration Infrastructure Components in the Migration Process Migration
  Workflow Overview Red Hat Ansible Automation Platform | Product Trial About the
  author Pedro Navarro Pérez More like this Blog post Blog post Keep exploring Browse
  by channel Automation Artificial intelligence Open hybrid cloud Security Edge computing
  Infrastructure Applications Virtualization Share When an organization currently
  on VMware evaluates transitioning to a new cloud platform, such as Red Hat OpenStack
  Services on OpenShift , a key initial concern is typically the effective migration
  of VMware virtual machine workloads. The Red Hat OpenStack VMware Migration toolkit
  specifically addresses this need, providing an Ansible collection that aims to simplify
  and automate the migration process from VMware environments into Red Hat OpenStack
  Services on OpenShift.
summary: 'Red Hat OpenStack VMware Migration toolkit deep-dive Highlights Ansible
  Integration with Ansible Automation Platform OpenStack APIs and Changed Block Tracking
  (CBT) for Warm Migration Infrastructure Components in the Migration Process Migration
  Workflow Overview Red Hat Ansible Automation Platform | Product Trial About the
  author Pedro Navarro Pérez More like this Blog post Blog post Keep exploring Browse
  by channel Automation Artificial intelligence Open hybrid cloud Security Edge computing
  Infrastructure Applications Virtualization Share When an organization currently
  on VMware evaluates transitioning to a new cloud platform, such as Red Hat OpenStack
  Services on OpenShift , a key initial concern is typically the effective migration
  of VMware virtual machine workloads. The Red Hat OpenStack VMware Migration toolkit
  specifically addresses this need, providing an Ansible collection that aims to simplify
  and automate the migration process from VMware environments into Red Hat OpenStack
  Services on OpenShift. This toolkit significantly reduces the complexity and downtime
  often associated with manual migrations, enabling organizations to rapidly and smoothly
  adopt cloud-native architectures. This article provides a deep dive into migrating
  VMware-based workloads to Red Hat OpenStack Services on OpenShift. By following
  this guide, you’ll gain the essential knowledge and tools needed to plan and execute
  a successful, efficient migration. The Red Hat OpenStack VMware Migration Toolkit,
  delivered as an Ansible collection, comes with a powerful set of features designed
  to streamline and scale your migration efforts: Discovery mode: automatically gathers
  metadata from VMware vCenter, including VM definitions, network configurations,
  and storage details. Network mapping: supports mapping of source networks and ports
  to target Red Hat OpenStack Services on OpenShift networks, including MAC address
  preservation. Flavor mapping and flavor creation: enables mapping VMware hardware
  profiles to OpenStack flavors or dynamically creates matching flavors during migration.
  Warm VM migration support: migrates running virtual machines with minimal disruption
  by leveraging snapshot and CBT-based mechanisms. Multi-disk and multi-NIC support:
  fully supports virtual machines with complex storage and networking setups, ensuring
  consistent and complete migration. Operating system compatibility: supports a broad
  range of guest OSes compatible with virt-v2v and certified for use with Red Hat
  OpenStack Services on OpenShift. One of the key advantages of the Red Hat OpenStack
  VMware Migration toolkit is its deep integration with Ansible, making it a natural
  fit for organizations using Ansible Automation Platform (AAP).'
---
Open the original post ↗ https://www.redhat.com/en/blog/red-hat-openstack-vmware-migration-toolkit-deep-dive
