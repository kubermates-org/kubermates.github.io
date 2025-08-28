---
title: 'Blog: GitOps your cloud native pipelines'
date: '2021-02-25T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2021/02/25/gitops-pipelines/
post_kind: link
draft: false
tldr: 'GitOps your cloud native pipelines The problem Previous solutions GitOps your
  pipelines Sharing Tasks and Steps across repositories SourceURI notation Reusing
  Tasks and Steps from Tekton Catalog How it looks Customizing an inherited step Inlining
  a pipeline step locally Viewing the effective pipeline Summary Tekton pipelines
  are cloud native and are designed from the ground up for kubernetes and the cloud:
  there’s no single point of failure and the pipelines are elastically scalable each
  pipeline is completely declarative and self defined each pipeline executes independently
  of any others pipelines are orchestrated via the sophisticated kubernetes scheduler:
  can use pipeline specific metadata for resource limits and node selectors: memory,
  CPU, machine type (GPU, windows/macOS/linux etc) can use pipeline specific metadata
  for resource limits and node selectors: memory, CPU, machine type (GPU, windows/macOS/linux
  etc) its easy to associate pipelines with Cloud IAM roles to avoid you having to
  upload cluster admin secrets to your public CI service which really helps security
  and helps reduce accidental bitcoin mining on your cloud account In a previous blog
  we talked about how you can accelerate your use of tekton with Jenkins X. We are
  moving towards a microservice kind of world with many teams writing many bits of
  software in many repositories.'
summary: 'GitOps your cloud native pipelines The problem Previous solutions GitOps
  your pipelines Sharing Tasks and Steps across repositories SourceURI notation Reusing
  Tasks and Steps from Tekton Catalog How it looks Customizing an inherited step Inlining
  a pipeline step locally Viewing the effective pipeline Summary Tekton pipelines
  are cloud native and are designed from the ground up for kubernetes and the cloud:
  there’s no single point of failure and the pipelines are elastically scalable each
  pipeline is completely declarative and self defined each pipeline executes independently
  of any others pipelines are orchestrated via the sophisticated kubernetes scheduler:
  can use pipeline specific metadata for resource limits and node selectors: memory,
  CPU, machine type (GPU, windows/macOS/linux etc) can use pipeline specific metadata
  for resource limits and node selectors: memory, CPU, machine type (GPU, windows/macOS/linux
  etc) its easy to associate pipelines with Cloud IAM roles to avoid you having to
  upload cluster admin secrets to your public CI service which really helps security
  and helps reduce accidental bitcoin mining on your cloud account In a previous blog
  we talked about how you can accelerate your use of tekton with Jenkins X. We are
  moving towards a microservice kind of world with many teams writing many bits of
  software in many repositories. So there are lots and lots of pipelines. These pipelines
  keep getting more sophisticated over time; doing much more (all kinds of building,
  analysis, reporting, testing, ChatOps etc) and the software/images/approaches they
  use change. So how can we manage, configure and maintain them all so that there
  are many pipelines for many repositories; where each repository can customise anything
  it needs but we can easily maintain everything continuously and its easy to understand
  and tool around? We’ve tried to tackle this problem in a number of ways over the
  years; each has pros and cons. One option is to put all your pipelines in a shared
  library. You can then reference the pipelines by name in each of your repositories.
  But what if you want to change a bit of a pipeline for a specific repository? If
  you change it globally for everyone you can break things. You may just want local
  customisation for your repository only. You can add parameters into your pipelines.
  They are quite verbose on Pipelines and PipelineRuns ; but it’s hard to think up
  front of every parameterisation that may be required by downstream repositories.
  e.'
---
Open the original post ↗ https://jenkins-x.io/blog/2021/02/25/gitops-pipelines/
