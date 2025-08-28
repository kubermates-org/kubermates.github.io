---
title: 'Blog: Kubernetes 1.22 - Breaking change!'
date: '2022-04-22T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2022/04/22/kubernetes-1.22-tekton/
post_kind: link
draft: false
tldr: To allow Jenkins X to support Kubernetes 1. 22, we had to update our version
  of Tekton.
summary: 'To allow Jenkins X to support Kubernetes 1. 22, we had to update our version
  of Tekton. This updated version of Tekton contains breaking changes that has consequences
  if you made your own custom Jenkins X pipelines. To make sure that your custom pipelines
  continue to work after this upgrade, you must edit the resource settings in your
  pipelines. Otherwise your pipelines will most likely not be able to start at all,
  or if they do, consume a lot of resources. Tekton made changes in how to calculate
  the resources needed to run a pipeline, in order to support the concept of LimitRange
  in Kubernetes (introduced in Kubernetes version 1. 10). Previously, Tekton simply
  used the maximum requested cpu and memory of any single step, and set that as limits
  for the all steps in the pipeline. For more details, please read the Tekton documentation
  on LimitRange. In the Tekton pipeline files, the StepTemplate needs to be changed
  to not specify resource requests , but only setting an empty resource limits : The
  resource requests should be set on only one individual step: To see examples of
  what changes you need to apply to your custom pipelines you may investigate this
  PR on The Jenkins X pipeline catalog. The PR will be merged and released simultaneous
  with the upgrade of Tekton. In the current version of Tekton used by Jenkins X,
  the resource requests are set on the stepTemplate.'
---
Open the original post ↗ https://jenkins-x.io/blog/2022/04/22/kubernetes-1.22-tekton/
