---
title: Day 2 Operations for AI Blueprints in VCF Automation
date: '2026-03-05T15:19:00+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/03/05/day-2-operations-for-ai-blueprints-in-vcf-automation/
post_kind: link
draft: false
tldr: 'Overview Editing a Blueprint in VCF Automation Blueprint Layout cloudInit and
  the dl_app. sh script Working with variables Testing a template Working in the deployed
  DLVM Editing a Form Publishing to the Catalog Overall Recommendations Resources
  Discover more from VMware Cloud Foundation (VCF) Blog Related Articles Building
  the Foundation for Private AI: Why Data Sovereignty Matters Day 2 Operations for
  AI Blueprints in VCF Automation Announcing the General Availability of Holodeck
  9.0.2 This is part three of six in a multi-blog series providing a practitioner’s
  guide to VMware Private AI Foundation with NVIDIA.'
summary: 'Overview Editing a Blueprint in VCF Automation Blueprint Layout cloudInit
  and the dl_app. sh script Working with variables Testing a template Working in the
  deployed DLVM Editing a Form Publishing to the Catalog Overall Recommendations Resources
  Discover more from VMware Cloud Foundation (VCF) Blog Related Articles Building
  the Foundation for Private AI: Why Data Sovereignty Matters Day 2 Operations for
  AI Blueprints in VCF Automation Announcing the General Availability of Holodeck
  9.0.2 This is part three of six in a multi-blog series providing a practitioner’s
  guide to VMware Private AI Foundation with NVIDIA. Most customers will want to customize
  the provided blueprints to meet their specific business requirements. This could
  be as simple as swapping out a specific NIM for a newer one, or maybe updating the
  LLM being deployed. It could also mean creating something significantly different.
  The possibilities are endless, but to get you started, here are some basics to consider.
  You will edit a blueprint under the Build & Deploy | Content Hub | Blueprint Design
  area in VCF Automation. This will display a basic UI of the blueprint’s major components.
  Clicking one takes you to that section and is helpful for navigation, especially
  when working with more complex templates. The right side shows the code for the
  template. This will be a combination of settings, variables, and code that will
  be executed in the Deep Learning VM (DLVM) once it is deployed. There are numerous
  developments in this area, so let us break down a few key areas and concepts for
  you.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/03/05/day-2-operations-for-ai-blueprints-in-vcf-automation/
