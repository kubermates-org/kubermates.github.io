---
title: 'runc container breakout  vulnerabilities: A technical overview'
date: '2025-11-28T12:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/11/28/runc-container-breakout-vulnerabilities-a-technical-overview/
post_kind: link
draft: false
tldr: 'The vulnerabilities Exploitation scenarios and threat model Kubernetes and
  cloud native implications Affected versions and patches Mitigations The bigger picture:
  Secure-by-default configurations Credits Posted on November 28, 2025 by Matteo Bisi,
  DevSecOps Team Leader at ReeVo and CNCF KCD Organizer CNCF projects highlighted
  in this post A set of high-severity vulnerabilities in runc were publicly disclosed
  in November 2025, allowing for full container breakouts. Runc is the cornerstone
  of containerization on Linux, serving as the default low-level container runtime
  for industry-standard tools like Docker, Podman, and Kubernetes.'
summary: 'The vulnerabilities Exploitation scenarios and threat model Kubernetes and
  cloud native implications Affected versions and patches Mitigations The bigger picture:
  Secure-by-default configurations Credits Posted on November 28, 2025 by Matteo Bisi,
  DevSecOps Team Leader at ReeVo and CNCF KCD Organizer CNCF projects highlighted
  in this post A set of high-severity vulnerabilities in runc were publicly disclosed
  in November 2025, allowing for full container breakouts. Runc is the cornerstone
  of containerization on Linux, serving as the default low-level container runtime
  for industry-standard tools like Docker, Podman, and Kubernetes. Its ubiquity means
  that a vulnerability in runc has far-reaching implications for the entire cloud-native
  ecosystem. This post summarizes the vulnerabilities, the affected versions, and
  the recommended actions to mitigate them. Three vulnerabilities were discovered,
  all related to bypassing runc’s restrictions on writing to arbitrary /proc files.
  These vulnerabilities can be exploited by starting containers with custom mount
  configurations, including those defined in Dockerfiles (RUN –mount=…). CVE-2025-31133:
  “container escape via ‘masked path’ abuse due to mount race conditions” CVSS: 7.3
  Description: This vulnerability exploits an issue with how masked paths are implemented.
  An attacker can replace /dev/null with a symlink to a procfs file (e. g. , /proc/sys/kernel/core_pattern
  or /proc/sysrq-trigger). Runc will then bind-mount the symlink target read-write,
  leading to a container breakout or a host crash. CVE-2025-52565: “container escape
  with malicious config due to /dev/console mount and related races” CVSS: 7.3 Description:
  Similar to the previous CVE, this vulnerability exploits a flaw in /dev/console
  bind-mounts.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/11/28/runc-container-breakout-vulnerabilities-a-technical-overview/
