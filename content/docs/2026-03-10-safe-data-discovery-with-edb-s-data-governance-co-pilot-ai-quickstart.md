---
title: Safe data discovery with EDB's Data Governance Co-Pilot AI quickstart
date: '2026-03-10T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/safe-data-discovery-edbs-data-governance-co-pilot-ai-quickstart
post_kind: link
draft: false
tldr: 'Safe data discovery with EDB''s Data Governance Co-Pilot AI quickstart Retrieval-augmented
  generation (RAG) with privacy Governance policies as filters An air-gapped cloud
  native stack "Restricted Mode" by default Fast time-to-insight Final takeaway Red
  Hat AI About the authors Giri Venkataraman Shane Heroux Bilge Ince Peter Samouelian
  More like this Enable intelligent insights with Red Hat Satellite MCP Server AI
  quickstart: Protecting inference with F5 Distributed Cloud and Red Hat AI Technically
  Speaking | Build a production-ready AI toolbox Technically Speaking | Platform engineering
  for AI agents Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share When Red Hat revealed our AI quickstarts , EDB suggested a use case to balance
  the business need for data with the non-negotiable demand for governance. We often
  treat this as a zero-sum game, but what if the architecture itself could negotiate
  peace? This Data Governance Co-Pilot AI quickstart , built on Red Hat OpenShift
  AI and EDB Postgres AI (PGAI) platform, treats safe data discovery as a requirement.'
summary: 'Safe data discovery with EDB''s Data Governance Co-Pilot AI quickstart Retrieval-augmented
  generation (RAG) with privacy Governance policies as filters An air-gapped cloud
  native stack "Restricted Mode" by default Fast time-to-insight Final takeaway Red
  Hat AI About the authors Giri Venkataraman Shane Heroux Bilge Ince Peter Samouelian
  More like this Enable intelligent insights with Red Hat Satellite MCP Server AI
  quickstart: Protecting inference with F5 Distributed Cloud and Red Hat AI Technically
  Speaking | Build a production-ready AI toolbox Technically Speaking | Platform engineering
  for AI agents Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share When Red Hat revealed our AI quickstarts , EDB suggested a use case to balance
  the business need for data with the non-negotiable demand for governance. We often
  treat this as a zero-sum game, but what if the architecture itself could negotiate
  peace? This Data Governance Co-Pilot AI quickstart , built on Red Hat OpenShift
  AI and EDB Postgres AI (PGAI) platform, treats safe data discovery as a requirement.
  It provides a protected workspace where any data consumer can navigate complex schemas
  and extract insights with less risk of tripping compliance wires. The real governance
  challenge with agentic AI isn''t just what the large language model (LLM) knows,
  it''s what it can do. Agents with direct database access can execute queries autonomously,
  bypass access controls, and return raw personally identifiable information (PII)
  to the chat interface. The architecture needs to make compliant behavior the only
  possible behavior. The AI quickstart is built on pg-airman-mcp , EDB''s open source
  Model Context Protocol (MCP) server for Postgres integrated with PGAI. It uses agentic
  tool calling to Postgres for an innovative safeguard—an analytics tool that merges
  static data governance policies with a natural language query interface. This means
  that policies concerning data privacy, confidentiality, and data timeliness become
  an active filter directly embedded within the analyst''s tooling and workflow. User
  queries are processed through an uploaded governance policy and the LLM to generate
  policy-compliant SQL statements, preventing data leakage to the chat interface.
  By handling masking at the SQL level, this prevents the LLM from accessing the raw
  data payload. Usually, data governance policies are static documents.'
---
Open the original post ↗ https://www.redhat.com/en/blog/safe-data-discovery-edbs-data-governance-co-pilot-ai-quickstart
