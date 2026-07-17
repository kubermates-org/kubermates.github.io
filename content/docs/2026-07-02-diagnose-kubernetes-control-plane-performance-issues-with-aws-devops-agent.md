---
title: Diagnose Kubernetes Control Plane Performance Issues with AWS DevOps Agent
date: '2026-07-02T17:03:59+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/diagnose-kubernetes-control-plane-performance-issues-with-aws-devops-agent/
post_kind: link
draft: false
tldr: 'Diagnose Kubernetes Control Plane Performance Issues with AWS DevOps Agent
  What is AWS DevOps Agent? Infrastructure setup Prerequisites Clone the repository
  Provision an EKS Auto Mode cluster Configure AWS DevOps Agent Scenario: Diagnosing
  API server overload and 429 throttling The challenge How the simulation works Scenario
  preparation Troubleshooting with AWS DevOps Agent Recovery Cleanup Why this matters:
  The APF transparency problem Improvements Conclusion About the authors This post
  demonstrates how AWS DevOps Agent diagnoses Amazon Elastic Kubernetes Service (Amazon
  EKS) API server performance degradation, specifically 429 throttling and API Priority
  and Fairness (APF) seat exhaustion. A realistic simulation introduces a misbehaving
  controller that floods the API server with excessive requests.'
summary: 'Diagnose Kubernetes Control Plane Performance Issues with AWS DevOps Agent
  What is AWS DevOps Agent? Infrastructure setup Prerequisites Clone the repository
  Provision an EKS Auto Mode cluster Configure AWS DevOps Agent Scenario: Diagnosing
  API server overload and 429 throttling The challenge How the simulation works Scenario
  preparation Troubleshooting with AWS DevOps Agent Recovery Cleanup Why this matters:
  The APF transparency problem Improvements Conclusion About the authors This post
  demonstrates how AWS DevOps Agent diagnoses Amazon Elastic Kubernetes Service (Amazon
  EKS) API server performance degradation, specifically 429 throttling and API Priority
  and Fairness (APF) seat exhaustion. A realistic simulation introduces a misbehaving
  controller that floods the API server with excessive requests. AWS DevOps Agent
  then autonomously identifies the offending workload, correlates Amazon CloudWatch
  audit logs with throttling patterns, and recommends targeted remediation to restore
  cluster stability. Managing production incidents in Amazon EKS environments presents
  unique challenges for DevOps and site reliability engineering (SRE) teams. When
  incidents occur, on-call engineers must simultaneously investigate root causes across
  distributed systems while providing timely updates to stakeholders. This process
  often involves correlating data from multiple observability sources, examining recent
  deployment changes, and orchestrating cross-functional response teams, frequently
  outside normal business hours. AWS DevOps Agent is an AI-powered operations assistant
  that autonomously investigates incidents, correlates signals across your infrastructure,
  and delivers actionable root cause analysis with recommended remediations. For a
  full overview, see the launch announcement. For Amazon EKS environments, the agent
  extends the following capabilities: Key capabilities for EKS environments: Autonomous
  incident investigation : Automatically begins investigating incidents when alerts
  are triggered, reducing Mean Time to Resolution (MTTR). EKS-specific insights :
  Direct integration with Amazon EKS clusters for introspection of cluster states,
  pod logs, and cluster events. Amazon CloudWatch log analysis : Queries Amazon CloudWatch
  Logs Insights to analyze EKS audit logs, identifying throttled requests and the
  workloads responsible. Multi-tool integration : Connects with observability tools,
  continuous integration and continuous delivery (CI/CD) pipelines, and communication
  platforms for comprehensive data correlation.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/diagnose-kubernetes-control-plane-performance-issues-with-aws-devops-agent/
