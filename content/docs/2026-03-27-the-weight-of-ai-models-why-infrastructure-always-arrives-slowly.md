---
title: 'The weight of AI models: Why infrastructure always arrives slowly'
date: '2026-03-27T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/03/27/the-weight-of-ai-models-why-infrastructure-always-arrives-slowly/
post_kind: link
draft: false
tldr: 'The gap nobody talks about — until it breaks production When your model weighs
  more than your entire app Three paths forward — and why none of them are enough
  Rethinking the delivery pipeline: Models deserve better than a shell script What
  If we shipped models the same way we ship code? Walking the pipeline: A build story
  in four steps Build Management Delivery Future Collaborative Projects References
  Posted on March 27, 2026 by Wenbo Qi (Dragonfly/ModelPack Maintainer), Chenyu Zhang
  (Harbor/ModelPack Maintainer) and Feynman Zhou (ORAS Maintainer and CNCF Ambassador)
  CNCF projects highlighted in this post As AI adoption accelerates across industries,
  organizations face a critical bottleneck that is often overlooked until it becomes
  a serious obstacle: reliably managing and distributing large model weight files
  at scale. A model’s weights serve as the central artifact that bridges both training
  and inference pipelines — yet the infrastructure surrounding this artifact is frequently
  an afterthought.'
summary: 'The gap nobody talks about — until it breaks production When your model
  weighs more than your entire app Three paths forward — and why none of them are
  enough Rethinking the delivery pipeline: Models deserve better than a shell script
  What If we shipped models the same way we ship code? Walking the pipeline: A build
  story in four steps Build Management Delivery Future Collaborative Projects References
  Posted on March 27, 2026 by Wenbo Qi (Dragonfly/ModelPack Maintainer), Chenyu Zhang
  (Harbor/ModelPack Maintainer) and Feynman Zhou (ORAS Maintainer and CNCF Ambassador)
  CNCF projects highlighted in this post As AI adoption accelerates across industries,
  organizations face a critical bottleneck that is often overlooked until it becomes
  a serious obstacle: reliably managing and distributing large model weight files
  at scale. A model’s weights serve as the central artifact that bridges both training
  and inference pipelines — yet the infrastructure surrounding this artifact is frequently
  an afterthought. This article addresses the operational challenges of managing AI
  model artifacts at enterprise scale, and introduces a cloud-native solution that
  brings software delivery best practices – versioning, immutability, and GitOps,
  to the world of large model files. The cloud native gap : Most existing ML model
  storage approaches were not designed with Kubernetes-native delivery in mind, leaving
  a critical gap between how software artifacts are managed and how model artifacts
  are managed. Within the CNCF ecosystem, projects such as ModelPack, ORAS, Harbor,
  and Dragonfly are exploring complementary approaches to managing and distributing
  large artifacts. Today, enterprises operate AI infrastructure on Kubernetes yet
  their model artifact management lags behind. Software containers are pulled from
  OCI registries with full versioning, security scanning, and rollback support. This
  gap creates deployment fragility, security risks, and operational overhead at scale.
  Modern foundation models are not small. A single model checkpoint can range from
  tens of gigabytes to several terabytes. For reference, a quantized LLaMA-3 70B model
  weighs approximately 140 GB, while frontier multimodal models can easily exceed
  1 TB. These are not files you version-control with standard Git — they demand dedicated
  storage strategies, efficient transfer protocols, and careful access control.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/03/27/the-weight-of-ai-models-why-infrastructure-always-arrives-slowly/
