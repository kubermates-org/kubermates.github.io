---
title: Navigating Failures in Pods With Devices
date: '2025-07-03T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/07/03/navigating-failures-in-pods-with-devices/
post_kind: link
draft: false
tldr: 'Navigating Failures in Pods With Devices The AI/ML boom and its impact on Kubernetes
  Understanding AI/ML workloads Why Kubernetes still reigns supreme The current state
  of device failure handling Failure modes: K8s infrastructure Failure modes: device
  failed Failure modes: container code failed Failure modes: device degradation Roadmap
  Roadmap for failure modes: K8s infrastructure Roadmap for failure modes: device
  failed Roadmap for failure modes: container code failed Roadmap for failure modes:
  device degradation Join the conversation Kubernetes is the de facto standard for
  container orchestration, but when it comes to handling specialized hardware like
  GPUs and other accelerators, things get a bit complicated. This blog post dives
  into the challenges of managing failure modes when operating pods with devices in
  Kubernetes, based on insights from Sergey Kanzhelev and Mrunal Patel''s talk at
  KubeCon NA 2024.'
summary: 'Navigating Failures in Pods With Devices The AI/ML boom and its impact on
  Kubernetes Understanding AI/ML workloads Why Kubernetes still reigns supreme The
  current state of device failure handling Failure modes: K8s infrastructure Failure
  modes: device failed Failure modes: container code failed Failure modes: device
  degradation Roadmap Roadmap for failure modes: K8s infrastructure Roadmap for failure
  modes: device failed Roadmap for failure modes: container code failed Roadmap for
  failure modes: device degradation Join the conversation Kubernetes is the de facto
  standard for container orchestration, but when it comes to handling specialized
  hardware like GPUs and other accelerators, things get a bit complicated. This blog
  post dives into the challenges of managing failure modes when operating pods with
  devices in Kubernetes, based on insights from Sergey Kanzhelev and Mrunal Patel''s
  talk at KubeCon NA 2024. You can follow the links to slides and recording. The rise
  of AI/ML workloads has brought new challenges to Kubernetes. These workloads often
  rely heavily on specialized hardware, and any device failure can significantly impact
  performance and lead to frustrating interruptions. As highlighted in the 2024 Llama
  paper , hardware issues, particularly GPU failures, are a major cause of disruption
  in AI/ML training. You can also learn how much effort NVIDIA spends on handling
  devices failures and maintenance in the KubeCon talk by Ryan Hallisey and Piotr
  Prokop All-Your-GPUs-Are-Belong-to-Us: An Inside Look at NVIDIA''s Self-Healing
  GeForce NOW Infrastructure ( recording ) as they see 19 remediation requests per
  1000 nodes a day! We also see data centers offering spot consumption models and
  overcommit on power, making device failures commonplace and a part of the business
  model. However, Kubernetes’s view on resources is still very static. The resource
  is either there or not. And if it is there, the assumption is that it will stay
  there fully functional - Kubernetes lacks good support for handling full or partial
  hardware failures. These long-existing assumptions combined with the overall complexity
  of a setup lead to a variety of failure modes, which we discuss here. Generally,
  all AI/ML workloads require specialized hardware, have challenging scheduling requirements,
  and are expensive when idle.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/07/03/navigating-failures-in-pods-with-devices/
