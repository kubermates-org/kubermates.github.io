---
title: Kubeflow Community Distribution 26.03.1 Release Announcement
date: '2026-04-11T00:00:00-05:00'
tags:
- kubeflow
- kubernetes
source: Kubeflow Blog
external_url: https://blog.kubeflow.org/kubeflow-26.03-release/
post_kind: link
draft: false
tldr: 'Highlight features 26.03 Highlight features 26.03.1 Kubeflow Community Distribution:
  Kubeflow Community Distribution 26.03 Kubeflow Community Distribution 26.03.1 Pipelines
  Model Registry → Hub Training Operator (Trainer) Katib Spark Operator Spark Operator
  Community KServe Dashboard and Notebooks Notebooks 2.0.0-alpha What’s New Kubeflow
  MCP Kale: Kubeflow Automated Pipelines Engine How to get started with 26.03 Join
  the Community Want to help? The release versioning is now calendar-based (Year.
  Month.'
summary: 'Highlight features 26.03 Highlight features 26.03.1 Kubeflow Community Distribution:
  Kubeflow Community Distribution 26.03 Kubeflow Community Distribution 26.03.1 Pipelines
  Model Registry → Hub Training Operator (Trainer) Katib Spark Operator Spark Operator
  Community KServe Dashboard and Notebooks Notebooks 2.0.0-alpha What’s New Kubeflow
  MCP Kale: Kubeflow Automated Pipelines Engine How to get started with 26.03 Join
  the Community Want to help? The release versioning is now calendar-based (Year.
  Month. Patch). Around two base releases are planned per year with optional patch
  releases. The best-effort only community support is roughly 6 months and there is
  commercial support available from multiple vendors. Please update regularly as explained
  in our upgrading and extending section to benefit also from security and performance
  improvements. Release details: 26.03 and 26.03.1. Kubernetes 1.35+ Kubeflow Pipelines
  2.16.0, Spark operator 2.5.0 Model registry v0.3.7, Kserve Web Application v0.16.0
  Compatibility of Kubeflow Pipelines v1 and v2 with PSS restricted Extended KServe
  tests with authentication and authorization from inside and outside the cluster
  as well as non-knative / raw deployments Simplified installation and automatic installation
  of the right Kustomize and Kubectl versions Installation steps tested and based
  on our CI, easier in-place updates (optimized PDBs) Cleanup of all synchronization
  steps for faster releases / updates of dependencies Knative 1.20, cert-manager 1.19.4,
  oauth2-proxy v7.14.3, Dex 2.45.0 Fix network policies for cert-manager, knative-serving,
  istio-system, dex, oauth2-proxy Kind 0.32+ and Kubernetes 1.36 CI tests Kubeflow
  Pipelines 2.16.1, Spark operator 2.5.0 Model Registry v0.3.9, KServe Web Application
  v0.18.0 Trainer 2.2.0 Kserve 0.18.0 Kubeflow/notebooks v1 update and workspaces
  (v2) beta Kubeflow/dashboard v2 Enable model registry, catalog, and UI in default
  Kubeflow installation Complete renaming of Model Registry to Kubeflow Hub, capturing
  the project’s broader scope Kubeflow Hub: Prepare for v1 release by ensuring stable
  API Knative 1.22.0, cert-manager 1.20.2, oauth2-proxy v7.15.2, Dex 2.45.1 Istio
  1.30.1 with hostUsers: false support CI, PSS restricted and network policies for
  the optional knative-eventing Restructure Upgrading section with version-specific
  upgrade notes Documentation updates that make it easier to install, extend and upgrade
  Kubeflow Complete MinIO deprecation has been implemented. SeaweedFS storage support
  has been added in 2.15.0. AWS SDK v2 now replaces the MinIO client code. Native
  OIDC support has been added. Control flows supporting conditional evaluation and
  parallel execution have been added to Local Runner.'
---
Open the original post ↗ https://blog.kubeflow.org/kubeflow-26.03-release/
