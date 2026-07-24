---
title: 'Outperforming Fable 5 at half the price: meet model synthesis, a new server-side
  tool on DigitalOcean Inference Engine'
date: '2026-07-23T20:03:12.073000+00:00'
tags:
- kubernetes
source: Digital Ocean
external_url: https://www.digitalocean.com/blog/model-synthesis
post_kind: link
draft: false
tldr: 'Outperforming Fable 5 at half the price: meet model synthesis, a new server-side
  tool on DigitalOcean Inference Engine How we tested it Results The synthesizer you
  choose drives the quality Efficiency: high quality for about half the cost What
  this means for you Get started Direct configuration About the author(s) Start building
  today Related Articles Built for Mass Scale: Hard-Won Lessons from Teams Running
  High Volume Inference Workloads in Production Run Codex in the cloud – DigitalOcean
  for Codex is now available The Inference Tax: How Prefix-Aware Routing Eliminates
  the Hidden Cost of LLMs at Scale By Hemasumanth Rasineni and Tyler Gillam Updated:
  July 23, 2026 8 min read Anyone building with AI runs into the same tradeoff: how
  to get the most intelligence per dollar, the right model at the right cost for each
  task. DigitalOcean Inference Engine is built to help you make that tradeoff, and
  one way is finding the right model for each job.'
summary: 'Outperforming Fable 5 at half the price: meet model synthesis, a new server-side
  tool on DigitalOcean Inference Engine How we tested it Results The synthesizer you
  choose drives the quality Efficiency: high quality for about half the cost What
  this means for you Get started Direct configuration About the author(s) Start building
  today Related Articles Built for Mass Scale: Hard-Won Lessons from Teams Running
  High Volume Inference Workloads in Production Run Codex in the cloud – DigitalOcean
  for Codex is now available The Inference Tax: How Prefix-Aware Routing Eliminates
  the Hidden Cost of LLMs at Scale By Hemasumanth Rasineni and Tyler Gillam Updated:
  July 23, 2026 8 min read Anyone building with AI runs into the same tradeoff: how
  to get the most intelligence per dollar, the right model at the right cost for each
  task. DigitalOcean Inference Engine is built to help you make that tradeoff, and
  one way is finding the right model for each job. But sometimes one model isn’t enough.
  On deep-research tasks, we found that running several models and synthesizing their
  outputs beats relying on one: an all-open-source panel (GLM 5.2 + Kimi K2. 6) scored
  higher than every single model we tested, including Fable 5, at about half its cost
  per task. Model synthesis , a new server-side tool on DigitalOcean Inference Engine
  , does that orchestration for you. It runs from a model configuration you define:
  a panel of models that process each request in parallel, and a synthesizer model
  that reviews the panel’s outputs and combines them into one response. Start from
  an optimized preset or define the panel and synthesizer yourself. It pays off. We
  benchmarked model synthesis on DRACO, a 100-task deep-research benchmark, across
  15 open-source and frontier model configurations. The key results: GLM 5.2 + Kimi
  K2. 6 panel scored 65.65% on quality at $0.83 per task, outperforming Fable 5 (62.21%
  at $1.59 per task).'
---
Open the original post ↗ https://www.digitalocean.com/blog/model-synthesis
