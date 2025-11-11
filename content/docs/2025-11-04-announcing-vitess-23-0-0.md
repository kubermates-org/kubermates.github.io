---
title: Announcing Vitess 23.0.0
date: '2025-11-04T19:13:35+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/11/04/announcing-vitess-23-0-0/
post_kind: link
draft: false
tldr: 'Why This Release Matters What’s New in Vitess 23 New Default Versions New &
  Improved Metrics Deprecations & Removals Topology & VTOrc Enhancements VTTablet
  & CLI / Docker Updates Upgrade Notes What’s Next Thanks & Acknowledgements Posted
  on November 4, 2025 by The Vitess Team CNCF projects highlighted in this post The
  Vitess team is excited to release Vitess 23.0.0 — the latest major version of Vitess
  — bringing new defaults, better operational tooling, and refined metrics. This release
  builds on the strong foundation of version 22 and is designed to make deployment
  and observability smoother, while continuing to scale MySQL workloads horizontally
  with confidence For production users of Vitess, this release is meaningful in several
  ways: Upgrading defaults: Moving to MySQL 8.4 as default future-proofs deployments
  and signals forward compatibility.'
summary: 'Why This Release Matters What’s New in Vitess 23 New Default Versions New
  & Improved Metrics Deprecations & Removals Topology & VTOrc Enhancements VTTablet
  & CLI / Docker Updates Upgrade Notes What’s Next Thanks & Acknowledgements Posted
  on November 4, 2025 by The Vitess Team CNCF projects highlighted in this post The
  Vitess team is excited to release Vitess 23.0.0 — the latest major version of Vitess
  — bringing new defaults, better operational tooling, and refined metrics. This release
  builds on the strong foundation of version 22 and is designed to make deployment
  and observability smoother, while continuing to scale MySQL workloads horizontally
  with confidence For production users of Vitess, this release is meaningful in several
  ways: Upgrading defaults: Moving to MySQL 8.4 as default future-proofs deployments
  and signals forward compatibility. Better metrics: The added observability enables
  deeper insights into transaction routing, shard behavior, and recovery actions —
  making debugging and alerting more precise. Clean-ups & deprecations: Removing legacy
  metrics and APIs simplifies monitoring and avoids confusion. Operational strength:
  Enhanced VTOrc and topology controls reduce risk in large-scale fleets and tighten
  security boundaries. Here are some of the standout changes you should know about:
  The default MySQL version for the vitess/lite:latest image has been bumped from
  8.0.40 to 8.4.6. → PR #18569 vitess/lite:latest VTGate now advertises MySQL version
  8.4.6 by default (instead of 8.0.40). If your backend uses a different version,
  set the mysql_server_version flag accordingly. → PR #18568 mysql_server_version
  Important upgrade detail for operator users: When upgrading from MySQL 8.0 → 8.4
  with the Vitess Operator, you must: Add innodb_fast_shutdown=0 to your extra. cnf
  in the YAML. Apply the file and wait until all pods are healthy. Switch the image
  to vitess/lite:v23.0.0.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/11/04/announcing-vitess-23-0-0/
