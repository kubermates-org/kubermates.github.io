---
title: 'Blog: New UI to visualize your pipelines and logs'
date: '2020-09-23T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2020/09/23/jx-pipelines-visualizer/
post_kind: link
draft: false
tldr: 'New UI to visualize your pipelines and logs Why a new UI? Features Roadmap
  Demo Next steps Welcome to the Jenkins X Pipelines Visualizer : a new open-source
  read-only UI for Jenkins X, with a very specific goal and scope: visualize the pipelines
  and logs. This project was started at Dailymotion and quickly shared with the Jenkins
  X community.'
summary: 'New UI to visualize your pipelines and logs Why a new UI? Features Roadmap
  Demo Next steps Welcome to the Jenkins X Pipelines Visualizer : a new open-source
  read-only UI for Jenkins X, with a very specific goal and scope: visualize the pipelines
  and logs. This project was started at Dailymotion and quickly shared with the Jenkins
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
  for example. But there are a few interesting features already: first, it’s very
  fast to get the logs. Much faster than the old JXUI. it can retrieve the logs from
  pipelines that have been garbage-collected - if you configure the URL of the buckets
  where the logs are stored. it has URLs compatible with the old JXUI - so it’s very
  easy to replace the old JXUI with this new UI and keep all the links working.'
---
Open the original post ↗ https://jenkins-x.io/blog/2020/09/23/jx-pipelines-visualizer/
