---
title: Introducing OpenShift Service Mesh 3.3 with post-quantum cryptography
date: '2026-03-17T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/openshift-service-mesh-33-adds-post-quantum-cryptography
post_kind: link
draft: false
tldr: 'Introducing OpenShift Service Mesh 3.3 with post-quantum cryptography Updates
  in Istio 1.28 Introducing post-quantum encryption support Why is quantum computing
  a security concern? How does service mesh help to address these concerns? Evolving
  sidecar-less ambient mode Support in FIPS mode Improved upgrades documentation Multicluster
  with ambient mode is now Technology Preview Kiali updates Performance and scale
  enhancements with large meshes Updated look and a new notification center OpenShift
  Service Mesh Console and Network Observability Coming soon: Upcoming Developer Preview
  features Kiali’s AI chatbot and MCP integrations OpenShift Service Mesh with external
  VM workloads Zero trust workload identity manager Getting started with OpenShift
  Service Mesh 3.3 Red Hat OpenShift Container Platform | Product Trial About the
  author Jamie Longmuir More like this MCP security: Implementing robust authentication
  and authorization AI trust through open collaboration: A new chapter for responsible
  innovation Post-quantum Cryptography | Compiler Understanding AI Security Frameworks
  | Compiler Keep exploring Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share Red Hat OpenShift Service Mesh 3.3 is now generally available with Red Hat
  OpenShift Container Platform and Red Hat OpenShift Platform Plus. Based on the Istio,
  Envoy, and Kiali projects, this release updates the version of Istio to 1.28 and
  Kiali to 2.22, and is supported on OpenShift Container Platform 4.18 and above.'
summary: 'Introducing OpenShift Service Mesh 3.3 with post-quantum cryptography Updates
  in Istio 1.28 Introducing post-quantum encryption support Why is quantum computing
  a security concern? How does service mesh help to address these concerns? Evolving
  sidecar-less ambient mode Support in FIPS mode Improved upgrades documentation Multicluster
  with ambient mode is now Technology Preview Kiali updates Performance and scale
  enhancements with large meshes Updated look and a new notification center OpenShift
  Service Mesh Console and Network Observability Coming soon: Upcoming Developer Preview
  features Kiali’s AI chatbot and MCP integrations OpenShift Service Mesh with external
  VM workloads Zero trust workload identity manager Getting started with OpenShift
  Service Mesh 3.3 Red Hat OpenShift Container Platform | Product Trial About the
  author Jamie Longmuir More like this MCP security: Implementing robust authentication
  and authorization AI trust through open collaboration: A new chapter for responsible
  innovation Post-quantum Cryptography | Compiler Understanding AI Security Frameworks
  | Compiler Keep exploring Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share Red Hat OpenShift Service Mesh 3.3 is now generally available with Red Hat
  OpenShift Container Platform and Red Hat OpenShift Platform Plus. Based on the Istio,
  Envoy, and Kiali projects, this release updates the version of Istio to 1.28 and
  Kiali to 2.22, and is supported on OpenShift Container Platform 4.18 and above.
  While this release includes many updates, it also sets the stage for the next generation
  of service mesh features, including post-quantum cryptographic (PQC) encryption,
  AI enablement, and support for the inclusion of external virtual machines (VMs)
  with service mesh. Istio 1.28 includes several major updates, including notable
  security feature enhancements and traffic management enhancements with support for
  Gateway API v1.4 and BackendTLSPolicy v1. Notable Red Hat contributions in Istio
  1.28 include: An improved JWT filter configuration to support custom space-delimited
  claims Default Kubernetes NetworkPolicies for Istio to make it easier for administrators
  to secure their service mesh Nftable support for ambient mode , which enables support
  for service mesh with Red Hat Enterprise Linux 10 (support coming with Red Hat OpenShift
  5 ) There have also been significant developments to ambient mode’s multicluster
  deployments, which enable us to upgrade this feature to Technology Preview. For
  a full list of updates in Istio 1.28, please see the announcement and detailed change
  notes. This release introduces support for PQC algorithms in service mesh. These
  new algorithms help to confirm that the encryption used with Istio’s gateways and
  workload proxies works against a new generation of threats that will arise as quantum
  computing becomes more widely available. Quantum computing represents an exciting
  up-and-coming technology, offering the ability to run complex calculations in a
  tiny fraction of the time they would take on a classical computer. But these same
  powers can be applied to break the encryption algorithms that are widely used in
  sensitive information and workloads today. This includes the standard algorithms
  used for Istio’s mTLS encryption. These threats—and the algorithms that mitigate
  them—were described in detail in our preview announcement of configuring Istio gateways
  with PQC algorithms.'
---
Open the original post ↗ https://www.redhat.com/en/blog/openshift-service-mesh-33-adds-post-quantum-cryptography
