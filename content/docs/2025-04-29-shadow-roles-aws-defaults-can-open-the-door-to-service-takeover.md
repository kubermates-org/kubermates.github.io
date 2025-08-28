---
title: 'Shadow Roles: AWS Defaults Can Open the Door to Service Takeover'
date: '2025-04-29T16:16:07+00:00'
tags:
- security
source: Aqua Security
external_url: https://blog.aquasec.com/shadow-roles-aws-defaults-lead-to-service-takeover
post_kind: link
draft: false
tldr: Our research uncovered security concerns in the deployment of resources within
  a few AWS services, specifically in the default AWS service roles. These roles,
  often created automatically or recommended during setup, grant overly broad permissions,
  such as full S3 access.
summary: 'Our research uncovered security concerns in the deployment of resources
  within a few AWS services, specifically in the default AWS service roles. These
  roles, often created automatically or recommended during setup, grant overly broad
  permissions, such as full S3 access. These default roles silently introduce attack
  paths that allow privilege escalation, cross-service access, and even potential
  account compromise. Security Threats (120) Container Security (118) Kubernetes Security
  (97) Cloud Native Security (84) Aqua Open Source (49) Image Vulnerability Scanning
  (49) AWS Security (38) Runtime Security (38) Aqua Security (37) Vulnerability Management
  (36) Docker Security (35) Software Supply Chain Security (29) CSPM (28) Cloud compliance
  (25) DevSecOps (25) Container Vulnerability (24) CI/CD (17) CNAPP (17) Supply Chain
  Attacks (13) Secrets (12) Application Security (11) Serverless-Security (11) Kubernetes
  (10) ebpf (10) Cloud security (9) Host Security (9) Advanced malware protection
  (8) Cloud security conferences (8) Fargate (8) Hybrid Cloud Security (8) Malware
  Attacks (8) Cloud Workload Protection Platform CWPP (7) Attack Vector (6) Container
  platforms (6) Google cloud security (6) OpenShift (6) SBOMs (6) Secure VM (6) Security
  Policy (6) Infrastructure-as-Code (IaC) (5) Security Automation (5) Windows Containers
  (5) Azure security (4) Docker containers (4) Kubernetes RBAC (4) Service Mesh (4)
  Container Deployment (3) IBM Cloud (3) Microservices (3) Nano-Segmentation (3) Agentless
  Security (2) FaaS (2) Network Firewall (2) VMware Tanzu (2) code security (2) Advanced
  Threat Mitigation (1) Cloud VM (1) Customer Support (1) Drift Prevention (1) Kubernetes
  Authorization (1) Network (1) shift Left security (1) Aqua Security is the largest
  pure-play cloud native security company, providing customers the freedom to innovate
  and accelerate their digital transformations. The Aqua Platform is the leading Cloud
  Native Application Protection Platform (CNAPP) and provides prevention, detection,
  and response automation across the entire application lifecycle to secure the supply
  chain, secure cloud infrastructure and secure running workloads wherever they are
  deployed. Aqua customers are among the world’s largest enterprises in financial
  services, software, media, manufacturing and retail, with implementations across
  a broad range of cloud providers and modern technology stacks spanning containers,
  serverless functions and cloud VMs. Automate DevSecOps Modernize Security Compliance
  and Auditing Serverless Containers & Functions Hybrid and Multi Cloud Kubernetes
  Security OpenShift Security Docker Security AWS Cloud Security Azure Cloud Security
  Google Cloud Security VMware PKS Security Contact Us Contact Support Aqua Cloud
  native security Open Source Container Security Platform Integrations Live Webinars
  O’Reilly Book: Kubernetes Security Cloud native Wiki About Aqua Newsroom Careers.'
---
Open the original post ↗ https://blog.aquasec.com/shadow-roles-aws-defaults-lead-to-service-takeover
