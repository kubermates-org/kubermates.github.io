---
title: 'Trust at every layer: How sealed images extend OS integrity from boot to runtime'
date: '2026-05-20T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/how-sealed-images-red-hat-enterprise-linux-extend-os-integrity-boot-runtime
post_kind: link
draft: false
tldr: 'Trust at every layer: How sealed images extend OS integrity from boot to runtime
  The gap in your boot chain From container workflows to OS integrity How it works
  What this means for your infrastructure Get started Red Hat Enterprise Linux | Product
  trial About the authors Mark Russell Colin Walters More like this Red Hat Enterprise
  Linux 10.2 and 9.8 are here: The intelligent evolution of enterprise Linux A decade
  of open innovation: Red Hat continues to scale the open hybrid cloud with Microsoft
  OS Wars_part 1 | Command Line Heroes OS Wars_part 2: Rise of Linux | Command Line
  Heroes Keep exploring Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share Consider a medical device running Linux in a hospital. It processes patient
  data, adjusts dosing, and reports to clinical systems.'
summary: 'Trust at every layer: How sealed images extend OS integrity from boot to
  runtime The gap in your boot chain From container workflows to OS integrity How
  it works What this means for your infrastructure Get started Red Hat Enterprise
  Linux | Product trial About the authors Mark Russell Colin Walters More like this
  Red Hat Enterprise Linux 10.2 and 9.8 are here: The intelligent evolution of enterprise
  Linux A decade of open innovation: Red Hat continues to scale the open hybrid cloud
  with Microsoft OS Wars_part 1 | Command Line Heroes OS Wars_part 2: Rise of Linux
  | Command Line Heroes Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share Consider a medical device running Linux in a hospital. It processes patient
  data, adjusts dosing, and reports to clinical systems. Or an ATM on a street corner,
  processing transactions around the clock. Or a gateway device at the edge of a manufacturing
  network, relaying sensor data from the factory floor. The operating system (OS)
  on each of these was verified when it was installed. But is every binary and library
  still exactly what was built? If you would demand that guarantee for a device in
  an operating room or on a factory floor, why not expect the same from the servers
  running your business? Typically, a default generic operating system install comes
  "unlocked", allowing you to be root on your computer and make persistent changes.
  So while a generic Red Hat Enterprise Linux (RHEL) or Debian install supports secure
  boot, it''s typically only the kernel that''s signed. The cryptographic chain of
  trust from firmware doesn''t cover the root filesystem or apps. But for organizations
  that want to make "appliances", it''s possible to increase security by chaining
  from secure boot to integrity of the operating system, using custom signatures.
  Most organizations already build, sign, and ship container images through CI/CD
  pipelines. Every container pull verifies a cryptographic digest. Every time a new
  container starts, the runtime confirms the image matches what was signed.'
---
Open the original post ↗ https://www.redhat.com/en/blog/how-sealed-images-red-hat-enterprise-linux-extend-os-integrity-boot-runtime
