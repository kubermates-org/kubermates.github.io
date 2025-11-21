---
title: Introducing OpenShift Service Mesh 3.2 with Istio’s ambient mode
date: '2025-11-17T00:00:00+00:00'
tags:
- openshift
source: OpenShift Blog
external_url: https://www.redhat.com/en/blog/introducing-openshift-service-mesh-32-istios-ambient-mode
post_kind: link
draft: false
tldr: 'Introducing OpenShift Service Mesh 3.2 with Istio’s ambient mode Upgrading
  to OpenShift Service Mesh 3.2 Sidecar-less service mesh: Istio’s ambient mode Ztunnel
  proxy Waypoint proxy Is Istio’s ambient mode right for you? What are the benefits
  and trade offs? Significantly reduced resource costs Lightweight zero trust networking
  Improved scalability Potential performance characteristics Easier adoption Feature
  support levels Upgrade considerations Getting started with Istio’s ambient mode
  If I am already using service mesh, can I migrate to ambient mode? Kiali with Istio’s
  ambient Istio 1.27 updates Gateway API Inference Extensions (GIE) Multicluster with
  ambient mode Native nftables support in sidecar mode Cert-manager Istio-CSR is generally
  available Getting started with OpenShift Service Mesh Red Hat Product Security About
  the author Jamie Longmuir More like this How to join a Linux system to an Active
  Directory domain How to configure your CA trust list in Linux What Is Product Security?
  | Compiler Technically Speaking | Security for the AI supply chain Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share We are thrilled
  to announce the general availability of Red Hat OpenShift Service Mesh 3.2. This
  release includes the general availability of Istio’s ambient mode —a new way of
  deploying service mesh without sidecars that significantly lowers the resource costs
  of using service mesh.'
summary: 'Introducing OpenShift Service Mesh 3.2 with Istio’s ambient mode Upgrading
  to OpenShift Service Mesh 3.2 Sidecar-less service mesh: Istio’s ambient mode Ztunnel
  proxy Waypoint proxy Is Istio’s ambient mode right for you? What are the benefits
  and trade offs? Significantly reduced resource costs Lightweight zero trust networking
  Improved scalability Potential performance characteristics Easier adoption Feature
  support levels Upgrade considerations Getting started with Istio’s ambient mode
  If I am already using service mesh, can I migrate to ambient mode? Kiali with Istio’s
  ambient Istio 1.27 updates Gateway API Inference Extensions (GIE) Multicluster with
  ambient mode Native nftables support in sidecar mode Cert-manager Istio-CSR is generally
  available Getting started with OpenShift Service Mesh Red Hat Product Security About
  the author Jamie Longmuir More like this How to join a Linux system to an Active
  Directory domain How to configure your CA trust list in Linux What Is Product Security?
  | Compiler Technically Speaking | Security for the AI supply chain Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share We are thrilled
  to announce the general availability of Red Hat OpenShift Service Mesh 3.2. This
  release includes the general availability of Istio’s ambient mode —a new way of
  deploying service mesh without sidecars that significantly lowers the resource costs
  of using service mesh. This provides a low overhead solution for zero trust networking
  with lightweight pod-to-pod mTLS encryption and authorization policies based on
  workload identities, with the ability to add more advanced features as required.
  Based on the Istio, Envoy, and Kiali projects, this release updates the version
  of Istio to 1.27 and Kiali to 2.17 , and is supported on Red Hat OpenShift 4.18
  and above. If you are running OpenShift Service Mesh 2.6 or earlier releases, you
  must upgrade to OpenShift Service Mesh 3.0, 3.1, and then 3.2. We recommend migrating
  to OpenShift Service Mesh 3.0 promptly, because version 2.6 reaches its end of life
  (EOL) on June 30, 2026 (recently extended from March 12, 2026). An in-depth migration
  guide is provided in the OpenShift Service Mesh 3.0 documentation , including an
  analysis of the differences between OpenShift Service Mesh 2.6 and 3.0. This blog
  post describes using the Kiali console for migrating between OpenShift Service Mesh
  2.6 and 3.0. For an example of OpenShift Service Mesh 3 in action, with fully configured
  metrics and the Kiali console, see this solution pattern. This release brings generally
  available support for Istio’s ambient mode to OpenShift Service Mesh. Istio’s ambient
  mode is a significant new feature that enables service mesh features on workloads
  without the need for sidecar proxies. With Istio’s traditional dataplane architecture,
  known as “sidecar mode,” each application pod requires a sidecar proxy container
  to enable service mesh features.'
---
Open the original post ↗ https://www.redhat.com/en/blog/introducing-openshift-service-mesh-32-istios-ambient-mode
