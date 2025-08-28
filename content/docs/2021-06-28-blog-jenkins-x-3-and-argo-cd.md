---
title: 'Blog: Jenkins X 3 and Argo CD'
date: '2021-06-28T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2021/06/28/argo/
post_kind: link
draft: false
tldr: Jenkins X 3 and Argo CD Install Argo CD with Jenkins X Conclusion There have
  been a number of requests from the Jenkins X community to use Argo CD for the last
  mile deployment phase of their continuous delivery pipelines. This blog explains
  some of the advantages of using Jenkins X and Argo CD all together.
summary: 'Jenkins X 3 and Argo CD Install Argo CD with Jenkins X Conclusion There
  have been a number of requests from the Jenkins X community to use Argo CD for the
  last mile deployment phase of their continuous delivery pipelines. This blog explains
  some of the advantages of using Jenkins X and Argo CD all together. What’s included?
  Jenkins X for Cloud Infrastructure using Terraform, core installation management
  with GitOps, external secret management, ingress controller, quickstarts, automated
  CI + CD pipelines, ChatOps Tekton for pipeline orchestration Argo CD for end users
  application deployments (not the main installation) Argo CD provides a declarative
  GitOps approach to deploying Kubernetes based applications. There is a GUI which
  helps construct the deployment definition (in the form of an Application custom
  resource) which offers a number of configuration options, as well and providing
  insight into your clusters applications. Application You might be wondering why
  you would want to use BOTH Jenkins X and Argo CD together. Jenkins X aims to embrace
  OSS, where possible providing a nice UX to integrate with other projects and help
  provide better solutions for building, developing and running software on Kubernetes.
  Jenkins X indeed does have a git operator that applies Kubernetes YAML from a Git
  repository but there are some differences: Jenkins X uses GitOps principles for
  the entire installation, i. e. the starting point is a Git repository which is used
  to provision a cluster and manage (automatic if users wish) upgrades whereas today
  Argo CD uses a manual kubectl apply to manage the Argo installation itself. Jenkins
  X uses GitOps principles for the entire installation, i. e. the starting point is
  a Git repository which is used to provision a cluster and manage (automatic if users
  wish) upgrades whereas today Argo CD uses a manual kubectl apply to manage the Argo
  installation itself.'
---
Open the original post ↗ https://jenkins-x.io/blog/2021/06/28/argo/
