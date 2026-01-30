---
title: Announcing the Checkpoint/Restore Working Group
date: '2026-01-21T10:00:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/01/21/introducing-checkpoint-restore-wg/
post_kind: link
draft: false
tldr: Announcing the Checkpoint/Restore Working Group Motivation and use cases Related
  events Connect with us The community around Kubernetes includes a number of Special
  Interest Groups (SIGs) and Working Groups (WGs) facilitating discussions on important
  topics between interested contributors. Today we would like to announce the new
  Kubernetes Checkpoint Restore WG focusing on the integration of Checkpoint/Restore
  functionality into Kubernetes.
summary: 'Announcing the Checkpoint/Restore Working Group Motivation and use cases
  Related events Connect with us The community around Kubernetes includes a number
  of Special Interest Groups (SIGs) and Working Groups (WGs) facilitating discussions
  on important topics between interested contributors. Today we would like to announce
  the new Kubernetes Checkpoint Restore WG focusing on the integration of Checkpoint/Restore
  functionality into Kubernetes. There are several high-level scenarios discussed
  in the working group: Optimizing resource utilization for interactive workloads,
  such as Jupyter notebooks and AI chatbots Accelerating startup of applications with
  long initialization times, including Java applications and LLM inference services
  Using periodic checkpointing to enable fault-tolerance for long-running workloads,
  such as distributed model training Providing interruption-aware scheduling with
  transparent checkpoint/restore, allowing lower-priority Pods to be preempted while
  preserving the runtime state of applications Facilitating Pod migration across nodes
  for load balancing and maintenance, without disrupting workloads. Enabling forensic
  checkpointing to investigate and analyze security incidents such as cyberattacks,
  data breaches, and unauthorized access. Across these scenarios, the goal is to help
  facilitate discussions of ideas between the Kubernetes community and the growing
  Checkpoint/Restore in Userspace (CRIU) ecosystem. The CRIU community includes several
  projects that support these use cases, including: CRIU - A tool for checkpointing
  and restoring running applications and containers checkpointctl - A tool for in-depth
  analysis of container checkpoints criu-coordinator - A tool for coordinated checkpoint/restore
  of distributed applications with CRIU checkpoint-restore-operator - A Kubernetes
  operator for managing checkpoints More information about the checkpoint/restore
  integration with Kubernetes is also available here. Following our presentation about
  transparent checkpointing at KubeCon EU 2025, we are excited to welcome you to our
  panel discussion and AI + ML session at KubeCon + CloudNativeCon Europe 2026. If
  you are interested in contributing to Kubernetes or CRIU, there are several ways
  to participate: Join our meeting every second Thursday at 17:00 UTC via the Zoom
  link in our meeting notes ; recordings of our prior meetings are available here.
  Chat with us on the Kubernetes Slack : #wg-checkpoint-restore Email us at the wg-checkpoint-restore
  mailing list ← Previous Next →.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/01/21/introducing-checkpoint-restore-wg/
