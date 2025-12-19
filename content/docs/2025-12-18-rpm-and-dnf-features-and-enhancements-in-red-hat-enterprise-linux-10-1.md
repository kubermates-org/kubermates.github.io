---
title: RPM and DNF features and enhancements in Red Hat Enterprise Linux 10.1
date: '2025-12-18T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/rpm-and-dnf-features-and-enhancements-red-hat-enterprise-linux-101
post_kind: link
draft: false
tldr: 'RPM and DNF features and enhancements in Red Hat Enterprise Linux 10.1 RPM
  signature improvements Modularity and DNF Better software management Red Hat Enterprise
  Linux | Product trial About the author Samantha Bueno More like this More than meets
  the eye: Behind the scenes of Red Hat Enterprise Linux 10 (Part 4) Looking ahead
  to 2026: Red Hat’s view across the hybrid cloud At Your Serverless | Command Line
  Heroes The Overlooked Operating System | Compiler: Stack/Unstuck Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share Red Hat Enterprise
  Linux 10.1 (RHEL) features some significant updates to RPM and DNF, two technologies
  designed to help you manage software installs and updates. The RPM package manager
  (RPM) creates installation files used to install and uninstall an application, and
  that can be queried for information about what libraries and binaries the application
  contains.'
summary: 'RPM and DNF features and enhancements in Red Hat Enterprise Linux 10.1 RPM
  signature improvements Modularity and DNF Better software management Red Hat Enterprise
  Linux | Product trial About the author Samantha Bueno More like this More than meets
  the eye: Behind the scenes of Red Hat Enterprise Linux 10 (Part 4) Looking ahead
  to 2026: Red Hat’s view across the hybrid cloud At Your Serverless | Command Line
  Heroes The Overlooked Operating System | Compiler: Stack/Unstuck Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share Red Hat Enterprise
  Linux 10.1 (RHEL) features some significant updates to RPM and DNF, two technologies
  designed to help you manage software installs and updates. The RPM package manager
  (RPM) creates installation files used to install and uninstall an application, and
  that can be queried for information about what libraries and binaries the application
  contains. The dnf command is the tool used on RHEL to search for available applications,
  and then to install, update, or uninstall them. These are important components of
  a computer system, so we''ve worked hard to improve them. dnf As we prepare for
  the next generation of security threats and adapt to the new and evolving post-quantum
  computing world, we''ve made a number of enhancements to RPM''s signature capabilities.
  RPM signatures are a security feature used with RPM packages to verify the package''s
  authenticity and integrity, ensuring it came from a trusted source and hasn''t been
  tampered with since it was signed. These changes include improvements to support
  differing formats and algorithms, and adding options that give customers greater
  control over managing signatures. It offers select signature algorithms of your
  choice like ML-DSA, which can be used for post-quantum signing. The introduction
  of RPMv6 signatures enables multiple signatures per package and adds support for
  the new, stronger OpenPGP v6 standard. OpenPGP v6 is the latest version of the OpenPGP
  cryptographic standard, finalized as RFC 9580, which updates the standard with modern
  cryptographic practices. Customers will also have the freedom to select signature
  algorithms of their choice. These new features ultimately enable us to ship packages
  with a set of signatures utilizing different algorithms currently thought to be
  post-quantum safe.'
---
Open the original post ↗ https://www.redhat.com/en/blog/rpm-and-dnf-features-and-enhancements-red-hat-enterprise-linux-101
