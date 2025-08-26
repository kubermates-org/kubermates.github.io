---
title: Introducing kube-scheduler-simulator
date: '2025-04-07T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/04/07/introducing-kube-scheduler-simulator/
post_kind: link
draft: false
tldr: The Kubernetes Scheduler is a crucial control plane component that determines
  which node a Pod will run on.
summary: The Kubernetes Scheduler is a crucial control plane component that determines
  which node a Pod will run on. Thus, anyone utilizing Kubernetes relies on a scheduler.
  kube-scheduler-simulator is a simulator for the Kubernetes scheduler, that started
  as a Google Summer of Code 2021 project developed by me (Kensei Nakada) and later
  received a lot of contributions. This tool allows users to closely examine the scheduler’s
  behavior and decisions. It is useful for casual users who employ scheduling constraints
  (for example, inter-Pod affinity ) and experts who extend the scheduler with custom
  plugins. The scheduler often appears as a black box, composed of many plugins that
  each contribute to th...
---
Open the original post ↗ https://kubernetes.io/blog/2025/04/07/introducing-kube-scheduler-simulator/
