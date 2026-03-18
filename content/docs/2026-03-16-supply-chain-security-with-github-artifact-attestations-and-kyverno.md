---
title: Supply Chain Security with GitHub Artifact Attestations and Kyverno
date: '2026-03-16T16:53:31+00:00'
tags:
- nirmata
- kubernetes
source: Nirmata Blog
external_url: https://nirmata.com/2026/03/16/supply-chain-security-with-github-artifact-attestations-and-kyverno/?utm_source=rss&utm_medium=rss&utm_campaign=supply-chain-security-with-github-artifact-attestations-and-kyverno
post_kind: link
draft: false
tldr: 'Easier Attestations: GitHub Attestations Enforcement With Kyverno Operationalizing
  at Scale with Nirmata Summary GitHub Artifact Attestations makes it easy to cryptographically
  sign software artifacts like scan reports and SBOMs. But this is where they stop.'
summary: 'Easier Attestations: GitHub Attestations Enforcement With Kyverno Operationalizing
  at Scale with Nirmata Summary GitHub Artifact Attestations makes it easy to cryptographically
  sign software artifacts like scan reports and SBOMs. But this is where they stop.
  Provenance data and SBOMs is produced in CI, stored in the registry, and occasionally
  reviewed, yet rarely enforced. This gap undermines security posture and complicates
  auditing, ultimately making systems more vulnerable to breaches by failing to verify
  the integrity of the software being deployed. Frameworks such as SLSA (Supply-chain
  Levels for Software Artifacts) emphasize not just generating provenance, but ensuring
  it is: Verifiable Tamper-resistant Enforced in downstream systems Without runtime
  enforcement, even an SLSA Build Level 3 pipeline can be bypassed. A compromised
  credential or a manual image push can still introduce untrusted artifacts into production;
  in other words, attestations alone improve visibility, but not assurance. To achieve
  meaningful supply chain security, those attestations must be evaluated at deployment
  time. In this post, you will learn how to use Kyverno’s ValidatingImagePolicy to
  fill this critical security gap by enforcing checks during admission controls. By
  leveraging Sigstore and OpenID Connect (OIDC), GitHub enables teams to generate:
  SLSA v1.0 Provenance: Cryptographically signed claims about how the artifact was
  built. SPDX-compliant SBOMs: A manifest of every dependency included in the build
  in the form of an SBOM. Keyless Identity: OIDC-backed claims that link the image
  to a specific GitHub repository and workflow. This eliminates the “Key Management
  Tax” as there are no private keys to rotate or to lose.'
---
Open the original post ↗ https://nirmata.com/2026/03/16/supply-chain-security-with-github-artifact-attestations-and-kyverno/?utm_source=rss&utm_medium=rss&utm_campaign=supply-chain-security-with-github-artifact-attestations-and-kyverno
