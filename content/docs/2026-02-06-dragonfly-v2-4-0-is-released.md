---
title: Dragonfly v2.4.0 is released
date: '2026-02-06T00:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/02/05/dragonfly-v2-4-0-is-released/
post_kind: link
draft: false
tldr: New features and enhancements Simple multi‑cluster Kubernetes deployment with
  scheduler cluster ID Performance and resource optimization for Manager and Scheduler
  components Enhanced preheating Calculate task ID based on image blob SHA256 to avoid
  redundant downloads Cache HTTP 307 redirects for split downloads Go Client deprecated
  and replaced by Rust client Significant bug fixes Nydus Others Links Dragonfly Github
  Posted on February 5, 2026 by epower CNCF projects highlighted in this post Dragonfly
  v2.4.0 is released! Thanks to all of the contributors who made this Dragonfly release
  happen. A two-stage scheduling algorithm combining central scheduling with node-level
  secondary scheduling to optimize P2P download performance, based on real-time load
  awareness.
summary: New features and enhancements Simple multi‑cluster Kubernetes deployment
  with scheduler cluster ID Performance and resource optimization for Manager and
  Scheduler components Enhanced preheating Calculate task ID based on image blob SHA256
  to avoid redundant downloads Cache HTTP 307 redirects for split downloads Go Client
  deprecated and replaced by Rust client Significant bug fixes Nydus Others Links
  Dragonfly Github Posted on February 5, 2026 by epower CNCF projects highlighted
  in this post Dragonfly v2.4.0 is released! Thanks to all of the contributors who
  made this Dragonfly release happen. A two-stage scheduling algorithm combining central
  scheduling with node-level secondary scheduling to optimize P2P download performance,
  based on real-time load awareness. For more information, please refer to the Scheduling.
  Dragonfly provides the new Vortex transfer protocol based on TLV to improve the
  download performance in the internal network. Use the TLV (Tag-Length-Value) format
  as a lightweight protocol to replace gRPC for data transfer between peers. TCP-based
  Vortex reduces large file download time by 50% and QUIC-based Vortex by 40% compared
  to gRPC, both effectively reducing peak memory usage. For more information, please
  refer to the TCP Protocol Support for P2P File Transfer and QUIC Protocol Support
  for P2P File Transfer. A SDK for routing User requests to Seed Peers using consistent
  hashing, replacing the previous Kubernetes Service load balancing approach. Dragonfly
  supports a simplified feature for deploying and managing multiple Kubernetes clusters
  by explicitly assigning a schedulerClusterID to each cluster. This approach allows
  users to directly control cluster affinity without relying on location‑based scheduling
  metadata such as IDC, hostname, or IP. Using this feature, each Peer, Seed Peer,
  and Scheduler determines its target scheduler cluster through a clearly defined
  scheduler cluster ID. This ensures precise separation between clusters and predictable
  cross‑cluster behavior.
---
Open the original post ↗ https://www.cncf.io/blog/2026/02/05/dragonfly-v2-4-0-is-released/
