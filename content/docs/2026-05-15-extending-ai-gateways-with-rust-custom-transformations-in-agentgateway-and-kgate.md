---
title: 'Extending AI gateways with Rust: Custom transformations in agentgateway and
  kgateway'
date: '2026-05-15T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/05/15/extending-ai-gateways-with-rust-custom-transformations-in-agentgateway-and-kgateway/
post_kind: link
draft: false
tldr: 'Architecture overview The stack Before you start Part 1: The Rust module The
  Cargo. toml file The transformation trait Part 2: The Docker image Part 3: Deploying
  to Kubernetes Part 4: Testing it all works Troubleshooting common issues Next steps:
  Production and real LLMs Complete code Final thoughts Posted on May 15, 2026 by
  Michael Uzukwu, kgateway and agentgateway Contributor CNCF projects highlighted
  in this post Every gateway ships with a set of built-in policies.'
summary: 'Architecture overview The stack Before you start Part 1: The Rust module
  The Cargo. toml file The transformation trait Part 2: The Docker image Part 3: Deploying
  to Kubernetes Part 4: Testing it all works Troubleshooting common issues Next steps:
  Production and real LLMs Complete code Final thoughts Posted on May 15, 2026 by
  Michael Uzukwu, kgateway and agentgateway Contributor CNCF projects highlighted
  in this post Every gateway ships with a set of built-in policies. Authentication.
  Rate limiting. Request routing. Prompt guards. These cover most use cases. But what
  about the ones they don’t cover? What if you need to add a custom header based on
  a database lookup? What if you need to transform a request body in a way no existing
  filter supports? What if your business has unique logic that no off-the-shelf gateway
  can anticipate? You build your own extension. This article walks through exactly
  how to do that using agentgateway, Envoy, and Rust. In this tutorial, you’ll learn
  how to: Build a custom Envoy dynamic module in Rust Package it into a production-ready
  Docker image Deploy it to Kubernetes with kgateway and agentgateway Test the entire
  stack with a mock LLM endpoint What you’ll need: Basic familiarity with Kubernetes,
  Docker, and command-line tools. No prior Rust experience required — I’ll explain
  the key parts as we go. Time to complete: About 30-45 minutes.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/05/15/extending-ai-gateways-with-rust-custom-transformations-in-agentgateway-and-kgateway/
