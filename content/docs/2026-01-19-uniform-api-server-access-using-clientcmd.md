---
title: Uniform API server access using clientcmd
date: '2026-01-19T10:00:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/01/19/clientcmd-apiserver-access/
post_kind: link
draft: false
tldr: 'Uniform API server access using clientcmd General philosophy Available features
  Configuration merging Overall process Configure the loading rules Configure the
  overrides Build a set of flags Bind the flags Build the merged configuration Obtain
  an API client Full example If you''ve ever wanted to develop a command line client
  for a Kubernetes API, especially if you''ve considered making your client usable
  as a kubectl plugin, you might have wondered how to make your client feel familiar
  to users of kubectl. A quick glance at the output of kubectl options might put a
  damper on that: "Am I really supposed to implement all those options?" kubectl kubectl
  kubectl options Fear not, others have done a lot of the work involved for you.'
summary: 'Uniform API server access using clientcmd General philosophy Available features
  Configuration merging Overall process Configure the loading rules Configure the
  overrides Build a set of flags Bind the flags Build the merged configuration Obtain
  an API client Full example If you''ve ever wanted to develop a command line client
  for a Kubernetes API, especially if you''ve considered making your client usable
  as a kubectl plugin, you might have wondered how to make your client feel familiar
  to users of kubectl. A quick glance at the output of kubectl options might put a
  damper on that: "Am I really supposed to implement all those options?" kubectl kubectl
  kubectl options Fear not, others have done a lot of the work involved for you. In
  fact, the Kubernetes project provides two libraries to help you handle kubectl -style
  command line arguments in Go programs: clientcmd and cli-runtime (which uses clientcmd
  ). This article will show how to use the former. kubectl clientcmd cli-runtime clientcmd
  As might be expected since it''s part of client-go , clientcmd ''s ultimate purpose
  is to provide an instance of restclient. Config that can issue requests to an API
  server. client-go clientcmd restclient. Config It follows kubectl semantics: kubectl
  defaults are taken from ~/. kube or equivalent; ~/. kube files can be specified
  using the KUBECONFIG environment variable; KUBECONFIG all of the above settings
  can be further overridden using command line arguments. It doesn''t set up a --kubeconfig
  command line argument, which you might want to do to align with kubectl ; you''ll
  see how to do this in the "Bind the flags" section. --kubeconfig kubectl clientcmd
  allows programs to handle clientcmd kubeconfig selection (using KUBECONFIG ); kubeconfig
  KUBECONFIG context selection; namespace selection; client certificates and private
  keys; user impersonation; HTTP Basic authentication support (username/password).'
---
Open the original post ↗ https://kubernetes.io/blog/2026/01/19/clientcmd-apiserver-access/
