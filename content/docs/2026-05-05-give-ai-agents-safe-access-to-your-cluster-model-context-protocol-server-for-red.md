---
title: 'Give AI agents safe access to your cluster: Model Context Protocol server
  for Red Hat OpenShift is now in technology preview'
date: '2026-05-05T00:00:00+00:00'
tags:
- openshift
source: OpenShift Blog
external_url: https://www.redhat.com/en/blog/model-context-protocol-server-red-hat-openshift-now-available-technology-preview
post_kind: link
draft: false
tldr: 'Give AI agents safe access to your cluster: Model Context Protocol server for
  Red Hat OpenShift is now in technology preview Architected for fleet-wide scale
  RBAC and auditability Deep observability and telemetry Extensible infrastructure
  management Evaluations Try MCP server for Red Hat OpenShift today! MCP lifecycle
  operator Red Hat OpenShift Container Platform | Product Trial About the authors
  Calum Murray Lukas Berk Matthias Weßendorf Marc Nuri Nader Ziada Ju Lim Gaurav Singh
  More like this When AI finds the bugs: Why defense in depth was always the answer
  Designing multitenant GPU infrastructure: Isolation across virtualization and Kubernetes
  platforms Technically Speaking | Build a production-ready AI toolbox Technically
  Speaking | Platform engineering for AI agents Keep exploring Browse by channel Automation
  Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share As organizations embrace agentic AI for cluster
  operations, the central challenge shifts from whether or not AI can control a cluster
  to whether it can do it safely and with accountability. How do large language models
  (LLMs) provide meaningful context and operational capability within our clusters
  without compromising security or relying on brittle, script-based wrappers? To address
  this challenge, Red Hat has introduced the Model Context Protocol (MCP) server for
  Red Hat OpenShift , available as a technology preview.'
summary: 'Give AI agents safe access to your cluster: Model Context Protocol server
  for Red Hat OpenShift is now in technology preview Architected for fleet-wide scale
  RBAC and auditability Deep observability and telemetry Extensible infrastructure
  management Evaluations Try MCP server for Red Hat OpenShift today! MCP lifecycle
  operator Red Hat OpenShift Container Platform | Product Trial About the authors
  Calum Murray Lukas Berk Matthias Weßendorf Marc Nuri Nader Ziada Ju Lim Gaurav Singh
  More like this When AI finds the bugs: Why defense in depth was always the answer
  Designing multitenant GPU infrastructure: Isolation across virtualization and Kubernetes
  platforms Technically Speaking | Build a production-ready AI toolbox Technically
  Speaking | Platform engineering for AI agents Keep exploring Browse by channel Automation
  Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share As organizations embrace agentic AI for cluster
  operations, the central challenge shifts from whether or not AI can control a cluster
  to whether it can do it safely and with accountability. How do large language models
  (LLMs) provide meaningful context and operational capability within our clusters
  without compromising security or relying on brittle, script-based wrappers? To address
  this challenge, Red Hat has introduced the Model Context Protocol (MCP) server for
  Red Hat OpenShift , available as a technology preview. MCP refers to an open source
  standard for connecting AI applications to external data and tools. The MCP server
  for Red Hat OpenShift uses the MCP to provide LLM Agents controlled access to OpenShift
  clusters. This helps your agents to safely and intelligently interact with your
  OpenShift clusters following rules you define. MCP server for Red Hat OpenShift
  The MCP server for Red Hat OpenShift introduces a suite of capabilities designed
  to bring AI-driven operations to the enterprise, focusing on security, observability,
  and scale: Platform engineers rarely manage single clusters. To support fleets of
  OpenShift clusters, the MCP server natively supports multicluster operations. Instead
  of relying on static, distributed kubeconfig files, the server introduces OAuth
  and OIDC integration, using token exchange protocols. Currently supporting Keycloak,
  this architecture allows the MCP server to reside on a Red Hat Advanced Cluster
  Management for Kubernetes hub. Authenticated agents more safely query and act upon
  managed OpenShift clusters dynamically without requiring impersonation flows, maintaining
  strict identity verification across the fleet. Here’s a short demo showing token
  exchange for the MCP server for Red Hat OpenShift. In addition to the OAuth and
  OIDC integration, the MCP server for Red Hat OpenShift server does not attempt to
  reinvent Kubernetes security; instead, it enforces it through: Read-only by default:
  The MCP server''s modular toolset architecture defaults to read-only operations.'
---
Open the original post ↗ https://www.redhat.com/en/blog/model-context-protocol-server-red-hat-openshift-now-available-technology-preview
