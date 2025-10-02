---
title: 'Fluentd to Fluent Bit: A Migration Guide'
date: '2025-10-01T15:13:55+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/10/01/fluentd-to-fluent-bit-a-migration-guide/
post_kind: link
draft: false
tldr: 'When and why to migrate? Why Migrate? Fluentd vs. Fluent Bit: What are the
  Differences Background Performance Routing Telemetry signal focus Custom processing
  Custom plugins Monitoring How to get started with a Fluentd to Fluent Bit migration
  Deployment Deployed as an Aggregator / Collector Adding a Telemetry Pipeline Configuration
  Custom Plugins Custom Processing Logic Migrating Portions at a Time Conclusion Frequently
  Asked Questions Why migrate from Fluentd to Fluent Bit What are some differences
  between Fluentd and Fluent Bit? Can Fluentd and Fluent Bit work together? Posted
  on October 1, 2025 by Anurag Gupta | Fluent Bit Maintainer | Field Architect | Chronosphere
  CNCF projects highlighted in this post Fluentd was created over 14 years ago and
  still continues to be one of the most widely deployed technologies for log collection
  in the enterprise.'
summary: 'When and why to migrate? Why Migrate? Fluentd vs. Fluent Bit: What are the
  Differences Background Performance Routing Telemetry signal focus Custom processing
  Custom plugins Monitoring How to get started with a Fluentd to Fluent Bit migration
  Deployment Deployed as an Aggregator / Collector Adding a Telemetry Pipeline Configuration
  Custom Plugins Custom Processing Logic Migrating Portions at a Time Conclusion Frequently
  Asked Questions Why migrate from Fluentd to Fluent Bit What are some differences
  between Fluentd and Fluent Bit? Can Fluentd and Fluent Bit work together? Posted
  on October 1, 2025 by Anurag Gupta | Fluent Bit Maintainer | Field Architect | Chronosphere
  CNCF projects highlighted in this post Fluentd was created over 14 years ago and
  still continues to be one of the most widely deployed technologies for log collection
  in the enterprise. Fluentd’s distributed plugin architecture and highly permissive
  licensing made it ideal as part of the Cloud Native Computing Foundation (CNCF)
  as a now graduated project. However, enterprises drowning in telemetry data are
  now requiring solutions that have higher performance, more native support for evolving
  schemas and formats, and increased flexibility in processing. Enter Fluent Bit.
  Fluent Bit , while initially growing as a sub-project within the Fluent ecosystem
  , expanded from Fluentd to support all telemetry types – logs, metrics, and traces.
  Fluent Bit now is the more popular of the two with over 15 billion deployments and
  used by Amazon, Google, Oracle and Microsoft to name a few. Fluent Bit also is fully
  aligned with OpenTelemetry signals, format and protocol, which ensures that users
  will be able to continue handling telemetry data as it grows and evolves. Among
  the most frequent questions we get as the maintainers of the projects are: How do
  we migrate? What should we watch out for? And what business value do we get for
  migrating? This article aims to answer these questions with examples. We want to
  help make it an easy decision to migrate from Fluentd to Fluent Bit. Here is a quick
  list of the reasons users switch from Fluentd to Fluent Bit: Higher performance
  for the same resources you are already using Full OpenTelemetry support for logs,
  metrics, and traces as well as Prometheus support for metrics Simpler configuration
  and routing ability to multiple locations Higher velocity for adding custom processing
  rules Integrated monitoring to better understand performance and dataflows To understand
  all the differences between the projects, it is important to understand the background
  of each project and the era it was built for. With Fluentd, the main language is
  Ruby and initially designed to help users push data to big data platforms such as
  Hadoop.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/10/01/fluentd-to-fluent-bit-a-migration-guide/
