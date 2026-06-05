---
title: 'Kiali and MCP: Bringing AI-native observability to Red Hat OpenShift Service
  Mesh'
date: '2026-05-28T00:00:00+00:00'
tags:
- openshift
source: OpenShift Blog
external_url: https://www.redhat.com/en/blog/kiali-and-mcp-bring-ai-native-observability-red-hat-openshift-service-mesh
post_kind: link
draft: false
tldr: 'Kiali and MCP: Bringing AI-native observability to Red Hat OpenShift Service
  Mesh Why Kiali in MCP? The Kiali toolset at a glance How to get started Operator
  method 1. Patch your Kiali CR Helm method 1.'
summary: 'Kiali and MCP: Bringing AI-native observability to Red Hat OpenShift Service
  Mesh Why Kiali in MCP? The Kiali toolset at a glance How to get started Operator
  method 1. Patch your Kiali CR Helm method 1. Add/Update the Kiali Helm Repository
  2. Upgrade the release Connecting to Red Hat OpenShift Lightspeed Use case: The
  AI SRE Try it yourself: An AI prompt example The future of mesh-aware AI Try it
  today Red Hat OpenShift Container Platform | Product Trial About the author Alberto
  Jesús Gutierrez Juanes More like this Accelerate autoscaling inference in Red Hat
  AI with Everpure The agentic paradox and the case for hybrid AI Keep exploring Browse
  by channel Automation Artificial intelligence Open hybrid cloud Security Edge computing
  Infrastructure Applications Virtualization Share The model context protocol (MCP)
  server for Kubernetes is moving toward technology preview (TP) , and it’s bringing
  a powerhouse integration with it: the Kiali toolset. By integrating Kiali into the
  MCP server, we are bridging the gap between large language models (LLM) and your
  service mesh. This means your AI assistant doesn''t just "talk" about your cluster,
  it can now visualize traffic, diagnose latency, and manage Istio configurations
  using the same trusted logic that powers the Kiali UI. While standard Kubernetes
  tools handle pods and services, the Kiali toolset provides mesh-awareness. It understands
  the "connect, secure, and observe" philosophy of Istio. Whether you are debugging
  a 503 error or mapping cross-namespace dependencies, these tools allow an LLM to
  act as a specialized service mesh engineer. The following tools are now available
  for use within the MCP server, allowing for deep introspection of your mesh: mesh_status:
  High-level health check of Istio, Kiali, and the control plane traffic_graph: Visualize
  service-to-service dependencies and mTLS status istio_config_read/write: List, get,
  create, or patch Istio objects (VirtualServices, for example) Resource_details:
  Get details about specific Kubernetes and Istio resource manifests trace_list/details:
  Pull Jaeger and Tempo distributed traces for request-level debugging pod_performance:
  Summarize CPU and memory usage compared to actual Kubernetes requests and limits
  logs: Fetch container logs with built-in severity (ERROR or WARN, for example) filtering
  metrics: See traffic trends, throughput, and latency quantiles (p95, p99). The Kiali
  MCP integration is a modernized approach to mesh management. To use these features,
  your environment must meet one of the following version requirements: Red Hat OpenShift
  Service Mesh: Requires v3.3.3 or higher Kiali: Requires Kiali v2.25 or higher If
  your current Kiali version is below v2.25, you can test the latest capabilities
  by using the Kiali operator or Helm to deploy the specific image.'
---
Open the original post ↗ https://www.redhat.com/en/blog/kiali-and-mcp-bring-ai-native-observability-red-hat-openshift-service-mesh
