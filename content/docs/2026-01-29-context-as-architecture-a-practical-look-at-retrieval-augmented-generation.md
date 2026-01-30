---
title: 'Context as architecture: A practical look at retrieval-augmented generation'
date: '2026-01-29T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/context-architecture-practical-look-retrieval-augmented-generation
post_kind: link
draft: false
tldr: 'Context as architecture: A practical look at retrieval-augmented generation
  From conversation to context RAG as a system, not a feature Why retrieval is harder
  than it looks Why enterprises adopt RAG anyway Where RAG stops Looking ahead The
  adaptable enterprise: Why AI readiness is disruption readiness About the authors
  Frank La Vigne Robbie Jerrom More like this Sovereign AI architecture: Scaling distributed
  training with Kubeflow Trainer and Feast on Red Hat OpenShift AI AI quickstarts:
  An easy and practical way to get started with Red Hat AI Technically Speaking |
  Build a production-ready AI toolbox Technically Speaking | Platform engineering
  for AI agents Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share In a previous article, The strategic choice: Making sense of LLM customization
  , we explored AI prompting as the first step in adapting large language models (LLMs)
  to real-world use. Prompting changes how an AI model responds in terms of tone,
  structure, and conversational behavior without changing what the model knows.'
summary: 'Context as architecture: A practical look at retrieval-augmented generation
  From conversation to context RAG as a system, not a feature Why retrieval is harder
  than it looks Why enterprises adopt RAG anyway Where RAG stops Looking ahead The
  adaptable enterprise: Why AI readiness is disruption readiness About the authors
  Frank La Vigne Robbie Jerrom More like this Sovereign AI architecture: Scaling distributed
  training with Kubeflow Trainer and Feast on Red Hat OpenShift AI AI quickstarts:
  An easy and practical way to get started with Red Hat AI Technically Speaking |
  Build a production-ready AI toolbox Technically Speaking | Platform engineering
  for AI agents Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share In a previous article, The strategic choice: Making sense of LLM customization
  , we explored AI prompting as the first step in adapting large language models (LLMs)
  to real-world use. Prompting changes how an AI model responds in terms of tone,
  structure, and conversational behavior without changing what the model knows. That
  strategy is effective until the model requires specific information it did not encounter
  during its initial training. At that point, the limitation is no longer conversational—it
  is architectural. Retrieval-augmented generation (RAG) helps address that limitation.
  Not by making models smarter, but by changing the systems they operate within. Prompting
  shapes behavior. It influences how a model reasons and responds, but it does not
  expand the model’s knowledge. LLMs are trained on broad, mostly public datasets
  that are frozen in time and detached from any single organization’s internal reality.
  As long as an application can tolerate that gap, prompting may be enough. Once an
  application depends on current documentation, internal policies, proprietary data,
  or rapidly evolving domain knowledge, however, prompting alone begins to fail. Prompts
  grow longer.'
---
Open the original post ↗ https://www.redhat.com/en/blog/context-architecture-practical-look-retrieval-augmented-generation
