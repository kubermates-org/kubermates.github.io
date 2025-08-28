---
title: 'IngressNightmare Vulnerabilities: All You Need to Know'
date: '2025-03-26T13:15:57+00:00'
tags:
- security
source: Aqua Security
external_url: https://blog.aquasec.com/ingress-nginx-vulnerabilities-what-you-need-to-know
post_kind: link
draft: false
tldr: 'IngressNightmare Vulnerabilities: All You Need to Know What is the Ingress
  Controller Understanding the IngressNightmare vulnerabilities Vulnerabilities Details
  and Impact Are you Affected? Detection and Mitigation Mitigating Vulnerabilities
  with Aqua Detecting and Mitigating with Aqua Trivy Vulnerability Impact Across Managed
  Kubernetes Platforms CVE-2025-1974 * CVE-2025-24514 * CVE-2025-1097 * CVE-2025-1098
  * CVE-2025-24513 On March 24, 2025, a set of critical vulnerabilities (CVE-2025-1097,
  CVE-2025-1098, CVE-2025-24514, and CVE-2025-1974 — collectively referred to as IngressNightmare
  was disclosed in the ingress-nginx Controller for Kubernetes. These vulnerabilities
  could lead to a complete cluster takeover by granting attackers unauthorized access
  to all secrets stored across all namespaces in the Kubernetes cluster.'
summary: 'IngressNightmare Vulnerabilities: All You Need to Know What is the Ingress
  Controller Understanding the IngressNightmare vulnerabilities Vulnerabilities Details
  and Impact Are you Affected? Detection and Mitigation Mitigating Vulnerabilities
  with Aqua Detecting and Mitigating with Aqua Trivy Vulnerability Impact Across Managed
  Kubernetes Platforms CVE-2025-1974 * CVE-2025-24514 * CVE-2025-1097 * CVE-2025-1098
  * CVE-2025-24513 On March 24, 2025, a set of critical vulnerabilities (CVE-2025-1097,
  CVE-2025-1098, CVE-2025-24514, and CVE-2025-1974 — collectively referred to as IngressNightmare
  was disclosed in the ingress-nginx Controller for Kubernetes. These vulnerabilities
  could lead to a complete cluster takeover by granting attackers unauthorized access
  to all secrets stored across all namespaces in the Kubernetes cluster. In Kubernetes,
  an Ingress Controller manages external access to services within a cluster, typically
  via HTTP or HTTPS. The ingress NGINX Controller, built on the NGINX web server ,
  is widely used to route incoming traffic to the appropriate backend services based
  on defined rules. HTTP HTTPS NGINX web server The disclosed vulnerabilities include:
  CVE-2025-1974 (CVSS Score 9. 8 Critical) Allows unauthenticated attackers with pod
  network access to execute arbitrary code in the ingress-nginx controller, potentially
  leading to full cluster takeover. CVE-2025-24514, CVE-2025-1097, CVE-2025-1098 (CVSS
  Score 8. 8 High) Involve improper handling of Ingress annotations that can lead
  to code execution or unauthorized data access. CVE-2025-24513 (CVSS Score 4. 8 Medium)
  Involves directory traversal that can lead to DoS or limited secret disclosure.
  The researchers who found these vulnerabilities indicated that over 40% of cloud
  environments were vulnerable to these remote code execution (RCE) risks. Their analysis
  discovered over 6,500 clusters, including those of Fortune 500 companies, that publicly
  expose the admission controllers of vulnerable Kubernetes ingress controllers to
  the public internet, placing them at immediate critical risk.'
---
Open the original post ↗ https://blog.aquasec.com/ingress-nginx-vulnerabilities-what-you-need-to-know
