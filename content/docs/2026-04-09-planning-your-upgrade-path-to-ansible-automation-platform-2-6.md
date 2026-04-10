---
title: Planning your upgrade path to Ansible Automation Platform 2.6
date: '2026-04-09T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/planning-your-upgrade-path-ansible-automation-platform-26
post_kind: link
draft: false
tldr: 'Planning your upgrade path to Ansible Automation Platform 2.6 Planning your
  upgrade Approaches to upgrading Database-centric migrations API-centric migration
  A note on secrets Considerations for both methods Externally managed databases Playbook
  compatibility Additional resources 5 steps to automate your business About the author
  Ryan Bontreger More like this Take your automation to the next level with Ansible
  Content Collections for Windows, Splunk, AIOps, MCP, and more Automating the modern
  network: A Q1 network automation recap Technically Speaking | Taming AI agents with
  observability You Can''t Automate The Fire | Code Comments Keep exploring Browse
  by channel Automation Artificial intelligence Open hybrid cloud Security Edge computing
  Infrastructure Applications Virtualization Share The release of Red Hat Ansible
  Automation Platform 2.6 marks a pivotal milestone. Before you begin your upgrade,
  there are 3 key things you need to know to make your transition smoother: This is
  the last version with an RPM-based installer.'
summary: 'Planning your upgrade path to Ansible Automation Platform 2.6 Planning your
  upgrade Approaches to upgrading Database-centric migrations API-centric migration
  A note on secrets Considerations for both methods Externally managed databases Playbook
  compatibility Additional resources 5 steps to automate your business About the author
  Ryan Bontreger More like this Take your automation to the next level with Ansible
  Content Collections for Windows, Splunk, AIOps, MCP, and more Automating the modern
  network: A Q1 network automation recap Technically Speaking | Taming AI agents with
  observability You Can''t Automate The Fire | Code Comments Keep exploring Browse
  by channel Automation Artificial intelligence Open hybrid cloud Security Edge computing
  Infrastructure Applications Virtualization Share The release of Red Hat Ansible
  Automation Platform 2.6 marks a pivotal milestone. Before you begin your upgrade,
  there are 3 key things you need to know to make your transition smoother: This is
  the last version with an RPM-based installer. Red Hat Ansible Automation Platform
  2.6 using the RPM method is only available for Red Hat Enterprise Linux (RHEL) 9,
  and the RPM installer will be retired after this release. Ansible Automation Platform
  2.7 will only support a containerized install method, the Red Hat OpenShift operator,
  or our cloud services, so now is the time to begin the transition. Ansible Automation
  Platform 2.6 is a cornerstone release. Every upgrade path to future versions of
  the platform must pass through 2.6. There''s no getting around it. RHEL 8 is no
  longer supported. If you''re still on RHEL 8, you''ll need to migrate to RHEL 9
  (or RHEL 10) before upgrading to Ansible Automation Platform 2.6. As you plan your
  transition to Ansible Automation Platform 2.6, two important considerations should
  shape your upgrade plan: Only one thing can change at a time. Whether it''s the
  underlying operating system (OS), the installation method, or the product version,
  the installer only handles one change per run. That means you may need to run it
  multiple times.'
---
Open the original post ↗ https://www.redhat.com/en/blog/planning-your-upgrade-path-ansible-automation-platform-26
