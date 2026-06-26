---
title: Spotlight on WG Device Management
date: '2026-06-24T10:00:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/06/24/wg-device-management-spotlight-2026/
post_kind: link
draft: false
tldr: Spotlight on WG Device Management Introducing Device Management The problem
  and the solution A cross-SIG effort Current focus areas Real-world impact Challenges
  and trade-offs Looking ahead Getting involved Summary The rising popularity of AI,
  Edge, and Telecommunications workloads on Kubernetes has led to new requirements
  for hardware management. We now need hardware specification beyond CPU time and
  memory allocations.
summary: 'Spotlight on WG Device Management Introducing Device Management The problem
  and the solution A cross-SIG effort Current focus areas Real-world impact Challenges
  and trade-offs Looking ahead Getting involved Summary The rising popularity of AI,
  Edge, and Telecommunications workloads on Kubernetes has led to new requirements
  for hardware management. We now need hardware specification beyond CPU time and
  memory allocations. This includes allocating GPUs, TPUs, network interfaces, and
  other hardware, sometimes after pod start and occasionally through time-sharing.
  Efficiently managing this specialized hardware is the mission of the Device Management
  Working Group. Their cornerstone project, Dynamic Resource Allocation (DRA) , recently
  graduated to GA, marking a fundamental shift in how the project handles hardware-intensive
  workloads at scale. In this spotlight, we sit down with working group chairs Kevin
  Klues , Patrick Ohly , and John Belamaric to discuss the limitations of the legacy
  device model, the NP-hard challenges of scheduling, and how they’re building a more
  programmable, hardware-aware future for Kubernetes. Natalie Fisher: Can you introduce
  yourself, your role, and how you got involved in the Device Management Working Group?
  Kevin Klues: My name is Kevin Klues. I am a Distinguished Engineer at NVIDIA. I
  have been a co-chair of the device management working group since its inception
  at Kubecon EU 2024. I have also been involved with DRA (the working group''s primary
  deliverable) since its inception in 2019 / 2020. I have also been a kubelet maintainer
  since 2019, with a focus on its device manager, CPU manager, and topology manager
  subcomponents. The challenges we saw with using these components for workloads that
  relied on external accelerators (e.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/06/24/wg-device-management-spotlight-2026/
