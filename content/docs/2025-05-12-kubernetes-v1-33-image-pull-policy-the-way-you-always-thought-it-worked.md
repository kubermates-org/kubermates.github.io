---
title: 'Kubernetes v1.33: Image Pull Policy the way you always thought it worked!'
date: '2025-05-12T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/05/12/kubernetes-v1-33-ensure-secret-pulled-images-alpha/
post_kind: link
draft: false
tldr: 'Kubernetes v1.33: Image Pull Policy the way you always thought it worked! Image
  Pull Policy the way you always thought it worked! IfNotPresent, even if I''m not
  supposed to have it IfNotPresent, but only if I am supposed to have it Never pull,
  but use if authorized Always pull, if authorized How it all works Try it out What''s
  next? How to get involved Some things in Kubernetes are surprising, and the way
  imagePullPolicy behaves might be one of them. Given Kubernetes is all about running
  pods, it may be peculiar to learn that there has been a caveat to restricting pod
  access to authenticated images for over 10 years in the form of issue 18787 ! It
  is an exciting release when you can resolve a ten-year-old issue.'
summary: 'Kubernetes v1.33: Image Pull Policy the way you always thought it worked!
  Image Pull Policy the way you always thought it worked! IfNotPresent, even if I''m
  not supposed to have it IfNotPresent, but only if I am supposed to have it Never
  pull, but use if authorized Always pull, if authorized How it all works Try it out
  What''s next? How to get involved Some things in Kubernetes are surprising, and
  the way imagePullPolicy behaves might be one of them. Given Kubernetes is all about
  running pods, it may be peculiar to learn that there has been a caveat to restricting
  pod access to authenticated images for over 10 years in the form of issue 18787
  ! It is an exciting release when you can resolve a ten-year-old issue. imagePullPolicy
  The gist of the problem is that the imagePullPolicy: IfNotPresent strategy has done
  precisely what it says, and nothing more. Let''s set up a scenario. To begin, Pod
  A in Namespace X is scheduled to Node 1 and requires image Foo from a private repository.
  For it''s image pull authentication material, the pod references Secret 1 in its
  imagePullSecrets. Secret 1 contains the necessary credentials to pull from the private
  repository. The Kubelet will utilize the credentials from Secret 1 as supplied by
  Pod A and it will pull container image Foo from the registry. This is the intended
  (and secure) behavior. imagePullPolicy: IfNotPresent imagePullSecrets But now things
  get curious. If Pod B in Namespace Y happens to also be scheduled to Node 1 , unexpected
  (and potentially insecure) things happen. Pod B may reference the same private image,
  specifying the IfNotPresent image pull policy.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/12/kubernetes-v1-33-ensure-secret-pulled-images-alpha/
