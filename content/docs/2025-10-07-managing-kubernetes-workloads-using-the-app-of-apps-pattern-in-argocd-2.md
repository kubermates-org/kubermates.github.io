---
title: Managing Kubernetes Workloads Using the App of Apps Pattern in ArgoCD-2
date: '2025-10-07T14:36:18+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/10/07/managing-kubernetes-workloads-using-the-app-of-apps-pattern-in-argocd-2/
post_kind: link
draft: false
tldr: Posted on October 7, 2025 by Marcin Kujawski, Principal Kubernetes Engineer,
  Software Mind CNCF projects highlighted in this post Managing a cloud native infrastructure
  at scale is no longer just about deploying single applications – it’s about organizing
  environments, defining clear boundaries and keeping everything version-controlled,
  consistent, automated and easily managed within a simple and clear lifecycle process.
  This is where GitOps practices – tools like ArgoCD – truly shine.
summary: 'Posted on October 7, 2025 by Marcin Kujawski, Principal Kubernetes Engineer,
  Software Mind CNCF projects highlighted in this post Managing a cloud native infrastructure
  at scale is no longer just about deploying single applications – it’s about organizing
  environments, defining clear boundaries and keeping everything version-controlled,
  consistent, automated and easily managed within a simple and clear lifecycle process.
  This is where GitOps practices – tools like ArgoCD – truly shine. One of ArgoCD’s
  most powerful patterns is called App of Apps – a design where a single parent ArgoCD
  Application manages and deploys multiple child ArgoCD Applications. It brings order
  to potentially chaotic deployments, improves observability and aligns perfectly
  with GitOps methodologies. In this article, we’ll explore the App of Apps pattern
  in ArgoCD, including its concept, structure, pros and cons, as well as a production-grade
  way to configure child applications via dedicated values files. You’ll learn how
  to build a reusable, scalable pattern by deploying two example applications: NGINX
  Ingress Controller Cert-Manager Let’s dive in. What Is the App of Apps Pattern in
  ArgoCD? Concept The App of Apps pattern is an ArgoCD deployment strategy where one
  central ArgoCD Application (the “parent”) is responsible for managing and deploying
  several other Applications (the “children”). Each child application corresponds
  to a logical unit (e. g. , a microservice, controller, or platform component) and
  is fully managed by ArgoCD. This enables a modular, hierarchical structure – especially
  useful in environments where infrastructure is composed of many separate but related
  components. Real-World Analogy Think of the parent app as a conductor of an orchestra.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/10/07/managing-kubernetes-workloads-using-the-app-of-apps-pattern-in-argocd-2/
