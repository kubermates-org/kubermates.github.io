---
title: 'Blog: How to debug your Tekton pipelines'
date: '2021-08-18T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2021/08/18/debug-tekton/
post_kind: link
draft: false
tldr: 'How to debug your Tekton pipelines How to debug Tekton Pipelines Prerequisites
  Enable a breakpoint Viewing breakpoints Using a breakpoint Opening a shell Continuing
  after the breakpoint Removing breakpoints Conclusion Tekton recently introduced
  a debug feature when you create TaskRun resources so that steps can be paused at
  a breakpoint until told to move forwards so that you can diagnose why pipeline steps
  fail. TaskRun The latest Tekton release only supports breakpoints on TaskRun resources
  but there is a Pull Request #4145 to add support also to debugging PipelineRun resources
  as well.'
summary: 'How to debug your Tekton pipelines How to debug Tekton Pipelines Prerequisites
  Enable a breakpoint Viewing breakpoints Using a breakpoint Opening a shell Continuing
  after the breakpoint Removing breakpoints Conclusion Tekton recently introduced
  a debug feature when you create TaskRun resources so that steps can be paused at
  a breakpoint until told to move forwards so that you can diagnose why pipeline steps
  fail. TaskRun The latest Tekton release only supports breakpoints on TaskRun resources
  but there is a Pull Request #4145 to add support also to debugging PipelineRun resources
  as well. If you are reading this please add your thumbs up emoji feedback to the
  PR #4145 TaskRun PipelineRun We’ve switched Jenkins X to use a preview image of
  Tekton with PR #4145 included so that Jenkins X developers can easily debug their
  pipelines (which typically are PipelineRun resources). PipelineRun Here is a demo
  which shows how to debug pipelines: Make sure your cluster is upgraded to the latest
  version stream. If you intend to use the jx in the below examples make sure you
  upgrade the CLI too jx To enable a breakpoint you can: use the Lens UI as shown
  in the above video by: right click on a Pipeline action menu select Breakpoint ->
  Add right click on a Pipeline action menu Pipeline select Breakpoint -> Add Breakpoint
  -> Add you can use the jx pipeline debug command then select the pipeline to add/remove
  a breakpoint. You can view breakpoints in the Lens UI in the Breakpoints tab or
  via: Breakpoints kubectl get lighthousebreakpoints # you can use the short name:
  kubectl get lhbp kubectl get lighthousebreakpoints # you can use the short name:
  kubectl get lhbp Once you have set a breakpoint defined for a particular Pipeline
  you need to trigger the pipeline. e. g. perform a git commit on the git branch to
  trigger a new pipeline to execute. The pipeline will execute as normal; you’ll be
  able to view it execute via: Lens UI run jx pipeline grid to watch pipelines run
  and select the one you wish to view the log run jx pipeline log to watch the log
  of a specific pipeline Once your breakpoint is reached the pipeline pod will pause,
  waiting to continue. At this point you can then open a shell inside the container.
  The easiest way to do this is via the Lens UI , click on the Pipeline action menu
  then Shell -> latest step and a shell will open.'
---
Open the original post ↗ https://jenkins-x.io/blog/2021/08/18/debug-tekton/
