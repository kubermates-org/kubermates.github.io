---
title: Introducing OpenShift Service Mesh 3.1
date: '2025-08-05T00:00:00+00:00'
tags:
- openshift
source: OpenShift Blog
external_url: https://www.redhat.com/en/blog/introducing-openshift-service-mesh-31
post_kind: link
draft: false
tldr: 'Introducing OpenShift Service Mesh 3.1 Upgrading to OpenShift Service Mesh
  3.1 Kubernetes Gateway API support in OCP 4.19+ Generally available dual-stack support
  for x86 clusters Moving to UBI Micro containers Toward a sidecar-less service mesh:
  Istio''s ambient mode Kiali updates Mesh Page Updates Performance and scalability
  with large meshes Get started with OpenShift Service Mesh Red Hat OpenShift Container
  Platform | Product Trial About the author Jamie Longmuir More like this Blog post
  Blog post Blog post Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share Red Hat OpenShift Service Mesh 3.1 has been released and is included with
  the Red Hat OpenShift Container Platform and Red Hat OpenShift Platform Plus. Based
  on the Istio, Envoy, and Kiali projects, this release updates the version of Istio
  to 1.26 and Kiali to 2.11 , and is supported on OpenShift Container Platform 4.16
  and above.'
summary: 'Introducing OpenShift Service Mesh 3.1 Upgrading to OpenShift Service Mesh
  3.1 Kubernetes Gateway API support in OCP 4.19+ Generally available dual-stack support
  for x86 clusters Moving to UBI Micro containers Toward a sidecar-less service mesh:
  Istio''s ambient mode Kiali updates Mesh Page Updates Performance and scalability
  with large meshes Get started with OpenShift Service Mesh Red Hat OpenShift Container
  Platform | Product Trial About the author Jamie Longmuir More like this Blog post
  Blog post Blog post Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share Red Hat OpenShift Service Mesh 3.1 has been released and is included with
  the Red Hat OpenShift Container Platform and Red Hat OpenShift Platform Plus. Based
  on the Istio, Envoy, and Kiali projects, this release updates the version of Istio
  to 1.26 and Kiali to 2.11 , and is supported on OpenShift Container Platform 4.16
  and above. This is the first minor release following Red Hat OpenShift Service Mesh
  3.0, a major update to converge OpenShift Service Mesh with the community Istio
  project, with installation and management using the Sail operator. This change helps
  ensure that OpenShift Service Mesh can offer the latest stable Istio features with
  Red Hat support. If you are running OpenShift Service Mesh 2.6 or earlier releases,
  you must upgrade to OpenShift Service Mesh 3.0 before upgrading to 3.1. We recommend
  migrating to OpenShift Service Mesh 3.0 promptly, because version 2.6 reaches its
  end of life on March 12, 2026. An in-depth migration guide is provided in the OpenShift
  Service Mesh 3.0 documentation , including an analysis of the differences between
  OpenShift Service Mesh 2.6 and 3.0. We''ve also recently published an article that
  describes how to use the Kiali console for migrating between OpenShift Service Mesh
  2.6 and 3.0. For an example of OpenShift Service Mesh 3.0 in action, with fully
  configured metrics and the Kiali console, see this solution pattern. Kubernetes
  Gateway API is the next generation of Kubernetes Ingress, load balancer, and service
  mesh APIs. Istio plans to make it the default set of APIs for creating and managing
  traffic using a service mesh, and it is required for using Istio''s ambient mode.
  Note that there are no plans to remove the stable Istio APIs, such as VirtualService,
  DestinationRule, and others.'
---
Open the original post ↗ https://www.redhat.com/en/blog/introducing-openshift-service-mesh-31
