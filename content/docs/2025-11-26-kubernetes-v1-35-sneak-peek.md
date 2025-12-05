---
title: Kubernetes v1.35 Sneak Peek
date: '2025-11-26T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/11/26/kubernetes-v1-35-sneak-peek/
post_kind: link
draft: false
tldr: Kubernetes v1.35 Sneak Peek Deprecations and removals for Kubernetes v1.35 cgroup
  v1 support Deprecation of ipvs mode in kube-proxy Kubernetes is deprecating containerd
  v1. y support Featured enhancements of Kubernetes v1.35 Node declared features In-place
  update of Pod resources Pod certificates Numeric values for taints User namespaces
  Support for mounting OCI images as volumes Want to know more? Get involved As the
  release of Kubernetes v1.35 approaches, the Kubernetes project continues to evolve.
summary: Kubernetes v1.35 Sneak Peek Deprecations and removals for Kubernetes v1.35
  cgroup v1 support Deprecation of ipvs mode in kube-proxy Kubernetes is deprecating
  containerd v1. y support Featured enhancements of Kubernetes v1.35 Node declared
  features In-place update of Pod resources Pod certificates Numeric values for taints
  User namespaces Support for mounting OCI images as volumes Want to know more? Get
  involved As the release of Kubernetes v1.35 approaches, the Kubernetes project continues
  to evolve. Features may be deprecated, removed, or replaced to improve the project's
  overall health. This blog post outlines planned changes for the v1.35 release that
  the release team believes you should be aware of to ensure the continued smooth
  operation of your Kubernetes cluster(s), and to keep you up to date with the latest
  developments. The information below is based on the current status of the v1.35
  release and is subject to change before the final release date. On Linux nodes,
  container runtimes typically rely on cgroups (short for "control groups"). Support
  for using cgroup v2 has been stable in Kubernetes since v1.25, providing an alternative
  to the original v1 cgroup support. While cgroup v1 provided the initial resource
  control mechanism, it suffered from well-known inconsistencies and limitations.
  Adding support for cgroup v2 allowed use of a unified control group hierarchy, improved
  resource isolation, and served as the foundation for modern features, making legacy
  cgroup v1 support ready for removal. The removal of cgroup v1 support will only
  impact cluster administrators running nodes on older Linux distributions that do
  not support cgroup v2; on those nodes, the kubelet will fail to start. Administrators
  must migrate their nodes to systems with cgroup v2 enabled. More details on compatibility
  requirements will be available in a blog post soon after the v1.35 release.
---
Open the original post ↗ https://kubernetes.io/blog/2025/11/26/kubernetes-v1-35-sneak-peek/
