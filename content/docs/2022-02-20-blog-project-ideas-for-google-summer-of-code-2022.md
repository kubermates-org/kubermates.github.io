---
title: 'Blog: Project ideas for Google Summer of Code 2022 ☀️'
date: '2022-02-20T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2022/02/20/gsoc2022-ideas/
post_kind: link
draft: false
tldr: Jenkins X has been accepted into the Google Summer of Code 2022 program, take
  a look at the follow up blog. Project proposal template can be found here.
summary: Jenkins X has been accepted into the Google Summer of Code 2022 program,
  take a look at the follow up blog. Project proposal template can be found here.
  We have put together some project ideas as part of our application to participate
  in the Google Summer of Code 2022 program. The only way to trigger jobs/workflows
  in Jenkins X at the moment is by listening to events from Source Control Management
  (SCM) providers like github, gitlab, bitbucket, however it would be nice to listen
  to other event sources and trigger jobs/pipelines in Jenkins X. One interesting
  application would be to trigger some Jenkins X job in response to some alerting
  event (pagerduty, opsgenie). As a start we should focus on (emitting and listening
  to) cloudevents which define a common format for events produced from different
  sources. This will also help make Jenkins X compatible with other platforms. Golang,
  kubernetes, cloudevents, familiarity with lighthouse would be great, but not required
  350 hours Hard With all the software breach that has happened recently, it has become
  necessary to add tooling to solve the issue around supply chain security. There
  are some good open source tools which can help with that (sigstore tools). As a
  CI/CD platform, Jenkins X needs to be integrated with them so that the end users
  can get this feature out of the box. Jenkins X leverages tekton as it’s pipeline
  execution engine. However, we dont integrate with tekton chain yet.
---
Open the original post ↗ https://jenkins-x.io/blog/2022/02/20/gsoc2022-ideas/
