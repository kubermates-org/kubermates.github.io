---
title: Bring your own knowledge to the automation intelligent assistant
date: '2026-06-17T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/bring-your-own-knowledge-automation-intelligent-assistant
post_kind: link
draft: false
tldr: 'Bring your own knowledge to the automation intelligent assistant Automation
  intelligence made more relevant Custom knowledge in practice Getting started and
  additional resources Red Hat Ansible Automation Platform | Product Trial About the
  author Tricia McConnell More like this Securing the enterprise software fabric:
  A blueprint for open source Scaling automated infrastructure compliance in telecommunications
  using Red Hat Ansible Automation Platform Operating System Management | Compiler
  Technically Speaking | Inside open source AI strategy Keep exploring Browse by channel
  Automation Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share Last year, we released the automation intelligent
  assistant (formerly Red Hat Ansible Lightspeed intelligent assistant), a generative
  AI service accessed through a chatbot embedded within Red Hat Ansible Automation
  Platform. Using a retrieval augmented generation (RAG) pipeline connected to Red
  Hat documentation and other trusted resources, the intelligent assistant allows
  administrators to use natural language prompts to help them manage and troubleshoot
  Ansible Automation Platform without leaving the platform UI.'
summary: 'Bring your own knowledge to the automation intelligent assistant Automation
  intelligence made more relevant Custom knowledge in practice Getting started and
  additional resources Red Hat Ansible Automation Platform | Product Trial About the
  author Tricia McConnell More like this Securing the enterprise software fabric:
  A blueprint for open source Scaling automated infrastructure compliance in telecommunications
  using Red Hat Ansible Automation Platform Operating System Management | Compiler
  Technically Speaking | Inside open source AI strategy Keep exploring Browse by channel
  Automation Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share Last year, we released the automation intelligent
  assistant (formerly Red Hat Ansible Lightspeed intelligent assistant), a generative
  AI service accessed through a chatbot embedded within Red Hat Ansible Automation
  Platform. Using a retrieval augmented generation (RAG) pipeline connected to Red
  Hat documentation and other trusted resources, the intelligent assistant allows
  administrators to use natural language prompts to help them manage and troubleshoot
  Ansible Automation Platform without leaving the platform UI. The automation intelligent
  assistant in the Red Hat Ansible Automation Platform UI The intelligent assistant
  can respond with transparency to prompts such as: What is an automation execution
  environment? How do I manage user access to Ansible Automation Platform? How do
  I configure Event-Driven Ansible? What''s in the release notes for Ansible Automation
  Platform 2.7? But what happens when your organization''s internal policies and procedures
  require additional steps or actions that are distinct from Red Hat''s more generalized
  recommendations? With the release of Ansible Automation Platform 2.7, you can now
  store proprietary data into the intelligent assistant''s RAG pipeline for model
  responses that reflect your organization''s unique operational requirements and
  best practices. By storing a custom knowledge base, you can prioritize your own
  documentation (policies, manuals, FAQs) in the models'' recommendations. Red Hat''s
  documentation becomes a secondary priority or supplies responses where enterprise
  specific-guidance is not available. This ability to apply custom knowledge to the
  intelligent assistant allows you to centralize critical and trusted documentation
  in one place, which reduces context switching and encourages adherence to your organization''s
  internal policies and preferences. As part of the release preparation for Ansible
  Automation Platform 2.7 , our engineers ran an internal test-a-thon with scenarios
  that clearly illustrate the value of storing custom knowledge. In this case, the
  "bring your own knowledge" image contained documentation for a fictional organization
  complete with custom naming conventions, approval workflows, and escalation procedures.
  Here''s how the intelligent assistant''s responses compared: Test Prompt Without
  custom knowledge With custom knowledge "How should I name my roles?" Displays Ansible
  syntax requirements and recommended best practices such as avoiding uppercase letters.
  Requires mycompany_ prefix, an organizational standard that, if missing, is flagged
  in code review. mycompany_ "How do I name inventory groups?" Provides suggestions
  such as " webservers "or " dbservers "; guidance to avoid spaces and hyphens. webservers
  dbservers Returns the mycompany_<env>_<tier> pattern used by organization.'
---
Open the original post ↗ https://www.redhat.com/en/blog/bring-your-own-knowledge-automation-intelligent-assistant
