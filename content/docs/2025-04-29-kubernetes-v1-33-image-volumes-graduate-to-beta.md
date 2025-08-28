---
title: 'Kubernetes v1.33: Image Volumes graduate to beta!'
date: '2025-04-29T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/04/29/kubernetes-v1-33-image-volume-beta/
post_kind: link
draft: false
tldr: 'Kubernetes v1.33: Image Volumes graduate to beta! What''s new Further reading
  Image Volumes were introduced as an Alpha feature with the Kubernetes v1.31 release
  as part of KEP-4639. In Kubernetes v1.33, this feature graduates to beta.'
summary: 'Kubernetes v1.33: Image Volumes graduate to beta! What''s new Further reading
  Image Volumes were introduced as an Alpha feature with the Kubernetes v1.31 release
  as part of KEP-4639. In Kubernetes v1.33, this feature graduates to beta. Please
  note that the feature is still disabled by default, because not all container runtimes
  have full support for it. CRI-O supports the initial feature since version v1.31
  and will add support for Image Volumes as beta in v1.33. containerd merged support
  for the alpha feature which will be part of the v2.1.0 release and is working on
  beta support as part of PR #11578. The major change for the beta graduation of Image
  Volumes is the support for subPath and subPathExpr mounts for containers via spec.
  containers[*]. volumeMounts. [subPath,subPathExpr]. This allows end-users to mount
  a certain subdirectory of an image volume, which is still mounted as readonly (
  noexec ). This means that non-existing subdirectories cannot be mounted by default.
  As for other subPath and subPathExpr values, Kubernetes will ensure that there are
  no absolute path or relative path components part of the specified sub path.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/04/29/kubernetes-v1-33-image-volume-beta/
