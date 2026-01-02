---
title: How to integrate Kairos architecturally into an edge AI platform
date: '2025-12-29T15:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/12/29/how-to-integrate-kairos-architecturally-into-an-edge-ai-platform/
post_kind: link
draft: false
tldr: Posted on December 29, 2025 by Jordan Karapanagiotis, Software Engineer - Aurea
  Imaging, Mauro Morales, Staff Engineer & Kairos Maintainer - Spectro Cloud CNCF
  projects highlighted in this post Remote sensing in agriculture requires complex
  systems that are able to communicate with various external devices like GPS and
  cameras, and use machine learning and AI inference to provide insights to the grower
  regarding their orchard, down to tree and crop-level precision. Aurea Imaging, a
  Dutch startup company, specializes in remote sensing solutions for agriculture using
  an embedded device with a powerful GPU-enabled NVIDIA Jetson on board.
summary: 'Posted on December 29, 2025 by Jordan Karapanagiotis, Software Engineer
  - Aurea Imaging, Mauro Morales, Staff Engineer & Kairos Maintainer - Spectro Cloud
  CNCF projects highlighted in this post Remote sensing in agriculture requires complex
  systems that are able to communicate with various external devices like GPS and
  cameras, and use machine learning and AI inference to provide insights to the grower
  regarding their orchard, down to tree and crop-level precision. Aurea Imaging, a
  Dutch startup company, specializes in remote sensing solutions for agriculture using
  an embedded device with a powerful GPU-enabled NVIDIA Jetson on board. Instead of
  opting for the traditional embedded C & ROS stack, we chose a cloud-native approach:
  running a lightweight distribution of Kubernetes (K3s) on the edge. Because of the
  team’s familiarity with cloud-native concepts, we took this (literally) to the edge.
  Even knowing there would be challenges due to the niche application, it was a clear
  choice given the vast amount of cloud-native projects and rapidly evolving landscape
  of AI on the edge in IoT applications. The major challenge to address was the Jetson
  board’s use of NVIDIA’s ecosystem for all the GPU work, and our ML models needing
  to be constantly updated to industry standards. How do you keep a fleet up-to-date,
  not only at an application level, but also in terms of host-level tooling, like
  JetPack (Jetson’s official software stack), CUDA (the GPU interface), firmware packages,
  peripheral drivers, or the OS distribution? The best place to find answers regarding
  cutting-edge use cases of Kubernetes is, of course, KubeCon + CloudNativeCon! During
  a presentation on deploying Kubernetes clusters around the world, we learned about
  Kairos , a CNCF Sandbox Project that allows you to convert Linux distributions into
  an immutable OS and simplify Day 2 operations. This means for any kind of host-level
  update, especially if it involves risky operations like firmware drivers and bootloaders,
  we do not need to send a technician with physical access to the farmer’s device
  but can perform the update remotely in a safe manner. Upgrading servers and continuous
  delivery work well in controlled environments like the cloud, but when your devices
  are mounted on a tractor in a field with flaky network connectivity, a traditional
  approach won’t cut it. Especially when you’re managing a global fleet of remote
  sensing devices, without IT technicians in the field, and with the rapidly evolving
  NVIDIA Jetson ecosystem. We needed a solution before deployment. Another important
  aspect to consider is the lifespan of agricultural products, which can typically
  be a decade long.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/12/29/how-to-integrate-kairos-architecturally-into-an-edge-ai-platform/
