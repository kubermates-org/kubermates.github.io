---
title: 'Kubernetes v1.34: User preferences (kuberc) are available for testing in kubectl
  1.34'
date: '2025-08-28T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/08/28/kubernetes-v1-34-kubectl-kuberc-beta/
post_kind: link
draft: false
tldr: 'Kubernetes v1.34: User preferences (kuberc) are available for testing in kubectl
  1.34 How it works Defaults Aliases Debugging Get involved Have you ever wished you
  could enable interactive delete , by default, in kubectl ? Or maybe, you''d like
  to have custom aliases defined, but not necessarily generate hundreds of them manually
  ? Look no further. SIG-CLI has been working hard to add user preferences to kubectl
  , and we are happy to announce that this functionality is reaching beta as part
  of the Kubernetes v1.34 release.'
summary: 'Kubernetes v1.34: User preferences (kuberc) are available for testing in
  kubectl 1.34 How it works Defaults Aliases Debugging Get involved Have you ever
  wished you could enable interactive delete , by default, in kubectl ? Or maybe,
  you''d like to have custom aliases defined, but not necessarily generate hundreds
  of them manually ? Look no further. SIG-CLI has been working hard to add user preferences
  to kubectl , and we are happy to announce that this functionality is reaching beta
  as part of the Kubernetes v1.34 release. kubectl A full description of this functionality
  is available in our official documentation , but this blog post will answer both
  of the questions from the beginning of this article. Before we dive into details,
  let''s quickly cover what the user preferences file looks like and where to place
  it. By default, kubectl will look for kuberc file in your default kubeconfig directory,
  which is $HOME/. kube. Alternatively, you can specify this location using --kuberc
  option or the KUBERC environment variable. kubectl kuberc $HOME/. kube --kuberc
  KUBERC Just like every Kubernetes manifest, kuberc file will start with an apiVersion
  and kind : kuberc apiVersion kind apiVersion : kubectl. config. k8s. io/v1beta1
  kind : Preference # the user preferences will follow here apiVersion : kubectl.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/08/28/kubernetes-v1-34-kubectl-kuberc-beta/
