---
title: 'Blog: Project ideas for Google Summer of Code 2022 ☀️'
date: '2022-02-20T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2022/02/20/gsoc2022-ideas/
post_kind: link
draft: false
tldr: Project ideas for Google Summer of Code 2022 ☀️ 1. Cloud events integration
  with Jenkins X 2.
summary: 'Project ideas for Google Summer of Code 2022 ☀️ 1. Cloud events integration
  with Jenkins X 2. Supply chain security: Improve integration with sigstore and look
  at tekton chains 3. New Jenkins X UI 4. Quickstart Improvements 5. Implement drift
  detection (gitops) 6. Multi-tenancy in Jenkins X Next Steps We have put together
  some project ideas as part of our application to participate in the Google Summer
  of Code 2022 program. The only way to trigger jobs/workflows in Jenkins X at the
  moment is by listening to events from Source Control Management (SCM) providers
  like github, gitlab, bitbucket, however it would be nice to listen to other event
  sources and trigger jobs/pipelines in Jenkins X. One interesting application would
  be to trigger some Jenkins X job in response to some alerting event (pagerduty,
  opsgenie). As a start we should focus on (emitting and listening to) cloudevents
  which define a common format for events produced from different sources. This will
  also help make Jenkins X compatible with other platforms. Jenkins X should be able
  to emit cloud events Jenkins X should be able to listen to cloud events, and run
  pipelines Updated documentation Golang, kubernetes, cloudevents, familiarity with
  lighthouse would be great, but not required Ankit D Mohapatra Christopher Vig Tom
  Hobson https://cloudevents.'
---
Open the original post ↗ https://jenkins-x.io/blog/2022/02/20/gsoc2022-ideas/
