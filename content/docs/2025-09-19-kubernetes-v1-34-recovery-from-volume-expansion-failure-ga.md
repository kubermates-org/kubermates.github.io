---
title: 'Kubernetes v1.34: Recovery From Volume Expansion Failure (GA)'
date: '2025-09-19T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/09/19/kubernetes-v1-34-recover-expansion-failure/
post_kind: link
draft: false
tldr: 'Kubernetes v1.34: Recovery From Volume Expansion Failure (GA) Reducing PVC
  size to recover from failed expansion Improved error handling and observability
  of volume expansion Improved observability of in-progress expansion Improved error
  handling and reporting Fixes long standing bugs in resizing workflows Have you ever
  made a typo when expanding your persistent volumes in Kubernetes? Meant to specify
  2TB but specified 20TiB ? This seemingly innocuous problem was kinda hard to fix
  - and took the project almost 5 years to fix. Automated recovery from storage expansion
  has been around for a while in beta; however, with the v1.34 release, we have graduated
  this to general availability.'
summary: 'Kubernetes v1.34: Recovery From Volume Expansion Failure (GA) Reducing PVC
  size to recover from failed expansion Improved error handling and observability
  of volume expansion Improved observability of in-progress expansion Improved error
  handling and reporting Fixes long standing bugs in resizing workflows Have you ever
  made a typo when expanding your persistent volumes in Kubernetes? Meant to specify
  2TB but specified 20TiB ? This seemingly innocuous problem was kinda hard to fix
  - and took the project almost 5 years to fix. Automated recovery from storage expansion
  has been around for a while in beta; however, with the v1.34 release, we have graduated
  this to general availability. 2TB 20TiB While it was always possible to recover
  from failing volume expansions manually, it usually required cluster-admin access
  and was tedious to do (See aformentioned link for more information). What if you
  make a mistake and then realize immediately? With Kubernetes v1.34, you should be
  able to reduce the requested size of the PersistentVolumeClaim (PVC) and, as long
  as the expansion to previously requested size hadn''t finished, you can amend the
  size requested. Kubernetes will automatically work to correct it. Any quota consumed
  by failed expansion will be returned to the user and the associated PersistentVolume
  should be resized to the latest size you specified. I''ll walk through an example
  of how all of this works. Imagine that you are running out of disk space for one
  of your database servers, and you want to expand the PVC from previously specified
  10TB to 100TB - but you make a typo and specify 1000TB. 10TB 100TB 1000TB kind :
  PersistentVolumeClaim apiVersion : v1 metadata : name : myclaim spec : accessModes
  : - ReadWriteOnce resources : requests : storage : 1000TB # newly specified size
  - but incorrect! kind : PersistentVolumeClaim apiVersion : v1 metadata : name :
  myclaim spec : accessModes : - ReadWriteOnce resources : requests : storage : 1000TB
  # newly specified size - but incorrect! Now, you may be out of disk space on your
  disk array or simply ran out of allocated quota on your cloud-provider. But, assume
  that expansion to 1000TB is never going to succeed. 1000TB In Kubernetes v1.34,
  you can simply correct your mistake and request a new PVC size, that is smaller
  than the mistake, provided it is still larger than the original size of the actual
  PersistentVolume. kind : PersistentVolumeClaim apiVersion : v1 metadata : name :
  myclaim spec : accessModes : - ReadWriteOnce resources : requests : storage : 100TB
  # Corrected size; has to be greater than 10TB.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/09/19/kubernetes-v1-34-recover-expansion-failure/
