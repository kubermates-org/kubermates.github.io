---
title: 'SAS Viya Platform with Red Hat OpenShift – Part 1: Reference Architecture
  and Deployment Considerations'
date: '2026-03-24T00:00:00+00:00'
tags:
- openshift
source: OpenShift Blog
external_url: https://www.redhat.com/en/blog/sas-viya-on-red-hat-openshift-part-1-reference-architecture-and-deployment-considerations
post_kind: link
draft: false
tldr: 'SAS Viya Platform with Red Hat OpenShift – Part 1: Reference Architecture and
  Deployment Considerations SAS Viya platform on OpenShift reference architecture
  SAS Cloud Analytic Services (CAS) (CAS NODE POOL) SAS Compute Services (COMPUTE
  NODE POOL) SAS Microservices and Web Applications (STATELESS NODE POOL) Infrastructure
  Services (STATEFUL NODE POOL) Core Platform Deployment Options – Red Hat OpenShift
  Deployment Options – SAS Viya Platform 1. Manual Deployment 2.'
summary: 'SAS Viya Platform with Red Hat OpenShift – Part 1: Reference Architecture
  and Deployment Considerations SAS Viya platform on OpenShift reference architecture
  SAS Cloud Analytic Services (CAS) (CAS NODE POOL) SAS Compute Services (COMPUTE
  NODE POOL) SAS Microservices and Web Applications (STATELESS NODE POOL) Infrastructure
  Services (STATEFUL NODE POOL) Core Platform Deployment Options – Red Hat OpenShift
  Deployment Options – SAS Viya Platform 1. Manual Deployment 2. SAS Deployment Operator
  3. sas-orchestration Utility SAS Viya Platform Deployment From A Process Perspective
  Conclusion About the authors Patrick Farley Hans-Joachim Edert More like this Modernize
  virtual machines on Google Cloud with Red Hat OpenShift Virtualization From experiment
  to production: A reliable architecture for version-controlled MLOps Technically
  Speaking | Build a production-ready AI toolbox Technically Speaking | Platform engineering
  for AI agents Browse by channel Automation Artificial intelligence Open hybrid cloud
  Security Edge computing Infrastructure Applications Virtualization Share In this
  two-part blog, we will provide essential technical information about SAS Institute''s
  SAS Viya platform, as well as a reference architecture for deploying SAS Viya on
  Red Hat OpenShift. Also, make sure to take a look at part 2 of this blog , where
  we will discuss security, machine management and storage considerations. Let’s start
  with a few introductory words before we get into the technical details. Since the
  launch of the SAS Viya platform in 2020, SAS has offered a fully containerized analytic
  platform based on a cloud-native architecture. Due to the scale of the platform,
  SAS Viya requires Kubernetes as an underlying runtime environment and takes full
  advantage of the native benefits of this technology. SAS supports numerous Kubernetes
  distributions, both in the public and private cloud. In fact, many SAS customers
  - partly due to specific use cases that do not allow otherwise from a regulatory
  perspective, but also due to strategic considerations - prefer to run their application
  infrastructure in a private cloud environment. In these cases, OpenShift provides
  a solid foundation for the SAS software stack. OpenShift offers both a hardened
  Kubernetes with many highly valued enterprise features as an execution platform,
  but also comes with an extensive ecosystem with a particular focus on supporting
  DevSecOps capabilities.'
---
Open the original post ↗ https://www.redhat.com/en/blog/sas-viya-on-red-hat-openshift-part-1-reference-architecture-and-deployment-considerations
