---
title: 'Supply Chain Security Risk: GitHub Action tj-actions/changed-files Compromised'
date: '2025-03-16T15:56:32+00:00'
tags:
- security
source: Aqua Security
external_url: https://blog.aquasec.com/supply-chain-security-threat-github-action-tj-actions-compromised
post_kind: link
draft: false
tldr: CVE-2025-30066 On March 14th, 2025, security researchers discovered a critical
  software supply chain vulnerability in the widely-used GitHub Action tj-actions/changed-files
  ( CVE-2025-30066 ). This vulnerability allows remote attackers to expose CI/CD secrets
  via the action’s build logs.
summary: CVE-2025-30066 On March 14th, 2025, security researchers discovered a critical
  software supply chain vulnerability in the widely-used GitHub Action tj-actions/changed-files
  ( CVE-2025-30066 ). This vulnerability allows remote attackers to expose CI/CD secrets
  via the action’s build logs. The issue affects users who rely on the tj-actions/changed-files
  action in GitHub workflows to track changed files within a pull request. Due to
  the compromised action, sensitive CI/CD secrets are being inadvertently logged in
  the GitHub Actions build logs. If these logs are publicly accessible, such as in
  public repositories, unauthorized users could access and retrieve the clear text
  secrets. However, there is no evidence suggesting that the exposed secrets were
  transmitted to any external network. The tj-actions/changed-files action is widely
  used in GitHub CI/CD workflows to efficiently detect file changes within pull requests,
  streamlining development processes by conditionally triggering actions based on
  modified files. With over 23,000 active repositories and more than 1 million monthly
  downloads, its widespread adoption makes this compromise particularly impactful,
  exposing numerous organizations to potential supply chain attacks. According to
  the initial report by StepSecurity this incident was first discovered at 4PM UTC
  on March 14th, 2025, and isolated by 10:30 AM UTC on March 15th, 2025. But, we still
  warmly advise to avoid using this action until this matter is fully resolved. Initial
  investigation implies on a malicious commit ( hash:0e58ed8671d6b60d0890c21b07f8835ace038e67
  ), and a retroactive compromise of multiple versions, possibly all versions. The
  attackers introduced malicious JavaScript code directly into the dist/index.
---
Open the original post ↗ https://blog.aquasec.com/supply-chain-security-threat-github-action-tj-actions-compromised
