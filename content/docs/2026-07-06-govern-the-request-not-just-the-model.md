---
title: Govern the Request, Not Just the Model
date: '2026-07-06T04:35:45+00:00'
tags:
- nirmata
- kubernetes
source: Nirmata Blog
external_url: https://nirmata.com/2026/07/05/govern-the-request/?utm_source=rss&utm_medium=rss&utm_campaign=govern-the-request
post_kind: link
draft: false
tldr: 'What we heard, and what we shipped One thing we learned the hard way The layer
  this sits at The product is the outcome What we heard from teams already using AI
  gateways — and what it still didn’t answer. Talking to platform and engineering
  teams putting AI into production, we kept hearing the same three questions — and
  the AI gateways they’d looked at answered none of them: Who just made that call
  — which developer, which team, which agent? What did it actually do — which tools
  did it touch, against which systems? Did any of it produce something worth the spend?
  The stories behind those questions were specific.'
summary: 'What we heard, and what we shipped One thing we learned the hard way The
  layer this sits at The product is the outcome What we heard from teams already using
  AI gateways — and what it still didn’t answer. Talking to platform and engineering
  teams putting AI into production, we kept hearing the same three questions — and
  the AI gateways they’d looked at answered none of them: Who just made that call
  — which developer, which team, which agent? What did it actually do — which tools
  did it touch, against which systems? Did any of it produce something worth the spend?
  The stories behind those questions were specific. A team in a regulated industry
  needed to prove which model had handled sensitive data — with real deadlines attached,
  not a next-quarter aspiration. A large engineering org was hand-building a developer-productivity
  scoreboard in a spreadsheet because nothing tied AI spend to shipped work. A platform
  team already running Kyverno across their clusters asked why their AI agents were
  the one workload with no policy layer at all. Model routing wasn’t the thing keeping
  these teams up at night. When it came up at all, it was table stakes. Routing governs
  one thing — which model handles a request — a real decision, and the narrowest one
  in the request path. It’s the floor of governance, not the ceiling, and none of
  the three questions above live at that layer. That’s the gap we built AIControls
  to close. Each question our users raised maps to something concrete in the product.
  “Who made this call?” Routing sees an API key.'
---
Open the original post ↗ https://nirmata.com/2026/07/05/govern-the-request/?utm_source=rss&utm_medium=rss&utm_campaign=govern-the-request
