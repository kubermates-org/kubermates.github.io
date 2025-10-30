---
title: Announcing Fedora 43
date: '2025-10-28T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/announcing-fedora-43
post_kind: link
draft: false
tldr: Announcing Fedora 43 RPM 6.0 Anaconda Fedora Workstation Fedora CoreOS Kinoite
  About the author Jef Spaleta More like this Blog post Blog post Original podcast
  Original podcast Browse by channel Automation Artificial intelligence Open hybrid
  cloud Security Edge computing Infrastructure Applications Virtualization Share Today,
  the Fedora Project is excited to announce the general availability of Fedora Linux
  43 , the latest version of the free and open source operating system. Learn more
  about the new and updated features of Fedora 43 below and don’t forget to ensure
  your system is fully up-to-date before upgrading from a previous release.
summary: 'Announcing Fedora 43 RPM 6.0 Anaconda Fedora Workstation Fedora CoreOS Kinoite
  About the author Jef Spaleta More like this Blog post Blog post Original podcast
  Original podcast Browse by channel Automation Artificial intelligence Open hybrid
  cloud Security Edge computing Infrastructure Applications Virtualization Share Today,
  the Fedora Project is excited to announce the general availability of Fedora Linux
  43 , the latest version of the free and open source operating system. Learn more
  about the new and updated features of Fedora 43 below and don’t forget to ensure
  your system is fully up-to-date before upgrading from a previous release. Fedora
  43 will include RPM 6.0, which brings an enhanced focus on security. RPM 6.0 enables
  support for: OpenPGP keys reference by fingerprint or full key id Updated OpenPGP
  keys with rpmkeys --import <key> and corresponding API(s) Multiple signatures per
  package Automatic signing on package build (mainly for local use) OpenPGP v6 keys
  and signatures (including PQC) Signing with Sequoia-sq as an alternative to GnuPG
  Fedora 43 features updates to Anaconda, including: DNF 5 for RPM packaging installation
  Default use of Anaconda WebUI used for Fedora Spins Enforced use of GPT partition
  tables for all UEFI-based Fedora installations for x86 architecture Support removal
  for DNF modularity Fedora Workstation 43 features GNOME 49 and will be Wayland-only.
  GNOME upstream has deprecated X11 session support and anticipates removing X11 support
  in the GNOME 50 release. Fedora CoreOS is now buildable using a Containerfile from
  the Fedora bootc image, instead of using a custom CoreOS Assembler tool. With this
  change, anyone with podman installed is able to build FCOS. This means that it''s
  easier for both users and pipelines to build it. Fedora CoreOS updates now rely
  on OCI images from the Fedora quay. io repository, instead of the OStree repository.
  Fedora 43 enables unattended updates in Plasma Discover that will provide default
  background updates in new installations and existing installations. This process
  uses rpm-ostree staged update support to download and prepare the new version of
  the system in the background, which is then used on reboot.'
---
Open the original post ↗ https://www.redhat.com/en/blog/announcing-fedora-43
