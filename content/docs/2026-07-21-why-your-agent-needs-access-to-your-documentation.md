---
title: Why your agent needs access to your documentation
date: '2026-07-21T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/07/21/why-your-agent-needs-access-to-your-documentation/
post_kind: link
draft: false
tldr: 'Finding #1: Documentation became the fallback Finding #2: Documentation adds
  context to the native tools Finding #3: Documentation helps the agent use its own
  tools The takeaway Posted on July 21, 2026 by Finn Bauer, kapa. ai What 1,192 agent
  conversations taught us about knowledge base search A few months ago we shipped
  an agent inside our own product.'
summary: 'Finding #1: Documentation became the fallback Finding #2: Documentation
  adds context to the native tools Finding #3: Documentation helps the agent use its
  own tools The takeaway Posted on July 21, 2026 by Finn Bauer, kapa. ai What 1,192
  agent conversations taught us about knowledge base search A few months ago we shipped
  an agent inside our own product. It lives in our web app and lets users ask questions
  about their deployment, things like “how many Slack bot questions have users asked
  in the last month?” We built it because the analytics tooling we had shipped (clustering,
  tagging, filters) never quite covered every use case, and we wanted to see whether
  a chat interface could. The agent has around 30 native tools to interact with our
  platform, such as search_conversations and display_chart. It also has a single search_knowledge_base
  tool that can read documentation, code examples, support FAQs, and API reference.
  We expected the native tools to do most of the work. But when we looked at the last
  1,192 conversations, search_knowledge_base was the most used tool, almost as much
  as all the native tools combined. This pattern is worth flagging for the cloud-native
  community in particular. Across the CNCF landscape, from Kubernetes and Prometheus
  to Envoy, Argo, and OpenTelemetry, documentation is one of the primary interfaces
  between a project and its users, and it tends to be large, fast-moving, and spread
  across many surfaces. As more teams add agents alongside that documentation, the
  question of how much the agent should read the docs versus call purpose-built tools
  becomes a practical design decision. Here is what we found when we looked at why
  documentation search mattered so much. The main use case for knowledge base search
  was acting as a failover when users asked questions that no native tool could answer.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/07/21/why-your-agent-needs-access-to-your-documentation/
