---
title: 'Reconciling the Past: Correcting Records for Unfixed Kubernetes CVEs'
date: '2026-05-26T09:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/05/26/reconciling-unfixed-kubernetes-cves/
post_kind: link
draft: false
tldr: 'Reconciling the Past: Correcting Records for Unfixed Kubernetes CVEs Why we
  are updating these records now Technical analysis of unfixed architectural risks
  CVE-2020-8561 : Webhook redirect in kube-apiserver CVE-2020-8562 : Proxy bypass
  via DNS TOCTOU CVE-2021-25740 : Cross-namespace forwarding via Endpoints Required
  actions for administrators Conclusion: maturity through transparency The Kubernetes
  project relies on transparency to empower cluster administrators and security researchers.
  One important way we do that is by publishing CVE records into the Common Vulnerabilities
  and Exposures database.'
summary: 'Reconciling the Past: Correcting Records for Unfixed Kubernetes CVEs Why
  we are updating these records now Technical analysis of unfixed architectural risks
  CVE-2020-8561 : Webhook redirect in kube-apiserver CVE-2020-8562 : Proxy bypass
  via DNS TOCTOU CVE-2021-25740 : Cross-namespace forwarding via Endpoints Required
  actions for administrators Conclusion: maturity through transparency The Kubernetes
  project relies on transparency to empower cluster administrators and security researchers.
  One important way we do that is by publishing CVE records into the Common Vulnerabilities
  and Exposures database. As part of our ongoing effort to mature the official Kubernetes
  CVE Feed , we have identified some discrepancies. CVE records for a few older, unfixed
  issues incorrectly include a fixed version field. The Kubernetes Security Response
  Committee (SRC) will correct the affected CVE records on June 1, 2026. This may
  result in vulnerability scanners identifying these vulnerabilities in places where
  they were previously not detected. To help reduce confusion, this post provides
  a technical update on three vulnerabilities that were disclosed in previous years
  but remain unfixed: CVE-2020-8561 , CVE-2020-8562 , and CVE-2021-25740. While these
  vulnerabilities have been public for several years, the recent work to generate
  official Open Source Vulnerabilities (OSV) files revealed that their corresponding
  CVE records did not accurately reflect their status. Specifically, some records
  suggested a fixed version existed, when in reality, these issues are architectural
  design trade-offs that cannot be fully remediated through code without breaking
  fundamental Kubernetes functionality. Correcting these records is vital for the
  community for: Automation Fidelity : Modern vulnerability scanners depend on precise
  version ranges. Inaccurate fixed tags lead to false negatives, giving users a false
  sense of security. Risk Documentation : By formalizing these as unfixed , we ensure
  that platform providers and administrators are aware of the persistent need for
  administrative mitigations.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/05/26/reconciling-unfixed-kubernetes-cves/
