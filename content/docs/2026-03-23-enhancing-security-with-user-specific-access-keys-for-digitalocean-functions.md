---
title: Enhancing Security with User-Specific Access Keys for DigitalOcean Functions
date: '2026-03-23T19:30:06.826000+00:00'
tags:
- kubernetes
source: Digital Ocean
external_url: https://www.digitalocean.com/blog/functions-user-specific-access-keys
post_kind: link
draft: false
tldr: 'Enhancing Security with User-Specific Access Keys for DigitalOcean Functions
  How user-specific access keys enhance security Tutorial: Managing Functions access
  keys via API Prerequisites Tutorial: Managing your access keys via doctl Prerequisites
  Migration and transition timeline for user-specific access keys A more secure future
  for DigitalOcean Functions About the author Try DigitalOcean for free Related Articles
  OAuth App Based Workload Identity for Droplets How DigitalOcean Uses Semgrep to
  Fortify Security: A Highlight From Our Toolset Contextual Vulnerability Management
  With Security Risk As Debt By Amulya Tomer Updated: March 23, 2026 5 min read As
  teams grow and scale their serverless workloads, managing security postures becomes
  just as critical as managing code. Our goal at DigitalOcean is to support your growth
  at every stage.'
summary: 'Enhancing Security with User-Specific Access Keys for DigitalOcean Functions
  How user-specific access keys enhance security Tutorial: Managing Functions access
  keys via API Prerequisites Tutorial: Managing your access keys via doctl Prerequisites
  Migration and transition timeline for user-specific access keys A more secure future
  for DigitalOcean Functions About the author Try DigitalOcean for free Related Articles
  OAuth App Based Workload Identity for Droplets How DigitalOcean Uses Semgrep to
  Fortify Security: A Highlight From Our Toolset Contextual Vulnerability Management
  With Security Risk As Debt By Amulya Tomer Updated: March 23, 2026 5 min read As
  teams grow and scale their serverless workloads, managing security postures becomes
  just as critical as managing code. Our goal at DigitalOcean is to support your growth
  at every stage. One way we support you is by iterating on our security architecture.
  Historically, DigitalOcean Functions used a shared credential model within a namespace
  that is configured in the settings tab of the function view. Same is shared among
  all users for a functions namespace While simple to start, this model presented
  challenges for growing teams: if a team member left or changed roles, the shared
  credentials remained valid. To secure the namespace, admins had to manually revoke
  and regenerate keys, disrupting workflows for every other developer and production
  workload using that shared key. Today, we are excited to announce a considerable
  upgrade to our access model: user-specific namespace access keys. This update shifts
  access control from the namespace level to the individual identity level, ensuring
  that access is granted to specific users rather than through a shared key. This
  transition to user-specific keys solves several critical use cases for teams: Automated
  access management: When a team member is removed from your DigitalOcean team, their
  specific access keys are automatically revoked by the platform. This removes the
  need for manual key rotation and ensures zero disruption to remaining team members.
  Automated access management: When a team member is removed from your DigitalOcean
  team, their specific access keys are automatically revoked by the platform. This
  removes the need for manual key rotation and ensures zero disruption to remaining
  team members.'
---
Open the original post ↗ https://www.digitalocean.com/blog/functions-user-specific-access-keys
