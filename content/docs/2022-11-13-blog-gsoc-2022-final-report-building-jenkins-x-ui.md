---
title: 'Blog: GSoC 2022 Final Report: Building Jenkins X UI'
date: '2022-11-13T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2022/11/13/gsoc-2022-work-report/
post_kind: link
draft: false
tldr: 'GSoC 2022 Final Report: Building Jenkins X UI Jenkins X New UI Why need a new
  UI? How to use it? Work Done Stop a running or pending PipelineActivity from UI
  Show message with status of the PipelineActivity Implement a DAG for PipelineActivity
  What’s next? Acknowledgements It is a web application built with Golang for the
  backend and Sveltekit for the frontend, both of which are built together and used
  in the same container. To function properly, it must be installed as a helm chart
  with Jenkins X CRDs.'
summary: 'GSoC 2022 Final Report: Building Jenkins X UI Jenkins X New UI Why need
  a new UI? How to use it? Work Done Stop a running or pending PipelineActivity from
  UI Show message with status of the PipelineActivity Implement a DAG for PipelineActivity
  What’s next? Acknowledgements It is a web application built with Golang for the
  backend and Sveltekit for the frontend, both of which are built together and used
  in the same container. To function properly, it must be installed as a helm chart
  with Jenkins X CRDs. 🌟 It has light and dark themes. A good UI is essential for
  a CI/CD tool, as not everyone is familiar with the CLI. The current UI (jx-pipeline-visualizer)
  is a read-only UI, the user can view the logs of PipelineActivity but neither can
  start nor stop the pipeline. Features that the UI will provide: Start and Stop a
  PipelineActivity. Have an audit trail. A graphical representation of PipelineActivity.
  RBAC to limit access to certain functionalities. New Jenkins X UI focus on Simplicity,
  Security and a Superb User Experience. This is NOT GA (General Availability) yet.
  Visit the project repo here to try it.'
---
Open the original post ↗ https://jenkins-x.io/blog/2022/11/13/gsoc-2022-work-report/
