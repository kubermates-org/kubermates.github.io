---
title: 'Blog: Jenkins X 3 and Argo CD'
date: '2021-06-28T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2021/06/28/argo/
post_kind: link
draft: false
tldr: There have been a number of requests from the Jenkins X community to use Argo
  CD for the last mile deployment phase of their continuous delivery pipelines. This
  blog explains some of the advantages of using Jenkins X and Argo CD all together.
summary: 'There have been a number of requests from the Jenkins X community to use
  Argo CD for the last mile deployment phase of their continuous delivery pipelines.
  This blog explains some of the advantages of using Jenkins X and Argo CD all together.
  What’s included? You might be wondering why you would want to use BOTH Jenkins X
  and Argo CD together. Jenkins X aims to embrace OSS, where possible providing a
  nice UX to integrate with other projects and help provide better solutions for building,
  developing and running software on Kubernetes. Jenkins X indeed does have a git
  operator that applies Kubernetes YAML from a Git repository but there are some differences:
  Jenkins X uses GitOps principles for the entire installation, i. e. the starting
  point is a Git repository which is used to provision a cluster and manage (automatic
  if users wish) upgrades whereas today Argo CD uses a manual kubectl apply to manage
  the Argo installation itself. External Secrets integration for Vault, Google Secrets
  manager etc is something that Jenkins X provides out of the box. When Kubernetes
  based applications require a secret we prefer the source is stored in a secrets
  manager and the value synchronised automatically into the cluster enabling easier
  secret rotation, avoiding local secrets on machines and an easier UX for working
  with secrets. When adding an Application via Argo CD users can leverage the Jenkins
  X approach to working with secrets and rely on Argo to manage the deployments. If
  users prefer to work with SOPS that is totally fine too and will work in the same
  way as they are used to. If you do not wish to expose direct access for the Kubernetes
  cluster to developers then using a combination of Jenkins X UI for accessing logs
  and Argo CD for managing application deployments may be enough.'
---
Open the original post ↗ https://jenkins-x.io/blog/2021/06/28/argo/
