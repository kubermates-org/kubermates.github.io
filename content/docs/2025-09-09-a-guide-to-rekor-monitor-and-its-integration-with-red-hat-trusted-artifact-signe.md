---
title: A guide to Rekor Monitor and its integration with Red Hat Trusted Artifact
  Signer
date: '2025-09-09T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/guide-rekor-monitor-and-its-integration-red-hat-trusted-artifact-signer
post_kind: link
draft: false
tldr: A guide to Rekor Monitor and its integration with Red Hat Trusted Artifact Signer
  Rekor-monitor functionality Enabling Rekor-monitor in Red Hat Trusted Artifact Signer
  About the author Firas Ghanmi More like this Blog post Blog post Original podcast
  Original podcast Browse by channel Automation Artificial intelligence Open hybrid
  cloud Security Edge computing Infrastructure Applications Virtualization Share Securing
  the software supply chain is paramount in today’s digital world. As more organizations
  adopt practices like keyless signing to verify the integrity of their software artifacts,
  the need for robust monitoring against the systems that maintain the software supply
  chain infrastructure is essential.
summary: A guide to Rekor Monitor and its integration with Red Hat Trusted Artifact
  Signer Rekor-monitor functionality Enabling Rekor-monitor in Red Hat Trusted Artifact
  Signer About the author Firas Ghanmi More like this Blog post Blog post Original
  podcast Original podcast Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share Securing the software supply chain is paramount in today’s digital world.
  As more organizations adopt practices like keyless signing to verify the integrity
  of their software artifacts, the need for robust monitoring against the systems
  that maintain the software supply chain infrastructure is essential. One such system
  when signing and verifying content where monitoring can be applied is within the
  transparency log. While logs are tamper-evident, they are not tamper-proof, making
  a monitoring solution essential for an immutable and append-only record. This is
  where the Rekor Monitor comes in, providing an easy-to-use solution for verifying
  log consistency within a Red Hat Trusted Artifact Signer deployment. Red Hat Trusted
  Artifact Signer offers a keyless solution for signing and verifying software artifacts,
  making it a crucial element within Red Hat’s Trusted Software Supply Chain portfolio.
  By integrating Rekor-monitor, we can extend the principles of supply chain security
  by actively verifying the integrity of the private Rekor logs. This powerful combination
  of a verifiable log and continuous monitoring creates a robust audit trail, ensuring
  that the software supply chain remains secure, transparent, and compliant. Rekor-monitor,
  also known as Rekor Log Monitor, is a tool that continuously checks the integrity
  of Rekor transparency logs. It is designed to run periodically at a specified interval
  to verify that the Rekor transparency log remains append-only and immutable. For
  easy observability, the monitor also exposes Prometheus based metrics, which can
  be used by monitoring systems to create dashboards and set up alerts based on key
  metrics. For example, you could configure an alert to notify you immediately if
  a consistency check fails, indicating a potential compromise of the log.
---
Open the original post ↗ https://www.redhat.com/en/blog/guide-rekor-monitor-and-its-integration-red-hat-trusted-artifact-signer
