---
title: Create efficient two-node edge infrastructure with Red Hat OpenShift and Portworx/Pure
  Storage
date: '2025-11-11T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/efficient-two-node-edge-infrastructure-red-hat-openshift-and-portworxpure-storage
post_kind: link
draft: false
tldr: 'Create efficient two-node edge infrastructure with Red Hat OpenShift and Portworx/Pure
  Storage The edge dilemma: High availability vs. cost optimization Two-node OpenShift
  with arbiter explained What''s the high-availability stance of TNA? Is the arbiter
  node a regular node? Unified data services at the edge Cost efficiency and resilience
  for the open hybrid cloud Red Hat OpenShift Container Platform | Product Trial About
  the authors Paul Lancaster Daniel Froehlich Andy Gower (Pure Storage) More like
  this Blog post Blog post Original podcast Original podcast Keep exploring Browse
  by channel Automation Artificial intelligence Open hybrid cloud Security Edge computing
  Infrastructure Applications Virtualization Share The demand to extend applications
  to the edge has never been greater.'
summary: 'Create efficient two-node edge infrastructure with Red Hat OpenShift and
  Portworx/Pure Storage The edge dilemma: High availability vs. cost optimization
  Two-node OpenShift with arbiter explained What''s the high-availability stance of
  TNA? Is the arbiter node a regular node? Unified data services at the edge Cost
  efficiency and resilience for the open hybrid cloud Red Hat OpenShift Container
  Platform | Product Trial About the authors Paul Lancaster Daniel Froehlich Andy
  Gower (Pure Storage) More like this Blog post Blog post Original podcast Original
  podcast Keep exploring Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share The demand to extend applications to the edge has never been greater. From
  retail shops to industrial and manufacturing sites, there''s a need to create, consume,
  and store data at the edge. Deploying applications at the edge comes with a set
  of physical constraints, but also with the need to deliver a truly cost-efficient
  and resilient architecture. When building applications at the edge, you must consider
  the needs of the individual site as well as the cost to deploy, manage, and maintain
  applications across multiple edge locations. The good news is that Red Hat OpenShift
  is evolving to meet this demand head-on. With the introduction of the two-node OpenShift
  with arbiter topology , Red Hat and partners like Portworx by Pure Storage are delivering
  a cost-efficient and resilient architecture designed specifically for the edge.
  The primary motivation behind the two-node OpenShift with arbiter (TNA) initiative
  is simple: Cost for large-scale edge deployments. For mission-critical edge sites,
  high availability is non-negotiable. Should a node fail, applications must continue
  running without disruption, which is why the control plane requires a quorum (typically
  three or more nodes) to prevent split-brain scenarios and maintain consistency (a
  principle known as the CAP theorem). Two-node OpenShift with arbiter, now generally
  available (GA) with OpenShift 4.20, solves this by dramatically reducing the hardware
  footprint while preserving three-node consistency and availability. Two-node OpenShift
  with arbiter architecture is a specialized, cost-sensitive solution that is technically
  a three-node cluster.'
---
Open the original post ↗ https://www.redhat.com/en/blog/efficient-two-node-edge-infrastructure-red-hat-openshift-and-portworxpure-storage
