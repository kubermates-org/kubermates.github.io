---
title: 'Kubernetes v1.35: Restricting executables invoked by kubeconfigs via exec
  plugin allowList added to kuberc'
date: '2026-01-09T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/01/09/kubernetes-v1-35-kuberc-credential-plugin-allowlist/
post_kind: link
draft: false
tldr: 'Kubernetes v1.35: Restricting executables invoked by kubeconfigs via exec plugin
  allowList added to kuberc How it works Selectively allowing plugins Future enhancements
  Get involved Did you know that kubectl can run arbitrary executables, including
  shell scripts, with the full privileges of the invoking user, and without your knowledge?
  Whenever you download or auto-generate a kubeconfig , the users[n]. exec.'
summary: 'Kubernetes v1.35: Restricting executables invoked by kubeconfigs via exec
  plugin allowList added to kuberc How it works Selectively allowing plugins Future
  enhancements Get involved Did you know that kubectl can run arbitrary executables,
  including shell scripts, with the full privileges of the invoking user, and without
  your knowledge? Whenever you download or auto-generate a kubeconfig , the users[n].
  exec. command field can specify an executable to fetch credentials on your behalf.
  Don''t get me wrong, this is an incredible feature that allows you to authenticate
  to the cluster with external identity providers. Nevertheless, you probably see
  the problem: Do you know exactly what executables your kubeconfig is running on
  your system? Do you trust the pipeline that generated your kubeconfig ? If there
  has been a supply-chain attack on the code that generates the kubeconfig, or if
  the generating pipeline has been compromised, an attacker might well be doing unsavory
  things to your machine by tricking your kubeconfig into running arbitrary code.
  kubectl kubeconfig users[n]. exec. command kubeconfig kubeconfig kubeconfig To give
  the user more control over what gets run on their system, SIG-Auth and SIG-CLI added
  the credential plugin policy and allowlist as a beta feature to Kubernetes 1.35.
  This is available to all clients using the client-go library, by filling out the
  ExecProvider. PluginPolicy struct on a REST config. To broaden the impact of this
  change, Kubernetes v1.35 also lets you manage this without writing a line of application
  code. You can configure kubectl to enforce the policy and allowlist by adding two
  fields to the kuberc configuration file: credentialPluginPolicy and credentialPluginAllowlist.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/01/09/kubernetes-v1-35-kuberc-credential-plugin-allowlist/
