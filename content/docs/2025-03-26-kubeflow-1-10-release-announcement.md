---
title: Kubeflow 1.10 Release Announcement
date: '2025-03-26T00:00:00-05:00'
tags:
- kubeflow
- kubernetes
source: Kubeflow Blog
external_url: https://blog.kubeflow.org/kubeflow-1.10-release/
post_kind: link
draft: false
tldr: 'Highlight features Kubeflow Platform (Manifests & Security) Manifests: Security:
  Pipelines Support for Placeholders in Resource Limits Support for Loop Parallelism
  Implement SubDAG Output Resolution Model Registry Model Registry UI Custom Storage
  Initializer Training Operator (Trainer) & Katib Hyperparameter Optimization API
  for LLMs Support for Various Parameter Distributions Push-Based Metrics Collection
  Dashboard & Notebooks Prometheus Metrics for Notebooks More Descriptive Error Messages
  Spark Operator KServe New Python SDK OCI Storage for Models Model Cache Feature
  Hugging Face Integration What comes next? How to get started with 1.10 Join the
  Community Want to help? Kubeflow 1.10.0 delivers essential updates that enhance
  the flexibility, efficiency, and scalability of machine learning workflows. The
  new features span across several components, improving both user experience and
  system performance.'
summary: 'Highlight features Kubeflow Platform (Manifests & Security) Manifests: Security:
  Pipelines Support for Placeholders in Resource Limits Support for Loop Parallelism
  Implement SubDAG Output Resolution Model Registry Model Registry UI Custom Storage
  Initializer Training Operator (Trainer) & Katib Hyperparameter Optimization API
  for LLMs Support for Various Parameter Distributions Push-Based Metrics Collection
  Dashboard & Notebooks Prometheus Metrics for Notebooks More Descriptive Error Messages
  Spark Operator KServe New Python SDK OCI Storage for Models Model Cache Feature
  Hugging Face Integration What comes next? How to get started with 1.10 Join the
  Community Want to help? Kubeflow 1.10.0 delivers essential updates that enhance
  the flexibility, efficiency, and scalability of machine learning workflows. The
  new features span across several components, improving both user experience and
  system performance. Trainer 2.0 New UI for Model Registry Spark Operator as a core
  Kubeflow component Kubernetes and container security (CISO compatibility) Hyperparameter
  Optimization for LLMs Fine-Tuning Loop parallelism in Pipelines New parameter distributions
  for Katib Deeper Model Registry integrations with KServe New Python SDK, OCI storage,
  and model caching for KServe New security contexts and rootless Istio-CNI integrations
  for Spark Operator The Kubeflow Platform Working Group focuses on simplifying Kubeflow
  installation, operations, and security. Spark Operator 2.1.0 included in Kubeflow
  platform, although not installed yet by default Documentation updates that make
  it easier to install, extend and upgrade Kubeflow For more details and future plans
  please consult the 1.10.0 and 1.10.1/1.11.0 milestones CVE reductions - regular
  scanning with trivy Kubernetes and container security best practices: Rootless containers
  / PodSecurityStandards restricted for: Istio-CNI, Knative, Dex, Oauth2-proxy, Spark
  50 % done : KFP, Notebooks / Workspaces, Katib, Trainer, Kserve, … Istio-CNI as
  default for rootless Kubeflow postponed to 1.10.1 Rootless containers / PodSecurityStandards
  restricted for: Istio-CNI, Knative, Dex, Oauth2-proxy, Spark 50 % done : KFP, Notebooks
  / Workspaces, Katib, Trainer, Kserve, … Istio-CNI as default for rootless Kubeflow
  postponed to 1.10.1 OIDC-authservice has been replaced by oauth2-proxy Oauth2-proxy
  and Dex documentation for external OIDC authentication (Keycloak, and OIDC providers
  such as Azure, Google etc. ) Trivy CVE scans March 25 2025: Kubeflow Pipelines 2.4.1
  introduces support for placeholders in resource limits , enhancing flexibility in
  pipeline execution. This update allows users to define dynamic resource limits using
  parameterized values, enabling more adaptable and reusable pipeline definitions.
  Kubeflow Pipelines 2.4.1 introduces a new Parallelism Limit for ParallelFor tasks
  , giving users the ability to run massively parallel inference pipelines, with more
  control over parallel execution in their workflows. This feature allows users to
  specify the maximum number of parallel iterations, preventing resource overutilization
  and improving system stability. When running large pipelines with GPUs, proper use
  of this feature could save your team thousands of dollars in compute expenses. ParallelFor
  Kubeflow 1.10 ensures that pipelines using nested DAGs work correctly and reliably
  when treated as components. Outputs from deeply nested DAGs will now resolve properly,
  avoiding broken dependencies. Model Registry introduces a new user interface and
  enhanced model management capabilities.'
---
Open the original post ↗ https://blog.kubeflow.org/kubeflow-1.10-release/
