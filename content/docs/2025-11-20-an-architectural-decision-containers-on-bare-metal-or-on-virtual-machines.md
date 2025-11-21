---
title: 'An architectural decision: Containers on bare metal or on virtual machines'
date: '2025-11-20T13:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/11/20/an-architectural-decision-containers-on-bare-metal-or-on-virtual-machines/
post_kind: link
draft: false
tldr: Posted on November 20, 2025 by Pankaj Gupta, VCF Division, Broadcom CNCF projects
  highlighted in this post Building and running modern applications begins with selecting
  Kubernetes distribution as a baseline. Once a platform team has selected its orchestration
  layer, one of the next architectural choices involves the deployment architecture
  where that cluster will run.
summary: 'Posted on November 20, 2025 by Pankaj Gupta, VCF Division, Broadcom CNCF
  projects highlighted in this post Building and running modern applications begins
  with selecting Kubernetes distribution as a baseline. Once a platform team has selected
  its orchestration layer, one of the next architectural choices involves the deployment
  architecture where that cluster will run. Containers can be deployed directly on
  either bare metal servers or virtual machines. This article examines the characteristics,
  tradeoffs, and community learnings around deploying containers on bare metal compared
  to virtual machines. Historically, running workloads in containers on bare metal
  appealed to organizations that prioritized maximum performance and minimal infrastructure
  overhead. By bypassing the hypervisor layer, containers could directly access compute
  and storage resources. However, advancements in hypervisor technology have significantly
  improved the performance and efficiency of virtualized environments, making containers
  on virtual machines (VMs) viable for production workloads with added operational
  benefits and flexibility. As IT requirements have grown in recent years, platform
  teams now face expanded responsibilities, including enforcing stricter security
  policies, reducing fault domains for higher application availability, supporting
  multiple versions of conformant Kubernetes, and meeting tighter service-level agreements
  (SLAs). These are themes frequently discussed in CNCF TAG Runtime and TAG Security
  , particularly around multi-tenancy models, workload isolation, and lifecycle management.
  These modern demands and technological enhancements have renewed community discussions
  on where clusters should run and how platform teams can meet SLA, security, and
  multi-version requirements IT practitioners should consider the following factors
  when making this decision: Historically, bare metal offered a performance edge.
  Direct hardware access reduced latency and overhead, giving it an advantage in CPU-
  or GPU-intensive workloads. Recent benchmark studies indicate that the historical
  performance gap between bare metal and virtualized environments is now negligible.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/11/20/an-architectural-decision-containers-on-bare-metal-or-on-virtual-machines/
