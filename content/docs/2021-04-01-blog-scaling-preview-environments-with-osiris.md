---
title: 'Blog: Scaling Preview Environments with Osiris'
date: '2021-04-01T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2021/04/01/jx3-osiris-preview-envs/
post_kind: link
draft: false
tldr: 'One of Jenkins X’s core features is the preview environments : temporary environments
  created automatically for each Pull Requests, to deploy your application and its
  dependencies. You can then use this preview environment to run integration tests,
  or manually use/test your application.'
summary: 'One of Jenkins X’s core features is the preview environments : temporary
  environments created automatically for each Pull Requests, to deploy your application
  and its dependencies. You can then use this preview environment to run integration
  tests, or manually use/test your application. This is all great until you have more
  and more applications, each with a few dependencies (postgresql, mongodb, …) and
  a few opened pull requests at any time. This means that you’ll get more and more
  pods running in your Kubernetes cluster, in addition to Jenkins X’s own components,
  your build pipelines, and of course your staging and production applications - unless
  you are using multi-cluster. The result is that you’ll need more nodes or bigger
  nodes. Which means more money. But, these preview environments are in fact idle
  most of the time: they are only used for the integration tests, and sometimes when
  someone manually uses them. The rest of the time - including all night for example
  - they are just staying there, idle, and consuming resources. What if we could easily
  scale them down when they are idle, and automatically bring them up when we need
  them? So that a Pull Request staying opened for 2 weeks because someone went on
  vacation won’t consume resources in your cluster. Enter Osiris ! Initially created
  by the Deislabs team , Osiris is a Kubernetes component that will automatically
  scale down your “idle” pods, and scale them up when a request comes in. Although
  the original project has been archived, the Dailymotion team has taken over the
  maintenance of a fork. And they have been using it with success in their Jenkins
  X dev cluster for more than 2 years: they regularly have around 50 preview environments
  active at any time, and… 0 pods from these environments running at night - or on
  weekends.'
---
Open the original post ↗ https://jenkins-x.io/blog/2021/04/01/jx3-osiris-preview-envs/
