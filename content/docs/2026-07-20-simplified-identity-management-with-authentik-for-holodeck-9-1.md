---
title: Simplified Identity Management with Authentik for Holodeck 9.1
date: '2026-07-20T17:04:39+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/07/20/identity-mgmt-for-holodeck/
post_kind: link
draft: false
tldr: 'Advantages of Authentik VCF SSO: One Identity Across the Entire Stack Advantages
  of VCF SSO The Use Case: Authentik as the VCF SSO Identity Provider Integrating
  Authentik with VCF SSO: Two Commands in Holodeck Command 1 — Initialize-Authentik
  Command 2 — Set-VCFSSOConfiguration Discover more from VMware Cloud Foundation (VCF)
  Blog Related Articles We Asked an Independent Lab to Time Us. Here''s What They
  Found.'
summary: 'Advantages of Authentik VCF SSO: One Identity Across the Entire Stack Advantages
  of VCF SSO The Use Case: Authentik as the VCF SSO Identity Provider Integrating
  Authentik with VCF SSO: Two Commands in Holodeck Command 1 — Initialize-Authentik
  Command 2 — Set-VCFSSOConfiguration Discover more from VMware Cloud Foundation (VCF)
  Blog Related Articles We Asked an Independent Lab to Time Us. Here''s What They
  Found. Simplified Identity Management with Authentik for Holodeck 9.1 The Modern
  Cloud Paradigm: Bridging the Gap Between Developer Velocity and Control Holodeck
  9.1 ships Authentik as a first-class service on the Holorouter. Two commands are
  all it takes to stand up a fully federated identity layer for your VMware Cloud
  Foundation (VCF) lab — no external LDAP, no manual UI clicks, no secrets scattered
  across config files. What is Authentik? Authentik is a self-hosted, open-source
  Identity Provider (IdP) that speaks the protocols modern platforms actually use:
  OIDC, OAuth2, SAML 2.0, and SCIM 2.0. Think of it as the identity backbone you would
  normally outsource to some third-party vendors — except it runs on your own infrastructure,
  costs nothing per user, and integrates natively with Kubernetes via a Helm chart.
  In Holodeck 9.1, Authentik is deployed inside the Holorouter’s single-node Kubernetes
  cluster at auth. vcf. lab. It is installed automatically as part of the Set-HoloRouter
  command, which in turn is part of New-HolodeckInstance command, so by the time your
  nested VCF deployment starts, the IdP is already healthy and waiting. Open Source
  and Self-Hosted — Fully open source with no per-seat licensing costs. Runs entirely
  inside the Holodeck environment on the Holorouter.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/07/20/identity-mgmt-for-holodeck/
