---
title: Building a hardened, image-based foundation for AI agents
date: '2026-04-28T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/building-hardened-image-based-foundation-ai-agents
post_kind: link
draft: false
tldr: 'Building a hardened, image-based foundation for AI agents What is fedora-bootc?
  The agentic OS: Why I built this image The power of the fleet How it works using
  fedora-bootc Secrets stay out of the image What could the future look like? About
  the author Sally O''Malley More like this Designing multitenant GPU infrastructure:
  Isolation across virtualization and Kubernetes platforms Announcing Fedora 44 Technically
  Speaking | Build a production-ready AI toolbox Technically Speaking | Platform engineering
  for AI agents Browse by channel Automation Artificial intelligence Open hybrid cloud
  Security Edge computing Infrastructure Applications Virtualization Share This week,
  I developed a community operating system image for running AI agents: an agentic
  OS prototype. It is built using fedora- bootc , a community project that allows
  for defining a bootable Linux OS directly in a Containerfile.'
summary: 'Building a hardened, image-based foundation for AI agents What is fedora-bootc?
  The agentic OS: Why I built this image The power of the fleet How it works using
  fedora-bootc Secrets stay out of the image What could the future look like? About
  the author Sally O''Malley More like this Designing multitenant GPU infrastructure:
  Isolation across virtualization and Kubernetes platforms Announcing Fedora 44 Technically
  Speaking | Build a production-ready AI toolbox Technically Speaking | Platform engineering
  for AI agents Browse by channel Automation Artificial intelligence Open hybrid cloud
  Security Edge computing Infrastructure Applications Virtualization Share This week,
  I developed a community operating system image for running AI agents: an agentic
  OS prototype. It is built using fedora- bootc , a community project that allows
  for defining a bootable Linux OS directly in a Containerfile. The creation of this
  agentic OS spotlights a critical evolution: By providing a hardened, image-based
  environment, it establishes a robust community template for what an agentic OS can
  look like in practice. It explores how a dedicated runtime built with open source
  tools could look – an example of open source’s profound ability to deliver a reliable
  infrastructure layer necessary to move from theoretical agent behavior to production-ready
  systems. To run any application in containers, you typically craft a Dockerfile,
  build an image, push it to a registry, pull it somewhere else, and run it. fedora-bootc
  takes that same ubiquitous workflow and extends it across entire operating systems.
  As a Fedora community project, fedora-bootc uses Open Container Initiative and Docker
  containers as the transport and delivery format for base operating systems. A fedora-bootc
  image includes the Linux kernel and can be converted into a full disk image (QEMU
  Copy On Write version 2 (QCOW2), Amazon Machine Image (AMI), ISO 9660 Image, Google
  Cloud Image, etc. ). Once booted, the container image is the system – owning the
  kernel, init process, and root filesystem. Most of the filesystem is read-only.
  You define your OS at build time, and at runtime, you’re limited to what you explicitly
  allow to change.'
---
Open the original post ↗ https://www.redhat.com/en/blog/building-hardened-image-based-foundation-ai-agents
