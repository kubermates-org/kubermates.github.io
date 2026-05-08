---
title: 'Securing GitHub Actions CI dependencies: Recipe card'
date: '2026-05-04T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/05/04/securing-github-actions-ci-dependencies-recipe-card/
post_kind: link
draft: false
tldr: 'TLDR: Utensils: Tools for cooking up a release A word of caution in the kitchen
  The Recipe: Step-by-step instructions Evaluate before using (source your ingredients)
  Pin your dependencies and runner images (protect your tools) Automatically update
  your dependencies (keeping it fresh) Self hosted runners vs GitHub Runners (choose
  your kitchen) Posted on May 4, 2026 by Marina Moore, Evan Anderson, and Sherine
  Khoury, CNCF Technical Advisory Group CNCF projects highlighted in this post 🗹 Source
  the Best Ingredients: Evaluate before using / Trust the source: Prefer actions from
  trusted organisations (or GitHub org itself) 🗹 Measure precisely: Limit permissions
  and access to the minimum necessary for the action 🗹 Protect your tools: Pin your
  dependencies and runner images 🗹 Keep it fresh: Automatically update your dependencies
  and images 🗹 Choose your kitchen: Evaluate self hosted runners vs GitHub hosted
  runners As a quick summary, here are specific tools mentioned in this post, along
  with their capabilities: Running a third-party action is equivalent to cloning its
  code and executing it inside your own permission space. A tainted dependency can
  spoil the entire dish by exposing build secrets, tampering with the recipe (modifying
  code), or hijacking your serving infrastructure (package publishing), all without
  a noticeable change in the workflow or original ingredients.'
summary: 'TLDR: Utensils: Tools for cooking up a release A word of caution in the
  kitchen The Recipe: Step-by-step instructions Evaluate before using (source your
  ingredients) Pin your dependencies and runner images (protect your tools) Automatically
  update your dependencies (keeping it fresh) Self hosted runners vs GitHub Runners
  (choose your kitchen) Posted on May 4, 2026 by Marina Moore, Evan Anderson, and
  Sherine Khoury, CNCF Technical Advisory Group CNCF projects highlighted in this
  post 🗹 Source the Best Ingredients: Evaluate before using / Trust the source: Prefer
  actions from trusted organisations (or GitHub org itself) 🗹 Measure precisely: Limit
  permissions and access to the minimum necessary for the action 🗹 Protect your tools:
  Pin your dependencies and runner images 🗹 Keep it fresh: Automatically update your
  dependencies and images 🗹 Choose your kitchen: Evaluate self hosted runners vs GitHub
  hosted runners As a quick summary, here are specific tools mentioned in this post,
  along with their capabilities: Running a third-party action is equivalent to cloning
  its code and executing it inside your own permission space. A tainted dependency
  can spoil the entire dish by exposing build secrets, tampering with the recipe (modifying
  code), or hijacking your serving infrastructure (package publishing), all without
  a noticeable change in the workflow or original ingredients. It’s just like cooking
  your favorite meal in a messy kitchen, with leaky plumbing, slippery floors and
  dirty kitchenware: A disaster is just lurking around the corner. The solarwinds
  attack is probably one of the most (in)famous in the series of supply chain attacks
  on CI dependencies. More recently the tj-actions/changed-files GitHub action was
  also compromised , not to mention hackerbot-claw exploiting github actions for trivy,
  datadog and others. Prefer actions directly provided by GitHub, or those from verified
  organisations. In the GitHub Marketplace , Actions with the “Verified” badge indicate
  that GitHub has verified the creator of the action as a partner organization. When
  choosing actions, particularly from unverified organizations, favor those with regular
  and recent updates and an active community that addresses issues regularly. Adopters,
  project longevity, stars, contributors and forks are quick ways to compare actions,
  but can be manipulated. Adopters and longevity are the best metrics. If badges are
  published, these can give you an indicator if last builds or tests are passing,
  results of code coverage, static code analysis, etc. It can be difficult to test
  Actions, so effort put in here is a strong sign of good practices.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/05/04/securing-github-actions-ci-dependencies-recipe-card/
