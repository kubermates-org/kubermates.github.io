---
title: 'Inspektor Gadget: Results from the first security audit'
date: '2026-06-03T23:01:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/06/03/inspektor-gadget-results-from-the-first-security-audit/
post_kind: link
draft: false
tldr: What is Inspektor Gadget? Why a security audit? How the audit was scoped What
  the audit found Two Medium severity findings One Low severity finding Hardening
  recommendations Gadget bypass testing What this means for users Resources Audit
  announcement and resources CVEs Posted on June 3, 2026 by Brian Benz, Francis Laniel,
  Maya Singh, Helen Woeste, and Pietro Tirenna - Inspektor Gadget CNCF projects highlighted
  in this post Inspektor Gadget , the open source eBPF -based toolkit for Kubernetes
  observability and Linux host inspection, has completed its first independent security
  audit. The audit was coordinated by the Open Source Technology Improvement Fund
  (OSTIF) , funded by the CNCF and carried out by Shielder.
summary: What is Inspektor Gadget? Why a security audit? How the audit was scoped
  What the audit found Two Medium severity findings One Low severity finding Hardening
  recommendations Gadget bypass testing What this means for users Resources Audit
  announcement and resources CVEs Posted on June 3, 2026 by Brian Benz, Francis Laniel,
  Maya Singh, Helen Woeste, and Pietro Tirenna - Inspektor Gadget CNCF projects highlighted
  in this post Inspektor Gadget , the open source eBPF -based toolkit for Kubernetes
  observability and Linux host inspection, has completed its first independent security
  audit. The audit was coordinated by the Open Source Technology Improvement Fund
  (OSTIF) , funded by the CNCF and carried out by Shielder. The findings, the fixes,
  and the hardening recommendations are now public, and every reported vulnerability
  has a patch available. This post walks through what Inspektor Gadget does, how the
  audit was scoped, what the researchers found, and what the results mean for teams
  running it in production. Inspektor Gadget is a framework and toolkit that uses
  eBPF to collect and inspect data on Kubernetes clusters and Linux hosts. It manages
  the packaging, deployment, and execution of “gadgets” — eBPF programs packaged as
  OCI images. OCI (the Open Container Initiative) is a Linux Foundation project that
  defines open industry standards for container image formats and runtimes, so the
  same image can be distributed and run across any compliant tool or registry. For
  teams running Kubernetes in production that need to understand what is happening
  inside a cluster, Inspektor Gadget provides that visibility without the usual tradeoffs.
  There is no need to rebuild container images with extra instrumentation, inject
  sidecars into every pod, attach debuggers or strace to running processes, restart
  workloads to toggle tracing on and off, or ship custom kernel modules to nodes.
  Instead, eBPF programs are loaded into the kernel at runtime to safely observe syscalls,
  network activity, and file access. Applications keep running unchanged while operators
  get the data they need. Any tool that runs with elevated privileges on shared infrastructure
  needs to earn trust.
---
Open the original post ↗ https://www.cncf.io/blog/2026/06/03/inspektor-gadget-results-from-the-first-security-audit/
