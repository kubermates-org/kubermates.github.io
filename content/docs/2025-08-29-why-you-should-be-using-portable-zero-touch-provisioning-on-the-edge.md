---
title: Why you should be using portable zero-touch provisioning on the edge
date: '2025-08-29T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/why-you-should-be-using-portable-zero-touch-provisioning-edge
post_kind: link
draft: false
tldr: Why you should be using portable zero-touch provisioning on the edge Challenges
  of provisioning air-gapped edge environments Portable edge ZTP architecture pattern
  How to design an air-gapped zero-touch provisioning solution Embracing container-native
  OS with RHEL image mode Laptop deployment Edge device image deployment Modern application
  distribution for edge Day 2 management evolution Automated zero-touch deployment
  Red Hat Device Edge | Product Trial About the author Silvio Pérez Torres More like
  this Blog post Blog post Blog post Keep exploring Browse by channel Automation Artificial
  intelligence Open hybrid cloud Security Edge computing Infrastructure Applications
  Virtualization Share Being connected is important, but for a dispersed, global,
  and mobile organization that works with increasingly sensitive data, sometimes it's
  better to stay disconnected for security, safety, operational, and other technical
  concerns. This type of deployment is often referred to as air-gapped.
summary: 'Why you should be using portable zero-touch provisioning on the edge Challenges
  of provisioning air-gapped edge environments Portable edge ZTP architecture pattern
  How to design an air-gapped zero-touch provisioning solution Embracing container-native
  OS with RHEL image mode Laptop deployment Edge device image deployment Modern application
  distribution for edge Day 2 management evolution Automated zero-touch deployment
  Red Hat Device Edge | Product Trial About the author Silvio Pérez Torres More like
  this Blog post Blog post Blog post Keep exploring Browse by channel Automation Artificial
  intelligence Open hybrid cloud Security Edge computing Infrastructure Applications
  Virtualization Share Being connected is important, but for a dispersed, global,
  and mobile organization that works with increasingly sensitive data, sometimes it''s
  better to stay disconnected for security, safety, operational, and other technical
  concerns. This type of deployment is often referred to as air-gapped. Common air-gapped
  environments include ships, vehicles, aircraft, remote industrial sites, nuclear
  facilities, and emergency field operations. These are locations where traditional
  network connectivity is unavailable or undesired, but where critical decision-making,
  predictive maintenance, resource estimation, safety monitoring, intrusion detection,
  and anomaly detection are essential. To address the challenges of operating in air-gapped
  environments (including lack of connectivity, limited hardware resources, manual
  update procedures, and the need for secure, autonomous systems) where agility in
  deployment and redeployment is critical, a portable edge zero touch provisioning
  (ZTP) solution can be adopted. Across various industry use cases, several essential
  requirements consistently emerge, which can be integrated into the ZTP solution:
  Self-contained: No dependency on cloud API or external data sources Long-lived:
  Must run for weeks or months without updates Secure by default: Threat models assume
  local tampering or sabotage Hardware-aware: Limited compute, storage, power, and
  rugged devices Manually updatable: Updates over USB, SD cards, or other physical
  media Network-constrained: Low, intermittent, or no connectivity (GSM, satellite,
  or fully offline) With common characteristics of air-gapped and resource-constrained
  environments identified, a portable edge ZTP architecture pattern can now be defined:
  Immutable infrastructure Description: The system, including operating system and
  services, is deployed as read-only, signed images. Benefits: Helps prevent drift
  and unauthorized changes, ensuring system integrity and security, which is crucial
  in an isolated environment. Description: The system, including operating system
  and services, is deployed as read-only, signed images. Benefits: Helps prevent drift
  and unauthorized changes, ensuring system integrity and security, which is crucial
  in an isolated environment. Hybrid workload: Description: Combine OCI-compliant
  containers with traditional package-based or virtualized workloads using Image Builder
  to enable seamless coexistence, with locally-hosted registries or USB transfers
  for modular, isolated deployment Benefits: Simplifies deployment, scalability, and
  management of applications, allowing for isolated updates without affecting other
  components. Description: Combine OCI-compliant containers with traditional package-based
  or virtualized workloads using Image Builder to enable seamless coexistence, with
  locally-hosted registries or USB transfers for modular, isolated deployment Benefits:
  Simplifies deployment, scalability, and management of applications, allowing for
  isolated updates without affecting other components. Offline, physical media, and
  network-isolated updates Description: Updates are delivered by physical media (USB,
  SD card) or through local network-restricted methods (DHCP/HTTP boot) using formats
  such as OSTree or container images.'
---
Open the original post ↗ https://www.redhat.com/en/blog/why-you-should-be-using-portable-zero-touch-provisioning-edge
