---
title: 'Kubeflow Trainer v2.2: JAX &amp; XGBoost Runtimes, Flux for HPC Support, and
  TrainJob progress and metrics observability'
date: '2026-03-20T00:00:00-05:00'
tags:
- kubeflow
- kubernetes
source: Kubeflow Blog
external_url: https://blog.kubeflow.org/kubeflow-trainer-v2.2-release/
post_kind: link
draft: false
tldr: 'Bringing JAX to Kubernetes with Trainer Bringing XGBoost to Kubernetes with
  Trainer Track TrainJob Progress and Expose Metrics How it works Future Plans Bringing
  Flux Framework for HPC and MPI Bootstrapping Resource Timeout for TrainJobs RuntimePatches
  API to override TrainJob defaults Breaking Changes Replace PodTemplateOverrides
  with RuntimePatches API Remove numProcPerNode from the Torch MLPolicy API Remove
  ElasticPolicy API Some TrainJob API fields are now immutable Release Notes Roadmap
  Moving Forward Join the Community Contribute: Connect with the Community: Learn
  More: Bringing JAX to Kubernetes with Trainer Bringing XGBoost to Kubernetes with
  Trainer Track TrainJob Progress and Expose Metrics How it works Future Plans How
  it works Future Plans Bringing Flux Framework for HPC and MPI Bootstrapping Resource
  Timeout for TrainJobs RuntimePatches API to override TrainJob defaults Breaking
  Changes Replace PodTemplateOverrides with RuntimePatches API Remove numProcPerNode
  from the Torch MLPolicy API Remove ElasticPolicy API Some TrainJob API fields are
  now immutable Replace PodTemplateOverrides with RuntimePatches API Remove numProcPerNode
  from the Torch MLPolicy API Remove ElasticPolicy API Some TrainJob API fields are
  now immutable Release Notes Roadmap Moving Forward Join the Community Contribute:
  Connect with the Community: Learn More: Contribute: Connect with the Community:
  Learn More: Just a little over one week ahead of KubeCon + CloudNativeCon EU 2026,
  the Kubeflow team is excited to ship Trainer v2.2. The v2.2 release reinforces our
  commitment to expanding the Kubeflow Trainer ecosystem – meeting developers where
  they are by adding native support for JAX, XGBoost, and Flux, while also delivering
  deeper observability into training jobs.'
summary: 'Bringing JAX to Kubernetes with Trainer Bringing XGBoost to Kubernetes with
  Trainer Track TrainJob Progress and Expose Metrics How it works Future Plans Bringing
  Flux Framework for HPC and MPI Bootstrapping Resource Timeout for TrainJobs RuntimePatches
  API to override TrainJob defaults Breaking Changes Replace PodTemplateOverrides
  with RuntimePatches API Remove numProcPerNode from the Torch MLPolicy API Remove
  ElasticPolicy API Some TrainJob API fields are now immutable Release Notes Roadmap
  Moving Forward Join the Community Contribute: Connect with the Community: Learn
  More: Bringing JAX to Kubernetes with Trainer Bringing XGBoost to Kubernetes with
  Trainer Track TrainJob Progress and Expose Metrics How it works Future Plans How
  it works Future Plans Bringing Flux Framework for HPC and MPI Bootstrapping Resource
  Timeout for TrainJobs RuntimePatches API to override TrainJob defaults Breaking
  Changes Replace PodTemplateOverrides with RuntimePatches API Remove numProcPerNode
  from the Torch MLPolicy API Remove ElasticPolicy API Some TrainJob API fields are
  now immutable Replace PodTemplateOverrides with RuntimePatches API Remove numProcPerNode
  from the Torch MLPolicy API Remove ElasticPolicy API Some TrainJob API fields are
  now immutable Release Notes Roadmap Moving Forward Join the Community Contribute:
  Connect with the Community: Learn More: Contribute: Connect with the Community:
  Learn More: Just a little over one week ahead of KubeCon + CloudNativeCon EU 2026,
  the Kubeflow team is excited to ship Trainer v2.2. The v2.2 release reinforces our
  commitment to expanding the Kubeflow Trainer ecosystem – meeting developers where
  they are by adding native support for JAX, XGBoost, and Flux, while also delivering
  deeper observability into training jobs. Key highlights of the v2.2 release include:
  First-class support for Training Runtimes for JAX and XGBoost , enabling native
  distributed training on Kubernetes. This marks a major milestone for the Trainer
  project, achieving full compatibility with Training Operator v1 CRDs: PyTorchJob,
  MPIJob, JAXJob, and XGBoostJob – now unified under a single TrainJob abstraction.
  Enhanced training observability , allowing progress and metrics to be propagated
  directly from training scripts to the TrainJob status. Hugging Face Transformers
  already integrate with the KubeflowTrainerCallback to automate this capability.
  Flux runtime support , bringing HPC workloads to Kubernetes and improving MPI bootstrapping
  within TrainJob. TrainJob activeDeadlineSeconds API , enabling explicit timeout
  policies for training jobs. RuntimePatches API , introducing a more flexible and
  scalable way to customize runtime configurations from the TrainJobs. You can now
  install the Kubeflow Trainer control plane and its training runtimes with a single
  command: helm install kubeflow-trainer oci://ghcr. io/kubeflow/charts/kubeflow-trainer
  \ --namespace kubeflow-system \ --create-namespace \ --version 2.2.0 \ --set runtimes.
  defaultEnabled = true helm install kubeflow-trainer oci://ghcr.'
---
Open the original post ↗ https://blog.kubeflow.org/kubeflow-trainer-v2.2-release/
