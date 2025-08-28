---
title: 'Blog: Kubernetes supports running kube-proxy in an unprivileged container'
date: '2024-01-05T00:00:00+00:00'
tags:
- kubernetes
- community
source: Kubernetes.dev Blog
external_url: https://www.kubernetes.dev/blog/2024/01/05/kube-proxy-non-privileged/
post_kind: link
draft: false
tldr: Kubernetes supports running kube-proxy in an unprivileged container Background
  Initializing kube-proxy in an init container Summary This post describes how the
  --init-only flag to kube-proxy can be used to run the main kube-proxy container
  in a stricter securityContext , by performing the configuration that requires privileged
  mode in a separate init container. Since Windows doesn’t have the equivalent of
  capabilities , this only works on Linux.
summary: Kubernetes supports running kube-proxy in an unprivileged container Background
  Initializing kube-proxy in an init container Summary This post describes how the
  --init-only flag to kube-proxy can be used to run the main kube-proxy container
  in a stricter securityContext , by performing the configuration that requires privileged
  mode in a separate init container. Since Windows doesn’t have the equivalent of
  capabilities , this only works on Linux. --init-only kube-proxy securityContext
  capabilities The kube-proxy Pod still only meets the privileged Pod Security Standard
  , but there is still an improvement because the running container doesn’t need to
  run privileged. kube-proxy Please note that kube-proxy can be installed in different
  ways. The examples below assume that kube-proxy is run from a pod, but similar changes
  could be made in clusters where it is run as a system service. kube-proxy It is
  undesirable to run a server container like kube-proxy in privileged mode. Security
  aware users wants to use capabilities instead. kube-proxy If kube-proxy is installed
  as a POD, the initialization requires “privileged” mode, mostly for setting sysctl’s.
  However, kube-proxy only tries to set the sysctl’s if they don’t already have the
  right values. In theory, then, if a privileged init container set the sysctls to
  the right values, then kube-proxy could run unprivileged. kube-proxy kube-proxy
  kube-proxy The problem is to know what to setup. Until now the only option has been
  to read the source to see what changes kube-proxy would have made, but with --init-only
  you can have kube-proxy itself do the setup exactly as on a normal start, and then
  exit.
---
Open the original post ↗ https://www.kubernetes.dev/blog/2024/01/05/kube-proxy-non-privileged/
