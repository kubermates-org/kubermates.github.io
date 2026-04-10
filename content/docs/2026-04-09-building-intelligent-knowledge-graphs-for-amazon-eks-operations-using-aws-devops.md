---
title: Building intelligent knowledge graphs for Amazon EKS operations using AWS DevOps
  Agent
date: '2026-04-09T18:26:10+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/building-intelligent-knowledge-graphs-for-amazon-eks-operations-using-aws-devops-agent/
post_kind: link
draft: false
tldr: 'Building intelligent knowledge graphs for Amazon EKS operations using AWS DevOps
  Agent Prerequisites Deploy a sample retail application Enabling AWS DevOps Agent
  access for Amazon EKS cluster Step 1: Getting DevOps Agent’s webhook information
  Step 2: Deploy Conclusion Further reading About the authors Modern observability
  has evolved significantly with the emergence of AIOps, transforming how organizations
  monitor and maintain their cloud infrastructure. Today’s intelligent agents can
  seamlessly integrate with monitoring tools, knowledge bases, and ticketing systems
  to triage issues and propose mitigation steps with unprecedented speed.'
summary: 'Building intelligent knowledge graphs for Amazon EKS operations using AWS
  DevOps Agent Prerequisites Deploy a sample retail application Enabling AWS DevOps
  Agent access for Amazon EKS cluster Step 1: Getting DevOps Agent’s webhook information
  Step 2: Deploy Conclusion Further reading About the authors Modern observability
  has evolved significantly with the emergence of AIOps, transforming how organizations
  monitor and maintain their cloud infrastructure. Today’s intelligent agents can
  seamlessly integrate with monitoring tools, knowledge bases, and ticketing systems
  to triage issues and propose mitigation steps with unprecedented speed. Despite
  these advances, reducing Mean Time to Identify (MTTI) and Mean Time to Resolve (MTTR)
  in complex microservices architectures remains a challenge. During a recent conversation
  with a customer running a sophisticated AIOps platform for Kubernetes operations,
  they expressed a familiar concern: while their tooling was powerful, identifying
  the true root cause of incidents was still remarkably difficult. Pod-to-pod communication
  creates a constantly shifting network topology that’s challenging to map and understand
  without relying on third-party providers or eBPF profiling. This adds operational
  overhead and complexity to an already demanding troubleshooting process. This is
  where AWS DevOps Agent changes the game. It goes beyond collecting insights from
  telemetry signals to build intelligent knowledge graphs that map the intricate relationships
  between your Amazon Elastic Kubernetes Service (Amazon EKS) resources. AWS DevOps
  Agent acts as your always-on DevOps engineer, autonomously investigating incidents
  and identifying operational improvements by learning your resources and their relationships.
  It works with your existing observability tools, runbooks, code repositories, and
  continuous integration and delivery (CI/CD) pipelines, correlating telemetry, code,
  and deployment data to understand the true topology of your applications—whether
  they run in the cloud or hybrid environments. For Amazon EKS specifically, the agent
  goes beyond cluster-level visibility, developing a deep understanding of Kubernetes
  objects and their interdependencies, from Services to Pods. This enables it to traverse
  dependency chains and pinpoint the deepest impaired object that’s likely causing
  your incident.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/building-intelligent-knowledge-graphs-for-amazon-eks-operations-using-aws-devops-agent/
