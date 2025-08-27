---
title: 'Blog: Prow and Tide for Kubernetes Contributors'
date: '2022-12-12T00:00:00+00:00'
tags:
- kubernetes
- community
source: Kubernetes.dev Blog
external_url: https://www.kubernetes.dev/blog/2022/12/12/prow-and-tide-for-kubernetes-contributors/
post_kind: link
draft: false
tldr: 'Authors: Chris Short , Frederico Muñoz In my work in the Kubernetes world,
  I look up a label or Prow command often. The systems behind the scenes ( Prow and
  Tide ) are here to help Kubernetes Contributors get stuff done.'
summary: 'Authors: Chris Short , Frederico Muñoz In my work in the Kubernetes world,
  I look up a label or Prow command often. The systems behind the scenes ( Prow and
  Tide ) are here to help Kubernetes Contributors get stuff done. Labeling which SIG,
  WG, or subproject is as important as the issue or PR having someone assigned. To
  quote the docs , “Tide is a Prow component for managing a pool of GitHub PRs that
  match a given set of criteria. It will automatically retest PRs that meet the criteria
  (’tide comes in’) and automatically merge them when they have up-to-date passing
  test results (’tide goes out’). ” What actually prompted this article is the awesomely
  amazing folks on the Contributor Comms team saying, “I need to squash my commits
  and push that. ” Which immediately made me remember the wonder of the Tide label:
  tide/merge-method-squash. Contributing to Kubernetes will, most of the time, involve
  some kind of git-based action, specifically on the Kubernetes GitHub. This can be
  an obstacle to those less exposed to git and/or GitHub, and is especially noticeable
  when we’re dealing with non-code contributions (documentation, blog posts, etc.
  ). When a contributor submits something, it will generally be through a pull request.
  When it comes to how the change will go from request to approval, there are a number
  of considerations that must be made, such as: These are some of the main tasks in
  which Tide will help, allowing us to use the GitHub interface for these tasks (and
  more), making the actions more visible to the community (since they are visible
  as plain comments in the GitHub discussion), and allowing us to manage contributions
  without necessarily having to clone git repositories or having to manually issue
  git commands.'
---
Open the original post ↗ https://www.kubernetes.dev/blog/2022/12/12/prow-and-tide-for-kubernetes-contributors/
