---
title: Zero-Downtime migration from ingress NGINX to Envoy Gateway
date: '2026-05-25T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/05/25/zero-downtime-migration-from-ingress-nginx-to-envoy-gateway/
post_kind: link
draft: false
tldr: 'Why migrate from ingress NGINX to Gateway API Migrating a customer from ingress
  NGINX to Envoy Gateway Picking the right Gateway API controller Testing Envoy Gateway
  on our own infrastructure first A Successful Gateway API migration, but not good
  enough Achieving Zero downtime with weighted DNS What production actually surfaced
  Where Gateway API goes from here Recap: Doing your Ingress NGINX migration right
  Posted on May 25, 2026 by Andrew Katsikas, Pelotech CNCF projects highlighted in
  this post Teams running Ingress NGINX in production are increasingly evaluating
  migration paths as Kubernetes networking evolves toward Gateway API. For many organizations,
  the challenge is not just selecting a Gateway API implementation, but designing
  a migration strategy that minimizes operational risk during cutover.'
summary: 'Why migrate from ingress NGINX to Gateway API Migrating a customer from
  ingress NGINX to Envoy Gateway Picking the right Gateway API controller Testing
  Envoy Gateway on our own infrastructure first A Successful Gateway API migration,
  but not good enough Achieving Zero downtime with weighted DNS What production actually
  surfaced Where Gateway API goes from here Recap: Doing your Ingress NGINX migration
  right Posted on May 25, 2026 by Andrew Katsikas, Pelotech CNCF projects highlighted
  in this post Teams running Ingress NGINX in production are increasingly evaluating
  migration paths as Kubernetes networking evolves toward Gateway API. For many organizations,
  the challenge is not just selecting a Gateway API implementation, but designing
  a migration strategy that minimizes operational risk during cutover. Most engineering
  teams know they need to migrate, but they are short on the bandwidth to do a proper
  evaluation, unsure which Gateway API controller is the right long-term bet, and
  aware that a rushed cutover will drop production traffic the moment DNS TTLs disagree
  with reality. This piece is a case study of an Ingress NGINX migration we recently
  ran for a customer on AWS. It walks through how we picked Envoy Gateway, how we
  tested the migration on our own infrastructure first, why our first successful cutover
  was not good enough, and the weighted DNS approach that finally got us a clean zero-downtime
  result. There is also a short FAQ at the end covering the questions we keep getting
  asked about this transition. If you are working through this migration yourself,
  the goal here is to save you the discovery work we have already done. Ingress NGINX
  controller is one of the most widely deployed controllers in the Kubernetes ecosystem,
  and plenty of production clusters are running it right now. With no security patches
  , no new features, and an Ingress API frozen in place, Gateway API is the logical
  next step. It is a more expressive specification that replaces annotations with
  dedicated resources for the same concerns. In a recent customer engagement on AWS,
  we evaluated several Gateway API implementations and migration approaches before
  settling on Envoy Gateway. Because we leverage Ingress NGINX in Foundation, our
  opinionated GitOps Kubernetes platform, this migration was just as relevant to us
  as it was to our customer.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/05/25/zero-downtime-migration-from-ingress-nginx-to-envoy-gateway/
