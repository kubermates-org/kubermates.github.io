---
title: 'Blog: Don''t use docker, use kubernetes'
date: '2021-05-17T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2021/05/17/dont-use-docker/
post_kind: link
draft: false
tldr: Are you developing software that’s intended to run on kubernetes? If so we recommend
  not to use docker on your laptop. Docker on Windows/MacOS helps you run a VM that
  can then run linux containers easily.
summary: Are you developing software that’s intended to run on kubernetes? If so we
  recommend not to use docker on your laptop. Docker on Windows/MacOS helps you run
  a VM that can then run linux containers easily. But why bother? We highly recommend
  just use a development kubernetes cluster - build and run your containers there
  instead then you’re closer to a production like environment. First you’ll need a
  kubernetes cluster. I fully agree with James Ward that developers should not need
  to run kubernetes. Friends don’t let friends setup and manage kubernetes clusters
  by hand :). So try ask your infrastructure team for a development cluster or, if
  you can, use the cloud to set-up a managed kubernetes cluster. All the public clouds
  have a relatively straightforward way to spin up a fully managed kubernetes cluster
  for you that will be relatively inexpensive & they are easy to scale down when you
  don’t need them. e. g. on Google Cloud it’s a couple of clicks and about 5 minutes
  later you’ll have a fully managed kubernetes cluster ready to use. Its easy to enable
  auto-scaling too.
---
Open the original post ↗ https://jenkins-x.io/blog/2021/05/17/dont-use-docker/
