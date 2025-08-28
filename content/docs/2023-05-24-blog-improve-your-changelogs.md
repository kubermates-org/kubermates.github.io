---
title: 'Blog: Improve your changelogs'
date: '2023-05-24T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2023/05/24/propagate-changelogs/
post_kind: link
draft: false
tldr: A standard part of the Jenkins X pipelines since a long time is the execution
  of jx changelog create that takes the commit messages between the release currently
  being created and the previous one and creates a change log from these. The change
  log is then stored as a release note in GitHub or other git provider.
summary: 'A standard part of the Jenkins X pipelines since a long time is the execution
  of jx changelog create that takes the commit messages between the release currently
  being created and the previous one and creates a change log from these. The change
  log is then stored as a release note in GitHub or other git provider. During the
  last year some improvements have landed in various Jenkins X components to improve
  the changelogs and their usefulness. So I’ll take this opportunity to describe these
  improvements and also in general give hints to how to get useful changelogs. Changelogs
  haven’t been very informative with regard to upgrades, ie those applied with jx
  promote or jx updatebot. One example of this is the release notes of jx after the
  split out of most functionality to plugins. Lately these have improved due to new
  functionality to propagate changelogs via pull requests. One place where changelogs
  have been completely lacking is in cluster repositories. But using the functionality
  for propagation of changelogs and some changes in jx boot job you can now a get
  a changelog for every successful application of changes in a cluster. An example
  of what this functionality achieves can be seen in a release of jx: https://github.
  com/jenkins-x/jx/releases/tag/v3. 10.'
---
Open the original post ↗ https://jenkins-x.io/blog/2023/05/24/propagate-changelogs/
