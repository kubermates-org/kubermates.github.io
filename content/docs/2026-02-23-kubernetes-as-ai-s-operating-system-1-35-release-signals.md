---
title: 'Kubernetes as AI’s operating system: 1.35 release signals'
date: '2026-02-23T12:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/02/23/kubernetes-as-ais-operating-system-1-35-release-signals/
post_kind: link
draft: false
tldr: 'Why v1.35 reads like an AI-infrastructure release The changes that matter for
  AI/ML operations In-place Pod resize is stable Device allocation keeps moving toward
  a baseline capability KYAML becomes the default kubectl output format Why AI keeps
  pushing teams toward a shared operating layer Platform engineering implications
  Ecosystem note: Ingress NGINX retirement timeline Practical evaluation steps for
  v1.35 About the author Posted on February 23, 2026 by Angel Ramirez, CEO of Cuemby
  and CNCF Ambassador CNCF projects highlighted in this post Kubernetes has become
  the place where teams coordinate mixed production workloads: services, batch jobs,
  data pipelines, and ML training. The Kubernetes v1.35 (“Timbernetes”) release reinforces
  that trajectory with changes that reduce operational friction in scheduling, resource
  control, and configuration workflows.'
summary: 'Why v1.35 reads like an AI-infrastructure release The changes that matter
  for AI/ML operations In-place Pod resize is stable Device allocation keeps moving
  toward a baseline capability KYAML becomes the default kubectl output format Why
  AI keeps pushing teams toward a shared operating layer Platform engineering implications
  Ecosystem note: Ingress NGINX retirement timeline Practical evaluation steps for
  v1.35 About the author Posted on February 23, 2026 by Angel Ramirez, CEO of Cuemby
  and CNCF Ambassador CNCF projects highlighted in this post Kubernetes has become
  the place where teams coordinate mixed production workloads: services, batch jobs,
  data pipelines, and ML training. The Kubernetes v1.35 (“Timbernetes”) release reinforces
  that trajectory with changes that reduce operational friction in scheduling, resource
  control, and configuration workflows. What stands out in v1.35 is practical: fewer
  restarts for resizing, new primitives for coordinated placement, and safer defaults
  for how teams generate and review manifests at scale. Taken together, these updates
  point to a Kubernetes control plane that’s adapting to bursty jobs, tightly coupled
  training runs, and continuously tuned inference services. Teams operating mixed
  clusters tend to feel the pressure first in placement efficiency, resize churn,
  and configuration review hygiene. The rest of this piece focuses on the v1.35 changes
  that ease those pressures and make AI/ML operations more predictable at scale. Kubernetes
  v1.35 introduces the workload API and workload-aware scheduling , along with an
  initial implementation of gang scheduling for “all-or-nothing” placement across
  a group of Pods. This helps distributed training and tightly coupled jobs avoid
  partial placement patterns that waste capacity and stall progress. If you want the
  deeper design context, the upstream proposal lives in the gang scheduling KEP. v1.35
  graduates in-place Pod resource resize to Stable. CPU and memory adjustments can
  happen without restarting containers, which reduces churn in inference services
  that need fast tuning under load and improves recovery options for long-running
  workloads. The upstream spec is captured in the in-place update of Pod resources
  KEP.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/02/23/kubernetes-as-ais-operating-system-1-35-release-signals/
