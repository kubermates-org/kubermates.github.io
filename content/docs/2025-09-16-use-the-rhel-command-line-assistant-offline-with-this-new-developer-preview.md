---
title: Use the RHEL command-line assistant offline with this new developer preview
date: '2025-09-16T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/use-rhel-command-line-assistant-offline-new-developer-preview
post_kind: link
draft: false
tldr: Use the RHEL command-line assistant offline with this new developer preview
  Architecture overview Prerequisites and requirements Hardware requirements Getting
  started Configure the GPU Configure the command-line assistant client Usage First
  query response delay CPU-only systems Intended for individual system use cases Conclusion
  Get started with AI Inference About the authors Brian Smith Máirín Duffy Sally O'Malley
  More like this Blog post Blog post Original podcast Original podcast Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share An offline version
  of the Red Hat Enterprise Linux (RHEL) command-line assistant powered by RHEL Lightspeed
  is now available as a developer preview to existing Red Hat Satellite subscribers.
  This delivers the power of the RHEL command-line assistant in a self-contained format
  that runs locally on a workstation or an individual RHEL system.
summary: 'Use the RHEL command-line assistant offline with this new developer preview
  Architecture overview Prerequisites and requirements Hardware requirements Getting
  started Configure the GPU Configure the command-line assistant client Usage First
  query response delay CPU-only systems Intended for individual system use cases Conclusion
  Get started with AI Inference About the authors Brian Smith Máirín Duffy Sally O''Malley
  More like this Blog post Blog post Original podcast Original podcast Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share An offline version
  of the Red Hat Enterprise Linux (RHEL) command-line assistant powered by RHEL Lightspeed
  is now available as a developer preview to existing Red Hat Satellite subscribers.
  This delivers the power of the RHEL command-line assistant in a self-contained format
  that runs locally on a workstation or an individual RHEL system. This enables the
  assistant to function in a completely disconnected, offline, or air-gapped environment
  because it doesn''t require any external network connectivity to operate. The command-line
  assistant provides AI-powered guidance and suggestions to help you with a wide range
  of RHEL tasks. We’ve extended its knowledge about RHEL installation and upgrades
  topics, enabling you to get assistance in these areas even with limited or no connectivity.
  The offline version of command-line assistant is delivered as a set of container
  images that can be run with Podman. The containers used are: installer container
  : Pulls the other required containers, installs the rhel-cla command, and optionally
  creates a systemd service rlsapi container : Provides the endpoint that the command-line
  assistant client communicates with rag-database container : The retrieval-augmented
  generation (RAG) database used to supplement the LLM’s knowledge with additional
  data such as the RHEL documentation ramalama container : Provides LLM inference
  Your Red Hat Satellite subscription provides you with tools to locally manage your
  RHEL environments. These tools include the Satellite product itself, as well as
  the recently introduced Red Hat Offline Knowledge Portal , which provides an offline
  version of Red Hat''s exclusive knowledge content. We''ve now expanded the Satellite
  subscription to also provide the offline version of the RHEL command-line assistant.
  The offline version of the command-line assistant is delivered as a set of containers,
  and can run on a RHEL system, or a Mac or Windows workstation. If you''re using
  a Mac system, Podman Desktop is required , and it''s recommended to use a system
  equipped with an NVIDIA, AMD, or Mac M-series GPU. CPU-only systems (RHEL 9.6+ and
  10+ / Fedora 42 / Windows 11): RAM : 8 GB CPU cores : 2 GPU-capable systems (RHEL
  9.6+ and 10+ / Fedora 42 / Windows 11): RAM : 4 GB GPU : At least 4 GB of VRAM Apple
  systems (macOS 15.'
---
Open the original post ↗ https://www.redhat.com/en/blog/use-rhel-command-line-assistant-offline-new-developer-preview
