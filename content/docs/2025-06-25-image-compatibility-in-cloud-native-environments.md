---
title: Image Compatibility In Cloud Native Environments
date: '2025-06-25T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/06/25/image-compatibility-in-cloud-native-environments/
post_kind: link
draft: false
tldr: Image Compatibility In Cloud Native Environments The need for image compatibility
  specification Dependencies between containers and host OS Multi-cloud and hybrid
  cloud challenges Image compatibility initiative Implementation in Node Feature Discovery
  Compatibility specification Client implementation for node validation Examples of
  usage Conclusion Get involved In industries where systems must run very reliably
  and meet strict performance criteria such as telecommunication, high-performance
  or AI computing, containerized applications often need specific operating system
  configuration or hardware presence. It is common practice to require the use of
  specific versions of the kernel, its configuration, device drivers, or system components.
summary: 'Image Compatibility In Cloud Native Environments The need for image compatibility
  specification Dependencies between containers and host OS Multi-cloud and hybrid
  cloud challenges Image compatibility initiative Implementation in Node Feature Discovery
  Compatibility specification Client implementation for node validation Examples of
  usage Conclusion Get involved In industries where systems must run very reliably
  and meet strict performance criteria such as telecommunication, high-performance
  or AI computing, containerized applications often need specific operating system
  configuration or hardware presence. It is common practice to require the use of
  specific versions of the kernel, its configuration, device drivers, or system components.
  Despite the existence of the Open Container Initiative (OCI) , a governing community
  to define standards and specifications for container images, there has been a gap
  in expression of such compatibility requirements. The need to address this issue
  has led to different proposals and, ultimately, an implementation in Kubernetes''
  Node Feature Discovery (NFD). NFD is an open source Kubernetes project that automatically
  detects and reports hardware and system features of cluster nodes. This information
  helps users to schedule workloads on nodes that meet specific system requirements,
  which is especially useful for applications with strict hardware or operating system
  dependencies. A container image is built on a base image, which provides a minimal
  runtime environment, often a stripped-down Linux userland, completely empty or distroless.
  When an application requires certain features from the host OS, compatibility issues
  arise. These dependencies can manifest in several ways: Drivers : Host driver versions
  must match the supported range of a library version inside the container to avoid
  compatibility problems. Examples include GPUs and network drivers. Libraries or
  Software : The container must come with a specific version or range of versions
  for a library or software to run optimally in the environment. Examples from high
  performance computing are MPI, EFA, or Infiniband.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/06/25/image-compatibility-in-cloud-native-environments/
