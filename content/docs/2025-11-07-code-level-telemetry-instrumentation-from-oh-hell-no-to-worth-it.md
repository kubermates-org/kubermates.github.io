---
title: 'Code-level telemetry instrumentation: From “oh hell no” to “worth it”'
date: '2025-11-07T15:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/11/07/code-level-telemetry-instrumentation-from-oh-hell-no-to-worth-it/
post_kind: link
draft: false
tldr: A platform engineer’s guide to developer buy-in Posted on November 7, 2025 by
  Whitney Lee CNCF projects highlighted in this post Originally published on the author’s
  personal blog, whitneylee. com As platform engineers, we want the holistic system
  insights that instrumented code can give us – yes, please.
summary: 'A platform engineer’s guide to developer buy-in Posted on November 7, 2025
  by Whitney Lee CNCF projects highlighted in this post Originally published on the
  author’s personal blog, whitneylee. com As platform engineers, we want the holistic
  system insights that instrumented code can give us – yes, please. With code-level
  insights plus infrastructure observability, we can connect infrastructure signals
  to business outcomes. We can prove our value with Service Level Objectives (SLOs)
  like “99% of checkouts complete within 2 seconds. ” Not to mention the ability to
  auto-detect dependencies between services, automatically create dependency graphs,
  and power intelligent scaling. But instrumenting code is often a pain in the ass
  for developers. How do we motivate them to participate? Well, first off, we build
  application-adjacent observability collections into the platform as much as possible.
  What can we observe about our applications without the developer having to lift
  a finger? Framework-level telemetry : OpenTelemetry provides auto-instrumentation
  for popular programming languages, enabling your platform to collect trace data
  without modifying the code. You simply attach an agent, run your app with a startup
  flag, and it automatically implements common frameworks like HTTP servers, database
  clients, messaging libraries, Spring Boot, Express, etc. Kernel-level telemetry
  : The platform can also collect kernel-level insights using an eBPF-powered observability
  tool, such as Pixie or Cilium. Network-level telemetry : These can come from your
  service mesh technologies, like Istio, Linkerd, or Cilium. All of this you can do
  without the developer writing a single line of observability-related code.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/11/07/code-level-telemetry-instrumentation-from-oh-hell-no-to-worth-it/
