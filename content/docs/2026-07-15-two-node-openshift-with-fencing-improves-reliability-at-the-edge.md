---
title: Two-node OpenShift with fencing improves reliability at the edge
date: '2026-07-15T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/two-node-openshift-fencing-improves-reliability-edge
post_kind: link
draft: false
tldr: 'Two-node OpenShift with fencing improves reliability at the edge Two-node OpenShift
  with fencing architecture The concept of fencing: Preventing split-brain scenarios
  Walkthrough: A node fails and is fenced Phase 1: Steady state Phase 2: The failure
  event Phase 3: Fencing initiated Phase 4: Recovery and regaining quorum Phase 5:
  Resuming normal operations Resilience in extreme conditions Summary Hatville: miniature
  city where edge computing comes to life About the authors Daniel Fröhlich Paul Lancaster
  More like this Sit, stay, deploy: Lessons from a real-world robotic blueprint on
  scaling edge computer vision Lessons from an autonomous computer vision system on
  the air-gapped edge Infrastructure At The Edge | Compiler Open Curiosity | Command
  Line Heroes Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share Edge computing environments present distinct hurdles as companies move processing
  capabilities nearer to where data is generated. Customers across industries, especially
  in retail, industrial, and telecommunications sectors, are increasingly demanding
  high availability for their edge deployments.'
summary: 'Two-node OpenShift with fencing improves reliability at the edge Two-node
  OpenShift with fencing architecture The concept of fencing: Preventing split-brain
  scenarios Walkthrough: A node fails and is fenced Phase 1: Steady state Phase 2:
  The failure event Phase 3: Fencing initiated Phase 4: Recovery and regaining quorum
  Phase 5: Resuming normal operations Resilience in extreme conditions Summary Hatville:
  miniature city where edge computing comes to life About the authors Daniel Fröhlich
  Paul Lancaster More like this Sit, stay, deploy: Lessons from a real-world robotic
  blueprint on scaling edge computer vision Lessons from an autonomous computer vision
  system on the air-gapped edge Infrastructure At The Edge | Compiler Open Curiosity
  | Command Line Heroes Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share Edge computing environments present distinct hurdles as companies move processing
  capabilities nearer to where data is generated. Customers across industries, especially
  in retail, industrial, and telecommunications sectors, are increasingly demanding
  high availability for their edge deployments. However, achieving high availability
  traditionally requires a three-node cluster to establish a reliable quorum. The
  primary factor driving organizations toward alternative topologies for large-scale
  edge deployments is the prohibitive cost of powering, maintaining, and deploying
  a third node across hundreds or thousands of sites—a motivation that has only grown
  stronger in light of the recent steep increase in hardware prices. To address this
  demand, we are introducing Red Hat OpenShift topologies targeting two nodes for
  edge deployments. While two-node OpenShift with arbiter offers a path that uses
  a small arbiter device to maintain quorum, it technically remains a three-node architecture.
  For cost-sensitive customers who require a strict, localized two-node footprint,
  Red Hat now offers two-node OpenShift with fencing. With the release of version
  4.22 of OpenShift, two-node OpenShift with fencing is now generally available. Two-node
  OpenShift with fencing is a true two-node solution designed from the ground up for
  edge environments. Currently supported exclusively on x86 bare-metal platforms,
  two-node OpenShift with fencing also fully supports Red Hat OpenShift Virtualization,
  allowing teams to run both containerized and virtualized workloads on a minimal
  footprint. Figure 1 provides an architectural overview of a two-node OpenShift with
  fencing deployment: Figure 1. Architecture overview diagram of two-node OpenShift
  with fencing Unlike a traditional setup that relies on a third node for tie-breaking,
  two-node OpenShift with fencing establishes high availability for the etcd database
  by relying on proven technologies in the Red Hat Enterprise Linux High Availability
  Add-On.'
---
Open the original post ↗ https://www.redhat.com/en/blog/two-node-openshift-fencing-improves-reliability-edge
