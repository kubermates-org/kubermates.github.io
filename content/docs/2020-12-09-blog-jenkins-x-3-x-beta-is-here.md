---
title: 'Blog: Jenkins X 3.x beta is here!'
date: '2020-12-09T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2020/12/09/jx-v3-beta/
post_kind: link
draft: false
tldr: Jenkins X 3. x beta is here! User Changes Platform Changes Getting started Final
  thoughts I’m super excited to announce the 3.
summary: 'Jenkins X 3. x beta is here! User Changes Platform Changes Getting started
  Final thoughts I’m super excited to announce the 3. 0 beta of Jenkins X! Christmas
  has come early this year! the main documentation of the changes are: the new architecture
  with modular plugins and improved extension points what has changed since 3. x started
  how 3. x compares to 2. x but here’s a brief summary of the differences: As a user
  the high level UX of Jenkins X is similar: automated Continuous Delivery pipelines
  for using tekton for your repositories with automatic promotion between your environments
  pull requests on your repositories create separate Preview Environments where your
  team can review your changes and give fast feedback before your changes are approved
  and merged into the main trunk. we now default to vanilla tekton YAML for defining
  pipelines while accelerating your tekton with tekton catalog we include an open
  source dashboard for visualising pipelines and logs which you can invoke via: jx
  dash jx dash we now use helm (3. x) and helmfile along with optionally kustomize
  in a GitOps style to define and configure both Jenkins X itself, your tools and
  applications in any namespace support multi cluster out of the box so you can keep
  Staging and Production in separate clusters to your development cluster where your
  pipelines run, you create and release immutable container images and other artifacts.
  Staging Production to setup or upgrade Jenkins X we use terraform to setup your
  cloud resources on Azure , Amazon or Google while also supporting on-premises, minkube
  and OpenShift - see the Admin Guides for more detail the actual installation of
  kubernetes resources takes place using the git operator so it runs reliably inside
  the cluster itself the actual installation of kubernetes resources takes place using
  the git operator so it runs reliably inside the cluster itself we default to using
  Kubernetes External Secrets to manage all secrets for Jenkins X itself, development
  tools and your applications too. This means we can support various secret backends
  such as Alibaba Cloud KMS Secret Manager, Amazon Secret Manager, Azure Key Vault,
  Hashicorp Vault or GCP Secret Manager It also means we can then check in all kubernetes
  resources and custom resources directly into git (apart from Kubernetes Secrets
  ) so that it super easy to version, review and reason about your kubernetes resources
  in a GitOps way. Secrets built in TLS and DNS support along with Heath reporting
  and visualising via kuberhealthy we now have an LTS distribution which lets you
  switch to a much more slower cadence of releases of Jenkins X We have been using
  Jenkins X 3. x in production now for many months (for CI/CD of all of the 3.'
---
Open the original post ↗ https://jenkins-x.io/blog/2020/12/09/jx-v3-beta/
