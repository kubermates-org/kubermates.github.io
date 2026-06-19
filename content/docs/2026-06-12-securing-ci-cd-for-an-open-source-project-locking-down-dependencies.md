---
title: 'Securing CI/CD for an open source project: Locking down dependencies'
date: '2026-06-12T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/06/12/securing-ci-cd-for-an-open-source-project-locking-down-dependencies/
post_kind: link
draft: false
tldr: 'Part two Locking down dependencies Pinning GitHub Actions by SHA digest The
  same tradeoff applies to Go dependencies Catching mistakes with static analysis
  Posted on June 12, 2026 by André Martins (Cilium maintainer and Software Engineer,
  Isovalent at Cisco) and Feroz Salam (Cilium Security Team and Security Engineer,
  Isovalent at Cisco) CNCF projects highlighted in this post This is the second post
  in a three-part series on how Cilium hardens its CI/CD pipeline. Part 1 covered
  access control: who can trigger builds and what code CI is allowed to execute.'
summary: 'Part two Locking down dependencies Pinning GitHub Actions by SHA digest
  The same tradeoff applies to Go dependencies Catching mistakes with static analysis
  Posted on June 12, 2026 by André Martins (Cilium maintainer and Software Engineer,
  Isovalent at Cisco) and Feroz Salam (Cilium Security Team and Security Engineer,
  Isovalent at Cisco) CNCF projects highlighted in this post This is the second post
  in a three-part series on how Cilium hardens its CI/CD pipeline. Part 1 covered
  access control: who can trigger builds and what code CI is allowed to execute. This
  post covers the dependency layer: what code those builds pull in, and how we make
  sure it hasn’t been tampered with. Once you control who triggers builds, the next
  question is what code those builds pull in. A pinned workflow that fetches a compromised
  dependency is still a compromised workflow. The single highest-leverage thing any
  project can do here is stop trusting mutable tags. Every uses: directive in our
  workflow files references actions by full 40-character commit SHA, with the human-readable
  version stuck on the end as a comment: uses: - uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd
  # v6.0.2 - uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
  If somebody compromises the v6 tag on actions/checkout and force-pushes malicious
  code, our workflows won’t pull it. They’re pinned to a specific commit. Same story
  for every third-party action we use: docker/build-push-action, sigstore/cosign-installer,
  golangci/golangci-lint-action, and dozens more. We pin container images used directly
  in workflow steps the same way, by @sha256: digest, so even the tools we run inside
  CI are content-addressed. docker/build-push-action, sigstore/cosign-installer, golangci/golangci-lint-action,
  @sha256: Pinning has one annoying blind spot, which is transitive dependencies.
  When we pin actions/checkout@de0fac2e… we know exactly which code runs for that
  action.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/06/12/securing-ci-cd-for-an-open-source-project-locking-down-dependencies/
