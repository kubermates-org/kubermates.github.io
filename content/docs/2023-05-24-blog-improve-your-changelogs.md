---
title: 'Blog: Improve your changelogs'
date: '2023-05-24T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2023/05/24/propagate-changelogs/
post_kind: link
draft: false
tldr: Improve your changelogs Background Overview of major improvements Example How
  to write commit messages Manually edit changelog Configuration Changelog for cluster
  repository Reuse pull requests Custom pipelines Jira as issue tracker More customizations
  References A standard part of the Jenkins X pipelines since a long time is the execution
  of jx changelog create that takes the commit messages between the release currently
  being created and the previous one and creates a change log from these. The change
  log is then stored as a release note in GitHub or other git provider.
summary: 'Improve your changelogs Background Overview of major improvements Example
  How to write commit messages Manually edit changelog Configuration Changelog for
  cluster repository Reuse pull requests Custom pipelines Jira as issue tracker More
  customizations References A standard part of the Jenkins X pipelines since a long
  time is the execution of jx changelog create that takes the commit messages between
  the release currently being created and the previous one and creates a change log
  from these. The change log is then stored as a release note in GitHub or other git
  provider. jx changelog create During the last year some improvements have landed
  in various Jenkins X components to improve the changelogs and their usefulness.
  So I’ll take this opportunity to describe these improvements and also in general
  give hints to how to get useful changelogs. Changelogs haven’t been very informative
  with regard to upgrades, ie those applied with jx promote or jx updatebot. One example
  of this is the release notes of jx after the split out of most functionality to
  plugins. Lately these have improved due to new functionality to propagate changelogs
  via pull requests. jx promote jx updatebot One place where changelogs have been
  completely lacking is in cluster repositories. But using the functionality for propagation
  of changelogs and some changes in jx boot job you can now a get a changelog for
  every successful application of changes in a cluster. An example of what this functionality
  achieves can be seen in a release of jx: https://github. com/jenkins-x/jx/releases/tag/v3.10.81
  If you scroll past the boilerplate installation instructions you first see the changelog
  of jx itself generated from commit messages: https://github. com/jenkins-x/jx/compare/v3.10.80.'
---
Open the original post ↗ https://jenkins-x.io/blog/2023/05/24/propagate-changelogs/
