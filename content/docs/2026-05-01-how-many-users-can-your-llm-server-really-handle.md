---
title: How Many Users Can Your LLM Server Really Handle?
date: '2026-05-01T01:17:25+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/04/30/how-many-users-can-your-llm-server-really-handle/
post_kind: link
draft: false
tldr: 'The Problem with the Just Run a Benchmark Concept What We Built What You Will
  Learn from the Paper Read the White Paper Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles How Many Users Can Your LLM Server Really Handle? From
  Infrastructure to Agents: A Hands-On Guide to Secure Private AI with Broadcom -
  Part 2 The New Frontier: Leading the Cloud-Native Evolution Deploying large language
  models (LLMs) in an enterprise environment has transitioned from a proof-of-concept
  exercise to a rigorous engineering discipline. Yet, accurately predicting the capacity
  of an inference server under real-world, concurrent load remains a formidable challenge.'
summary: 'The Problem with the Just Run a Benchmark Concept What We Built What You
  Will Learn from the Paper Read the White Paper Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles How Many Users Can Your LLM Server Really Handle? From
  Infrastructure to Agents: A Hands-On Guide to Secure Private AI with Broadcom -
  Part 2 The New Frontier: Leading the Cloud-Native Evolution Deploying large language
  models (LLMs) in an enterprise environment has transitioned from a proof-of-concept
  exercise to a rigorous engineering discipline. Yet, accurately predicting the capacity
  of an inference server under real-world, concurrent load remains a formidable challenge.
  Infrastructure engineers frequently confront complex configuration spaces, questioning
  whether tuning parameters like --max-num-batched-tokens or --gpu-memory-utilization
  in vLLM will optimize throughput or inadvertently degrade tail latency. Official
  documentation provides the mechanisms for tuning, but it rarely offers a systematic
  method for discovering the optimal configuration for a specific workload, hardware
  architecture, and strict Service Level Agreement (SLA). --max-num-batched-tokens
  --gpu-memory-utilization To address this, we undertook a comprehensive capacity
  planning initiative for a 120-billion parameter Mixture-of-Experts (MoE) model (gpt-oss-120b),
  deployed across multiple NVIDIA H100 and H200 clusters to power an internal AI coding
  assistant. Rather than merely publishing our final capacity metrics, we have documented
  the rigorous, end-to-end methodology we developed to achieve them. We have compiled
  our findings into a detailed technical white paper: SPOC: a Stateful, Profile-based
  Optimization for LLM Capacity Planning Methodology. This white paper serves as a
  comprehensive guide to LLM performance engineering. It is designed to equip infrastructure
  teams with the analytical tools and empirical techniques required to: Construct
  stateful, multi-turn datasets that accurately simulate the complex context accumulation
  of developers querying shared enterprise monorepos. Apply multi-objective evolutionary
  algorithms ( Optuna NSGA-II ) to mathematically navigate the inference engine’s
  parameter space, replacing heuristic guesswork with rigorous optimization. Deploy
  an advanced telemetry stack ( Prometheus and DCGM Exporter ) to correlate internal
  inference-engine metrics with physical hardware state. Capture and interpret kernel-level
  NVIDIA Nsight Systems traces to identify the true architectural bottlenecks, which
  frequently defy the predictions of a simple theoretical roofline model.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/04/30/how-many-users-can-your-llm-server-really-handle/
