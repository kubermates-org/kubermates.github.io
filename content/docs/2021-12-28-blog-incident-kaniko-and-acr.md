---
title: 'Blog: Incident: Kaniko and ACR'
date: '2021-12-28T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2021/12/28/kanikoacrandjenkinsx/
post_kind: link
draft: false
tldr: 'Incident: Kaniko and ACR So what happened? So what are you going to do about
  it? How can I fix it in the meantime? We’re hoping to make this simpler Help us
  find and fix things like this in future We’ve recently had an issue with one of
  our packages come to light. We wanted to talk through the resolution steps we’re
  going to put into place.'
summary: 'Incident: Kaniko and ACR So what happened? So what are you going to do about
  it? How can I fix it in the meantime? We’re hoping to make this simpler Help us
  find and fix things like this in future We’ve recently had an issue with one of
  our packages come to light. We wanted to talk through the resolution steps we’re
  going to put into place. Azure users started reporting seeing the following error
  within the build step: error checking push permissions -- make sure you entered
  the correct tag name, and that you are authenticated correctly, and try again: checking
  push permission for "xyz. azurecr. io/myorg/myrepo:0.0.1": resolving authorization
  for xyz. azurecr. io failed: error getting credentials - err: exec: "docker-credential-acr-env":
  executable file not found in $PATH error checking push permissions -- make sure
  you entered the correct tag name, and that you are authenticated correctly, and
  try again: checking push permission for "xyz. azurecr. io/myorg/myrepo:0.0.1": resolving
  authorization for xyz. azurecr. io failed: error getting credentials - err: exec:
  "docker-credential-acr-env": executable file not found in $PATH This seemed to be
  indicating to an authorization issues with the terraform module. Other users were
  seemingly unaffected by this issue.'
---
Open the original post ↗ https://jenkins-x.io/blog/2021/12/28/kanikoacrandjenkinsx/
