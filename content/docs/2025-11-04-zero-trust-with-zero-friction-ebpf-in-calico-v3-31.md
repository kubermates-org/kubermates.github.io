---
title: Zero-Trust with Zero-Friction eBPF in Calico v3.31
date: '2025-11-04T21:28:38+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/zero-trust-with-zero-friction-ebpf-in-calico-v3-31/
post_kind: link
draft: false
tldr: Calico eBPF by default* The Road to Seamless Installation How the Operator Automates
  Setup High-Availability (HA) Kubernetes API Server Support Manifest-Based Installations
  Limitations Join the Conversation Calico has used eBPF as one of its dataplanes
  since version 3.13 , released more than five years ago. At the time, this was an
  exciting step forward, introducing a new, innovative data plane that quickly gained
  traction within the Calico community.
summary: 'Calico eBPF by default* The Road to Seamless Installation How the Operator
  Automates Setup High-Availability (HA) Kubernetes API Server Support Manifest-Based
  Installations Limitations Join the Conversation Calico has used eBPF as one of its
  dataplanes since version 3.13 , released more than five years ago. At the time,
  this was an exciting step forward, introducing a new, innovative data plane that
  quickly gained traction within the Calico community. Since then, there have been
  many changes and continued evolution, all thanks to the many adopters of the then-new
  data plane. However, there has been one persistent challenge in the installation
  process since day one: bootstrapping the eBPF data plane required a manual setup
  step. This extra friction point often frustrated operators and slowed adoption.
  With the launch of Calico v3.31, that hurdle to using the eBPF data plane has finally
  been removed. For many environments (see Limitations section below), you can now
  install Calico with eBPF enabled right out of the box with no manual setup required.
  Simply use the provided installation manifest ( custom-resources-bpf. yaml ), which
  comes preconfigured with the data plane option set to eBPF. To get started, follow
  the instructions in Install Calico networking and network policy for on-premises
  deployments to enjoy a much smoother installation experience. See Calico eBPF in
  action with this short demo, highlighting how version 3.31 makes setup easier and
  increases performance: The Calico eBPF data plane includes a kube-proxy replacement,
  enabling faster service implementation than the upstream version of kube-proxy for
  iptables and better integration with the rest of the data plane for overall superior
  performance. However, a kube-proxy replacement requires knowing how to reach the
  Kubernetes API server.'
---
Open the original post ↗ https://www.tigera.io/blog/zero-trust-with-zero-friction-ebpf-in-calico-v3-31/
