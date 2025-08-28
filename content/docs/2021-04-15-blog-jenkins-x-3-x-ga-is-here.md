---
title: 'Blog: Jenkins X 3.x GA is here!'
date: '2021-04-15T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2021/04/15/jx-v3-ga/
post_kind: link
draft: false
tldr: Jenkins X 3. x GA is here! Demo Documentation Changes since the 3.
summary: 'Jenkins X 3. x GA is here! Demo Documentation Changes since the 3. x beta
  User Changes since 2. x Platform Changes Getting started Final thoughts I’m super
  excited to announce the 3.0 GA (General Availability) release of Jenkins X! Jenkins
  X automates your CI/CD on kubernetes to help you accelerate : Automated CI/CD pipelines
  lets you focus on your actually application code while Jenkins X automatically creates
  battle tested Tekton CI/CD pipelines for your project which are managed via GitOps
  so that its super easy to keep your pipelines up to date across your repositories
  or to upgrade or override pipelines or steps for specific repositories. Automatic
  promotion of versioned artifacts via GitOps through your Environments such as Staging
  , Pre-production and Production whether they are running in the same kubernetes
  cluster or you are using multiple clusters for your environments Staging Pre-production
  Production Preview Environments lets you propose code changes via Pull Requests
  and have a Preview Environment automatically created, running your code in kubernetes
  to get fast feedback from your team before agreeing to merge changes to the main
  branch ChatOps comment on Pull Requests to give feedback, approve/hold changes,
  trigger optional pipelines for additional testing and other ChatOps commands Here’s
  a demo of how to develop code with Jenkins X the main documentation of the changes
  are: the new architecture with modular plugins and improved extension points what
  has changed since 3. x started how 3. x compares to 2. x DevOps Guides and DevOps
  Patterns provides an overview of our learnings in the DevOps space here’s a brief
  summary of the differences: The following improvements have been made since the
  first beta : Integrated observability and monitoring with Pipeline Tracing Auto
  scale preview environments with Osiris Enable auto upgrade to keep your cluster
  up to date As a user the high level UX of Jenkins X is similar: automated Continuous
  Delivery pipelines for using tekton for your repositories with automatic promotion
  between your environments pull requests on your repositories create separate Preview
  Environments where your team can review your changes and give fast feedback before
  your changes are approved and merged into the main trunk. we now default to vanilla
  tekton YAML for defining pipelines while accelerating your tekton with tekton catalog
  we include an open source dashboard for visualising pipelines and logs which you
  can invoke via: jx dash jx dash we now use helm (3. x) and helmfile along with optionally
  kustomize in a GitOps style to define and configure both Jenkins X itself, your
  tools and applications in any namespace support multi cluster out of the box so
  you can keep Staging and Production in separate clusters to your development cluster
  where your pipelines run, you create and release immutable container images and
  other artifacts. Staging Production to setup or upgrade Jenkins X we use terraform
  to setup your cloud resources on Azure , Amazon or Google while also supporting
  on-premises, minkube and OpenShift - see the Admin Guides for more detail the actual
  installation of kubernetes resources takes place using the git operator so it runs
  reliably inside the cluster itself the actual installation of kubernetes resources
  takes place using the git operator so it runs reliably inside the cluster itself
  we default to using Kubernetes External Secrets to manage all secrets for Jenkins
  X itself, development tools and your applications too. This means we can support
  various secret backends such as Alibaba Cloud KMS Secret Manager, Amazon Secret
  Manager, Azure Key Vault, Hashicorp Vault or GCP Secret Manager It also means we
  can then check in all kubernetes resources and custom resources directly into git
  (apart from Kubernetes Secrets ) so that it super easy to version, review and reason
  about your kubernetes resources in a GitOps way.'
---
Open the original post ↗ https://jenkins-x.io/blog/2021/04/15/jx-v3-ga/
