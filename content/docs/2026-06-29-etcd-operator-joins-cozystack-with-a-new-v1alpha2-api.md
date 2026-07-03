---
title: etcd-operator joins Cozystack with a new v1alpha2 API
date: '2026-06-29T10:46:12+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/06/29/etcd-operator-joins-cozystack-with-a-new-v1alpha2-api/
post_kind: link
draft: false
tldr: Key features What changed compared to v1alpha1 Comparison with the official
  operator Posted on June 29, 2026 by Andrey Kolkov and Andrei Kvapil, Ænix CNCF projects
  highlighted in this post The etcd-operator project, which develops an operator for
  deploying and maintaining etcd clusters on Kubernetes, has been donated to the Cozystack
  project. Alongside the donation, a from-scratch implementation of the operator has
  been published under a new API version — etcd-operator.
summary: Key features What changed compared to v1alpha1 Comparison with the official
  operator Posted on June 29, 2026 by Andrey Kolkov and Andrei Kvapil, Ænix CNCF projects
  highlighted in this post The etcd-operator project, which develops an operator for
  deploying and maintaining etcd clusters on Kubernetes, has been donated to the Cozystack
  project. Alongside the donation, a from-scratch implementation of the operator has
  been published under a new API version — etcd-operator. cozystack. io/v1alpha2,
  superseding the previous etcd. aenix. io/v1alpha1. Instead of managing members through
  a StatefulSet, the new implementation directly drives etcd’s native Membership API
  (the MemberAdd, MemberPromote and MemberRemove operations), giving the operator
  full control over cluster membership. The new implementation was written by Timofei
  Larkin , one of the maintainers of the previous codebase, which is preserved in
  the v1alpha1 branch. The project is written in Go and distributed under the Apache
  2.0 license. The project was started by Ænix, which assembled an initiative group
  from the Kubernetes community to build it. After the base implementation was completed,
  an attempt was made to donate the project to the CNCF. Prompted by this initiative,
  the etcd project concluded that an official operator was needed and formed its own
  working group, which, after evaluating existing implementations, chose to develop
  a codebase from scratch — this is how etcd-io/etcd-operator came to be.
---
Open the original post ↗ https://www.cncf.io/blog/2026/06/29/etcd-operator-joins-cozystack-with-a-new-v1alpha2-api/
