---
title: How Should Prometheus Handle OpenTelemetry Resource Attributes? – A UX Research
  Report
date: '2025-08-25T19:42:02+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/08/25/how-should-prometheus-handle-opentelemetry-resource-attributes-a-ux-research-report/
post_kind: link
draft: false
tldr: Posted on August 25, 2025 by Victoria Nduka, User Experience Designer CNCF projects
  highlighted in this post On May 29th, 2025, I wrapped up my mentorship with Prometheus
  through the Linux Foundation Mentorship Program. My project focused on understanding
  how Prometheus handles OpenTelemetry resource attributes and how that experience
  could be improved for users.
summary: 'Posted on August 25, 2025 by Victoria Nduka, User Experience Designer CNCF
  projects highlighted in this post On May 29th, 2025, I wrapped up my mentorship
  with Prometheus through the Linux Foundation Mentorship Program. My project focused
  on understanding how Prometheus handles OpenTelemetry resource attributes and how
  that experience could be improved for users. My job was to conduct user research
  to get the user perspective on this challenge. In three months, I conducted user
  and stakeholder interviews, ran a survey, and analyzed the findings. In this article,
  I’ll share how I conducted the research, what I uncovered and where the communities
  involved could go from here. OpenTelemetry (OTel) has something called a resource
  attribute, which is extra information about the source of a metric, like the service,
  host, or environment that generated it. Prometheus, a time-series database, uses
  labels to identify and query metrics. If resource attributes are converted to labels,
  they can cause what’s known as “a cardinality explosion”, essentially creating too
  many unique combinations that overwhelm the system. This usually happens if the
  attributes change often or include a lot of unique values, like user IDs or pod
  names. Currently, there are three main approaches to handling this challenge: These
  aren’t bad solutions technically, but they don’t provide the best user experience.
  So, I conducted this research to understand what the Prometheus maintainers might
  be missing about the user experience. The research objectives were: My research
  approach was a mix of qualitative and quantitative research.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/08/25/how-should-prometheus-handle-opentelemetry-resource-attributes-a-ux-research-report/
