---
title: 'Blog: Spotlight on SIG Testing'
date: '2023-11-24T00:00:00+00:00'
tags:
- kubernetes
- community
source: Kubernetes.dev Blog
external_url: https://www.kubernetes.dev/blog/2023/11/24/sig-testing-spotlight-2023/
post_kind: link
draft: false
tldr: Spotlight on SIG Testing Meet the contributors Testing practices and tools Subprojects
  owned by SIG Testing Key challenges and accomplishments The people and the scope
  Looking ahead Welcome to another edition of the SIG spotlight blog series, where
  we highlight the incredible work being done by various Special Interest Groups (SIGs)
  within the Kubernetes project. In this edition, we turn our attention to SIG Testing
  , a group interested in effective testing of Kubernetes and automating away project
  toil.
summary: 'Spotlight on SIG Testing Meet the contributors Testing practices and tools
  Subprojects owned by SIG Testing Key challenges and accomplishments The people and
  the scope Looking ahead Welcome to another edition of the SIG spotlight blog series,
  where we highlight the incredible work being done by various Special Interest Groups
  (SIGs) within the Kubernetes project. In this edition, we turn our attention to
  SIG Testing , a group interested in effective testing of Kubernetes and automating
  away project toil. SIG Testing focus on creating and running tools and infrastructure
  that make it easier for the community to write and run tests, and to contribute,
  analyze and act upon test results. To gain some insights into SIG Testing, Sandipan
  Panda spoke with Michelle Shepardson , a senior software engineer at Google and
  a chair of SIG Testing, and Patrick Ohly , a software engineer and architect at
  Intel and a SIG Testing Tech Lead. Sandipan: Could you tell us a bit about yourself,
  your role, and how you got involved in the Kubernetes project and SIG Testing? Michelle:
  Hi! I’m Michelle, a senior software engineer at Google. I first got involved in
  Kubernetes through working on tooling for SIG Testing, like the external instance
  of TestGrid. I’m part of oncall for TestGrid and Prow, and am now a chair for the
  SIG. Patrick: Hello! I work as a software engineer and architect in a team at Intel
  which focuses on open source Cloud Native projects. When I ramped up on Kubernetes
  to develop a storage driver, my very first question was “how do I test it in a cluster
  and how do I log information?” That interest led to various enhancement proposals
  until I had (re)written enough code that also took over official roles as SIG Testing
  Tech Lead (for the E2E framework ) and structured logging WG lead. Sandipan: Testing
  is a field in which multiple approaches and tools exist; how did you arrive at the
  existing practices? Patrick: I can’t speak about the early days because I wasn’t
  around yet 😆, but looking back at some of the commit history it’s pretty obvious
  that developers just took what was available and started using it. For E2E testing,
  that was Ginkgo+Gomega. Some hacks were necessary, for example around cleanup after
  a test run and for categorising tests.'
---
Open the original post ↗ https://www.kubernetes.dev/blog/2023/11/24/sig-testing-spotlight-2023/
