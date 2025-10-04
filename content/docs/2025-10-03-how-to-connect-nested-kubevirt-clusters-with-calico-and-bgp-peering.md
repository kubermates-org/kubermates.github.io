---
title: How to Connect Nested KubeVirt Clusters with Calico and BGP Peering
date: '2025-10-03T18:28:12+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/how-to-connect-nested-kubevirt-clusters-with-calico-and-bgp-peering/
post_kind: link
draft: false
tldr: Why BGP Peering for Nested Clusters? Key Challenges When Peering With Nested
  Clusters Dynamic IPs vs. With KubeVirt , a virtualization add-on for Kubernetes
  that uses QEMU (an open-source machine emulator and virtualizer), you can run full-featured
  Kubernetes clusters as virtual machines (VMs) inside a parent Kubernetes cluster.
summary: 'Why BGP Peering for Nested Clusters? Key Challenges When Peering With Nested
  Clusters Dynamic IPs vs. With KubeVirt , a virtualization add-on for Kubernetes
  that uses QEMU (an open-source machine emulator and virtualizer), you can run full-featured
  Kubernetes clusters as virtual machines (VMs) inside a parent Kubernetes cluster.
  This nested architecture makes it possible to unify containerized and virtualized
  workloads, and opens the door to new platform engineering use cases. But here’s
  the challenge: how can you ensure that these nested clusters, and the workloads
  within, can reach, and be reached by, your physical network and are treated the
  same way as any other cluster? That’s where Calico’s Advanced BGP (Border Gateway
  Protocol) peering with workloads comes into play. By enabling BGP route exchange
  between the parent cluster and nested KubeVirt VMs, Calico extends dynamic routing
  directly to virtualized workloads. This allows nested clusters to participate in
  the broader network topology and advertise their pod and service IPs just like any
  other node. Thus eliminating the need for tunnels or overlays to achieve true layer
  3 connectivity. In this blog, we’ll walk through the big picture, prerequisites,
  and step-by-step configuration for setting up BGP peering between parent clusters
  and nested clusters running inside KubeVirt. Platform engineering teams today face
  a common challenge: delivering a platform that meets performance, security, and
  cost requirements—without forcing developers to decide where their applications
  should run. Whether the underlying platform is on-premises, in the cloud, or virtualized
  with KubeVirt, those choices should be taken care of automatically, without developer
  involvement. Developers should simply request a resource to run their applications,
  while the platform team ensures the correct resources are delivered on available
  platforms. Enabling BGP peering on nested KubeVirt clusters means they can be treated
  just like any other cluster, with no ‘special’ or snowflake-style configurations
  required simply because they are virtualized.'
---
Open the original post ↗ https://www.tigera.io/blog/how-to-connect-nested-kubevirt-clusters-with-calico-and-bgp-peering/
