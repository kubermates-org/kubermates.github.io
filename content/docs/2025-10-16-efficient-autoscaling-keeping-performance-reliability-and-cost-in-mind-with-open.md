---
title: 'Efficient autoscaling: Keeping performance, reliability, and cost in mind
  with open source projects'
date: '2025-10-16T16:30:52+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/10/16/efficient-autoscaling-keeping-performance-reliability-and-cost-in-mind-with-open-source-projects/
post_kind: link
draft: false
tldr: 'Kubernetes autoscaling comes with trade-offs Performance Cost Reliability It’s
  all about trade-offs Author bio Posted on October 16, 2025 by Christian Melendez,
  AWS CNCF projects highlighted in this post During ContainerDays in Hamburg, Kelsey
  Hightower posed a simple but powerful question: “Why are we still talking about
  containers?” His point resonated with me deeply — even in the AI era, the cloud-native
  community is still refining the fundamentals of container orchestration, scalability,
  and efficiency. In this post, I’ll explore how open source projects like KEDA and
  Karpenter can help you balance performance, reliability, and cost in Kubernetes
  autoscaling.'
summary: 'Kubernetes autoscaling comes with trade-offs Performance Cost Reliability
  It’s all about trade-offs Author bio Posted on October 16, 2025 by Christian Melendez,
  AWS CNCF projects highlighted in this post During ContainerDays in Hamburg, Kelsey
  Hightower posed a simple but powerful question: “Why are we still talking about
  containers?” His point resonated with me deeply — even in the AI era, the cloud-native
  community is still refining the fundamentals of container orchestration, scalability,
  and efficiency. In this post, I’ll explore how open source projects like KEDA and
  Karpenter can help you balance performance, reliability, and cost in Kubernetes
  autoscaling. When we talk about Kubernetes autoscaling , it’s not just about adding
  replicas or nodes when demand grows and removing them when it shrinks. You have
  to balance performance , reliability , and cost — three forces that constantly pull
  against each other. The way I like to think about these three pillars is as a triangle
  , like in the following figure. These three pillars create natural tension. Before
  your application’s performance degrades, you need to add resources — which increases
  cost. To save on cost, you scale down resources — which can impact reliability.
  So how do we find the right balance? Let’s explore tools and recommendations for
  each pillar. Before you start scaling, you need to understand what truly impacts
  the performance of your application — what matters to your users and stakeholders.
  Most of the time, they don’t care about CPU or memory usage directly. These may
  be indicators, but they don’t always tell the full story.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/10/16/efficient-autoscaling-keeping-performance-reliability-and-cost-in-mind-with-open-source-projects/
