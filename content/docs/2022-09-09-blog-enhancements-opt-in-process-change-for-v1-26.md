---
title: 'Blog: Enhancements Opt-in Process Change for v1.26'
date: '2022-09-09T00:00:00+00:00'
tags:
- kubernetes
- community
source: Kubernetes.dev Blog
external_url: https://www.kubernetes.dev/blog/2022/09/09/enhancements-opt-in/
post_kind: link
draft: false
tldr: 'Enhancements Opt-in Process Change for v1.26 Context and Motivations How does
  the Github Project Board work? What does this mean for the community? Author: Grace
  Nguyen Since the inception of the Kubernetes release team, we have used a spreadsheet
  to keep track of enhancements for the release. The project has scaled massively
  in the past few years, with almost a hundred enhancements collected for the 1.24
  release.'
summary: 'Enhancements Opt-in Process Change for v1.26 Context and Motivations How
  does the Github Project Board work? What does this mean for the community? Author:
  Grace Nguyen Since the inception of the Kubernetes release team, we have used a
  spreadsheet to keep track of enhancements for the release. The project has scaled
  massively in the past few years, with almost a hundred enhancements collected for
  the 1.24 release. This process has become error-prone and time consuming. A lot
  of manual work is required from the release team and the SIG leads to populate KEPs
  data in the sheet. We have received continuous feedback from our contributors to
  streamline the process. Starting with the 1.26 release, we are replacing the enhancements
  tracking spreadsheet with an automated GitHub project board. The board is populated
  with a script gathering all KEP issues in the kubernetes/enhancements repo that
  have the label lead-opted-in. The enhancements’ stage and SIG information will also
  be automatically pulled from the KEP issue. kubernetes/enhancements lead-opted-in
  After the KEP is populated on the Github Project Board, the Enhancements team will
  manually update the KEP with the label tracked/yes , tracked/no and on occasions,
  tracked/out-of-tree. The tracked label signifies qualification for the closest approaching
  milestone. For example, at the beginning of the release, tracked/yes means that
  the KEP has satisfied all Enhancements Freeze requirements and similarly for Code
  Freeze, tracked/yes means that all code related to the KEP has been merged. The
  tracked label is reserved for the Enhancements team use only.'
---
Open the original post ↗ https://www.kubernetes.dev/blog/2022/09/09/enhancements-opt-in/
