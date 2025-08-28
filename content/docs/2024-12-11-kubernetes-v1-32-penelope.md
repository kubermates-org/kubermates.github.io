---
title: 'Kubernetes v1.32: Penelope'
date: '2024-12-11T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2024/12/11/kubernetes-v1-32-release/
post_kind: link
draft: false
tldr: 'Kubernetes v1.32: Penelope Release theme and logo Updates to recent key features
  A note on DRA enhancements Quality of life improvements on nodes and sidecar containers
  update Highlights of features graduating to Stable Custom Resource field selectors
  Support to size memory backed volumes Bound service account token improvement Structured
  authorization configuration Auto remove PVCs created by StatefulSet Highlights of
  features graduating to Beta Job API managed-by mechanism Only allow anonymous auth
  for configured endpoints Per-plugin callback functions for accurate requeueing in
  kube-scheduler enhancements Recover from volume expansion failure Volume group snapshot
  Structured parameter support Label and field selector authorization Highlights of
  new features in Alpha Asynchronous preemption in the Kubernetes Scheduler Mutating
  admission policies using CEL expressions Pod-level resource specifications Allow
  zero value for sleep action of PreStop hook DRA: Standardized network interface
  data for resource claim status New statusz and flagz endpoints for core components
  Windows strikes back! Graduations, deprecations, and removals in 1.32 Graduations
  to Stable Deprecations and removals Release notes and upgrade actions required Availability
  Release team Project velocity Event updates Upcoming release webinar Get involved
  Editors: Matteo Bianchi, Edith Puclla, William Rizzo, Ryota Sawada, Rashan Smith
  Announcing the release of Kubernetes v1.32: Penelope! In line with previous releases,
  the release of Kubernetes v1.32 introduces new stable, beta, and alpha features.
  The consistent delivery of high-quality releases underscores the strength of our
  development cycle and the vibrant support from our community.'
summary: 'Kubernetes v1.32: Penelope Release theme and logo Updates to recent key
  features A note on DRA enhancements Quality of life improvements on nodes and sidecar
  containers update Highlights of features graduating to Stable Custom Resource field
  selectors Support to size memory backed volumes Bound service account token improvement
  Structured authorization configuration Auto remove PVCs created by StatefulSet Highlights
  of features graduating to Beta Job API managed-by mechanism Only allow anonymous
  auth for configured endpoints Per-plugin callback functions for accurate requeueing
  in kube-scheduler enhancements Recover from volume expansion failure Volume group
  snapshot Structured parameter support Label and field selector authorization Highlights
  of new features in Alpha Asynchronous preemption in the Kubernetes Scheduler Mutating
  admission policies using CEL expressions Pod-level resource specifications Allow
  zero value for sleep action of PreStop hook DRA: Standardized network interface
  data for resource claim status New statusz and flagz endpoints for core components
  Windows strikes back! Graduations, deprecations, and removals in 1.32 Graduations
  to Stable Deprecations and removals Release notes and upgrade actions required Availability
  Release team Project velocity Event updates Upcoming release webinar Get involved
  Editors: Matteo Bianchi, Edith Puclla, William Rizzo, Ryota Sawada, Rashan Smith
  Announcing the release of Kubernetes v1.32: Penelope! In line with previous releases,
  the release of Kubernetes v1.32 introduces new stable, beta, and alpha features.
  The consistent delivery of high-quality releases underscores the strength of our
  development cycle and the vibrant support from our community. This release consists
  of 44 enhancements in total. Of those enhancements, 13 have graduated to Stable,
  12 are entering Beta, and 19 have entered in Alpha. The Kubernetes v1.32 Release
  Theme is "Penelope". If Kubernetes is Ancient Greek for "pilot", in this release
  we start from that origin and reflect on the last 10 years of Kubernetes and our
  accomplishments: each release cycle is a journey, and just like Penelope, in "The
  Odyssey", weaved for 10 years -- each night removing parts of what she had done
  during the day -- so does each release add new features and removes others, albeit
  here with a much clearer purpose of constantly improving Kubernetes. With v1.32
  being the last release in the year Kubernetes marks its first decade anniversary,
  we wanted to honour all of those that have been part of the global Kubernetes crew
  that roams the cloud-native seas through perils and challanges: may we continue
  to weave the future of Kubernetes together. In this release, like the previous one,
  the Kubernetes project continues proposing a number of enhancements to the Dynamic
  Resource Allocation (DRA), a key component of the Kubernetes resource management
  system. These enhancements aim to improve the flexibility and efficiency of resource
  allocation for workloads that require specialized hardware, such as GPUs, FPGAs
  and network adapters. These features are particularly useful for use-cases such
  as machine learning or high-performance computing applications. The core part enabling
  DRA Structured parameter support got promoted to beta. SIG Node has the following
  highlights that go beyond KEPs: The systemd watchdog capability is now used to restart
  the kubelet when its health check fails, while also limiting the maximum number
  of restarts within a given time period.'
---
Open the original post ↗ https://kubernetes.io/blog/2024/12/11/kubernetes-v1-32-release/
