---
title: 'Mapping the AI attack surface: Vulnerabilities in the model lifecycle'
date: '2026-03-25T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/mapping-ai-attack-surface-vulnerabilities-model-lifecycle
post_kind: link
draft: false
tldr: 'Mapping the AI attack surface: Vulnerabilities in the model lifecycle The model
  lifecycle as an attack surface—where attackers enter Mapping model phases to familiar
  SDLC phases Training-time attacks Data poisoning Backdoors (trojans) Post-training
  model theft Model extraction: stealing functionality through prediction APIs Privacy
  attacks - training data risk Membership inference: "Was this record in the training
  data?" Training data extraction and memorization - especially for LLMs What you
  can do now Poisoning / backdoors Extraction Privacy Conclusion Red Hat AI About
  the author Juan Pérez de Algaba Sierra More like this From experiment to production:
  A reliable architecture for version-controlled MLOps AI security: Defending against
  prompt injection and unsafe actions Technically Speaking | Build a production-ready
  AI toolbox Technically Speaking | Platform engineering for AI agents Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share Standard AI security
  benchmarks can''t check for all of the possible ways an AI model can be compromised.
  A backdoor trigger could cause targeted failure, a competitor could clone your API
  model through repeated queries, or a privacy probe might reveal whether a specific
  person’s data was used in training.'
summary: 'Mapping the AI attack surface: Vulnerabilities in the model lifecycle The
  model lifecycle as an attack surface—where attackers enter Mapping model phases
  to familiar SDLC phases Training-time attacks Data poisoning Backdoors (trojans)
  Post-training model theft Model extraction: stealing functionality through prediction
  APIs Privacy attacks - training data risk Membership inference: "Was this record
  in the training data?" Training data extraction and memorization - especially for
  LLMs What you can do now Poisoning / backdoors Extraction Privacy Conclusion Red
  Hat AI About the author Juan Pérez de Algaba Sierra More like this From experiment
  to production: A reliable architecture for version-controlled MLOps AI security:
  Defending against prompt injection and unsafe actions Technically Speaking | Build
  a production-ready AI toolbox Technically Speaking | Platform engineering for AI
  agents Keep exploring Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share Standard AI security benchmarks can''t check for all of the possible ways
  an AI model can be compromised. A backdoor trigger could cause targeted failure,
  a competitor could clone your API model through repeated queries, or a privacy probe
  might reveal whether a specific person’s data was used in training. For this reason,
  organizations deploying AI must understand the variety of potential attacks and
  proactively address them during model training and after deployment. In our previous
  article, What does "AI security" mean and why does it matter to your business?,
  we talked about protecting AI systems from attacks that compromise confidentiality,
  integrity, and availability. In this article, we focus on attacks that target the
  model—both during training and after deployment. Models have a lifecycle similar
  to software, but instead of replacing the usual software process, they extend it.
  In a traditional secure development lifecycle (SDLC), teams protect code, dependencies,
  build pipelines, and deployments. With an AI system, you still must do all of that,
  but you also have data pipelines and learning artifacts that behave like first-class
  "build inputs" and "build outputs. " The Red Hat SDLC extends naturally to AI. It
  treats datasets as build inputs and model weights as build outputs that require
  the same checks for provenance, signing, and verification. A helpful way to think
  about it is: SDLC still applies : Source code security, dependency/supply chain
  controls, CI/CD hardening, secrets management, infrastructure security, and runtime
  monitoring. Model lifecycle is the AI-specific layer added on top : The "build inputs"
  now include datasets and labels, and the "build outputs" now include checkpoints,
  adapters, and evaluation artifacts.'
---
Open the original post ↗ https://www.redhat.com/en/blog/mapping-ai-attack-surface-vulnerabilities-model-lifecycle
