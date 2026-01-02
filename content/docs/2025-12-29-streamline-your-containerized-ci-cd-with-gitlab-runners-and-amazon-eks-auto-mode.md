---
title: Streamline your containerized CI/CD with GitLab Runners and Amazon EKS Auto
  Mode
date: '2025-12-29T15:22:33+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/streamline-your-containerized-ci-cd-with-gitlab-runners-and-amazon-eks-auto-mode/
post_kind: link
draft: false
tldr: Streamline your containerized CI/CD with GitLab Runners and Amazon EKS Auto
  Mode Solution overview Prerequisites Walkthrough Configuration files Get started
  Policies Cleaning up Conclusion About the authors Although Kubernetes offers scalability
  for GitLab Runner deployments, the operational overhead can’t be ignored. Organizations
  starting with containerized continuous integration/continuous development (CI/CD)
  without mature container practices often underestimate both the financial implications
  and security complexities.
summary: Streamline your containerized CI/CD with GitLab Runners and Amazon EKS Auto
  Mode Solution overview Prerequisites Walkthrough Configuration files Get started
  Policies Cleaning up Conclusion About the authors Although Kubernetes offers scalability
  for GitLab Runner deployments, the operational overhead can’t be ignored. Organizations
  starting with containerized continuous integration/continuous development (CI/CD)
  without mature container practices often underestimate both the financial implications
  and security complexities. The true Total Cost of Ownership (TCO) extends far beyond
  the initial infrastructure provisioning, demanding meticulous architectural decisions
  that balance scale, cost efficiency, and security posture. To navigate these complexities
  successfully, enterprises need a managed solution that abstracts the operational
  burden. Amazon Elastic Kubernetes Service (Amazon EKS) provides a robust platform
  for container orchestration. With the introduction of Amazon EKS Auto Mode , the
  management of Kubernetes clusters has been streamlined by automatically provisioning
  infrastructure, choosing optimal compute instances, dynamically scaling resources,
  continually optimizing compute for costs, patching operating systems (OS), and integrating
  with AWS security services. In this post we demonstrate how using GitLab Runners
  on EKS Auto Mode, combined with Amazon Elastic Compute Cloud (Amazon EC2) Spot Instances
  , can deliver enterprise-scale CI/CD capabilities while achieving up to 90% cost
  reduction when compared to traditional deployment models. This approach not only
  optimizes operational expenses, but also provides resilient, scalable pipeline execution.
  This solution implements a production-ready GitLab Runner deployment on EKS Auto
  Mode, using infrastructure as code (IaC) best practices, as shown in the following
  figure. It uses Amazon EC2 Spot Instance fleet management for optimal cost-performance
  ratio, while implementing comprehensive security controls through predefined Role
  Bases Access Control (RBAC) policies and AWS Identity and Access Management (IAM)
  roles. This solution uses credentials with IRSA for the runner’s AWS identity. The
  better pod identity approach isn’t possible as of this writing, but could be added
  following this issue being resolved.
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/streamline-your-containerized-ci-cd-with-gitlab-runners-and-amazon-eks-auto-mode/
