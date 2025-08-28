---
title: More resilient, flexible networking for the cloud workloads that matter
date: '2025-06-26T16:50:42.648000+00:00'
tags:
- kubernetes
source: Digital Ocean
external_url: https://www.digitalocean.com/blog/networking-partnernetworkconnect-byoip-reservedipv6
post_kind: link
draft: false
tldr: "By Anantha Ramachandran and Udhay Ravindran Building and scaling cloud infrastructure\
  \ often means navigating fragile network configurations, unpredictable IP behavior,\
  \ and rigid networking provider limitations. Whether itâ\x80\x99s dealing with flaky\
  \ multi-cloud connections, scrambling to update IP allow-lists after a restart,\
  \ or hesitating to migrate workloads due to reputation-bound IPs, these challenges\
  \ add unnecessary risk and complexity to modern deployments."
summary: "By Anantha Ramachandran and Udhay Ravindran Building and scaling cloud infrastructure\
  \ often means navigating fragile network configurations, unpredictable IP behavior,\
  \ and rigid networking provider limitations. Whether itâ\x80\x99s dealing with flaky\
  \ multi-cloud connections, scrambling to update IP allow-lists after a restart,\
  \ or hesitating to migrate workloads due to reputation-bound IPs, these challenges\
  \ add unnecessary risk and complexity to modern deployments. Weâ\x80\x99re excited\
  \ to announce three new updates designed to simplify cloud networking and enhance\
  \ deployment flexibility: Partner Network Connect supports high availability and\
  \ DOKS, general availability of Reserved IPv6 on Droplets, and public preview of\
  \ Bring Your Own IP (BYOIP). These improvements address real-world infrastructure\
  \ challenges and are built with simplicity, scalability, and reliability in mind.\
  \ Multi-cloud architectures are great, until the private links between them become\
  \ a single point of failure. For teams routing traffic between multiple cloud providers\
  \ like DigitalOcean, AWS, Microsoft Azure, or Google Cloud Platform, even brief\
  \ disruptions can stall ML pipelines, gaming platforms, or analytics services. Traditional\
  \ setups offer limited redundancy, and recovering from outages usually involves\
  \ manual intervention or rerouting traffic over public networks. High Availability\
  \ for Partner Network Connect helps solve this by letting you provision redundant\
  \ links across two separate DigitalOcean gateway routers. Traffic automatically\
  \ fails over if one link goes down, with no manual steps required and no impact\
  \ to your customers. With fully managed failover, this update removes operational\
  \ overhead while helping meet the needs of latency-sensitive or distributed systems.\
  \ Key benefits include: Automatic failover: Eliminate downtime from single link\
  \ failures. Reliable for demanding workloads: Especially useful for platforms in\
  \ streaming, AI, or multiplayer applications."
---
Open the original post ↗ https://www.digitalocean.com/blog/networking-partnernetworkconnect-byoip-reservedipv6
