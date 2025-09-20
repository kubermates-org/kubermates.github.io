---
title: 'Kubernetes v1.34: DRA Consumable Capacity'
date: '2025-09-18T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/09/18/kubernetes-v1-34-dra-consumable-capacity/
post_kind: link
draft: false
tldr: 'Kubernetes v1.34: DRA Consumable Capacity Background: device sharing via ResourceClaims
  Benefits of DRA consumable capacity support Device sharing across multiple ResourceClaims
  or DeviceRequests Device resource allocation DistinctAttribute constraint How to
  use consumable capacity? As a DRA driver developer As a consumer Integration with
  DRA device status What can you do next? Conclusion Further Reading Dynamic Resource
  Allocation (DRA) is a Kubernetes API for managing scarce resources across Pods and
  containers. It enables flexible resource requests, going beyond simply allocating
  N number of devices to support more granular usage scenarios.'
summary: 'Kubernetes v1.34: DRA Consumable Capacity Background: device sharing via
  ResourceClaims Benefits of DRA consumable capacity support Device sharing across
  multiple ResourceClaims or DeviceRequests Device resource allocation DistinctAttribute
  constraint How to use consumable capacity? As a DRA driver developer As a consumer
  Integration with DRA device status What can you do next? Conclusion Further Reading
  Dynamic Resource Allocation (DRA) is a Kubernetes API for managing scarce resources
  across Pods and containers. It enables flexible resource requests, going beyond
  simply allocating N number of devices to support more granular usage scenarios.
  With DRA, users can request specific types of devices based on their attributes,
  define custom configurations tailored to their workloads, and even share the same
  resource among multiple containers or Pods. In this blog, we focus on the device
  sharing feature and dive into a new capability introduced in Kubernetes 1.34: DRA
  consumable capacity , which extends DRA to support finer-grained device sharing.
  From the beginning, DRA introduced the ability for multiple Pods to share a device
  by referencing the same ResourceClaim. This design decouples resource allocation
  from specific hardware, allowing for more dynamic and reusable provisioning of devices.
  In Kubernetes 1.33, the new support for partitionable devices allowed resource drivers
  to advertise slices of a device that are available, rather than exposing the entire
  device as an all-or-nothing resource. This enabled Kubernetes to model shareable
  hardware more accurately. But there was still a missing piece: it didn''t yet support
  scenarios where the device driver manages fine-grained, dynamic portions of a device
  resource — like network bandwidth — based on user demand, or to share those resources
  independently of ResourceClaims, which are restricted by their spec and namespace.
  That’s where consumable capacity for DRA comes in. Here''s a taste of what you get
  in a cluster with the DRAConsumableCapacity feature gate enabled. DRAConsumableCapacity
  Resource drivers can now support sharing the same device — or even a slice of a
  device — across multiple ResourceClaims or across multiple DeviceRequests.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/09/18/kubernetes-v1-34-dra-consumable-capacity/
