---
title: 'Kyverno Security Advisory: Cross-Namespace Privilege Escalation'
date: '2026-01-27T20:22:10+00:00'
tags:
- nirmata
- kubernetes
source: Nirmata Blog
external_url: https://nirmata.com/2026/01/27/kyverno-security-advisory/?utm_source=rss&utm_medium=rss&utm_campaign=kyverno-security-advisory
post_kind: link
draft: false
tldr: 'Kyverno Security Advisory: Cross-Namespace Privilege Escalation Kyverno Security
  Advisories (Jan 27, 2026) Remediation Paths Cross-Namespace Privilege Escalation
  Explanation Mitigations Denial of Service via Context Variable Amplification Explanation
  Mitigations Need Help Securing Older Versions? Nirmata OSS engineers, alongside
  OSS security researchers, have identified and issued fixes for one critical and
  one high-severity CVE that impact all versions of Kyverno. At this time, we have
  no evidence of these vulnerabilities being actively exploited in the wild but request
  that all users upgrade their deployments.'
summary: 'Kyverno Security Advisory: Cross-Namespace Privilege Escalation Kyverno
  Security Advisories (Jan 27, 2026) Remediation Paths Cross-Namespace Privilege Escalation
  Explanation Mitigations Denial of Service via Context Variable Amplification Explanation
  Mitigations Need Help Securing Older Versions? Nirmata OSS engineers, alongside
  OSS security researchers, have identified and issued fixes for one critical and
  one high-severity CVE that impact all versions of Kyverno. At this time, we have
  no evidence of these vulnerabilities being actively exploited in the wild but request
  that all users upgrade their deployments. Here are the recommended actions: For
  Open Source Users: We have released patched versions for supported releases. We
  recommend upgrading immediately to: v1.16.3 v1.15.3 https://github. com/kyverno/kyverno/releases
  For Nirmata Enterprise Customers: We realize that upgrading admission controllers
  in critical environments requires significant testing. To support our customers
  based on enteroprise SLAs, Nirmata has back-ported these security patches to all
  Long Term Support (LTS) versions dating back to v1.12. Action: If you are a Nirmata
  customer, you do not need to perform a major version upgrade. Simply pull the latest
  patch for your current Long Term Support (LTS) version. Please contact your Customer
  Success Manager if you need assistance. Below are details on these vulnerabilities:
  Kyverno policies can use the apiCall feature to lookup cluster resources. Kyverno
  executes the API call using its own service account, and this vulnerability allows
  a Kyverno namespaced policy to access cluster-wide resources, and resources in other
  namespaces. By default, Kyverno uses role aggregation to allow the system admin
  role access to manage policies.'
---
Open the original post ↗ https://nirmata.com/2026/01/27/kyverno-security-advisory/?utm_source=rss&utm_medium=rss&utm_campaign=kyverno-security-advisory
