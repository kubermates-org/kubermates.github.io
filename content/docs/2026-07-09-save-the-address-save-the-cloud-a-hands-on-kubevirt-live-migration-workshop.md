---
title: 'Save the Address, Save the Cloud: A Hands-on KubeVirt Live Migration Workshop'
date: '2026-07-09T13:58:26+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/save-the-address-save-the-cloud-a-hands-on-kubevirt-live-migration-workshop/
post_kind: link
draft: false
tldr: 'Requirements Create a multi-node cluster Install Calico Install KubeVirt Preparing
  KubeVirt Create a VM Live VM Migration Gathering The Report Clean up Conclusion
  In the previous post in this series , we covered why Virtual Machine (VM) Live Migration
  in Kubernetes is difficult: a VM’s IP is its identity, and the “new” VM on the destination
  node has to come up with the same IP, this something that Kubernetes is not known
  for, and on top of that, traffic has to switch over only after network security
  policies are in place. Calico v3.32.0 delivers all the above and allows you to Live
  Migrate a VM without any network disruptions and this post is a short, do-it-yourself
  workshop to achieve it.'
summary: 'Requirements Create a multi-node cluster Install Calico Install KubeVirt
  Preparing KubeVirt Create a VM Live VM Migration Gathering The Report Clean up Conclusion
  In the previous post in this series , we covered why Virtual Machine (VM) Live Migration
  in Kubernetes is difficult: a VM’s IP is its identity, and the “new” VM on the destination
  node has to come up with the same IP, this something that Kubernetes is not known
  for, and on top of that, traffic has to switch over only after network security
  policies are in place. Calico v3.32.0 delivers all the above and allows you to Live
  Migrate a VM without any network disruptions and this post is a short, do-it-yourself
  workshop to achieve it. In about 5 minutes you’ll bring up a 3-node cluster, install
  Calico + KubeVirt, run a VM, and migrate it live. A Linux or a Windows Machine preferably
  WSL2 ( Mac Is not supported by KubeVirt ) Docker or Podman with at least 8 GB RAM
  kubectl KIND (v0.31.0) virtctl (v1.8.2) Note: In many Linux distros the default
  for most kernel parameters are too low, for a kind cluster running KubeVirt. Use
  the following command to temporarily increase these limits. sudo sysctl -w fs. inotify.
  max_user_instances=2048 sudo sysctl -w fs. inotify. max_user_watches=1048576 sudo
  sysctl -w fs. inotify. max_user_instances=2048 sudo sysctl -w fs.'
---
Open the original post ↗ https://www.tigera.io/blog/save-the-address-save-the-cloud-a-hands-on-kubevirt-live-migration-workshop/
