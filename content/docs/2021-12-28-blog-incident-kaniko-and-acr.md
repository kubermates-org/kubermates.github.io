---
title: 'Blog: Incident: Kaniko and ACR'
date: '2021-12-28T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2021/12/28/kanikoacrandjenkinsx/
post_kind: link
draft: false
tldr: We’ve recently had an issue with one of our packages come to light. We wanted
  to talk through the resolution steps we’re going to put into place.
summary: 'We’ve recently had an issue with one of our packages come to light. We wanted
  to talk through the resolution steps we’re going to put into place. Azure users
  started reporting seeing the following error within the build step: This seemed
  to be indicating to an authorization issues with the terraform module. Other users
  were seemingly unaffected by this issue. Upon further analysis, kaniko seems to
  have issues with the latest version and grabbing credentials for acr. The latest
  working version that we are aware of is 1. 3. There wasn’t a massive influx of people
  seeing this issue due to it only occuring once versionstream had been updated with
  jx gitops upgrade. For starters, most users are probably using the latest kaniko
  features, so we’re unable to just roll this back for everyone. We’re getting started
  by creating a PR to kaniko to resolve the issue. However, due to release schedules
  etc, this will mean that getting started with azure will be broken for quite a while.
  If you’re on azure, the resolution is quite simple, here’s a step by step guide:
  1.'
---
Open the original post ↗ https://jenkins-x.io/blog/2021/12/28/kanikoacrandjenkinsx/
