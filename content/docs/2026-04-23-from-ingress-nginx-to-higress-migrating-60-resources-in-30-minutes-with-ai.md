---
title: 'From Ingress NGINX to Higress: migrating 60+ resources in 30 minutes with
  AI'
date: '2026-04-23T13:37:18+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/04/23/from-ingress-nginx-to-higress-migrating-60-resources-in-30-minutes-with-ai/
post_kind: link
draft: false
tldr: 'The solution: Why Higress for the AI era? Outcome: 30 Minutes to compliance
  Posted on April 23, 2026 by Tianyi Zhang, Alibaba CNCF projects highlighted in this
  post With the official retirement of Ingress NGINX that took place in March 2026,
  enterprise platform teams are facing an urgent security and compliance mandate.
  Remaining on a retired controller leaves critical infrastructure vulnerable to unpatched
  security risks.'
summary: 'The solution: Why Higress for the AI era? Outcome: 30 Minutes to compliance
  Posted on April 23, 2026 by Tianyi Zhang, Alibaba CNCF projects highlighted in this
  post With the official retirement of Ingress NGINX that took place in March 2026,
  enterprise platform teams are facing an urgent security and compliance mandate.
  Remaining on a retired controller leaves critical infrastructure vulnerable to unpatched
  security risks. For one infrastructure engineer managing a cluster with over 60
  complex Ingress resources, the challenge was clear: find a modern, enterprise-ready
  replacement that could be implemented without months of manual refactoring. This
  blog post explains how full migration validation was achieved in just 30 minutes
  by leveraging an AI agent and Higress , a cloud-native and AI-native API gateway
  founded by Alibaba that recently joined the CNCF Sandbox. Higress, which is built
  on the industry-standard Envoy and Istio , is specifically designed as an AI-native
  gateway that addresses the shortcomings of legacy controllers while providing specialized
  features for Large Language Models (LLMs). AI-Native Architecture: Unlike traditional
  gateways, Higress treats LLMs as first-class citizens. It includes specialized features
  like Token-based rate limiting (to manage model costs) and caching capabilities
  (to reduce latency for common AI prompts). LLM Protocol Governance: It provides
  a unified protocol to interface with various LLM providers, enabling teams to switch
  models behind a single, secure endpoint. Zero-Downtime Reliability: Leveraging Envoy’s
  xDS protocol , Higress allows for configuration updates in milliseconds. This eliminates
  the “NGINX reload” issue, which is critical for maintaining persistent connections
  in AI streaming and gRPC. Model Context Protocol (MCP): Higress supports hosting
  MCP servers, allowing AI agents to securely interact with enterprise tools and data
  via the gateway. AI-Assisted Migration Workflow To accelerate the transition, the
  Alibaba engineer utilized an AI agent equipped with specialized “Skills.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/04/23/from-ingress-nginx-to-higress-migrating-60-resources-in-30-minutes-with-ai/
