---
title: 'Kubernetes v1.34: Autoconfiguration for Node Cgroup Driver Goes GA'
date: '2025-09-12T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/09/12/kubernetes-v1-34-cri-cgroup-driver-lookup-now-ga/
post_kind: link
draft: false
tldr: 'Kubernetes v1.34: Autoconfiguration for Node Cgroup Driver Goes GA Automated
  cgroup driver detection Announcement: Kubernetes is deprecating containerd v1. y
  support Historically, configuring the correct cgroup driver has been a pain point
  for users running new Kubernetes clusters.'
summary: 'Kubernetes v1.34: Autoconfiguration for Node Cgroup Driver Goes GA Automated
  cgroup driver detection Announcement: Kubernetes is deprecating containerd v1. y
  support Historically, configuring the correct cgroup driver has been a pain point
  for users running new Kubernetes clusters. On Linux systems, there are two different
  cgroup drivers: cgroupfs and systemd. In the past, both the kubelet and CRI implementation
  (like CRI-O or containerd) needed to be configured to use the same cgroup driver,
  or else the kubelet would misbehave without any explicit error message. This was
  a source of headaches for many cluster admins. Now, we''ve (almost) arrived at the
  end of that headache. cgroupfs systemd In v1.28.0, the SIG Node community introduced
  the feature gate KubeletCgroupDriverFromCRI , which instructs the kubelet to ask
  the CRI implementation which cgroup driver to use. After many releases of waiting
  for each CRI implementation to have major versions released and packaged in major
  operating systems, this feature has gone GA as of Kubernetes 1.34.0. KubeletCgroupDriverFromCRI
  In addition to setting the feature gate, a cluster admin needs to ensure their CRI
  implementation is new enough: containerd: Support was added in v2.0.0 CRI-O: Support
  was added in v1.28.0 While CRI-O releases versions that match Kubernetes versions,
  and thus CRI-O versions without this behavior are no longer supported, containerd
  maintains its own release cycle. containerd support for this feature is only in
  v2.0 and later, but Kubernetes 1.34 still supports containerd 1.7 and other LTS
  releases of containerd. The Kubernetes SIG Node community has formally agreed upon
  a final support timeline for containerd v1. y.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/09/12/kubernetes-v1-34-cri-cgroup-driver-lookup-now-ga/
