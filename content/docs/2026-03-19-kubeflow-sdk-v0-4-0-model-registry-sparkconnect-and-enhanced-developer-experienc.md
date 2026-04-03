---
title: 'Kubeflow SDK v0.4.0: Model Registry, SparkConnect, and Enhanced Developer
  Experience'
date: '2026-03-19T00:00:00-05:00'
tags:
- kubeflow
- kubernetes
source: Kubeflow Blog
external_url: https://blog.kubeflow.org/kubeflow-sdk-0.4.0-release/
post_kind: link
draft: false
tldr: 'Unified Model Management: The Model Registry Client Usage Example Distributed
  AI Data at Scale: SparkClient & SparkConnect Usage Example A New Home for Documentation
  Infrastructure & Breaking Changes Better Isolation with Namespaced TrainingRuntimes
  Furthering Parity Between Local and Remote Execution Required: Upgrading to Python
  3.10+ What’s Next for Kubeflow SDK Get Involved! Unified Model Management: The Model
  Registry Client Usage Example Usage Example Distributed AI Data at Scale: SparkClient
  & SparkConnect Usage Example Usage Example A New Home for Documentation Infrastructure
  & Breaking Changes Better Isolation with Namespaced TrainingRuntimes Furthering
  Parity Between Local and Remote Execution Required: Upgrading to Python 3.10+ Better
  Isolation with Namespaced TrainingRuntimes Furthering Parity Between Local and Remote
  Execution Required: Upgrading to Python 3.10+ What’s Next for Kubeflow SDK Get Involved!
  Explore the full documentation at sdk. kubeflow.'
summary: 'Unified Model Management: The Model Registry Client Usage Example Distributed
  AI Data at Scale: SparkClient & SparkConnect Usage Example A New Home for Documentation
  Infrastructure & Breaking Changes Better Isolation with Namespaced TrainingRuntimes
  Furthering Parity Between Local and Remote Execution Required: Upgrading to Python
  3.10+ What’s Next for Kubeflow SDK Get Involved! Unified Model Management: The Model
  Registry Client Usage Example Usage Example Distributed AI Data at Scale: SparkClient
  & SparkConnect Usage Example Usage Example A New Home for Documentation Infrastructure
  & Breaking Changes Better Isolation with Namespaced TrainingRuntimes Furthering
  Parity Between Local and Remote Execution Required: Upgrading to Python 3.10+ Better
  Isolation with Namespaced TrainingRuntimes Furthering Parity Between Local and Remote
  Execution Required: Upgrading to Python 3.10+ What’s Next for Kubeflow SDK Get Involved!
  Explore the full documentation at sdk. kubeflow. org With KubeCon just around the
  corner, we are pleased to announce the release of Kubeflow SDK v0.4.0. This release
  continues the work toward providing a unified, Pythonic interface for all AI workloads
  on Kubernetes. The v0.4.0 release focuses on bridging the gap between data engineering,
  model management, and production-ready ML pipelines. The Kubeflow SDK now covers
  most of the MLOps lifecycle – from data processing and hyperparameter optimization
  to model training and registration: Highlights in Kubeflow SDK v0.4.0 include: Model
  Registry Client for managing model artifacts, versions, and metadata directly from
  the SDK. SparkClient API with SparkConnect support for interactive data processing
  Namespaced TrainingRuntimes for improved isolation and multi-tenant platform management
  Dataset and Model Initializers enabling better parity between local and Kubernetes
  execution A new Kubeflow SDK documentation website with examples, and API reference
  Minimum Python version updated to Python 3.10 for improved security, typing, and
  runtime performance Managing model artifacts, versions, and metadata across experiments
  has historically required stitching together multiple tools outside of your training
  code. In v0.4.0, the SDK introduces ModelRegistryClient – a Pythonic interface to
  the Kubeflow Model Registry, available under the new kubeflow. hub submodule. ModelRegistryClient
  kubeflow. hub The client exposes a minimal, curated API: register models, retrieve
  them by name and version, update their metadata, and iterate over what’s in your
  registry – all without leaving the SDK. It integrates directly with the Model Registry
  server and supports token auth and custom CA configuration for production clusters.'
---
Open the original post ↗ https://blog.kubeflow.org/kubeflow-sdk-0.4.0-release/
