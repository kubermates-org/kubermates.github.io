---
title: 'Blog: Jenkins X 3.x - beta is close!'
date: '2020-12-04T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2020/12/04/jx-v3-update/
post_kind: link
draft: false
tldr: Jenkins X 3. x - beta is close! It has been ‘all hands on deck’ in recent months
  with the focus on Jenkins X 3 alpha.
summary: 'Jenkins X 3. x - beta is close! It has been ‘all hands on deck’ in recent
  months with the focus on Jenkins X 3 alpha. First off a huge thankyou to everyone
  involved. The OSS community spirit has really shone through what has been a very
  difficult year for everyone. Knowing that people from all over the world come and
  help each other, share banter and work at all hours of the day to help build out
  a true open source cloud native continuous delivery solution for developers - it’s
  quite fantastic to see and amazing to be apart of. As a result of all this hard
  work the Beta is iminent so this is a good opportunity to thank all involved so
  far and to outline what to expect in the coming days. While we’ve been in the Alpha
  phase it has provided us with the opportunity to deprecate and remove APIs, commands
  and obsolete features that existed in v2. This means we will not have any code dependency
  on the v2 codebase and so going forward v3 will be easier to maintain without the
  tech debt. With that, we aim to make a big push and roll out a few last changes
  in preparation for Beta, here’s a couple you will notice if you are already on the
  Alpha. We recommend taking time to understand these, and avoid upgrading for a few
  days so that changes can be handled in one go, as there will be a constant stream
  of larger updates happening: jx requirements - this is the yaml file used to describe
  install needs for Jenkins X, until now there have been options available that were
  unsupported, confusing and in some cases did nothing. These have now all been removed
  and the structure of the file has changed to be CRD like including an API version.
  Upon upgrade jx gitops upgrade will migrate your jx-requirements.'
---
Open the original post ↗ https://jenkins-x.io/blog/2020/12/04/jx-v3-update/
