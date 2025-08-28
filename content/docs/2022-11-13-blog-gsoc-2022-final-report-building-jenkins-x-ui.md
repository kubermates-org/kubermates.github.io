---
title: 'Blog: GSoC 2022 Final Report: Building Jenkins X UI'
date: '2022-11-13T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2022/11/13/gsoc-2022-work-report/
post_kind: link
draft: false
tldr: It is a web application built with Golang for the backend and Sveltekit for
  the frontend, both of which are built together and used in the same container. To
  function properly, it must be installed as a helm chart with Jenkins X CRDs.
summary: 'It is a web application built with Golang for the backend and Sveltekit
  for the frontend, both of which are built together and used in the same container.
  To function properly, it must be installed as a helm chart with Jenkins X CRDs.
  🌟 It has light and dark themes. A good UI is essential for a CI/CD tool, as not
  everyone is familiar with the CLI. The current UI (jx-pipeline-visualizer) is a
  read-only UI, the user can view the logs of PipelineActivity but neither can start
  nor stop the pipeline. Features that the UI will provide: New Jenkins X UI focus
  on Simplicity, Security and a Superb User Experience. This is NOT GA (General Availability)
  yet. Visit the project repo here to try it. We have added a button in pipelines
  page and pipelineDetails page, it asks for confirmation and on selecting Yes it
  will stop the PipelineActivity. We can stop the PipelineActivity from the pipelines
  tables. We can also stop the PipelineActivity from the pipelines details page. Issue:
  https://github.'
---
Open the original post ↗ https://jenkins-x.io/blog/2022/11/13/gsoc-2022-work-report/
