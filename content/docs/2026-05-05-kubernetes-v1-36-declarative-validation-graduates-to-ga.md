---
title: 'Kubernetes v1.36: Declarative Validation Graduates to GA'
date: '2026-05-05T10:35:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/05/05/kubernetes-v1-36-declarative-validation-ga/
post_kind: link
draft: false
tldr: 'Kubernetes v1.36: Declarative Validation Graduates to GA The Motivation: Escaping
  the "Handwritten" Technical Debt Enter validation-gen A Comprehensive Suite of +k8s:
  Tags Advanced Capabilities: "Ambient Ratcheting" Scaling API Reviews with kube-api-linter
  What''s next? Getting involved Acknowledgments In Kubernetes v1.36, Declarative
  Validation for Kubernetes native types has reached General Availability (GA). For
  users, this means more reliable, predictable, and better-documented APIs.'
summary: 'Kubernetes v1.36: Declarative Validation Graduates to GA The Motivation:
  Escaping the "Handwritten" Technical Debt Enter validation-gen A Comprehensive Suite
  of +k8s: Tags Advanced Capabilities: "Ambient Ratcheting" Scaling API Reviews with
  kube-api-linter What''s next? Getting involved Acknowledgments In Kubernetes v1.36,
  Declarative Validation for Kubernetes native types has reached General Availability
  (GA). For users, this means more reliable, predictable, and better-documented APIs.
  By moving to a declarative model, the project also unlocks the future ability to
  publish validation rules via OpenAPI and integrate with ecosystem tools like Kubebuilder.
  For contributors and ecosystem developers, this replaces thousands of lines of handwritten
  validation code with a unified, maintainable framework. This post covers why this
  migration was necessary, how the declarative validation framework works, and what
  new capabilities come with this GA release. For years, the validation of Kubernetes
  native APIs relied almost entirely on handwritten Go code. If a field needed to
  be bounded by a minimum value, or if two fields needed to be mutually exclusive,
  developers had to write explicit Go functions to enforce those constraints. As the
  Kubernetes API surface expanded, this approach led to several systemic issues: Technical
  Debt: The project accumulated roughly 18,000 lines of boilerplate validation code.
  This code was difficult to maintain, error-prone, and required intense scrutiny
  during code reviews. Inconsistency: Without a centralized framework, validation
  rules were sometimes applied inconsistently across different resources. Opaque APIs:
  Handwritten validation logic was difficult to discover or analyze programmatically.
  This meant clients and tooling couldn''t predictably know validation rules without
  consulting the source code or encountering errors at runtime.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/05/05/kubernetes-v1-36-declarative-validation-ga/
