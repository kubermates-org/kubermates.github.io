---
title: GitHub Actions Under Attack. The Ultimate Defense Guide.
date: '2026-03-24T16:30:29+00:00'
tags:
- nirmata
- kubernetes
source: Nirmata Blog
external_url: https://nirmata.com/2026/03/24/github-actions-is-under-attack/?utm_source=rss&utm_medium=rss&utm_campaign=github-actions-is-under-attack
post_kind: link
draft: false
tldr: 'What Just Happened The Trivy Supply Chain Attack TeamPCP Hacks Checkmarx via
  Stolen CI Credentials HackerBot / CLAW Campaign The Common Thread: Workflow Hygiene
  Failures Introducing nctl scan github-actions How It Works Would nctl Have Caught
  These Attacks? Trivy / TeamPCP: Yes — Two Policies Fire Directly CLAW / HackerBot
  Injection Campaign: Multiple Policies Fire What nctl Cannot Catch (And What Can)
  Example: Scanning the Kyverno Website Repo Getting Started Three major supply chain
  attacks. One common thread.'
summary: 'What Just Happened The Trivy Supply Chain Attack TeamPCP Hacks Checkmarx
  via Stolen CI Credentials HackerBot / CLAW Campaign The Common Thread: Workflow
  Hygiene Failures Introducing nctl scan github-actions How It Works Would nctl Have
  Caught These Attacks? Trivy / TeamPCP: Yes — Two Policies Fire Directly CLAW / HackerBot
  Injection Campaign: Multiple Policies Fire What nctl Cannot Catch (And What Can)
  Example: Scanning the Kyverno Website Repo Getting Started Three major supply chain
  attacks. One common thread. In the past few months, GitHub Actions has become one
  of the most actively targeted surfaces in software supply chains. Three attacks
  — the Orca HackerBot/CLAW campaign, the TeamPCP/Checkmarx compromise, and the Trivy
  supply chain attack — have demonstrated that CI/CD workflows are no longer a secondary
  concern for security teams. They are a primary attack vector. This post breaks down
  what happened, what these attacks have in common, and how nctl scan github-actions
  — Nirmata’s new static analysis capability — can detect and prevent the class of
  vulnerabilities that made them possible. nctl scan github-actions Aqua Security’s
  open-source Trivy scanner was compromised after attackers gained access to CI credentials.
  The attackers force-pushed malicious commits to 76 of 77 Trivy release tags on GitHub.
  Any workflow consuming aquasecurity/trivy-action@v0.24.0 — a mutable tag — pulled
  the malicious entrypoint instead of the legitimate one. aquasecurity/trivy-action@v0.24.0
  The payload performed multi-stage exfiltration: scraping PATs from memory via /proc/{PID}/mem
  , harvesting cloud credentials from IMDS endpoints, encrypting and staging the data,
  then POSTing it to an attacker-controlled domain. A fallback path used the compromised
  GITHUB_TOKEN to create a new repository as a data drop. /proc/{PID}/mem GITHUB_TOKEN
  Aqua has confirmed their commercial platform was isolated and unaffected, but the
  open-source ecosystem impact was broad.'
---
Open the original post ↗ https://nirmata.com/2026/03/24/github-actions-is-under-attack/?utm_source=rss&utm_medium=rss&utm_campaign=github-actions-is-under-attack
