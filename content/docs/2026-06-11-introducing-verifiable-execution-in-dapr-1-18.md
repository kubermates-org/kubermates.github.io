---
title: Introducing Verifiable Execution in Dapr 1.18
date: '2026-06-11T13:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/06/11/introducing-verifiable-execution-in-dapr-1-18/
post_kind: link
draft: false
tldr: Bringing attestation, provenance, and tamper-evident execution history to workflows
  and AI agents Why Observability Is Not Enough Introducing Workflow History Signing
  Introducing workflow history propagation Introducing workflow attestation Built
  on SPIFFE-based workload I=identity Why this matters for AI agents From durable
  execution to verifiable execution Looking ahead Getting started Posted on June 11,
  2026 by epower CNCF projects highlighted in this post For years, the cloud native
  ecosystem has focused on making distributed systems resilient. Applications recover
  from failures.
summary: 'Bringing attestation, provenance, and tamper-evident execution history to
  workflows and AI agents Why Observability Is Not Enough Introducing Workflow History
  Signing Introducing workflow history propagation Introducing workflow attestation
  Built on SPIFFE-based workload I=identity Why this matters for AI agents From durable
  execution to verifiable execution Looking ahead Getting started Posted on June 11,
  2026 by epower CNCF projects highlighted in this post For years, the cloud native
  ecosystem has focused on making distributed systems resilient. Applications recover
  from failures. Services retry requests. Workflows survive crashes and resume where
  they left off. Durable execution has become a foundational building block for long-running
  business processes and, increasingly, AI agent systems. But as organizations move
  AI agents and autonomous workflows into production, a new challenge is emerging:
  How do you verify what happened in a tamper-proof way? When a workflow triggers
  an activity, invokes a service, delegates work to another workflow, or coordinates
  multiple AI agents, how can downstream systems determine whether that execution
  context can be trusted? How can security teams verify that execution history has
  not been altered? How can compliance teams establish a chain of custody for critical
  decisions? How can organizations prove how work was executed, trace where it originated,
  and verify that its history has remained intact? Dapr 1.18 introduces a new set
  of capabilities designed to address these challenges: Workflow History Signing ,
  Workflow History Propagation , and Workflow Attestation. Together, these capabilities
  establish a foundation for Verifiable Execution in Dapr. Modern cloud native systems
  already generate enormous amounts of telemetry. Logs explain what happened. Metrics
  show performance. Traces reveal execution paths. Audit records provide historical
  context.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/06/11/introducing-verifiable-execution-in-dapr-1-18/
