---
title: 'Blog: E2E Testing Best Practices, Reloaded'
date: '2023-04-12T00:00:00+00:00'
tags:
- kubernetes
- community
source: Kubernetes.dev Blog
external_url: https://www.kubernetes.dev/blog/2023/04/12/e2e-testing-best-practices-reloaded/
post_kind: link
draft: false
tldr: End-to-end (E2E) testing in Kubernetes is how the project validates functionality
  with real clusters. Contributors sooner or later encounter it when asked to write
  E2E tests for new features or to help with debugging test failures.
summary: End-to-end (E2E) testing in Kubernetes is how the project validates functionality
  with real clusters. Contributors sooner or later encounter it when asked to write
  E2E tests for new features or to help with debugging test failures. Cluster admins
  or vendors might run the conformance tests, a subset of all tests in the E2E test
  suite. The underlying E2E framework for writing these E2E tests has been around
  for a long time. Functionality was added to it as needed, leading to code that became
  hard to maintain and use. The testing commons WG started cleaning it up, but dissolved
  before completely achieving their goals. After the migration to Gingko v2 in Kubernetes
  1. 25, I picked up several of the loose ends and started untangling them. This blog
  post is a summary of those changes. Some of this content is also found in the Kubernetes
  contributor document about writing good E2E tests and gets reproduced here to raise
  awareness that the document has been updated. At the moment, the framework is used
  in-tree for testing against a cluster ( test/e2e ), testing kubeadm ( test/e2e_kubeadm
  ) and kubelet ( test/e2e_node ). The goal is to make the core test/e2e/framework
  a package that has no dependencies on internal code and that can be used in different
  E2E suites without polluting them with features or options that make no sense for
  them.
---
Open the original post ↗ https://www.kubernetes.dev/blog/2023/04/12/e2e-testing-best-practices-reloaded/
