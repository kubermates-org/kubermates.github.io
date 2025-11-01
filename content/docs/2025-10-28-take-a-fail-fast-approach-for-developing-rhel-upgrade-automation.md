---
title: Take a fail-fast approach for developing RHEL upgrade automation
date: '2025-10-28T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/take-fail-fast-approach-developing-rhel-upgrade-automation
post_kind: link
draft: false
tldr: Take a fail-fast approach for developing RHEL upgrade automation The challenge
  The solution 1. Automate Everything 2.
summary: 'Take a fail-fast approach for developing RHEL upgrade automation The challenge
  The solution 1. Automate Everything 2. Snapshot with rollback 3. Custom Modules
  4. Reporting dashboard (optional, but VERY useful) Lessons learned from automating
  a million RHEL in-place upgrades Learn more about RHEL upgrades We''re here to help
  Red Hat Ansible Automation Platform | Product Trial About the authors Bob Mader
  Bob Handlin More like this Blog post Blog post Original podcast Original podcast
  Keep exploring Browse by channel Automation Artificial intelligence Open hybrid
  cloud Security Edge computing Infrastructure Applications Virtualization Share It''s
  been just over two years since we wrote about automating in-place upgrades for Red
  Hat Enterprise Linux (RHEL). During that time, we''ve seen dozens of customers upgrade
  hundreds of thousands of systems using our prescriptive, automated approach to make
  RHEL upgrades happen at scale. In this article, we’ll do a quick review of the key
  features that help accelerate the roll out of RHEL upgrade automation. We’ll look
  at what’s worked well, but also at some of the challenges and lessons learned. The
  key learning: Fail fast, iterate, and try again. The most important thing this accomplishes
  is making the upgrade process less scary, allowing quick recovery to the original
  state when things don''t go perfectly right away. Many of our biggest customers
  have large RHEL environments that have grown and evolved through the decades since
  enterprise adoption of Linux took off in the early 2000s. Organizations have tried
  to virtualize and containerize with the best intentions of modernizing how they
  deploy and manage application workloads, but some still have vast numbers of RHEL
  hosts that haven''t caught up.'
---
Open the original post ↗ https://www.redhat.com/en/blog/take-fail-fast-approach-developing-rhel-upgrade-automation
