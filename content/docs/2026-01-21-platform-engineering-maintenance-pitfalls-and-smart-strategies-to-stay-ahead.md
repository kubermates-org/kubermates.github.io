---
title: Platform engineering maintenance pitfalls and smart strategies to stay ahead
date: '2026-01-21T15:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/01/21/platform-engineering-maintenance-pitfalls-and-smart-strategies-to-stay-ahead/
post_kind: link
draft: false
tldr: Catching Up With Software Upstream Changes Controlling the Supply Chain Keeping
  Up With Kubernetes Upgrades Maintaining Helm Chart Upgrades Maintaining Applications
  With Persistent Data The Necessity of Runtime Validation Final Thoughts Posted on
  January 21, 2026 by Jehoszafat Zimnowoda, Senior Software Engineer, Akamai and Matthias
  Erll, Senior Software Engineer, Akamai CNCF projects highlighted in this post Platform
  engineering is a discipline that aims to increase the productivity of software engineering
  teams by designing, building, and maintaining internal platforms that abstract underlying
  infrastructure complexity and provide self-service capabilities. Kubernetes-based
  platforms are often complex multi-Open Source Software (OSS) integrations; thus,
  platform engineering is not a “declare once and forget it” process.
summary: 'Catching Up With Software Upstream Changes Controlling the Supply Chain
  Keeping Up With Kubernetes Upgrades Maintaining Helm Chart Upgrades Maintaining
  Applications With Persistent Data The Necessity of Runtime Validation Final Thoughts
  Posted on January 21, 2026 by Jehoszafat Zimnowoda, Senior Software Engineer, Akamai
  and Matthias Erll, Senior Software Engineer, Akamai CNCF projects highlighted in
  this post Platform engineering is a discipline that aims to increase the productivity
  of software engineering teams by designing, building, and maintaining internal platforms
  that abstract underlying infrastructure complexity and provide self-service capabilities.
  Kubernetes-based platforms are often complex multi-Open Source Software (OSS) integrations;
  thus, platform engineering is not a “declare once and forget it” process. It requires
  continuous dependency maintenance and strategies for inevitable breaking changes.
  In this blog post, we’ll go over the integration of fourteen OSS projects to maintain
  the platform that is built on top of a Kubernetes cluster. We explore the following
  challenges: Catching up with software upstream changes Controlling the supply chain
  Keeping up with Kubernetes upgrades Maintaining Helm chart upgrades Maintaining
  Applications with persistent data The necessity of runtime validation For this article,
  we have analyzed the last three years of releases for the following OSS projects:
  argo-cd , knative-serving , istio , harbor , keycloak , cloudnative-pg , gitea ,
  ingress-nginx , grafana , sealed-secrets , kyverno , prometheus , external-dns ,
  and cert-manager. Based on our experience and analysis, you can expect between 2-5
  major upgrades, 43-52 minor upgrades, and 276-327 software patches every year. That’s
  nearly an update a day! A significant challenge arises from the responsibility of
  maintaining a robust security posture. Every day, a number of security vulnerabilities
  are discovered. They are addressed in upstream projects that your platform needs
  to apply as security patches. This significantly contributes to the number of patches
  from the diagram above. Such changes must be monitored and quickly adopted into
  your platform. In line with this, a project or its chart maintainers may opt to
  stop maintaining previous versions and only provide an upgrade path towards the
  latest major release, which effectively marks an older major version as end-of-life.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/01/21/platform-engineering-maintenance-pitfalls-and-smart-strategies-to-stay-ahead/
