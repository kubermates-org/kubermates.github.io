---
title: Lessons from an autonomous computer vision system on the air-gapped edge
date: '2026-06-09T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/lessons-autonomous-computer-vision-system-air-gapped-edge
post_kind: link
draft: false
tldr: 'Lessons from an autonomous computer vision system on the air-gapped edge What
  visitors experienced Delivering edge air gap infrastructure Red Hat’s advanced compute
  platform approach Bootstrap automation for consistency and repeatability Device
  edge management Final thoughts: Building reliable infrastructure at the edge Ready
  to get started? Red Hat Device Edge | Product Trial About the authors Ken Osborn
  Josh Swanson Stephen Smith More like this Red Hat Device Edge now available to run
  on NVIDIA Jetson Orin Closing the gap: Bringing AI and Kubernetes to the source
  of the data WebAssembly breaks away from the browser | Technically Speaking A composable
  industrial edge platform | Technically Speaking Keep exploring Browse by channel
  Automation Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share Red Hat Summit demonstration booth featuring a
  model train track, edge computing hardware, monitoring displays, and supporting
  infrastructure used to demonstrate AI-driven automation at the edge. Many AI demos
  stop at detection.'
summary: 'Lessons from an autonomous computer vision system on the air-gapped edge
  What visitors experienced Delivering edge air gap infrastructure Red Hat’s advanced
  compute platform approach Bootstrap automation for consistency and repeatability
  Device edge management Final thoughts: Building reliable infrastructure at the edge
  Ready to get started? Red Hat Device Edge | Product Trial About the authors Ken
  Osborn Josh Swanson Stephen Smith More like this Red Hat Device Edge now available
  to run on NVIDIA Jetson Orin Closing the gap: Bringing AI and Kubernetes to the
  source of the data WebAssembly breaks away from the browser | Technically Speaking
  A composable industrial edge platform | Technically Speaking Keep exploring Browse
  by channel Automation Artificial intelligence Open hybrid cloud Security Edge computing
  Infrastructure Applications Virtualization Share Red Hat Summit demonstration booth
  featuring a model train track, edge computing hardware, monitoring displays, and
  supporting infrastructure used to demonstrate AI-driven automation at the edge.
  Many AI demos stop at detection. A dashboard highlights an object, a model produces
  a classification, or a graph updates in real time. Those are valuable building blocks,
  but operational environments often require something more immediate—systems that
  can react locally, autonomously, and in near time. Using the Red Hat edge portfolio
  , we set out to explore what happens when AI moves beyond observation and begins
  driving real operational behavior. To bring that concept to life at Red Hat Summit
  2026, we built a live train demonstration that transformed visual recognition directly
  into physical action at the edge. The demo became a tangible way to show how edge
  AI, containerized workloads, and fleet management technologies can work together
  in operational environments. The booth setup was intentionally physical and interactive.
  Visitors could hold up printed placards representing commands such as: ‘Start’ ‘Stop’
  ‘Slow’ ‘Reverse’ Four visual command placards labeled Start, Stop, Slow, and Reverse
  used by a computer vision model to control train behavior through AI-based image
  recognition. A webcam connected to a managed edge gateway continuously captured
  video frames. Those frames were processed locally using OpenCV and passed into a
  MobileNetV3-based image classification model running with ONNX Runtime inside a
  Podman container on Red Hat Enterprise Linux image mode. Once the model confidently
  identified a placard, the application published a JSON message over MQTT (Message
  Queuing Telemetry Transport) to an industrial control system responsible for train
  behavior.'
---
Open the original post ↗ https://www.redhat.com/en/blog/lessons-autonomous-computer-vision-system-air-gapped-edge
