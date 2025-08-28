---
title: 'Blog: How to use GitOps and Kubernetes External Secrets for better audit and
  security'
date: '2021-08-17T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2021/08/17/gitops-secrets/
post_kind: link
draft: false
tldr: 'So GitOps is a cool approach to managing kubernetes resources in a cluster,
  by checking in the source code for: Then everything is versioned and audited; you
  know who changed what, when and why. If a change breaks things, just revert via
  git like any other source code change.'
summary: 'So GitOps is a cool approach to managing kubernetes resources in a cluster,
  by checking in the source code for: Then everything is versioned and audited; you
  know who changed what, when and why. If a change breaks things, just revert via
  git like any other source code change. You can then add pipelines to verify changes
  in the Pull Requests result in valid kubernetes YAML etc. Then if you merge changes
  to git then an operator detect the change and do the kubectl apply (or helm install
  or whatever). There are a number of tools out there for doing this. e. g. Anthos
  Config Management , argo cd , fleet , flux cd and kapp controller So why did Jenkins
  X not use these tools and instead created its own git operator ? Over time it would
  be great to have more standardisation of the Git layout given the different tool.
  Our current recommended layout that works with many GitOps tools is described here.
  A number of solutions in the GitOps space define which helm charts to install in
  git with configuration files; or specify which kustomize templates to apply etc.
  However Jenkins X defaults to using helmfile to manage installing, upgrading and
  configuring multiple helm charts. Then we use helmfile template to render the helm
  charts as kubernetes resources.'
---
Open the original post ↗ https://jenkins-x.io/blog/2021/08/17/gitops-secrets/
