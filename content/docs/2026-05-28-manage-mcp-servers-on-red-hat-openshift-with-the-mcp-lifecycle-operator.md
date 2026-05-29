---
title: Manage MCP servers on Red Hat OpenShift with the MCP lifecycle operator
date: '2026-05-28T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/manage-mcp-servers-red-hat-openshift-mcp-lifecycle-operator
post_kind: link
draft: false
tldr: 'Manage MCP servers on Red Hat OpenShift with the MCP lifecycle operator Why
  an operator for MCP servers? Deploying the MCP server What the operator gives you
  out of the box MCP catalog integration What''s next The adaptable enterprise: Why
  AI readiness is disruption readiness About the authors Calum Murray Matthias Weßendorf
  Ali Ok Jaideep Rao Ju Lim Manaswini Das More like this The agentic paradox and the
  case for hybrid AI The same 16 GPUs, twice the users: Inference-aware routing for
  LLM clusters Technically Speaking | Build a production-ready AI toolbox Technically
  Speaking | Platform engineering for AI agents Keep exploring Browse by channel Automation
  Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share Model Context Protocol (MCP) is quickly becoming
  the standard for connecting AI agents to external tools and data. With the recent
  technology preview of the MCP server for Red Hat OpenShift , organizations can give
  AI agents controlled access to their clusters.'
summary: 'Manage MCP servers on Red Hat OpenShift with the MCP lifecycle operator
  Why an operator for MCP servers? Deploying the MCP server What the operator gives
  you out of the box MCP catalog integration What''s next The adaptable enterprise:
  Why AI readiness is disruption readiness About the authors Calum Murray Matthias
  Weßendorf Ali Ok Jaideep Rao Ju Lim Manaswini Das More like this The agentic paradox
  and the case for hybrid AI The same 16 GPUs, twice the users: Inference-aware routing
  for LLM clusters Technically Speaking | Build a production-ready AI toolbox Technically
  Speaking | Platform engineering for AI agents Keep exploring Browse by channel Automation
  Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share Model Context Protocol (MCP) is quickly becoming
  the standard for connecting AI agents to external tools and data. With the recent
  technology preview of the MCP server for Red Hat OpenShift , organizations can give
  AI agents controlled access to their clusters. Deploying and managing MCP servers
  at scale introduces its own operational challenge: how do you treat MCP servers
  as first-class infrastructure? Today, we''re making the MCP lifecycle operator available
  as a developer preview (v0.1.0). MCP lifecycle operator is a Kubernetes-native operator
  that provides a declarative API to deploy, manage, and safely roll out MCP servers
  on OpenShift and Kubernetes. Running an MCP server in a container is straightforward.
  Running it in production is not. You need health checks, role-based access control
  (RBAC), configuration management, service discovery, and lifecycle automation. The
  MCP lifecycle operator handles all of this through a single custom resource: MCPServer.
  MCPServer When you create an MCPServer resource, the operator automatically: MCPServer
  Creates a Deployment with security-hardened defaults (non-root, read-only filesystem,
  dropped capabilities) Exposes the server via a Service with a cluster-internal discovery
  URL Validates that referenced ConfigMaps and Secrets exist before rolling out Injects
  a default readiness probe so containers are not marked Ready until they are listening
  on the configured port Let''s walk through a concrete example. Deploying the MCP
  server for OpenShift using the operator with proper RBAC for read-only cluster access.
  First, install the operator with this manifest file. After that, apply the following
  manifests for creating the MCP server and its configuration: --- # ServiceAccount
  for the MCP server apiVersion: v1 kind: ServiceAccount metadata: name: mcp-viewer
  namespace: default --- # Grant read-only access using the built-in ''view'' ClusterRole
  apiVersion: rbac.'
---
Open the original post ↗ https://www.redhat.com/en/blog/manage-mcp-servers-red-hat-openshift-mcp-lifecycle-operator
