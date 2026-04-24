---
title: SELinux Volume Label Changes goes GA (and likely implications in v1.37)
date: '2026-04-22T10:35:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/04/22/breaking-changes-in-selinux-volume-labeling/
post_kind: link
draft: false
tldr: 'SELinux Volume Label Changes goes GA (and likely implications in v1.37) The
  problem What Kubernetes is improving The breaking change seLinuxChangePolicy SELinux
  warning controller (optional) Suggested upgrade path Further reading Acknowledgements
  If you run Kubernetes on Linux with SELinux in enforcing mode, plan ahead: a future
  release (anticipated to be v1.37) is expected to turn the SELinuxMount feature gate
  on by default. This makes volume setup faster for most workloads, but it can break
  applications that still depend on the older recursive relabeling model in subtle
  ways (for example, sharing one volume between privileged and unprivileged Pods on
  the same node).'
summary: 'SELinux Volume Label Changes goes GA (and likely implications in v1.37)
  The problem What Kubernetes is improving The breaking change seLinuxChangePolicy
  SELinux warning controller (optional) Suggested upgrade path Further reading Acknowledgements
  If you run Kubernetes on Linux with SELinux in enforcing mode, plan ahead: a future
  release (anticipated to be v1.37) is expected to turn the SELinuxMount feature gate
  on by default. This makes volume setup faster for most workloads, but it can break
  applications that still depend on the older recursive relabeling model in subtle
  ways (for example, sharing one volume between privileged and unprivileged Pods on
  the same node). Kubernetes v1.36 is the right release to audit your cluster and
  fix or opt out of this change. SELinuxMount If your nodes do not use SELinux, nothing
  changes for you: the kubelet skips the whole SELinux logic when SELinux is unavailable
  or disabled in the Linux kernel. You can skip this article completely. This blog
  builds on the earlier work described in the Kubernetes 1.27: Efficient SELinux Relabeling
  (Beta) post, where the SELinuxMountReadWriteOncePod feature gate was described.
  The problem to be addressed remains the same, however, this blog extends that same
  approach to all volumes. SELinuxMountReadWriteOncePod Linux systems with Security
  Enhanced Linux (SELinux) enabled use labels attached to objects (for example, files
  and network sockets) to make access control decisions. Historically, the container
  runtime applies SELinux labels to a Pod and all its volumes. Kubernetes only passes
  the SELinux label from a Pod''s securityContext fields to the container runtime.
  securityContext The container runtime then recursively changes the SELinux label
  on all files that are visible to the Pod''s containers. This can be time-consuming
  if there are many files on the volume, especially when the volume is on a remote
  filesystem.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/04/22/breaking-changes-in-selinux-volume-labeling/
