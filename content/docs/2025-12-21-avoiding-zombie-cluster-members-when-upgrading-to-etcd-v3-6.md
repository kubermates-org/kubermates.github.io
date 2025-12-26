---
title: Avoiding Zombie Cluster Members When Upgrading to etcd v3.6
date: '2025-12-21T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/12/21/preventing-etcd-zombies/
post_kind: link
draft: false
tldr: Avoiding Zombie Cluster Members When Upgrading to etcd v3.6 Issue summary The
  fix and upgrade path Additional technical detail Key takeaway Acknowledgements This
  article is a mirror of an original that was recently published to the official etcd
  blog. The key takeaway ? Always upgrade to etcd v3.5.26 or later before moving to
  v3.6.
summary: Avoiding Zombie Cluster Members When Upgrading to etcd v3.6 Issue summary
  The fix and upgrade path Additional technical detail Key takeaway Acknowledgements
  This article is a mirror of an original that was recently published to the official
  etcd blog. The key takeaway ? Always upgrade to etcd v3.5.26 or later before moving
  to v3.6. This ensures your cluster is automatically repaired, and avoids zombie
  members. Recently, the etcd community addressed an issue that may appear when users
  upgrade from v3.5 to v3.6. This bug can cause the cluster to report "zombie members",
  which are etcd nodes that were removed from the database cluster some time ago,
  and are re-appearing and joining database consensus. The etcd cluster is then inoperable
  until these zombie members are removed. In etcd v3.5 and earlier, the v2store was
  the source of truth for membership data, even though the v3store was also present.
  As a part of our v2store deprecation plan , in v3.6 the v3store is the source of
  truth for cluster membership. Through a bug report we found out that, in some older
  clusters, v2store and v3store could become inconsistent. This inconsistency manifests
  after upgrading as seeing old, removed "zombie" cluster members re-appearing in
  the cluster. We’ve added a mechanism in etcd v3.5.26 to automatically sync v3store
  from v2store, ensuring that affected clusters are repaired before upgrading to 3.6.
  x.
---
Open the original post ↗ https://kubernetes.io/blog/2025/12/21/preventing-etcd-zombies/
