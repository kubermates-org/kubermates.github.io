---
title: 'Blog: Introducing KWOK: Kubernetes WithOut Kubelet'
date: '2023-03-01T00:00:00+00:00'
tags:
- kubernetes
- community
source: Kubernetes.dev Blog
external_url: https://www.kubernetes.dev/blog/2023/03/01/introducing-kwok/
post_kind: link
draft: false
tldr: 'Introducing KWOK: Kubernetes WithOut Kubelet What is KWOK? Why use KWOK? What
  are the use cases? What are the limitations? Getting started Getting Involved Author:
  Shiming Zhang (DaoCloud), Wei Huang (Apple), Yibo Zhuang (Apple) Have you ever wondered
  how to set up a cluster of thousands of nodes just in seconds, how to simulate real
  nodes with a low resource footprint, and how to test your Kubernetes controller
  at scale without spending much on infrastructure? If you answered “yes” to any of
  these questions, then you might be interested in KWOK, a toolkit that enables you
  to create a cluster of thousands of nodes in seconds. KWOK stands for Kubernetes
  WithOut Kubelet.'
summary: 'Introducing KWOK: Kubernetes WithOut Kubelet What is KWOK? Why use KWOK?
  What are the use cases? What are the limitations? Getting started Getting Involved
  Author: Shiming Zhang (DaoCloud), Wei Huang (Apple), Yibo Zhuang (Apple) Have you
  ever wondered how to set up a cluster of thousands of nodes just in seconds, how
  to simulate real nodes with a low resource footprint, and how to test your Kubernetes
  controller at scale without spending much on infrastructure? If you answered “yes”
  to any of these questions, then you might be interested in KWOK, a toolkit that
  enables you to create a cluster of thousands of nodes in seconds. KWOK stands for
  Kubernetes WithOut Kubelet. So far, it provides two tools: kwok kwok kwokctl kwokctl
  kwok KWOK has several advantages: Speed : You can create and delete clusters and
  nodes almost instantly, without waiting for boot or provisioning. Compatibility
  : KWOK works with any tools or clients that are compliant with Kubernetes APIs,
  such as kubectl, helm, kui, etc. Portability : KWOK has no specific hardware or
  software requirements. You can run it using pre-built images, once Docker or Nerdctl
  is installed. Alternatively, binaries are also available for all platforms and can
  be easily installed. Flexibility : You can configure different node types, labels,
  taints, capacities, conditions, etc. , and you can configure different pod behaviors,
  status, etc. to test different scenarios and edge cases. Performance : You can simulate
  thousands of nodes on your laptop without significant consumption of CPU or memory
  resources. KWOK can be used for various purposes: Learning : You can use KWOK to
  learn about Kubernetes concepts and features without worrying about resource waste
  or other consequences.'
---
Open the original post ↗ https://www.kubernetes.dev/blog/2023/03/01/introducing-kwok/
