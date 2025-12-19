---
title: KubeVirt undergoes OSTIF security audit
date: '2025-12-17T15:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/12/17/kubevirt-undergoes-ostif-security-audit/
post_kind: link
draft: false
tldr: Audit Process Audit Results Resources Posted on December 17, 2025 by By Helen
  Woeste Operations, Communications, and Community at Open Source Technology Improvement
  Fund CNCF projects highlighted in this post The Open Source Technology Improvement
  Fund (OSTIF) is proud to share the results of a recent security audit of KubeVirt
  , a Kubernetes virtualization API and runtime for managing virtual machines. With
  the continued support of Quarkslab and the Cloud Native Computing Foundation (CNCF),
  KubeVirt maintains support for end-users running virtual-machine workloads that
  need to containerize applications.
summary: 'Audit Process Audit Results Resources Posted on December 17, 2025 by By
  Helen Woeste Operations, Communications, and Community at Open Source Technology
  Improvement Fund CNCF projects highlighted in this post The Open Source Technology
  Improvement Fund (OSTIF) is proud to share the results of a recent security audit
  of KubeVirt , a Kubernetes virtualization API and runtime for managing virtual machines.
  With the continued support of Quarkslab and the Cloud Native Computing Foundation
  (CNCF), KubeVirt maintains support for end-users running virtual-machine workloads
  that need to containerize applications. This audit took place over 37 days in early
  2025. Two auditors reviewed the function and structure of KubeVirt to create a threat
  model that would inform the following work. The threat model, which was discussed
  with the project maintainers, defines threat actors, attack scenarios, and attack
  surfaces of the project. It also directed the next part of the audit, which consisted
  of automated testing and manual code review in areas scoped based on the threat
  model’s recommended weak areas. 15 Findings with Security Impact 1 High 7 Medium
  4 Low 3 Informational CVE 2025-64324 1 High 7 Medium 4 Low 3 Informational CVE 2025-64324
  Custom Threat Model Fix Recommendations The auditors pointed out that the architecture
  of the project prioritizes sandboxing and isolation, making it harder to escalate
  the exploitation of vulnerabilities. The majority of the reported findings from
  this audit fall under those conditions, which limits their impact and informs their
  severity ranking. Thank you to the individuals and groups that made this engagement
  possible: KubeVirt maintainers and community, especially: Andrew Burden, Fabian
  Deutsch Quarkslab: Sébastien Rolland, Mihail Kirov, and Pauline Sauder The Cloud
  Native Computing Foundation You can read the Audit Report HERE You can read KubeVirt’s
  Blog HERE Share.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/12/17/kubevirt-undergoes-ostif-security-audit/
