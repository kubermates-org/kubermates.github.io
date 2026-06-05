---
title: 'Securing CI/CD for an open source project: Controlling who runs what'
date: '2026-06-04T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/06/04/securing-ci-cd-for-an-open-source-project-controlling-who-runs-what/
post_kind: link
draft: false
tldr: Part one TL;DR Controlling who runs what Workflow trigger restrictions with
  Ariane Separating trusted and untrusted code in CI CODEOWNERS as a review gate Posted
  on June 4, 2026 by André Martins, Cilium maintainer and Software Engineer, Isovalent
  at Cisco and Feroz Salam, Cilium Security Team and a Security Engineer, Isovalent
  at Cisco. CNCF projects highlighted in this post The last twelve months have been
  rough on the open source supply chain.
summary: 'Part one TL;DR Controlling who runs what Workflow trigger restrictions with
  Ariane Separating trusted and untrusted code in CI CODEOWNERS as a review gate Posted
  on June 4, 2026 by André Martins, Cilium maintainer and Software Engineer, Isovalent
  at Cisco and Feroz Salam, Cilium Security Team and a Security Engineer, Isovalent
  at Cisco. CNCF projects highlighted in this post The last twelve months have been
  rough on the open source supply chain. Axios was compromised on npm and shipped
  a remote access trojan inside otherwise normal-looking releases. LiteLLM’s PyPI
  package was hijacked to exfiltrate environment variables. Typosquatted forks of
  Trivy were published to catch people who fat-finger go install. And the canonical
  example, the 2020 SolarWinds breach , is still the cautionary tale we keep coming
  back to: attackers got into the build system and pushed malware through normal Orion
  updates to roughly 18,000 organizations, including U. S. federal agencies, NATO,
  and Microsoft. The malware sat dormant for months. The breach went undetected for
  the better part of a year. Cilium runs in the kernel-level networking path of millions
  of Kubernetes pods. If our supply chain were compromised, the blast radius would
  not be small.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/06/04/securing-ci-cd-for-an-open-source-project-controlling-who-runs-what/
