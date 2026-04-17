---
title: 'Announcing Red Hat OpenShift Pipelines 1.21: Faster builds, smarter caching,
  and improved troubleshooting'
date: '2026-04-15T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/announcing-red-hat-openshift-pipelines-121-faster-builds-smarter-caching-and-improved-troubleshooting
post_kind: link
draft: false
tldr: 'Announcing Red Hat OpenShift Pipelines 1.21: Faster builds, smarter caching,
  and improved troubleshooting AI-assisted pipeline troubleshooting with Red Hat OpenShift
  Lightspeed Tekton Cache is now generally available Resolver caching for faster pipeline
  execution More control with taskRun timeout overrides Security improvements for
  pipeline components Improvements in Pipelines as Code and console experience Conclusion
  The adaptable enterprise: Why AI readiness is disruption readiness About the authors
  Jaafar Chraibi Jawed Khelil More like this AI optimization: 7 powerful techniques
  you can use today! 233% 3-year return on investment and 13 months to payback with
  Red Hat AI Technically Speaking | Build a production-ready AI toolbox Technically
  Speaking | Platform engineering for AI agents Keep exploring Browse by channel Automation
  Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share Red Hat OpenShift Pipelines 1.21 is now available,
  improving pipeline performance, security capabilities, and troubleshooting for Kubernetes-native
  continuous integration and delivery (CI/CD) on Red Hat OpenShift. This release introduces
  AI-assisted troubleshooting via Red Hat OpenShift Lightspeed and moves Tekton Cache
  to general availability.'
summary: 'Announcing Red Hat OpenShift Pipelines 1.21: Faster builds, smarter caching,
  and improved troubleshooting AI-assisted pipeline troubleshooting with Red Hat OpenShift
  Lightspeed Tekton Cache is now generally available Resolver caching for faster pipeline
  execution More control with taskRun timeout overrides Security improvements for
  pipeline components Improvements in Pipelines as Code and console experience Conclusion
  The adaptable enterprise: Why AI readiness is disruption readiness About the authors
  Jaafar Chraibi Jawed Khelil More like this AI optimization: 7 powerful techniques
  you can use today! 233% 3-year return on investment and 13 months to payback with
  Red Hat AI Technically Speaking | Build a production-ready AI toolbox Technically
  Speaking | Platform engineering for AI agents Keep exploring Browse by channel Automation
  Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share Red Hat OpenShift Pipelines 1.21 is now available,
  improving pipeline performance, security capabilities, and troubleshooting for Kubernetes-native
  continuous integration and delivery (CI/CD) on Red Hat OpenShift. This release introduces
  AI-assisted troubleshooting via Red Hat OpenShift Lightspeed and moves Tekton Cache
  to general availability. It also features several updates designed to enhance pipeline
  speed, reliability, and ease of use. This blog post will explore several key highlights
  of OpenShift Pipelines 1.21. OpenShift Pipelines 1.21 integrates with Red Hat OpenShift
  Lightspeed to enable AI-assisted troubleshooting directly from the OpenShift console.
  When a pipeline fails, developers often need to inspect logs and pipeline resources
  to determine the root cause. Red Hat OpenShift Lightspeed analyzes the context of
  failed PipelineRun and TaskRun executions and provides AI-generated explanations
  and remediation guidance based on logs and events. This helps developers quickly
  understand what went wrong and how to fix it, reducing the time spent manually investigating
  failures. PipelineRun TaskRun The introduction of the command line “opc assist pipelinerun
  diagnose” also allows users to interact with OpenShift Lightspeed from a terminal.
  Explore the interactive demo for more information. Image 1: Troubleshooting a failed
  pipeline using OpenShift Lightspeed Tekton Cache is generally available with OpenShift
  Pipelines 1.21, enabling pipelines to reuse dependencies and build artifacts across
  runs. By storing cached data in Open Container Initiative (OCI) registries, teams
  can avoid repeatedly downloading dependencies or rebuilding unchanged artifacts.'
---
Open the original post ↗ https://www.redhat.com/en/blog/announcing-red-hat-openshift-pipelines-121-faster-builds-smarter-caching-and-improved-troubleshooting
