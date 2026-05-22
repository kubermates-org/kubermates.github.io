---
title: Automating Confidential Containers (CoCo) infrastructure with Kyverno
date: '2026-05-19T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/05/19/automating-confidential-containers-coco-infrastructure-with-kyverno/
post_kind: link
draft: false
tldr: 'Understanding Confidential Containers (CoCo) What a CoCo-Enabled workload typically
  needs Practical deployment challenges The Solution: Automating CoCo infrastructure
  with Kyverno The trust paradox: Kyverno in an untrusted control plane Kyverno inaction:
  An example deployment flow Deployment and attestation process Conclusion Posted
  on May 19, 2026 by Shuting Zhao, Project Maintainer (Nirmata) CNCF projects highlighted
  in this post Confidential Containers (CoCo) adds a critical security layer for containerized
  workloads, especially in environments where parts of the platform are not inherently
  trusted. However, deploying CoCo-enabled workloads often requires application teams
  to manage infrastructure-heavy details that are easy to get wrong.'
summary: 'Understanding Confidential Containers (CoCo) What a CoCo-Enabled workload
  typically needs Practical deployment challenges The Solution: Automating CoCo infrastructure
  with Kyverno The trust paradox: Kyverno in an untrusted control plane Kyverno inaction:
  An example deployment flow Deployment and attestation process Conclusion Posted
  on May 19, 2026 by Shuting Zhao, Project Maintainer (Nirmata) CNCF projects highlighted
  in this post Confidential Containers (CoCo) adds a critical security layer for containerized
  workloads, especially in environments where parts of the platform are not inherently
  trusted. However, deploying CoCo-enabled workloads often requires application teams
  to manage infrastructure-heavy details that are easy to get wrong. By leveraging
  Kyverno as a Policy as Code engine, platform teams can automate much of that CoCo-specific
  wiring, improving developer experience while preserving the core zero-trust security
  model. Confidential Containers (CoCo) is an open-source initiative dedicated to
  securing container workloads in untrusted environments. The fundamental tenet of
  the CoCo trust model is that the Kubernetes control plane is explicitly untrusted.
  Consequently, any pod specifications provided by the Kubernetes control plane are
  considered untrusted and must be verified by the runtime environment before it is
  used. This verification process is typically handled through remote attestation.
  A pod intended to run within a CoCo environment requires the following in its specification:
  runtimeClass (typically required): Specifies the required confidential runtime environment.
  runtimeClass initdata (typically required): This component provides the bootstrap
  configuration for the confidential environment. It includes essential details such
  as remote attestation server details, container image policy, and kata-agent policy.
  This information is crucial for establishing trust and is verified via remote attestation.
  Ref: https://confidentialcontainers.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/05/19/automating-confidential-containers-coco-infrastructure-with-kyverno/
