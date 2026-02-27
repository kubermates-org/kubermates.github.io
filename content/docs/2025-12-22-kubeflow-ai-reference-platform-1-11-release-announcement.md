---
title: Kubeflow AI Reference Platform 1.11 Release Announcement
date: '2025-12-22T00:00:00-06:00'
tags:
- kubeflow
- kubernetes
source: Kubeflow Blog
external_url: https://blog.kubeflow.org/kubeflow-1.11-release/
post_kind: link
draft: false
tldr: 'Highlight features Kubeflow Platform (Manifests & Security) Manifests: Security:
  Pipelines Default object store update Database backend upgrade Model Registry Model
  Registry UI Model Catalog KServe Integration Storage Integrations Additional Improvements
  Training Operator (Trainer) & Katib New API Architecture Python-First Experience
  LLM Fine-Tuning Distributed AI Data Cache Scheduler Integrations Katib Spark Operator
  Broader Spark Support Workload Management & Scheduling Operations & Security Observability
  KServe Multi-Node Inference Model Cache Improvements KEDA Autoscaling Integration
  Gateway API Support vLLM & Hugging Face Runtime Updates Inference Graph Enhancements
  Operational & Security Improvements Kubeflow SDK Dashboard and Notebooks How to
  get started with 1.11 Join the Community Want to help? Kubeflow AI Reference Platform
  1.11 delivers substantial platform improvements focused on scalability, security,
  and operational efficiency. The release reduces per namespace overhead, strengthens
  multi-tenant defaults, and improves overall reliability for running Kubeflow at
  scale on Kubernetes.'
summary: 'Highlight features Kubeflow Platform (Manifests & Security) Manifests: Security:
  Pipelines Default object store update Database backend upgrade Model Registry Model
  Registry UI Model Catalog KServe Integration Storage Integrations Additional Improvements
  Training Operator (Trainer) & Katib New API Architecture Python-First Experience
  LLM Fine-Tuning Distributed AI Data Cache Scheduler Integrations Katib Spark Operator
  Broader Spark Support Workload Management & Scheduling Operations & Security Observability
  KServe Multi-Node Inference Model Cache Improvements KEDA Autoscaling Integration
  Gateway API Support vLLM & Hugging Face Runtime Updates Inference Graph Enhancements
  Operational & Security Improvements Kubeflow SDK Dashboard and Notebooks How to
  get started with 1.11 Join the Community Want to help? Kubeflow AI Reference Platform
  1.11 delivers substantial platform improvements focused on scalability, security,
  and operational efficiency. The release reduces per namespace overhead, strengthens
  multi-tenant defaults, and improves overall reliability for running Kubeflow at
  scale on Kubernetes. Trainer v2.1.0 with unified TrainJob API, Python-first workflows,
  and built-in LLM fine-tuning support Multi-tenant S3 storage with per-namespace
  credentials, with SeaweedFS replacing MinIO as the default backend Massive scalability
  improvements enabling Kubeflow deployments to scale to 1,000+ users, profiles, and
  namespaces Zero pod overhead by default for namespaces and profiles, significantly
  reducing baseline resource consumption Optimized Istio service mesh configuration
  to dramatically reduce sidecar memory usage and network traffic in large clusters
  Stronger security defaults with Pod Security Standards (restricted for system namespaces,
  baseline for user namespaces) Improved authentication and exposure patterns for
  KServe inference services, with automated tests and documentation Expanded Helm
  chart support (experimental) to improve modularity and deployment flexibility Updates
  across core components, including Kubeflow Pipelines, Katib, KServe, Model Registry,
  Istio, and Spark Operator The Kubeflow Platform Working Group focuses on simplifying
  Kubeflow installation, operations, and security. Documentation updates that make
  it easier to install, extend and upgrade Kubeflow For more details and future plans
  please check 1.12.0 roadmap. Pod Security Standards enforced by default : restricted
  for all Kubeflow system namespaces ( #3190 , #3050 ) baseline for user namespaces
  ( #3204 , #3220 ) restricted for all Kubeflow system namespaces ( #3190 , #3050
  ) restricted baseline for user namespaces ( #3204 , #3220 ) baseline Network policies
  enabled by default for critical system namespaces ( knative-serving , oauth2-proxy
  , cert-manager , istio-system , auth ) ( #3228 ) knative-serving oauth2-proxy cert-manager
  istio-system auth Improved multi-tenant isolation for object storage , with per-namespace
  S3 credentials ( #3240 ) Authentication enforcement for KServe inference services
  ( #3180 ) Trivy CVE scans December 15 2025: This release of KFP introduces several
  notable changes that users should consider prior to upgrading. Comprehensive upgrade
  and documentation notes will follow shortly. In the interim, please note the following
  key modifications Kubeflow Pipelines now defaults to SeaweedFS for the object store
  deployment, replacing the previous default of MinIO. MinIO remains fully supported,
  as does any S3-compatible object storage backend, only the default deployment configuration
  has changed. Existing MinIO manifests are still available for users who wish to
  continue using MinIO, though these legacy manifests may be removed in future releases.
  Users with existing data are advised to back up and restore as needed when switching
  object store backends. This release includes a major upgrade to the Gorm database
  backend, which introduces an automated database index migration for users upgrading
  from versions prior to 2.15.0. Because this migration does not support rollback,
  it is strongly recommended that production databases be backed up before performing
  the upgrade.'
---
Open the original post ↗ https://blog.kubeflow.org/kubeflow-1.11-release/
