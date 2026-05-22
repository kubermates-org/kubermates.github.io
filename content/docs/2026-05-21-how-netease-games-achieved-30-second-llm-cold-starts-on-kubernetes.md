---
title: How NetEase Games achieved 30-second LLM cold starts on Kubernetes
date: '2026-05-21T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/05/21/how-netease-games-achieved-30-second-llm-cold-starts-on-kubernetes/
post_kind: link
draft: false
tldr: 'The Day 2 problem: Cold starts, shared models, and fragmented GPU capacity
  Why we didn’t just run Alluxio directly Fluid: Adding operational control to Alluxio
  What changed in production A useful way to frame the choice Posted on May 21, 2026
  by Haifeng Liao, Senior Infrastructure Engineer at NetEase Games and Xiang Zhang,
  Head of AI Infrastructure at NetEase Games CNCF projects highlighted in this post
  At NetEase Games, we learned a hard lesson about large language model (LLM) inference
  in production: elastic compute is only useful if data can move just as fast. “Elastic
  compute is only useful if data can move just as fast.'
summary: 'The Day 2 problem: Cold starts, shared models, and fragmented GPU capacity
  Why we didn’t just run Alluxio directly Fluid: Adding operational control to Alluxio
  What changed in production A useful way to frame the choice Posted on May 21, 2026
  by Haifeng Liao, Senior Infrastructure Engineer at NetEase Games and Xiang Zhang,
  Head of AI Infrastructure at NetEase Games CNCF projects highlighted in this post
  At NetEase Games, we learned a hard lesson about large language model (LLM) inference
  in production: elastic compute is only useful if data can move just as fast. “Elastic
  compute is only useful if data can move just as fast. ” On paper, serverless GPU
  infrastructure looked like a good fit for inference workloads. Game traffic is bursty,
  peaks differ by title and time of day, and reserving GPU capacity for every possible
  spike is expensive. But once we started scaling LLM services across regions, a different
  bottleneck emerged. The real problem was not scheduling containers. It was loading
  model data. For 70B-class models, pulling hundreds of gigabytes of weights from
  remote storage into inference nodes could take tens of minutes. That erased the
  value of autoscaling. In one representative workload, model load time was reduced
  from 42 minutes with cross-region direct storage access to 14 minutes with a traditional
  Alluxio-based cache and then to 3 minutes after we enabled Fluid’s prefetching workflow.
  That difference turned serverless inference from an architectural idea into something
  we could actually operate. Our AI platform, Tmax, runs on Kubernetes and supports
  the full ML lifecycle, from notebook-based development to training and inference
  deployment.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/05/21/how-netease-games-achieved-30-second-llm-cold-starts-on-kubernetes/
