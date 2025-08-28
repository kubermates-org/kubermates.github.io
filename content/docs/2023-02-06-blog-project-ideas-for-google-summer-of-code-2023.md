---
title: 'Blog: Project ideas for Google Summer of Code 2023 ☀️'
date: '2023-02-06T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2023/02/06/gsoc2023-ideas/
post_kind: link
draft: false
tldr: We have put together some project ideas as part of our application to participate
  in the Google Summer of Code 2023 program. The cdEvents project standardises the
  way systems talk to each other, which enables Interoperability between systems so
  they speak a common language through the cdEvents spec in the event.
summary: We have put together some project ideas as part of our application to participate
  in the Google Summer of Code 2023 program. The cdEvents project standardises the
  way systems talk to each other, which enables Interoperability between systems so
  they speak a common language through the cdEvents spec in the event. Creating a
  capability in Jenkins X that can receive and sent a cdEvent would benefit the project
  and the DevOps ecosystem in general, by stopping glue code used to integrate systems
  and power innovation by letting end users swap out tools with no effort. Jenkins
  X, Kubernetes, golang, cdEvents 350 hours Hard Jenkins X only applies changes to
  cluster when contents of the gitops repository changes as part of a git pull request
  or git commit. This does not satisfy one of the requirements of the gitops model
  where we need continuous reconciliation. It would be nice to detect drift between
  the current state (kubernetes) and the desired state (git) and apply only those
  changes. This has the side effect of making the boot job faster. Also, our bootjob
  is made up of a makefile which calls cli commands written in golang, instead it
  would be desirable to move to a controller based approach similar to other tools
  in the kubernetes ecosystem. Kubernetes, golang, Jenkins X, kubebuiler, basic understanding
  of gitops. 350 hours Hard In the last GSoC project, we created a modern UI which
  has more functionalities than the older viewer UI. However, as we added the ability
  to start/stop pipelines from the new UI, this opened up an issue around access.
  Users of Jenkins X would like to restrict who can start/stop pipelines from the
  UI.
---
Open the original post ↗ https://jenkins-x.io/blog/2023/02/06/gsoc2023-ideas/
