---
title: Running a self-hosted LLM in Kubernetes with vLLM
date: '2026-07-16T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/07/16/running-a-self-hosted-llm-in-kubernetes-with-vllm/
post_kind: link
draft: false
tldr: Background on vLLM Overview of the setup Prerequisites Deployment Creating the
  PVC and secret Deploying vLLM Watching the logs Testing the deployment Pausing the
  deployment Conclusion Posted on July 16, 2026 by Michael Troutman, LINBIT CNCF projects
  highlighted in this post Running large language model (LLM) workloads in-house is
  one of several patterns teams adopt alongside managed API services. Managed API
  services are convenient and well suited to many workloads.
summary: Background on vLLM Overview of the setup Prerequisites Deployment Creating
  the PVC and secret Deploying vLLM Watching the logs Testing the deployment Pausing
  the deployment Conclusion Posted on July 16, 2026 by Michael Troutman, LINBIT CNCF
  projects highlighted in this post Running large language model (LLM) workloads in-house
  is one of several patterns teams adopt alongside managed API services. Managed API
  services are convenient and well suited to many workloads. Self-hosting is a complementary
  option that some teams choose for reasons such as cost predictability at high request
  volumes, more control over latency, and controlling data-residency to meet contractual
  or regulatory requirements. A hybrid approach (running open source models locally
  for high-volume or sensitive workloads while using managed API calls for tasks that
  benefit from them) is a practical middle ground that combines both. This article
  documents what it took to set up that kind of self-hosted inference stack in a Kubernetes
  lab environment. In this example, we’ve chosen to use vLLM for inference and LINSTOR®
  for persistent storage. vLLM is a high-performance, open source inference engine
  for large language models. It is designed for serving many concurrent requests efficiently
  in a cluster environment. An important characteristic of vLLM for this use case
  is that it exposes an OpenAI-compatible REST API. Anything that already talks to
  the OpenAI API (LangChain, LlamaIndex, or your own code that calls the OpenAI SDK)
  can be pointed at a self-hosted vLLM instance with nothing more than a URL change.
  That compatibility is what makes the hybrid architecture described earlier a viable
  alternative. Instructions in this article use a Kubernetes cluster with LINSTOR
  providing persistent storage through the LINSTOR Container Storage Interface (CSI)
  driver.
---
Open the original post ↗ https://www.cncf.io/blog/2026/07/16/running-a-self-hosted-llm-in-kubernetes-with-vllm/
