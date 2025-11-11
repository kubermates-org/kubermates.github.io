---
title: Self-hosted human and machine identities in Keycloak 26.4
date: '2025-11-07T15:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/11/07/self-hosted-human-and-machine-identities-in-keycloak-26-4/
post_kind: link
draft: false
tldr: What’s New in 26.4 Passwordless user authentication with Passkeys Tightened
  OpenID Connect security with FAPI 2 and DPoP Simplified deployments across multiple
  availability zones Authenticating applications with Kubernetes service account tokens
  or SPIFFE Looking ahead Posted on November 7, 2025 by Alexander Schwartz CNCF projects
  highlighted in this post Keycloak is a leading open source solution in the cloud-native
  ecosystem for Identity and Access Management, a key component of accessing applications
  and their data. With the release of Keycloak 26.4, we’ve added features for both
  machine and human identities.
summary: 'What’s New in 26.4 Passwordless user authentication with Passkeys Tightened
  OpenID Connect security with FAPI 2 and DPoP Simplified deployments across multiple
  availability zones Authenticating applications with Kubernetes service account tokens
  or SPIFFE Looking ahead Posted on November 7, 2025 by Alexander Schwartz CNCF projects
  highlighted in this post Keycloak is a leading open source solution in the cloud-native
  ecosystem for Identity and Access Management, a key component of accessing applications
  and their data. With the release of Keycloak 26.4, we’ve added features for both
  machine and human identities. New features focus on security enhancement, deeper
  integration, and improved server administration. See below for the release highlights,
  or dive deeper in our Keycloak 26.4 release announcement. Keycloak recently surpassed
  30k GitHub stars and 1,350 contributors. If you’re attending KubeCon + CloudNativeCon
  North America in Atlanta, stop by and say hi —we’d love to hear how you’re using
  Keycloak! Keycloak now offers full support for Passkeys. As secure, passwordless
  authentication becomes the new standard, we’ve made passkeys simple to configure.
  For environments that are unable to adopt passkeys, Keycloak continues to support
  OTP and recovery codes. You can find a passkey walkthrough on the Keycloak blog.
  Keycloak 26.4 implements the Financial-grade API (FAPI) 2.0 standard, ensuring strong
  security best practices. This includes support for Demonstrating Proof-of-Possession
  (DPoP), which is a safer way to handle tokens in public OpenID Connect clients.
  Deployment across multiple availability zones or data centers is simplified in 26.4:
  Split-brain detection Full support in the Keycloak Operator Latency optimizations
  when Keycloak nodes run in different data centers Keycloak docs contain a full step-by-step
  guide , and we published a blog post on how to scale to 2,000 logins/sec and 10,000
  token refreshes/sec.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/11/07/self-hosted-human-and-machine-identities-in-keycloak-26-4/
