---
title: 'Blog: Moving Jenkins X v2 artifacts'
date: '2021-08-26T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2021/08/26/moving-v2-artifacts/
post_kind: link
draft: false
tldr: Moving Jenkins X v2 artifacts ACTION REQUIRED Why the disruption? What is changing?
  v2 users v3 users When will all this take place? Why are only the most recent versions
  v2 images copied to GitHub packages and not all versions? I’m on v2 and use a builder
  image which is not available on GitHub container registry, how do I build my own
  version to work with the new helm and image repositories? I’m getting a missing
  arg --provider-values-dir and helm repository https://jenkins-x-charts. github.
summary: Moving Jenkins X v2 artifacts ACTION REQUIRED Why the disruption? What is
  changing? v2 users v3 users When will all this take place? Why are only the most
  recent versions v2 images copied to GitHub packages and not all versions? I’m on
  v2 and use a builder image which is not available on GitHub container registry,
  how do I build my own version to work with the new helm and image repositories?
  I’m getting a missing arg --provider-values-dir and helm repository https://jenkins-x-charts.
  github. io/v2 does not have an associated prefix in in the ‘charts/repositories.
  yml’ error TL;DR - Jenkins X specific helm repositories and container registries
  hosted on GCP have been moved to GitHub. This will mainly affect jx v2 users but
  there is expected to be a small impact on v3 users too. Below describes the steps
  we believe are needed to keep Jenkins X installations working as normal but there
  will be some action needed. When Jenkins X first started we made heavy use of GCP’s
  services for hosting the cloud infrastructure needed by users to install and run
  Jenkins X. This was great as we could use the same IAM to push and maintain content
  from our own hosted build infrastructure and ensure we were validating the same
  experience of using cloud provider hosted services wherever possible. As Jenkins
  X grew in popularity the cloud costs began to increase with the pricing model from
  GCP , specifically the networking costs of cross continent egress. Given this, for
  jx3 we decided to see if switching to GitHub packages for container images and GitHub
  pages for helm repositories would be better, the result was it is better. In fact
  we have made it super easy for users to switch to using GitHub pages for releasing
  helm charts and using GitHub packages. Now that we have validated GitHub is more
  cost effective for hosting public images and helm charts for the Jenkins X project,
  we want to switch to using GitHub for all v2 plus v3 users, then shutdown the GCP
  services which are causing unnecessary cost.
---
Open the original post ↗ https://jenkins-x.io/blog/2021/08/26/moving-v2-artifacts/
