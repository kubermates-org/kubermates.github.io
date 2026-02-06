---
title: Conversing with Large Language Models using Dapr
date: '2026-02-04T20:51:48+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/02/04/conversing-with-large-language-models-using-dapr/
post_kind: link
draft: false
tldr: 'Posted on February 4, 2026 by Siri Varma Vegiraju, CNCF Project Maintainer
  CNCF projects highlighted in this post Imagine you are running a bunch of microservices,
  each living within its own boundary. What are some of the challenges that come into
  mind when operating them? Retries : Service-to-service calls are not always reliable.'
summary: 'Posted on February 4, 2026 by Siri Varma Vegiraju, CNCF Project Maintainer
  CNCF projects highlighted in this post Imagine you are running a bunch of microservices,
  each living within its own boundary. What are some of the challenges that come into
  mind when operating them? Retries : Service-to-service calls are not always reliable.
  They can fail due to a number of reasons, ranging from timeouts to transient network
  issues, or downstream outages. In order to recover, it is common for applications
  to implement retry logic. Over time, this logic becomes tightly coupled with business
  code, and every developer is expected to configure retries correctly. Observability
  also presents a similar challenge. Each service must be instrumented with metrics,
  logs, and traces to understand request flow, latency, and failures. This instrumentation
  is often repetitive and easy to get wrong or overlook and when observability is
  inconsistent, debugging production issues becomes slow and frustrating. This is
  where Distributed Application Runtime ( Dapr ) comes into picture. Dapr is a CNCF-hosted,
  open-source runtime that provides building blocks for distributed applications through
  a sidecar architecture. It helps abstract most of these constructs into a sidecar
  runtime so that you as developers can concentrate on business logic. Simply put,
  it is an open-source and event-driven runtime that simplifies some of the common
  problems developers face with building distributed systems and microservices.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/02/04/conversing-with-large-language-models-using-dapr/
