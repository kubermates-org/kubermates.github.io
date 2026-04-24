---
title: 'Taming costs in cloud environments: Rating in OpenStack with CloudKitty'
date: '2026-04-15T00:00:00+00:00'
tags:
- openshift
source: OpenShift Blog
external_url: https://www.redhat.com/en/blog/taming-costs-cloud-environments-rating-openstack-cloudkitty
post_kind: link
draft: false
tldr: 'Taming costs in cloud environments: Rating in OpenStack with CloudKitty Why
  is CloudKitty important? How does CloudKitty work? Setting the rules If you can
  measure it, you can rate it Generate rating reports: The moment of truth A look
  under the hood Architecture overview Why Loki? The metrics configuration Inspecting
  the raw data Ready to count costs? Get started See it in action Red Hat OpenShift
  Container Platform | Product Trial About the authors Simon Herlofsson Juan Larriba
  More like this Bridging legacy and cloud-native: A new path with Red Hat OpenShift
  Dedicated deployed on Google Cloud and Google Cloud NetApp Volume The power shift:
  Why the future of the electric grid will be software-defined Transforming Your Secrets
  Management | Code Comments Transforming Your Database | Code Comments Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share Does your private
  cloud feel like a free-for-all buffet? You know it''s providing value, but when
  the bill comes due, it’s nearly impossible to tell who’s eating what. In today''s
  dynamic cloud environments, it’s increasingly important to be able to properly attribute
  costs to internal users, especially for enterprises running their own cloud infrastructure.'
summary: 'Taming costs in cloud environments: Rating in OpenStack with CloudKitty
  Why is CloudKitty important? How does CloudKitty work? Setting the rules If you
  can measure it, you can rate it Generate rating reports: The moment of truth A look
  under the hood Architecture overview Why Loki? The metrics configuration Inspecting
  the raw data Ready to count costs? Get started See it in action Red Hat OpenShift
  Container Platform | Product Trial About the authors Simon Herlofsson Juan Larriba
  More like this Bridging legacy and cloud-native: A new path with Red Hat OpenShift
  Dedicated deployed on Google Cloud and Google Cloud NetApp Volume The power shift:
  Why the future of the electric grid will be software-defined Transforming Your Secrets
  Management | Code Comments Transforming Your Database | Code Comments Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share Does your private
  cloud feel like a free-for-all buffet? You know it''s providing value, but when
  the bill comes due, it’s nearly impossible to tell who’s eating what. In today''s
  dynamic cloud environments, it’s increasingly important to be able to properly attribute
  costs to internal users, especially for enterprises running their own cloud infrastructure.
  You need to establish accountability in order to distribute costs fairly among departments
  or encourage teams to right-size their workloads—and gaining visibility is the first
  step. With feature release 5 (FR5) of Red Hat OpenStack Services on OpenShift 18,
  we are shipping a critical piece to help solve that puzzle: the ability to perform
  rating based on your tenants'' measured usage. We are introducing CloudKitty, the
  OpenStack-native rating service, as generally available in FR5. This service fills
  the gap between your raw technical metrics and your financial operations. CloudKitty
  provides a translation layer that turns data about server usage into information
  that can inform departmental budgets. Think of CloudKitty as the meter reader: it
  sits between your collected metrics and your FinOps or billing solution. It takes
  raw technical data, like how many hours a virtual machine (VM) ran or how much storage
  was consumed, and applies your specific rating rules to generate a report. This
  helps you achieve 2 major goals: Transparent cost recovery: You can now see a clear,
  itemized breakdown of resource usage per tenant. This allows you to recoup operational
  expenses accurately without surprising internal customers with opaque charges. Trust
  and optimization: When tenants see how their own consumption (broken down by project,
  flavor, and metric) affects their costs, they can make informed decisions, like
  archiving stale data or optimizing their VM usage.'
---
Open the original post ↗ https://www.redhat.com/en/blog/taming-costs-cloud-environments-rating-openstack-cloudkitty
