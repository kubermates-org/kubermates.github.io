---
title: 'Calico Ingress Gateway: Key FAQs Before Migrating from NGINX Ingress Controller'
date: '2026-02-03T23:39:01+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/calico-ingress-gateway-key-faqs-before-migrating-from-nginx-ingress-controller/
post_kind: link
draft: false
tldr: 'What Platform Teams Need to Know Before Moving to Gateway API Question 1: Can
  I use the upstream Envoy Gateway as a PoC before moving to Calico Ingress? Question
  2: What is the difference between Calico Open Source and Calico Enterprise in terms
  of Gateway API features? Question 3: What exactly does a “hardened” image mean?
  Are they modified, security-validated, or aligned with compliance requirements?
  Question 4: Do I need to install the Calico CNI to use Calico Ingress Gateway? Question
  5: Can I migrate incrementally, or is it an “all-or-nothing” big bang? Question
  6: Are there any recommendations or best practices for capturing and evaluating
  performance with Gateway API? Migrating from Ingress API to Gateway API Your Roadmap
  to Modern Ingress Coming next: A step-by-step NGINX controller migration guide See
  the Migration in Action We recently sat down with representatives from 42 companies
  to discuss a pivotal moment in Kubernetes networking: the NGINX Ingress retirement.
  With the March 2026 retirement of the NGINX Ingress Controller fast approaching,
  platform teams are now facing a hard deadline to modernize their ingress strategy.'
summary: 'What Platform Teams Need to Know Before Moving to Gateway API Question 1:
  Can I use the upstream Envoy Gateway as a PoC before moving to Calico Ingress? Question
  2: What is the difference between Calico Open Source and Calico Enterprise in terms
  of Gateway API features? Question 3: What exactly does a “hardened” image mean?
  Are they modified, security-validated, or aligned with compliance requirements?
  Question 4: Do I need to install the Calico CNI to use Calico Ingress Gateway? Question
  5: Can I migrate incrementally, or is it an “all-or-nothing” big bang? Question
  6: Are there any recommendations or best practices for capturing and evaluating
  performance with Gateway API? Migrating from Ingress API to Gateway API Your Roadmap
  to Modern Ingress Coming next: A step-by-step NGINX controller migration guide See
  the Migration in Action We recently sat down with representatives from 42 companies
  to discuss a pivotal moment in Kubernetes networking: the NGINX Ingress retirement.
  With the March 2026 retirement of the NGINX Ingress Controller fast approaching,
  platform teams are now facing a hard deadline to modernize their ingress strategy.
  This urgency was reflected in our recent workshop, “ Switching from NGINX Ingress
  Controller to Calico Ingress Gateway ” which saw an overwhelming turnout, with engineers
  representing a cross-section of the industry, from financial services to high-growth
  tech startups. During the session, the Tigera team highlighted a hard truth for
  platform teams: the original Ingress API was designed for a simpler era. Today,
  teams are struggling to manage production traffic through “annotation sprawl”—a
  web of brittle, implementation-specific hacks that make multi-tenancy and consistent
  security an operational nightmare. The move to the Kubernetes Gateway API isn’t
  just a mandatory update; it’s a graduation to a role-oriented, expressive networking
  model. We’ve previously explored this shift in our blogs on Understanding the NGINX
  Retirement and Why the Ingress NGINX Controller is Dead. After the workshop, we
  narrowed down the top questions keeping platform engineers up at night. Here is
  a detailed breakdown of those key concerns and our answers. Answer: Yes. Calico
  Ingress Gateway is built on a 100% upstream distribution of Envoy Gateway. Because
  we maintain strict compatibility with the Kubernetes Gateway API standard , you
  can confidently start a Proof of Concept (PoC) using standard Envoy Ingress Gateway.'
---
Open the original post ↗ https://www.tigera.io/blog/calico-ingress-gateway-key-faqs-before-migrating-from-nginx-ingress-controller/
