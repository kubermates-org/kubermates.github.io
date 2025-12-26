---
title: 'The end of static secrets: Ford’s OpenShift strategy'
date: '2025-12-19T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/fords-keyless-strategy-managing-200-red-hat-openshift-clusters
post_kind: link
draft: false
tldr: 'The end of static secrets: Ford’s OpenShift strategy Managing 200+ clusters
  Automation and identity: The keyless mandate Governance: PoC and admission control
  Building the foundational infrastructure for AI Ready to build your own keyless,
  automated Red Hat OpenShift platform? Red Hat Learning Subscription | Product Trial
  About the author Debbie Margulies More like this F5 BIG-IP Virtual Edition is now
  validated for Red Hat OpenShift Virtualization More than meets the eye: Behind the
  scenes of Red Hat Enterprise Linux 10 (Part 4) The Containers_Derby | Command Line
  Heroes Can Kubernetes Help People Find Love? | Compiler Keep exploring Browse by
  channel Automation Artificial intelligence Open hybrid cloud Security Edge computing
  Infrastructure Applications Virtualization Share At Red Hat OpenShift Commons Gathering
  in Atlanta on November 10, 2025, Satish Puranam, Director of Cloud and Developer
  Experience at Ford, and Sitaram Iyer, VP of Emerging Technologies at CyberArk, outlined
  how Ford manages over 200 Red Hat OpenShift clusters amid a complex digital transition.
  Their strategy relies on a single, non-negotiable mandate: everything must be keyless.'
summary: 'The end of static secrets: Ford’s OpenShift strategy Managing 200+ clusters
  Automation and identity: The keyless mandate Governance: PoC and admission control
  Building the foundational infrastructure for AI Ready to build your own keyless,
  automated Red Hat OpenShift platform? Red Hat Learning Subscription | Product Trial
  About the author Debbie Margulies More like this F5 BIG-IP Virtual Edition is now
  validated for Red Hat OpenShift Virtualization More than meets the eye: Behind the
  scenes of Red Hat Enterprise Linux 10 (Part 4) The Containers_Derby | Command Line
  Heroes Can Kubernetes Help People Find Love? | Compiler Keep exploring Browse by
  channel Automation Artificial intelligence Open hybrid cloud Security Edge computing
  Infrastructure Applications Virtualization Share At Red Hat OpenShift Commons Gathering
  in Atlanta on November 10, 2025, Satish Puranam, Director of Cloud and Developer
  Experience at Ford, and Sitaram Iyer, VP of Emerging Technologies at CyberArk, outlined
  how Ford manages over 200 Red Hat OpenShift clusters amid a complex digital transition.
  Their strategy relies on a single, non-negotiable mandate: everything must be keyless.
  Image 1: From left, Satish Puranam, Director of Cloud and Developer Experience at
  Ford, and Sitaram Iyer, VP of Emerging Technologies at CyberArk. To achieve this
  scale, Ford has abandoned static secrets entirely, implementing 100% identity-driven
  automation and Policy as Code (PoC) enforcement directly on the Kubernetes platform.
  Ford’s Red Hat OpenShift footprint spans diverse workloads, from consumer-facing
  applications to highly regulated manufacturing and warranty systems. This highly
  dynamic environment requires clusters to be regularly spun up and torn down, often
  pushing core Kubernetes limits (such as etcd capacity) and necessitating constant
  defragmentation or provisioning of new clusters. To manage this scale, Ford imposes
  strict guardrails and standardizes on Red Hat OpenShift across its multicloud and
  multi-datacenter infrastructure. As Satish noted, "Our decades-long journey is all
  about hiding complexity and barriers for the developer. You learn it once, use it
  over and over again, and it scales very well. It allows us to actually update and
  upgrade our systems at a rapid clip. " Image 2: Ford’s journey with Red Hat OpenShift
  By standardizing the platform, Ford can upgrade systems rapidly without burdening
  teams with infrastructure friction. Ford’s scaling strategy eliminates long-lived,
  static credentials, or "secrets," in favor of 100% automated machine identity.'
---
Open the original post ↗ https://www.redhat.com/en/blog/fords-keyless-strategy-managing-200-red-hat-openshift-clusters
