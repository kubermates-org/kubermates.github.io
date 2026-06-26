---
title: 'Kyverno Policy Benchmarks: Same Model, Different Harness, Very Different Results'
date: '2026-06-15T11:05:45+00:00'
tags:
- nirmata
- kubernetes
source: Nirmata Blog
external_url: https://nirmata.com/2026/06/15/kyverno-policy-benchmarks/?utm_source=rss&utm_medium=rss&utm_campaign=kyverno-policy-benchmarks
post_kind: link
draft: false
tldr: 'What We Were Testing The Dataset Results Policy Conversion and Generation (50
  tasks) Kyverno CLI Test Generation (6 tasks) Chainsaw Test Generation (1 task) What
  We Found Building the Benchmark Models hallucinate field names without schema documentation
  A prompt template bug was suppressing required fields kyverno test works natively
  on non-Kubernetes resources Some tasks that appeared to pass were never testing
  the hard part Single-run results are noisy Reported cost is nearly meaningless What
  the Gap Is Actually Made Of How we know: the prompt experiments Skills bridge what
  training data can’t The feedback loop is a safety net, not the primary driver Limitations
  Try It Yourself We benchmarked our own tool against two general-purpose AI agents
  on Kyverno policy tasks. Here’s what we found, including the parts that complicate
  the story.'
summary: 'What We Were Testing The Dataset Results Policy Conversion and Generation
  (50 tasks) Kyverno CLI Test Generation (6 tasks) Chainsaw Test Generation (1 task)
  What We Found Building the Benchmark Models hallucinate field names without schema
  documentation A prompt template bug was suppressing required fields kyverno test
  works natively on non-Kubernetes resources Some tasks that appeared to pass were
  never testing the hard part Single-run results are noisy Reported cost is nearly
  meaningless What the Gap Is Actually Made Of How we know: the prompt experiments
  Skills bridge what training data can’t The feedback loop is a safety net, not the
  primary driver Limitations Try It Yourself We benchmarked our own tool against two
  general-purpose AI agents on Kyverno policy tasks. Here’s what we found, including
  the parts that complicate the story. We build nctl , a CLI-based controller for
  Nirmata and policy as code powered by Kyverno. That means we have an obvious stake
  in what follows. Here’s what we did about it: we open-sourced the benchmark, used
  identical bare-minimum prompts across all tools, ran each tool in an isolated container
  with no special access, and published the dataset, evaluation code, and raw results
  at nirmata/policy-bench. With that said, here’s the result: across 50 policy tasks
  using bare-minimum prompts and containerized isolation, nctl finished at 98%, Claude
  Code at 62%, and Cursor at 58%. Same underlying model (Claude Sonnet 4.6) in all
  three cases. Same prompt. Same input policies. The gap is real. But the most interesting
  things we found weren’t in the headline numbers. They were in the bugs we discovered
  in our own benchmark along the way.'
---
Open the original post ↗ https://nirmata.com/2026/06/15/kyverno-policy-benchmarks/?utm_source=rss&utm_medium=rss&utm_campaign=kyverno-policy-benchmarks
