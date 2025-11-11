---
title: Multi-cluster GitOps with the Argo CD Agent Technology Preview
date: '2025-11-05T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/multi-cluster-gitops-argo-cd-agent-openshift-gitops
post_kind: link
draft: false
tldr: Multi-cluster GitOps with the Argo CD Agent Technology Preview Topologies for
  Argo CD What is the Argo CD Agent? Centralized visibility and insights Reduce Argo
  CD resource usage Best of both topologies Integration with Red Hat Advanced Cluster
  Management The road ahead Getting started Red Hat Ansible Automation Platform |
  Product Trial About the authors Harriet Lawrence Gerald Nunn Jann Fischer More like
  this Blog post Blog post Keep exploring Browse by channel Automation Artificial
  intelligence Open hybrid cloud Security Edge computing Infrastructure Applications
  Virtualization Share Running a single instance of Argo CD on a single cluster used
  to be common, but now a multi-cluster GitOps architecture has become the norm. This
  way of working does come with its own set of challenges.
summary: Multi-cluster GitOps with the Argo CD Agent Technology Preview Topologies
  for Argo CD What is the Argo CD Agent? Centralized visibility and insights Reduce
  Argo CD resource usage Best of both topologies Integration with Red Hat Advanced
  Cluster Management The road ahead Getting started Red Hat Ansible Automation Platform
  | Product Trial About the authors Harriet Lawrence Gerald Nunn Jann Fischer More
  like this Blog post Blog post Keep exploring Browse by channel Automation Artificial
  intelligence Open hybrid cloud Security Edge computing Infrastructure Applications
  Virtualization Share Running a single instance of Argo CD on a single cluster used
  to be common, but now a multi-cluster GitOps architecture has become the norm. This
  way of working does come with its own set of challenges. Typically organizations
  have had to make compromises when deploying Argo CD in varying topologies depending
  on their specific priorities (for example, management or scalability). But multi-cluster
  deployments just got easier to manage and secure with the Argo CD Agent in Red Hat
  OpenShift GitOps. A new addition to the GitOps operator, the agent is part of the
  Red Hat OpenShift Platform Plus (OPP) subscription. Broadly, there are two common
  topologies for implementing Argo CD. The first is centralized, in which a single
  Argo CD instance runs in a management cluster and is responsible for deploying resources
  across a fleet of OpenShift or Kubernetes clusters. This provides for a single pane
  of glass which simplifies management, but can become challenging to scale as the
  number of applications and clusters grow. The other common topology is distributed,
  in which Argo CD is distributed across the fleet of OpenShift or Kubernetes clusters.
  This provides increased scalability, but also increases the complexity of provisioning
  and managing those instances. Scale has become the major blocker for large production
  implementations. It's not just Argo CD's performance that's important.
---
Open the original post ↗ https://www.redhat.com/en/blog/multi-cluster-gitops-argo-cd-agent-openshift-gitops
