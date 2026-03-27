---
title: 'AI security: Defending against prompt injection and unsafe actions'
date: '2026-03-26T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/ai-security-defending-against-prompt-injection-and-unsafe-actions
post_kind: link
draft: false
tldr: 'AI security: Defending against prompt injection and unsafe actions What is
  prompt injection and why does it work? What are AI guardrails? Input guardrails
  Output guardrails Runtime guardrails RAG defenses: treat retrieved data as hostile
  Security architectures that can help Dual LLM generator and critic model Capability
  mediation What guardrails should enforce beyond “bad content” Testing guardrails
  like a product security team Final thoughts Red Hat AI About the authors Juan Pérez
  de Algaba Sierra Florencio Cano Gabarda More like this From experiment to production:
  A reliable architecture for version-controlled MLOps Mapping the AI attack surface:
  Vulnerabilities in the model lifecycle Keeping Track Of Vulnerabilities With CVEs
  | Compiler Post-quantum Cryptography | Compiler Keep exploring Browse by channel
  Automation Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share In previous articles, we framed AI security as
  protecting confidentiality, integrity, and availability of the whole AI system,
  not just the model. We also mapped AI risks onto familiar secure development lifecycle
  (SDLC) thinking, treating data and model artifacts as first-class build inputs and
  outputs.'
summary: 'AI security: Defending against prompt injection and unsafe actions What
  is prompt injection and why does it work? What are AI guardrails? Input guardrails
  Output guardrails Runtime guardrails RAG defenses: treat retrieved data as hostile
  Security architectures that can help Dual LLM generator and critic model Capability
  mediation What guardrails should enforce beyond “bad content” Testing guardrails
  like a product security team Final thoughts Red Hat AI About the authors Juan Pérez
  de Algaba Sierra Florencio Cano Gabarda More like this From experiment to production:
  A reliable architecture for version-controlled MLOps Mapping the AI attack surface:
  Vulnerabilities in the model lifecycle Keeping Track Of Vulnerabilities With CVEs
  | Compiler Post-quantum Cryptography | Compiler Keep exploring Browse by channel
  Automation Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share In previous articles, we framed AI security as
  protecting confidentiality, integrity, and availability of the whole AI system,
  not just the model. We also mapped AI risks onto familiar secure development lifecycle
  (SDLC) thinking, treating data and model artifacts as first-class build inputs and
  outputs. This article examines the primary security risk for enterprise large language
  model (LLM) applications: prompt injection. This vulnerability occurs when the model
  fails to distinguish between data and instructions, allowing external prompts to
  seize control of the system. The risk is particularly acute when models use retrieval-augmented
  generation (RAG) to access documents or employ tools to take autonomous actions.
  We will explore how to test these applications to minimize the possibility that
  prompt injection results in a security incident. Prompt injection is a security
  vulnerability where an AI model is tricked into executing unauthorized instructions
  by a malicious actor. This occurs because LLMs currently process both developer
  instructions and user data as a single stream of text, with no architectural way
  to distinguish between what to do and what to process. Prompt injection is best
  understood as an instruction-confusion bug: The system ingests untrusted data like
  user input, retrieved documents, tickets, emails, and web pages. The model is asked
  to follow instructions in that text. The model cannot distinguish policy from content
  unless you enforce boundaries. In other words, prompt injection succeeds when your
  system treats external content as if it were a trusted control input.'
---
Open the original post ↗ https://www.redhat.com/en/blog/ai-security-defending-against-prompt-injection-and-unsafe-actions
