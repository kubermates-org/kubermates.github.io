---
title: 'Blog: Kubernetes 1.22 - Breaking change!'
date: '2022-04-22T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2022/04/22/kubernetes-1.22-tekton/
post_kind: link
draft: false
tldr: Kubernetes 1.22 - Breaking change! To allow Jenkins X to support Kubernetes
  1.22, we had to update our version of Tekton. This updated version of Tekton contains
  breaking changes that has consequences if you made your own custom Jenkins X pipelines.
summary: 'Kubernetes 1.22 - Breaking change! To allow Jenkins X to support Kubernetes
  1.22, we had to update our version of Tekton. This updated version of Tekton contains
  breaking changes that has consequences if you made your own custom Jenkins X pipelines.
  To make sure that your custom pipelines continue to work after this upgrade, you
  must edit the resource settings in your pipelines. Otherwise your pipelines will
  most likely not be able to start at all, or if they do, consume a lot of resources.
  Tekton made changes in how to calculate the resources needed to run a pipeline,
  in order to support the concept of LimitRange in Kubernetes (introduced in Kubernetes
  version 1.10). Previously, Tekton simply used the maximum requested cpu and memory
  of any single step, and set that as limits for the all steps in the pipeline. For
  more details, please read the Tekton documentation on LimitRange. In the Tekton
  pipeline files, the StepTemplate needs to be changed to not specify resource requests
  , but only setting an empty resource limits : requests limits stepTemplate : image
  : uses:jenkins-x/jx3-pipeline-catalog/tasks/go/release. yaml@a5ab19ebc5a074e0402c5016b11bc11b32cc5c83
  name : "" resources : # override limits for all containers here limits : {} stepTemplate
  : image : uses:jenkins-x/jx3-pipeline-catalog/tasks/go/release. yaml@a5ab19ebc5a074e0402c5016b11bc11b32cc5c83
  name : "" resources : # override limits for all containers here limits : {} The
  resource requests should be set on only one individual step: requests steps : -
  image : uses:Mentor-Medier/jx3-pipeline-catalog/tasks/git-clone/git-clone-pr. yaml@versionStream
  name : "" resources : {} - name : jx-variables resources : requests : cpu : 400m
  memory : 512Mi steps : - image : uses:Mentor-Medier/jx3-pipeline-catalog/tasks/git-clone/git-clone-pr.
  yaml@versionStream name : "" resources : {} - name : jx-variables resources : requests
  : cpu : 400m memory : 512Mi To see examples of what changes you need to apply to
  your custom pipelines you may investigate this PR on The Jenkins X pipeline catalog.'
---
Open the original post ↗ https://jenkins-x.io/blog/2022/04/22/kubernetes-1.22-tekton/
