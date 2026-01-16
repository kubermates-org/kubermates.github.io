---
title: 'Technical Deep Dive: How DigitalOcean and AMD Delivered a 2x Production Inference
  Performance Increase for Character.ai'
date: '2026-01-13T12:30:00.048000+00:00'
tags:
- kubernetes
source: Digital Ocean
external_url: https://www.digitalocean.com/blog/technical-deep-dive-character-ai-amd
post_kind: link
draft: false
tldr: 'Technical Deep Dive: How DigitalOcean and AMD Delivered a 2x Production Inference
  Performance Increase for Character. ai Background: How Character.'
summary: 'Technical Deep Dive: How DigitalOcean and AMD Delivered a 2x Production
  Inference Performance Increase for Character. ai Background: How Character. ai worked
  with DigitalOcean and AMD to optimize performance Technical deep dive overview Technical
  optimizations DP1 / TP8 / EP8 with AITER DP2 / EP4 / TP4 with AITER Infrastructure
  setup Managed Kubernetes Cached Weights The New AI Systems Paradigm About the author(s)
  Related Articles DoTs SDK Development: Automating TypeScript Client Generation Currents
  Report: How Growing Tech Businesses Use AI Today How startups scale on DigitalOcean
  Kubernetes: Best Practices Part VI - Security By Piyush Srivastava and Karnik Modi
  Published: January 13, 2026 13 min read Character. ai , a leading AI entertainment
  platform with about 20 million worldwide users, wanted to optimize GPU performance
  and achieve lower inference costs for its application, which requires low-latency
  performance at large scale. They approached DigitalOcean and AMD in order to achieve
  this goal. Working closely together, the Character. ai , AMD, and DigitalOcean teams
  optimized AMD Instinct™ MI300X and MI325X GPU platforms, resulting in a 2x production
  inference throughput. In optimized configurations, DigitalOcean delivered high request
  density per node while maintaining exceptional p90 responsiveness for initial token
  and sustained token generation throughput, outperforming prior deployments on generic,
  non-optimized GPU infrastructure. These gains were achieved through platform-level
  optimizations, including clever parallelization strategies for large Mixture-of-Experts
  models, efficient FP8 execution paths, optimized kernels with AITER, topology-aware
  GPU allocation, and production-ready Kubernetes orchestration through DigitalOcean
  Kubernetes (DOKS). Together, these capabilities allowed Character. ai to scale inference
  predictably without increasing operational burden. In this post, we will explore
  the specific orchestration and tuning strategies that made these gains possible.'
---
Open the original post ↗ https://www.digitalocean.com/blog/technical-deep-dive-character-ai-amd
