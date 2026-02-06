---
title: 'Ingress Security for AI Workloads in Kubernetes: Protecting AI Endpoints with
  WAF'
date: '2026-01-22T19:27:17+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/ingress-security-for-ai-workloads-in-kubernetes-protecting-ai-endpoints-with-waf/
post_kind: link
draft: false
tldr: AI Workloads Have a New Front Door Why the Stakes Have Changed for Platform
  Teams Why AI Inference Changes the Ingress Security Model The High Cost of the “Successful”
  Request AI-Specific Ingress Threats Platform Teams Are Seeing Resource Exhaustion
  and LLM Jacking Prompt Injection & Input Abuse Data Exposure and the AI Pipeline
  The Ingress Blind Spot in Kubernetes Today Securing AI Ingress with Calico Ingress
  Gateway Integrated Web Application Firewall Identity-Aware Access Control Fine-Grained
  Rate Limiting for AI Workloads Real-Time Observability and Security as Code Security
  as an AI Enabler Secure Your AI Infrastructure Today Scale AI Safely with Calico
  For years, AI and machine learning workloads lived in the lab. They ran as internal
  experiments, batch jobs in isolated clusters, or offline data pipelines.
summary: AI Workloads Have a New Front Door Why the Stakes Have Changed for Platform
  Teams Why AI Inference Changes the Ingress Security Model The High Cost of the “Successful”
  Request AI-Specific Ingress Threats Platform Teams Are Seeing Resource Exhaustion
  and LLM Jacking Prompt Injection & Input Abuse Data Exposure and the AI Pipeline
  The Ingress Blind Spot in Kubernetes Today Securing AI Ingress with Calico Ingress
  Gateway Integrated Web Application Firewall Identity-Aware Access Control Fine-Grained
  Rate Limiting for AI Workloads Real-Time Observability and Security as Code Security
  as an AI Enabler Secure Your AI Infrastructure Today Scale AI Safely with Calico
  For years, AI and machine learning workloads lived in the lab. They ran as internal
  experiments, batch jobs in isolated clusters, or offline data pipelines. Security
  focused on internal access controls and protecting the data perimeter. That model
  no longer holds. Today, AI models are increasingly part of production traffic, which
  is driving new challenges around securing AI workloads in Kubernetes. Whether serving
  a large language model for a customer-facing chatbot or a computer vision model
  for real-time analysis, these models are exposed through APIs, typically REST or
  gRPC, running as microservices in Kubernetes. From a platform engineering perspective,
  these AI inference endpoints are now Tier 1 services. They sit alongside login APIs
  and payment gateways in terms of criticality, but they introduce a different and
  more expensive risk profile than traditional web applications. For AI inference
  endpoints, ingress security increasingly means Layer 7 inspection and WAF (Web Application
  Firewall) level controls at the cluster edge. By analyzing the full request payload,
  a WAF can detect and block abusive or malicious traffic before it ever reaches expensive
  GPU resources or sensitive data. This sets the stage for protecting AI workloads
  from both operational and security risks. Exposing AI workloads to the internet
  creates a direct path to some of your most sensitive and costly infrastructure.
---
Open the original post ↗ https://www.tigera.io/blog/ingress-security-for-ai-workloads-in-kubernetes-protecting-ai-endpoints-with-waf/
