---
title: Surviving the NGINX EOL? A Practical Policy-as-Code Migration Guide
date: '2026-03-30T23:51:23+00:00'
tags:
- nirmata
- kubernetes
source: Nirmata Blog
external_url: https://nirmata.com/2026/03/30/surviving-the-nginx-eol-a-practical-policy-as-code-migration-guide/?utm_source=rss&utm_medium=rss&utm_campaign=surviving-the-nginx-eol-a-practical-policy-as-code-migration-guide
post_kind: link
draft: false
tldr: 'Why This Isn’t a Simple Swap Phase 1: Assessment and Discovery Phase 2: Annotation
  Mapping: Not Always 1-to-1 Consider Moving to VirtualServer CRDs Using Kyverno to
  Reduce Migration Risk Phase 3: DNS Cutover: Don’t Rush This Part Final Thoughts
  With the community NGINX Ingress controller reaching its retirement this month,
  many of us are facing a looming migration deadline. This guide focuses specifically
  on moving to the F5 NGINX Open Source Ingress Controller , which is the free, open-source
  version maintained by the NGINX engineering team at F5, not the commercial NGINX
  Plus version.'
summary: 'Why This Isn’t a Simple Swap Phase 1: Assessment and Discovery Phase 2:
  Annotation Mapping: Not Always 1-to-1 Consider Moving to VirtualServer CRDs Using
  Kyverno to Reduce Migration Risk Phase 3: DNS Cutover: Don’t Rush This Part Final
  Thoughts With the community NGINX Ingress controller reaching its retirement this
  month, many of us are facing a looming migration deadline. This guide focuses specifically
  on moving to the F5 NGINX Open Source Ingress Controller , which is the free, open-source
  version maintained by the NGINX engineering team at F5, not the commercial NGINX
  Plus version. It offers a production-grade solution without the licensing fees,
  but there is a catch: it operates quite differently from the community version you’re
  currently running. Before you run a single kubectl command, it’s important to understand
  one thing: This is not an image replacement exercise. Even though both controllers
  use NGINX under the hood, their control planes are entirely different implementations.
  That means: Annotation formats differ Feature behavior is not always identical Some
  configurations don’t map directly. If you assume compatibility, you’ll break things.
  The first step is not installation, it’s visibility. Every Ingress resource in your
  cluster needs to be reviewed because the annotation syntax changes between the two
  controllers. Start with a full audit: Enumerate all Ingress resources across namespaces
  Extract the metadata. annotations section Identify which annotations are actively
  used Your goal here is simple: understand what needs to change before making changes.
  This is where automation helps.'
---
Open the original post ↗ https://nirmata.com/2026/03/30/surviving-the-nginx-eol-a-practical-policy-as-code-migration-guide/?utm_source=rss&utm_medium=rss&utm_campaign=surviving-the-nginx-eol-a-practical-policy-as-code-migration-guide
