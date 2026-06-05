---
title: OAuth 2.0 Authentication Using VMware Cloud Foundation PowerCLI 9.1
date: '2026-06-01T14:22:30+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/06/01/oauth-2-0-authentication-using-vmware-cloud-foundation-powercli-9-1/
post_kind: link
draft: false
tldr: Passwordless Authentication The Workflow 1. Register the API Client 2.
summary: 'Passwordless Authentication The Workflow 1. Register the API Client 2. Generate
  the API Token 3. Exchange for a Bearer Access Token 4. Authenticate with VCF Components
  Using OAuth 2.0 Authentication Token in VCF PowerCLI Conclusion Resources Discover
  more from VMware Cloud Foundation (VCF) Blog Related Articles Explore What’s New:
  VMware vSphere Foundation 9.1 Resources Now Available Unified Cloud Value: Accelerating
  Cloud Fin-Ops with VCF 9.1 and FOCUS VCF 9.1 Tag Management: Elevating Operational
  Governance The release of VMware Cloud Foundation (VCF) 9.1 introduces plenty of
  new enhancements and updates. I previously outlined the idea of a fully programmable
  infrastructure and how we achieved this milestone with the VCF 9.1 release. If you
  are new to the concept of programmable infrastructure, I highly recommend checking
  out my previous blog post: Unlocking the Full Potential of Programmable Infrastructure
  with VMware Cloud Foundation 9.1: New Features and Capabilities. In this blog post,
  I will detail the steps required to establish OAuth 2.0 authentication using VCF
  SSO. Historically, developers were assigned service accounts or often used their
  own credentials to programmatically authenticate VCF components. While this isn’t
  an issue during interactive authentication via a CLI prompt, it becomes a major
  security concern when passwords are saved in plain text files or hardcoded into
  scripts. If those scripts are compromised, you jeopardize the security of your critical
  infrastructure, leaving your cloud environment vulnerable to misuse by bad actors.
  The ideal alternative is to implement token-based authentication within your automation
  scripts and workflows.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/06/01/oauth-2-0-authentication-using-vmware-cloud-foundation-powercli-9-1/
