---
title: 'What’s new in Calico: Spring 2026 Release'
date: '2026-06-02T16:10:41+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/whats-new-in-calico-spring-2026-release/
post_kind: link
draft: false
tldr: 'What’s new in Calico Open Source v3.32 KubeVirt Live Migration in Bridge Mode
  Scenario: Live Migration That Keeps VMs on the Pod Network Whisker Policy Verdict
  and UI Improvements Scenario: The Five-Minute Incident That Used to Take an Hour
  ClusterNetworkPolicy: Cluster-Wide Policy Goes Standard OpenStack Live Migration
  Improvements Scenario: Migrating a Trading Workload During Market Hours Also in
  this release: Istio Ambient Mode comes to Calico Open Source What’s new in Calico
  Enterprise and Calico Cloud Last Evaluated Metrics, Now via API (Cloud and Enterprise)
  Scenario: Pruning a Microsegmentation Estate at Scale Egress Gateway Layer 2 Advertisements
  Scenario: Cluster Scale-Up Without a Firewall Ticket Policy Recommendations for
  VMs and Hosts Scenario: Microsegmenting a Thousand VMs Without a Thousand Authoring
  Tasks Calico Load Balancer – Maintenance Mode (Enterprise Exclusive) Scenario: Maintenance
  That Customers Never Notice Get Started with Calico Spring 2026 Kubernetes has come
  a long way since its debut in 2014. It’s gone from running a couple of containerized
  microservices to orchestrating fleets of production workloads spanning everything
  from AI agents to full scale VMs running in pods.'
summary: 'What’s new in Calico Open Source v3.32 KubeVirt Live Migration in Bridge
  Mode Scenario: Live Migration That Keeps VMs on the Pod Network Whisker Policy Verdict
  and UI Improvements Scenario: The Five-Minute Incident That Used to Take an Hour
  ClusterNetworkPolicy: Cluster-Wide Policy Goes Standard OpenStack Live Migration
  Improvements Scenario: Migrating a Trading Workload During Market Hours Also in
  this release: Istio Ambient Mode comes to Calico Open Source What’s new in Calico
  Enterprise and Calico Cloud Last Evaluated Metrics, Now via API (Cloud and Enterprise)
  Scenario: Pruning a Microsegmentation Estate at Scale Egress Gateway Layer 2 Advertisements
  Scenario: Cluster Scale-Up Without a Firewall Ticket Policy Recommendations for
  VMs and Hosts Scenario: Microsegmenting a Thousand VMs Without a Thousand Authoring
  Tasks Calico Load Balancer – Maintenance Mode (Enterprise Exclusive) Scenario: Maintenance
  That Customers Never Notice Get Started with Calico Spring 2026 Kubernetes has come
  a long way since its debut in 2014. It’s gone from running a couple of containerized
  microservices to orchestrating fleets of production workloads spanning everything
  from AI agents to full scale VMs running in pods. As Kubernetes adoption grows,
  and its use cases stretch to cover more ground, managing its increasingly complex
  networking and security landscape demands operational maturity and a platform that
  supports it. The Spring 2026 release of Calico provides that support in two key
  areas: Unified operations across Kubernetes pods and VMs KubeVirt Live Migration
  in Bridge Mode allows you to migrate VM workloads with IPs preserved, minimal packet
  loss, and fast route convergence. VMs can move between nodes for planned maintenance,
  load balancing and to support high availability without interrupting network connectivity.
  Egress Gateway Layer 2 Advertisements (Enterprise exclusive) lets pod traffic egress
  with IPs from the host’s own subnet so workloads get a stable identity the rest
  of your network already recognizes eliminating the need for BGP Peering to advertise
  Egress Gateway IPs. Policy recommendations for VMs and hosts (Enterprise exclusive)
  automates and scales policy authoring for Calico-managed workloads running outside
  of your Kubernetes clusters. OpenStack Live Migration Improvements lets you migrate
  VM workloads running in high availability OpenStack environments with minimal risk
  of service disruption during maintenance. Preloading policies on the target node
  keeps downtime inside the single-digit-second SLOs regulated workloads require.
  Production-grade operations at scale Whisker Policy Verdict and UI Improvements
  reveal connectivity blockers in minutes by letting you see the actual tier, policy,
  and rule that denied a flow. Calico Load Balancer – Maintenance Mode (Enterprise
  exclusive) supports graceful node maintenance by excluding backends on nodes marked
  for maintenance from new Maglev assignments, allowing existing connections to drain
  naturally. Operators can monitor active connections via Prometheus metrics to determine
  when it is safe to proceed with node maintenance Two new noteworthy features headline
  this release: Kubevirt Live Migration and Whisker UI improvements.'
---
Open the original post ↗ https://www.tigera.io/blog/whats-new-in-calico-spring-2026-release/
