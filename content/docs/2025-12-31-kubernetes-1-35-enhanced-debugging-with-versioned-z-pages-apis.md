---
title: 'Kubernetes 1.35: Enhanced Debugging with Versioned z-pages APIs'
date: '2025-12-31T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/12/31/kubernetes-v1-35-structured-zpages/
post_kind: link
draft: false
tldr: 'Kubernetes 1.35: Enhanced Debugging with Versioned z-pages APIs What are z-pages?
  What''s new in Kubernetes 1.35? Backward compatible design Structured JSON responses
  Why structured responses matter 1. Automated health checks and monitoring 2.'
summary: 'Kubernetes 1.35: Enhanced Debugging with Versioned z-pages APIs What are
  z-pages? What''s new in Kubernetes 1.35? Backward compatible design Structured JSON
  responses Why structured responses matter 1. Automated health checks and monitoring
  2. Better debugging tools 3. API versioning and stability How to use structured
  z-pages Prerequisites Example: Getting structured responses Important considerations
  Alpha feature status Security and access control Future evolution Try it out Learn
  more Get involved Debugging Kubernetes control plane components can be challenging,
  especially when you need to quickly understand the runtime state of a component
  or verify its configuration. With Kubernetes 1.35, we''re enhancing the z-pages
  debugging endpoints with structured, machine-parseable responses that make it easier
  to build tooling and automate troubleshooting workflows. z-pages are special debugging
  endpoints exposed by Kubernetes control plane components. Introduced as an alpha
  feature in Kubernetes 1.32, these endpoints provide runtime diagnostics for components
  like kube-apiserver , kube-controller-manager , kube-scheduler , kubelet and kube-proxy.
  The name "z-pages" comes from the convention of using /*z paths for debugging endpoints.
  kube-apiserver kube-controller-manager kube-scheduler kubelet kube-proxy /*z Currently,
  Kubernetes supports two primary z-page endpoints: /statusz /flagz These endpoints
  are valuable for human operators who need to quickly inspect component state, but
  until now, they only returned plain text output that was difficult to parse programmatically.
  Kubernetes 1.35 introduces structured, versioned responses for both /statusz and
  /flagz endpoints. This enhancement maintains backward compatibility with the existing
  plain text format while adding support for machine-readable JSON responses. /statusz
  /flagz The new structured responses are opt-in.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/12/31/kubernetes-v1-35-structured-zpages/
