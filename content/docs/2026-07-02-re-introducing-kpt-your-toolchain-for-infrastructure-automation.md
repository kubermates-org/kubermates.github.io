---
title: '(re)introducing kpt: Your toolchain for infrastructure automation'
date: '2026-07-02T15:01:38+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/07/02/reintroducing-kpt-your-toolchain-for-infrastructure-automation/
post_kind: link
draft: false
tldr: What is kpt? package-centric toolchain WYSIWYG configuration authoring, automation,
  and delivery managing Kubernetes platforms and KRM-driven infrastructure manipulating
  declarative Configuration as Data Why do we need it? Use cases for kpt Current status
  and plans Join us! Posted on July 2, 2026 by Ciaran Johnston, Ericsson CNCF projects
  highlighted in this post The opening tagline of the kpt documentation describes
  it as “… a package-centric toolchain that enables a WYSIWYG configuration authoring,
  automation, and delivery experience, which simplifies managing Kubernetes platforms
  and KRM-driven infrastructure at scale by manipulating declarative Configuration
  as Data. ” This is a concise and detailed description of kpt, but sometimes it feels
  like it was written by a lawyer, or a consultant on a per-industry-buzzword contract.
summary: What is kpt? package-centric toolchain WYSIWYG configuration authoring, automation,
  and delivery managing Kubernetes platforms and KRM-driven infrastructure manipulating
  declarative Configuration as Data Why do we need it? Use cases for kpt Current status
  and plans Join us! Posted on July 2, 2026 by Ciaran Johnston, Ericsson CNCF projects
  highlighted in this post The opening tagline of the kpt documentation describes
  it as “… a package-centric toolchain that enables a WYSIWYG configuration authoring,
  automation, and delivery experience, which simplifies managing Kubernetes platforms
  and KRM-driven infrastructure at scale by manipulating declarative Configuration
  as Data. ” This is a concise and detailed description of kpt, but sometimes it feels
  like it was written by a lawyer, or a consultant on a per-industry-buzzword contract.
  Let’s break it down. Kpt works on packages – specifically bundles of Kubernetes
  Resource Model (KRM) files, declarative YAML manifests that define the desired state
  of cluster resources for Kubernetes (or Kubernetes Operator extensions) to continuously
  reconcile. These are pretty lightweight – they can be a directory on your computer,
  a zip file, or (most typically, given the GitOps nature of kpt) the contents of
  a git repository or git repository subfolder. Kpt is a CLI, but also provides a
  number of tools – validators and mutators – that can be executed in a kpt pipeline
  to verify and / or modify the contents of a kpt package. What You See Is What You
  Get is more typically associated with graphical editing tools or print-friendly
  editors. In this context, it refers to the fact that the kpt file contents you have
  at any point in time are exactly the resources that will end up in your cluster
  – they are not modified out-of-band on the way to the cluster, nor do they depend
  on external templates or metamodels. kpt supports the full lifecycle of a package
  of kubernetes resource descriptors. The CLI supports bootstrapping a new package
  with the basic content and configuration templates, while kpt pipelines provide
  a mechanism to automate the process of specializing those templates into site-specific
  parameterized packages, potentially across hundreds of different sites. Kpt also
  supports the package review and validation processes required to ensure configuration
  correctness before applying to live networks. Finally, kpt can be used to deploy
  packages to a live environment, monitoring their reconciliation status as it does
  so.
---
Open the original post ↗ https://www.cncf.io/blog/2026/07/02/reintroducing-kpt-your-toolchain-for-infrastructure-automation/
