---
title: Benchmarking AI agent retrieval strategies on Kubernetes bug fixes
date: '2026-05-08T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/05/08/benchmarking-ai-agent-retrieval-strategies-on-kubernetes-bug-fixes/
post_kind: link
draft: false
tldr: The setup The test cases (Benchmark) Timing Token economics What I actually
  learned The bottom line Posted on May 8, 2026 by Brandon Foley CNCF projects highlighted
  in this post I’ve been using AI coding agents as part of my daily engineering workflow
  and wanted to understand how well they actually perform on real-world bugs. To test
  this, I ran a series of structured experiments using bug reports from the Kubernetes
  repository, evaluating whether agents could produce correct, complete fixes without
  guidance in a large, multi-million-line codebase.
summary: 'The setup The test cases (Benchmark) Timing Token economics What I actually
  learned The bottom line Posted on May 8, 2026 by Brandon Foley CNCF projects highlighted
  in this post I’ve been using AI coding agents as part of my daily engineering workflow
  and wanted to understand how well they actually perform on real-world bugs. To test
  this, I ran a series of structured experiments using bug reports from the Kubernetes
  repository, evaluating whether agents could produce correct, complete fixes without
  guidance in a large, multi-million-line codebase. My initial assumption was simple.
  Success would largely depend on retrieval. Whether via retrieval-augmented generation
  (RAG) or filesystem search, a model that finds the right code should be able to
  generate the right fix. That assumption didn’t fully hold. Even when agents surfaced
  the right files, they often failed to connect changes across them, misidentified
  the true scope of the issue, or produced fixes that were locally plausible but globally
  incorrect. The bottleneck wasn’t just finding code, it was reasoning over it in
  context. I took open pull requests from the kubernetes GitHub repo. Real bugs, actively
  being fixed by real contributors. I extracted just the issue description (not the
  PR description, not the diff, nothing that would leak the solution) and gave each
  issue to three different agent configurations: RAG Only : Hybrid retrieval over
  an indexed copy of the Kubernetes codebase via KAITO RAG Engine (Qdrant) , combining
  BM25 for keyword matching with embedding based semantic search. KAITO also provides
  an auto-indexing controller which is perfect for indexing huge git repos with the
  capability of incremental indexing.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/05/08/benchmarking-ai-agent-retrieval-strategies-on-kubernetes-bug-fixes/
