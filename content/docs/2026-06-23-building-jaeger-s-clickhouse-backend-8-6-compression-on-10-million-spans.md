---
title: 'Building Jaeger’s ClickHouse backend: 8.6× compression on 10 million spans'
date: '2026-06-23T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/06/23/building-jaegers-clickhouse-backend-8-6x-compression-on-10-million-spans/
post_kind: link
draft: false
tldr: Why columnar storage wins High-throughput ingest and low-latency queries Compression
  that actually matters Real-time analytics Designing the schema Trade-offs in primary
  key Storing typed attributes Materialized views Five levels of attributes Span throughput
  at scale Getting started Posted on June 23, 2026 by Mahad Zaryab, CNCF Jaeger Project
  Maintainer and Software Engineer at Meta CNCF projects highlighted in this post
  As someone who’s been maintaining Jaeger , I’ve watched users request ClickHouse
  support consistently over the past few years. With Jaeger v2.18.0, we’ve finally
  delivered it.
summary: 'Why columnar storage wins High-throughput ingest and low-latency queries
  Compression that actually matters Real-time analytics Designing the schema Trade-offs
  in primary key Storing typed attributes Materialized views Five levels of attributes
  Span throughput at scale Getting started Posted on June 23, 2026 by Mahad Zaryab,
  CNCF Jaeger Project Maintainer and Software Engineer at Meta CNCF projects highlighted
  in this post As someone who’s been maintaining Jaeger , I’ve watched users request
  ClickHouse support consistently over the past few years. With Jaeger v2.18.0, we’ve
  finally delivered it. What excites me most isn’t just that ClickHouse is available—it’s
  that its architecture is practically custom-built for telemetry at scale. It swallows
  massive, append-only write streams and handles complex analytical aggregations in
  milliseconds, offering teams a highly efficient, production-grade storage backend.
  For those new to the project, Jaeger is a graduated Cloud Native Computing Foundation
  (CNCF) distributed tracing platform built to monitor and troubleshoot complex microservices.
  It tracks requests across service boundaries to expose latency bottlenecks and root
  causes, ultimately reducing a team’s mean time to repair (MTTR). By natively integrating
  ClickHouse, Jaeger can now leverage columnar storage to deliver blazing-fast query
  performance and high-ratio data compression for billions of spans. In this post,
  I’ll explain why ClickHouse is a strong choice for storing traces, how the schema
  is designed under the hood, and how you can start using it with Jaeger today. At
  its core, the tracing problem is twofold: storing massive volumes of semi-structured
  event data and then searching that data quickly across multiple dimensions—service,
  operation, tags, duration, time range, and trace ID. Cassandra and Elasticsearch
  have served the Jaeger community well, but they come with operational costs. Indexing
  overhead adds latency and expense. Scaling becomes complex.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/06/23/building-jaegers-clickhouse-backend-8-6x-compression-on-10-million-spans/
