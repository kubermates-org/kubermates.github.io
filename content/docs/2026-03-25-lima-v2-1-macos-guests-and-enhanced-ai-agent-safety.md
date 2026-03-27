---
title: 'Lima v2.1: macOS guests and enhanced AI agent safety'
date: '2026-03-25T07:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/03/25/lima-v2-1-macos-guests-and-enhanced-ai-agent-safety/
post_kind: link
draft: false
tldr: 'What is Lima ? Updates in v2.1 FreeBSD guests (experimental) AI Safety: limactl
  shell –sync Performance and efficiency improvements Other improvements Catch us
  at KubeCon + CloudNativeCon Europe 2026! Posted on March 25, 2026 by Ansuman Sahoo,
  Lima Project Maintainer CNCF projects highlighted in this post Following our expansion
  into AI workflows in v2.0, Lima v2.1 introduces highly anticipated experimental
  support for macOS and FreeBSD guests and further hardens local environments against
  unpredictable AI agents. Lima (Linux Machines) is a command-line tool to launch
  local virtual machines.'
summary: 'What is Lima ? Updates in v2.1 FreeBSD guests (experimental) AI Safety:
  limactl shell –sync Performance and efficiency improvements Other improvements Catch
  us at KubeCon + CloudNativeCon Europe 2026! Posted on March 25, 2026 by Ansuman
  Sahoo, Lima Project Maintainer CNCF projects highlighted in this post Following
  our expansion into AI workflows in v2.0, Lima v2.1 introduces highly anticipated
  experimental support for macOS and FreeBSD guests and further hardens local environments
  against unpredictable AI agents. Lima (Linux Machines) is a command-line tool to
  launch local virtual machines. Originally focused on running containers on a laptop
  and promoting containerd to Mac users, Lima joined the CNCF as a Sandbox project
  in September 2022 and was promoted to Incubating in October 2025. Today, Lima supports
  a wide variety of non-container workloads, non-macOS hosts, and robust AI sandboxing.
  If you are using Homebrew, Lima can be installed using: brew install lima brew install
  lima For other installation methods, see https://lima-vm. io/docs/installation/.
  One of the most requested features is finally here: Lima now experimentally supports
  running macOS guests using the `vz` driver on macOS. This expands Lima’s utility
  beyond Linux virtual machines, allowing developers to easily spin up isolated macOS
  environments for testing, building, or running platform-specific workloads. To create
  and start a macOS guest, simply run: limactl start template:macos limactl start
  template:macos The user password is randomly generated and stored in the `~/password
  file` in the VM. Consider changing it after the first login: limactl shell macos
  cat /Users/${USER}. guest/password limactl shell macos cat /Users/${USER}. guest/password
  Note: It requires an Apple Silicon Mac as a host machine to work.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/03/25/lima-v2-1-macos-guests-and-enhanced-ai-agent-safety/
