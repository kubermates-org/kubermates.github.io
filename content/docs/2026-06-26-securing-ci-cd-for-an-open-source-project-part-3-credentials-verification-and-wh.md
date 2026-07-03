---
title: 'Securing CI/CD for an open source project, part 3: Credentials, verification,
  and what’s next'
date: '2026-06-26T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/06/26/securing-ci-cd-for-an-open-source-project-part-3-credentials-verification-and-whats-next/
post_kind: link
draft: false
tldr: 'Protecting credentials Strong defaults Signing and attesting what we ship The
  Cilium security team Additional layers What we’re still working on GitHub’s 2026
  Actions security roadmap and how it maps to what we do Dependency locking: making
  SHA pinning first-class Scoped secrets: closing the implicit inheritance gap Native
  egress firewall Actions data stream: making CI observable The point Posted on June
  26, 2026 by André Martins (Cilium maintainer and Software Engineer, Isovalent at
  Cisco) and Feroz Salam (Cilium Security Team and Security Engineer, Isovalent at
  Cisco) CNCF projects highlighted in this post This is the third and final post in
  a series on how Cilium hardens its CI/CD pipeline. Part 1 covered access control
  and Part 2 covered dependency hardening.'
summary: 'Protecting credentials Strong defaults Signing and attesting what we ship
  The Cilium security team Additional layers What we’re still working on GitHub’s
  2026 Actions security roadmap and how it maps to what we do Dependency locking:
  making SHA pinning first-class Scoped secrets: closing the implicit inheritance
  gap Native egress firewall Actions data stream: making CI observable The point Posted
  on June 26, 2026 by André Martins (Cilium maintainer and Software Engineer, Isovalent
  at Cisco) and Feroz Salam (Cilium Security Team and Security Engineer, Isovalent
  at Cisco) CNCF projects highlighted in this post This is the third and final post
  in a series on how Cilium hardens its CI/CD pipeline. Part 1 covered access control
  and Part 2 covered dependency hardening. This post covers the last layer: keeping
  CI and production credentials isolated, signing and attesting every release, and
  the gaps we’re still working to close. We assume any individual layer can fail.
  If a CI workflow ever gets compromised, it’s important the attacker can’t reach
  anything that matters. By default our GITHUB_TOKENs are scoped to minimal read permissions
  on contents and packages. Workflows that need anything more have to opt in explicitly,
  so a workflow that forgets to declare permissions doesn’t end up with broad org-wide
  write access. GITHUB_TOKENs We keep two distinct sets of registry credentials behind
  separate GitHub protected environments : CI credentials can push to our development
  image registry ( quay. io/cilium/*-ci ) and are available to CI builds. Even if
  a CI workflow is compromised somehow, these credentials cannot push to production
  image tags. quay. io/cilium/*-ci Production credentials sit behind the release environment
  , which requires an explicit maintainer approval before a workflow run can touch
  them.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/06/26/securing-ci-cd-for-an-open-source-project-part-3-credentials-verification-and-whats-next/
