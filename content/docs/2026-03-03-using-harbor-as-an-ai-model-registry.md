---
title: Using Harbor as an AI Model Registry
date: '2026-03-03T08:59:46+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/03/03/using-harbor-as-an-ai-model-registry/
post_kind: link
draft: false
tldr: 'THE PROBLEM: WHY AI MODELS NEED A REGISTRY OCI ARTIFACTS: THE FOUNDATION What
  Is an OCI Artifact? The CNAI Model Spec Tools for Packaging Models as OCI Artifacts
  HOW HARBOR EVOLVED TO SUPPORT AI MODELS Harbor’s OCI Foundation The AI Model Journey
  The Architecture END-TO-END EXAMPLE: DOWNLOAD, CONVERT, PACKAGE, AND PUSH Prerequisites
  Step 1: Download the Model from Hugging Face Step 2: Convert to GGUF Format with
  llama. cpp Step 3: Package and Push the Model to Harbor Verifying in Harbor MODEL
  LIFECYCLE OPERATIONS IN HARBOR CONCLUSION Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles Implementing Cross-Region Replication with Harbor in
  VMware Cloud Foundation Securing Your Software Supply Chain with Harbor Using Harbor
  as a Proxy Cache for Cloud-Based Registries The container ecosystem solved software
  distribution decades ago: build an image, push it to a registry, pull it anywhere.'
summary: 'THE PROBLEM: WHY AI MODELS NEED A REGISTRY OCI ARTIFACTS: THE FOUNDATION
  What Is an OCI Artifact? The CNAI Model Spec Tools for Packaging Models as OCI Artifacts
  HOW HARBOR EVOLVED TO SUPPORT AI MODELS Harbor’s OCI Foundation The AI Model Journey
  The Architecture END-TO-END EXAMPLE: DOWNLOAD, CONVERT, PACKAGE, AND PUSH Prerequisites
  Step 1: Download the Model from Hugging Face Step 2: Convert to GGUF Format with
  llama. cpp Step 3: Package and Push the Model to Harbor Verifying in Harbor MODEL
  LIFECYCLE OPERATIONS IN HARBOR CONCLUSION Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles Implementing Cross-Region Replication with Harbor in
  VMware Cloud Foundation Securing Your Software Supply Chain with Harbor Using Harbor
  as a Proxy Cache for Cloud-Based Registries The container ecosystem solved software
  distribution decades ago: build an image, push it to a registry, pull it anywhere.
  In contrast, AI model management remains fragmented. Models live on shared drives,
  cloud buckets, or are integrated directly into container images. However, what if
  we could treat AI models the same way we treat container images? This post walks
  through the technical underpinnings that make this possible: what Open Container
  Initiative (OCI) artifacts are, how AI models are packaged into them, and how Harbor
  evolved to become a model registry. Then, we’ll share a complete end-to-end workflow
  from pulling a model from Hugging Face, converting it for CPU inference with llama.
  cpp, pushing it to Harbor using different packaging tools, and deploying it on a
  Kubernetes cluster with KServe and vLLM. A trained AI model is, at its core, a collection
  of files: weight tensors serialized in formats like SafeTensors or GGUF, a tokenizer
  configuration, and metadata describing the architecture and training process. Today,
  distributing these files typically involves: Downloading from Hugging Face Hub or
  a similar model zoo Copying weights into a shared filesystem (NFS or S3) Baking
  model weights directly into a Docker image alongside the inference server However,
  incorporating weights into container images conflates the model lifecycle with the
  inference server lifecycle. A 7B parameter model can be 14GB+, and you don’t want
  to rebuild and re-push a multi-gigabyte image every time you update your serving
  code. Consequently, what organizations need is a system that provides: Versioned,
  immutable storage for model artifacts Role-based access control and audit trails
  Vulnerability scanning of the serving environment Replication across geographies
  and environments Integration with existing CI/CD and Kubernetes tooling Container
  registries already provide all of this for container images. The key insight is
  that the OCI specification was designed to be extensible enough to store any type
  of artifact including AI models.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/03/03/using-harbor-as-an-ai-model-registry/
