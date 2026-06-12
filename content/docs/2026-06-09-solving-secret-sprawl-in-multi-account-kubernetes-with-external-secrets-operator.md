---
title: Solving secret sprawl in multi-account Kubernetes with External Secrets Operator
date: '2026-06-09T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/06/09/solving-secret-sprawl-in-multi-account-kubernetes-with-external-secrets-operator/
post_kind: link
draft: false
tldr: 'The challenge: Managing shared secrets across isolated environments The solution:
  External Secrets Operator as the bridge How the architecture works The outcome:
  Centralized secret management at scale Posted on June 9, 2026 by Viktoria Bisova,
  DevOps Engineer, Itigix CNCF projects highlighted in this post Infrastructure provisioning
  in Kubernetes has become increasingly automated, but secret management often remains
  a challenge as environments grow. Organizations commonly separate development, staging,
  and production workloads across clusters, namespaces, or cloud accounts to improve
  security and reduce blast radius.'
summary: 'The challenge: Managing shared secrets across isolated environments The
  solution: External Secrets Operator as the bridge How the architecture works The
  outcome: Centralized secret management at scale Posted on June 9, 2026 by Viktoria
  Bisova, DevOps Engineer, Itigix CNCF projects highlighted in this post Infrastructure
  provisioning in Kubernetes has become increasingly automated, but secret management
  often remains a challenge as environments grow. Organizations commonly separate
  development, staging, and production workloads across clusters, namespaces, or cloud
  accounts to improve security and reduce blast radius. While this isolation is beneficial,
  it introduces a recurring operational problem: how should shared credentials be
  distributed and rotated consistently across those boundaries? Our team recently
  faced this while designing a scalable environment for a client running on AWS EKS.
  The problem we set out to solve is not unique to AWS, or to cloud infrastructure
  in general. Whether you’re running on Azure, Google Cloud, a multi-cloud setup,
  on-premise infrastructure, or automating local development environments with tools
  like KIND or Minikube, the pain point remains identical: ensuring seamless secret
  replication across isolated boundaries. Each environment (Dev, Staging, Prod) resides
  in its own distinct account, namespace, or cluster. This separation is excellent
  for security and blast radius mitigation, but it introduces significant operational
  complexity. How do you replicate shared secrets across these isolated environments
  without manual copy-pasting? This article explains how we solved the multi-account
  secret synchronization problem using External Secrets Operator (ESO) and Bitwarden
  Secrets Manager. Our client runs two applications with heavy dependencies on third-party
  integrations. We hit a wall when designing automation for provisioning new environments:
  Shared credentials: In non-production environments, the applications share identical
  “sandbox” credentials for third-party tools. Fragmented storage: Each EKS cluster
  lives in a separate AWS account. Using AWS Secrets Manager per account meant that
  when a third-party API key rotated, we had to manually update it across every single
  AWS account.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/06/09/solving-secret-sprawl-in-multi-account-kubernetes-with-external-secrets-operator/
