---
title: 'Blog: New UI to visualize your pipelines and logs'
date: '2020-09-23T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2020/09/23/jx-pipelines-visualizer/
post_kind: link
draft: false
tldr: 'Welcome to the Jenkins X Pipelines Visualizer : a new open-source read-only
  UI for Jenkins X, with a very specific goal and scope: visualize the pipelines and
  logs. This project was started at Dailymotion and quickly shared with the Jenkins
  X community.'
summary: 'Welcome to the Jenkins X Pipelines Visualizer : a new open-source read-only
  UI for Jenkins X, with a very specific goal and scope: visualize the pipelines and
  logs. This project was started at Dailymotion and quickly shared with the Jenkins
  X community. There is already the Octant-based UI , so why a new UI? The main reason
  is that Octant “is an application and is intended as a single client tool and at
  this time there are no plans to support hosted versions of Octant” - see this thread
  on the Octant github repository for more information and details. So while Octant
  answers to a lot of use-cases, there is one for which it is not suited: quickly
  printing the build logs on a browser, for a specific pipeline. We want to be able
  to click on a link from a Pull/Merge Request, and get the pipeline logs. This is
  the specific use-case covered by the Pipelines Visualizer. We want to keep it small,
  focused, and fast. It’s a read-only UI, so there won’t be “actions” to trigger a
  pipeline - because it can already be done using “chatops” commands in the Pull Request
  for example. But there are a few interesting features already: This project was
  shared very early with the community, after just a few hours of work. So our short-term
  goal is to improve the UI - make it beautiful. We did a demo of jx-pipelines-visualizer
  at the last office hours : Check out the jx-pipelines-visualizer github repository
  if you want to install it in your cluster - there is a Helm Chart which can be added
  to your Jenkins X Dev Environment. And any contributions are welcomed - either create
  an issue or pull request in the project’s github repository, or come in the #jenkins-x-dev
  Slack Channel.'
---
Open the original post ↗ https://jenkins-x.io/blog/2020/09/23/jx-pipelines-visualizer/
