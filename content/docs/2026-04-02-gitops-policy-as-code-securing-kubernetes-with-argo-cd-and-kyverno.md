---
title: 'GitOps policy-as-code: Securing Kubernetes with Argo CD and Kyverno'
date: '2026-04-02T09:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/04/02/gitops-policy-as-code-securing-kubernetes-with-argo-cd-and-kyverno/
post_kind: link
draft: false
tldr: 'What is Kyverno? Why Kyverno with Argo CD? Step 1: Add Kyverno as an Argo CD
  application infra-services/kyverno. yaml Step 2: Wrap the official Kyverno Helm
  chart kyverno/Chart.'
summary: 'What is Kyverno? Why Kyverno with Argo CD? Step 1: Add Kyverno as an Argo
  CD application infra-services/kyverno. yaml Step 2: Wrap the official Kyverno Helm
  chart kyverno/Chart. yaml kyverno/values. yaml Step 3: In ArgoCD UI Confirm Argo
  application Kyverno is created Step 4: Add Kyverno Policies as an Argo CD Application
  infra-services/kyverno-policies. yaml Step 5: Wrap and configure the Kyverno policies
  Helm chart kyverno-policies/Chart. yaml kyverno-policies/values. yaml Step 6: Add
  support for custom Kyverno policies (optional) Step 7: Using custom policies Viewing
  policy violations Kyverno policy reports Posted on April 2, 2026 by Albena Galabova,
  Igtix CNCF projects highlighted in this post A hands-on guide to deploying Kyverno
  with Argo CD and enforcing custom policies As Kubernetes environments develop, GitOps
  with Argo CD has become the standard for declarative, self-healing infrastructure.
  Yet without guardrails for your deployments, misconfigured, insecure, or non-compliant
  resources can easily make it to production. This blog explores how to deploy Kyverno
  alongside Argo CD, using baseline policies from the official Kyverno Policies Helm
  chart and demonstrating how to add your own custom policies on top. Kyverno is a
  CNCF graduated project that acts as a policy engine for Kubernetes. It lets you
  define rules for what is and isn’t allowed in your cluster, all written as standard
  Kubernetes YAML. Kyverno operates at the admission controller level, meaning it
  intercepts resource requests before they hit the cluster and acts on them based
  on your policies.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/04/02/gitops-policy-as-code-securing-kubernetes-with-argo-cd-and-kyverno/
