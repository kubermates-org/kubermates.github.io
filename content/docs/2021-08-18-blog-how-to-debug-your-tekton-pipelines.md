---
title: 'Blog: How to debug your Tekton pipelines'
date: '2021-08-18T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2021/08/18/debug-tekton/
post_kind: link
draft: false
tldr: 'Tekton recently introduced a debug feature when you create TaskRun resources
  so that steps can be paused at a breakpoint until told to move forwards so that
  you can diagnose why pipeline steps fail. The latest Tekton release only supports
  breakpoints on TaskRun resources but there is a Pull Request #4145 to add support
  also to debugging PipelineRun resources as well.'
summary: 'Tekton recently introduced a debug feature when you create TaskRun resources
  so that steps can be paused at a breakpoint until told to move forwards so that
  you can diagnose why pipeline steps fail. The latest Tekton release only supports
  breakpoints on TaskRun resources but there is a Pull Request #4145 to add support
  also to debugging PipelineRun resources as well. If you are reading this please
  add your thumbs up emoji feedback to the PR #4145 We’ve switched Jenkins X to use
  a preview image of Tekton with PR #4145 included so that Jenkins X developers can
  easily debug their pipelines (which typically are PipelineRun resources). Here is
  a demo which shows how to debug pipelines: Make sure your cluster is upgraded to
  the latest version stream. If you intend to use the jx in the below examples make
  sure you upgrade the CLI too To enable a breakpoint you can: You can view breakpoints
  in the Lens UI in the Breakpoints tab or via: Once you have set a breakpoint defined
  for a particular Pipeline you need to trigger the pipeline. e. g. perform a git
  commit on the git branch to trigger a new pipeline to execute. The pipeline will
  execute as normal; you’ll be able to view it execute via: Once your breakpoint is
  reached the pipeline pod will pause, waiting to continue. At this point you can
  then open a shell inside the container. The easiest way to do this is via the Lens
  UI , click on the Pipeline action menu then Shell -> latest step and a shell will
  open. Otherwise you can use: If you wish to continue the execution of a pipeline
  there are multiple scripts you can run inside the shell you can run inside the shell
  in the pipeline to tell the pipeline to continue: There are a few ways to delete
  breakpoints.'
---
Open the original post ↗ https://jenkins-x.io/blog/2021/08/18/debug-tekton/
