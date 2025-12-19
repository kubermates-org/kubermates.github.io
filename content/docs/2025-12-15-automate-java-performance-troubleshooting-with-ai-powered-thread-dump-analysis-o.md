---
title: Automate java performance troubleshooting with AI-Powered thread dump analysis
  on Amazon ECS and EKS
date: '2025-12-15T18:57:47+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/automate-java-performance-troubleshooting-with-ai-powered-thread-dump-analysis-on-amazon-ecs-and-eks/
post_kind: link
draft: false
tldr: 'Automate java performance troubleshooting with AI-Powered thread dump analysis
  on Amazon ECS and EKS Overview of the solution Prerequisites Walkthrough Step 1:
  Deploying the base infrastructure Step 2: Setting up container environment and deploy
  the monitoring and analysis stack Implementation details Design principles JMX metrics
  with Spring Boot Automated thread dump collection via Grafana webhook AI-powered
  analysis with Amazon Bedrock Triggering a thread dump analysis Example Analysis
  Output Cleaning up Conclusion About the authors Picture this: your containerized
  Java application that was running smoothly yesterday is now consuming 90% CPU and
  barely responding to user requests. Now your customers are experiencing timeouts,
  and your ops team is under pressure to resolve the issue quickly.'
summary: 'Automate java performance troubleshooting with AI-Powered thread dump analysis
  on Amazon ECS and EKS Overview of the solution Prerequisites Walkthrough Step 1:
  Deploying the base infrastructure Step 2: Setting up container environment and deploy
  the monitoring and analysis stack Implementation details Design principles JMX metrics
  with Spring Boot Automated thread dump collection via Grafana webhook AI-powered
  analysis with Amazon Bedrock Triggering a thread dump analysis Example Analysis
  Output Cleaning up Conclusion About the authors Picture this: your containerized
  Java application that was running smoothly yesterday is now consuming 90% CPU and
  barely responding to user requests. Now your customers are experiencing timeouts,
  and your ops team is under pressure to resolve the issue quickly. When debugging
  unresponsive applications or excessive CPU consumption, one of the most valuable
  diagnostic tools available is the thread dump. A thread dump provides a snapshot
  of the threads in a Java Virtual Machine (JVM) at a specific moment, revealing thread
  states, stack traces, and lock information. While thread dumps are essential for
  diagnosing complex performance issues, traditional thread dump analysis presents
  several challenges. Analyzing thread dumps requires deep JVM expertise. In many
  teams, only a handful of engineers know how to interpret them, which slows down
  troubleshooting. Manual analysis can also be time‑consuming, taking hours, if not
  days to sift through, especially with hundreds of threads. Furthermore, this reactive
  approach only identifies issues after degradation has already occurred, potentially
  impacting your customers. Generative AI can make proactive, expert-level troubleshooting
  faster and more straightforward for developers and operations teams. In this blog,
  we’ll walk through how to build an automated thread dump analysis pipeline that
  uses Prometheus for monitoring, Grafana for alerting, AWS Lambda for orchestration,
  and Amazon Bedrock for AI‑powered analysis. The solution works on both Amazon Elastic
  Container Servics (Amazon ECS ) and Amazon Elastic Kubernetes Service (Amazon EKS
  ), helping teams go from raw thread dumps to actionable insights within seconds
  of detecting an issue.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/automate-java-performance-troubleshooting-with-ai-powered-thread-dump-analysis-on-amazon-ecs-and-eks/
