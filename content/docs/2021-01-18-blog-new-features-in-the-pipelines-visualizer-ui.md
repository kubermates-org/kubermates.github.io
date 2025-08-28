---
title: 'Blog: New features in the pipelines visualizer UI'
date: '2021-01-18T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2021/01/18/jx-pipelines-visualizer-v1/
post_kind: link
draft: false
tldr: The Jenkins X Pipelines Visualizer UI has recently received a number of new
  features, so let’s do a little tour of these new features! When viewing a pipeline,
  the biggest new feature is the collapsed logs. No more hundreds - or thousands -
  of log lines, we now group the logs per-container (step), which are collapsed by
  default.
summary: 'The Jenkins X Pipelines Visualizer UI has recently received a number of
  new features, so let’s do a little tour of these new features! When viewing a pipeline,
  the biggest new feature is the collapsed logs. No more hundreds - or thousands -
  of log lines, we now group the logs per-container (step), which are collapsed by
  default. Along with the status of the step and its duration, so it’s easier to go
  to the interesting part of the logs. Clicking on a log line will expand the logs
  for this specific container. You can also use the “Toggle Steps” button to expand/collapse
  the logs for all the steps at once. While we’re talking about the logs, you can
  notice the 2 new buttons: On top of the logs, we now display some information about
  the pipeline: The pipeline timeline has been improved to include all the steps for
  all stages, but it is currently hidden by default - to avoid using too much space.
  Clicking on a stage will bring you to the steps, and clicking on a step will bring
  you to the logs for this step. Note that for a pipeline which includes a deployment
  to a Preview Environment, the UI will also display a link to the application’s URL
  in that specific Preview Environment. The homepage got some love too, with: We started
  this project at v0, and we believe that now it has enough features to be a v1! On
  our roadmap - without any specific order - we have: Thanks to all the contributors!
  All contributions are welcomed, the source code is: github. com/jenkins-x/jx-pipelines-visualizer.'
---
Open the original post ↗ https://jenkins-x.io/blog/2021/01/18/jx-pipelines-visualizer-v1/
