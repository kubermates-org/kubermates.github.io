---
title: 'Blog: K8s CI Bot Helper Job: automating "make update"'
date: '2022-03-15T00:00:00+00:00'
tags:
- kubernetes
- community
source: Kubernetes.dev Blog
external_url: https://www.kubernetes.dev/blog/2022/03/15/k8s-triage-bot-helper-ci-job/
post_kind: link
draft: false
tldr: 'Authors: Subhasmita Swain , Davanum Srinivas If you are contributing to the
  Kubernetes project and are developing on a Windows PC, it is conceivable that you
  will encounter certain issues that will cause your pull request to get held up by
  test failures. This article describes a workaround for a similar issue I encountered
  when attempting to have my modifications approved and merged into the master branch.'
summary: 'Authors: Subhasmita Swain , Davanum Srinivas If you are contributing to
  the Kubernetes project and are developing on a Windows PC, it is conceivable that
  you will encounter certain issues that will cause your pull request to get held
  up by test failures. This article describes a workaround for a similar issue I encountered
  when attempting to have my modifications approved and merged into the master branch.
  While contributing to kubernetes/kubernetes for some minor documentation changes,
  the pushed changes needed to be updated with other verified contents of the entire
  documentation. So, in order for the change to take effect, a single command must
  be performed to ensure that all tests on the CI pipeline pass. The single command
  make update runs all presubmission verification tests. For some reason on the “Windows
  Subsystem for Linux” environment the tests, specifically the update-openapi-spec.
  sh script, failed (in my case, take a look at the conversation here ), eventually
  failing the pull-kubernetes-verify tests. You might encounter the following on your
  PR The tests failing the particular issue: Consecutively, Additionally one can check
  the failed test via the link provided under details in the above image. Run the
  failing. sh scripts individually known from the CI job output, to generate the expected
  files to fix up the failures. The. sh scripts can be found residing under the hack/
  directory at the root of the kubernetes/kubernetes code base.'
---
Open the original post ↗ https://www.kubernetes.dev/blog/2022/03/15/k8s-triage-bot-helper-ci-job/
