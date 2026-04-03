---
title: Using containers to bring software engineering rigor to AI workloads
date: '2026-03-31T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/using-containers-bring-software-engineering-rigor-ai-workloads
post_kind: link
draft: false
tldr: 'Using containers to bring software engineering rigor to AI workloads What is
  the Open Container Initiative? Containerizing AI models with ModelCar What is a
  ModelCar container? Model size considerations OCI artifacts for models Containerizing
  MCP servers for enterprise deployment Benefits of containerized MCP servers When
  not to containerize your MCP servers Containerizing Agent Skills Containerizing
  AI agents Single-user agents and sub-agents Containers for sandboxing Benefits of
  containerizing AI workloads Software supply chain security Version control and rollback
  Consistent deployment Observability Isolation and access control Looking ahead:
  Workload identity and zero trust Final thoughts The adaptable enterprise: Why AI
  readiness is disruption readiness About the author Ann Marie Fred More like this
  Red Hat and NVIDIA: Setting standards for high-performance AI inference Red Hat
  AI tops MLPerf Inference v6.0 with vLLM on Qwen3-VL, Whisper, and GPT-OSS-120B Technically
  Speaking | Build a production-ready AI toolbox Technically Speaking | Platform engineering
  for AI agents Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share As AI workloads move from experimental prototypes into production environments,
  enterprises face a familiar challenge—how do you protect, manage, and govern these
  new components with the same rigor you apply to traditional software applications?
  A key piece of the puzzle lies in something your organization likely already uses
  extensively—containers, specifically Open Container Initiative (OCI) containers.
  The Open Container Initiative defines open specifications for image formats, container
  runtimes, and distribution, helping organizations avoid vendor lock-in.'
summary: 'Using containers to bring software engineering rigor to AI workloads What
  is the Open Container Initiative? Containerizing AI models with ModelCar What is
  a ModelCar container? Model size considerations OCI artifacts for models Containerizing
  MCP servers for enterprise deployment Benefits of containerized MCP servers When
  not to containerize your MCP servers Containerizing Agent Skills Containerizing
  AI agents Single-user agents and sub-agents Containers for sandboxing Benefits of
  containerizing AI workloads Software supply chain security Version control and rollback
  Consistent deployment Observability Isolation and access control Looking ahead:
  Workload identity and zero trust Final thoughts The adaptable enterprise: Why AI
  readiness is disruption readiness About the author Ann Marie Fred More like this
  Red Hat and NVIDIA: Setting standards for high-performance AI inference Red Hat
  AI tops MLPerf Inference v6.0 with vLLM on Qwen3-VL, Whisper, and GPT-OSS-120B Technically
  Speaking | Build a production-ready AI toolbox Technically Speaking | Platform engineering
  for AI agents Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share As AI workloads move from experimental prototypes into production environments,
  enterprises face a familiar challenge—how do you protect, manage, and govern these
  new components with the same rigor you apply to traditional software applications?
  A key piece of the puzzle lies in something your organization likely already uses
  extensively—containers, specifically Open Container Initiative (OCI) containers.
  The Open Container Initiative defines open specifications for image formats, container
  runtimes, and distribution, helping organizations avoid vendor lock-in. OCI containers
  are an industry-standard format for packaging software applications, so they are
  able to run consistently across different environments, container engines (like
  Docker or Podman), and cloud platforms. An OCI artifact is similar to a container,
  but instead of executable images, artifacts store other content like files and directories.
  OCI-compatible artifact repositories (including Quay, Artifactory, Docker Hub and
  registries from the major cloud providers) can store and manage versioning of OCI
  containers and artifacts. OCI provides a standardized and portable way to package
  and distribute software. By packaging your AI models, Model Context Protocol (MCP)
  servers, and AI agents using OCI containers, you can use your existing software
  supply chain security processes, CI/CD pipelines, and container orchestration infrastructure.
  This approach brings the same governance and auditability to your AI stack that
  you already apply to your application workloads. Large language models (LLMs) and
  other AI models present unique packaging challenges. They consist of large binary
  files, configuration metadata, and specific file structure requirements. In the
  past, organizations have relied on S3-compatible object storage to distribute models,
  but this approach creates friction with existing container-based workflows and security
  processes. We recommend building your AI models into OCI containers using a specific
  file structure we call ModelCar.'
---
Open the original post ↗ https://www.redhat.com/en/blog/using-containers-bring-software-engineering-rigor-ai-workloads
