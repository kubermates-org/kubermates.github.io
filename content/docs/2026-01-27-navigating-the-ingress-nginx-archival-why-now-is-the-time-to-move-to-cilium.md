---
title: 'Navigating the ingress-nginx archival: why now is the time to move to Cilium'
date: '2026-01-27T15:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/01/27/navigating-the-ingress-nginx-archival-why-now-is-the-time-to-move-to-cilium/
post_kind: link
draft: false
tldr: 'Archival of Ingress-nginx: What Does This Mean for You? What Are Your Options?
  Option 1 – Quickest: Moving to Cilium Ingress Option 2 – Recommended: Upgrading
  to Cilium’s Gateway API Implementation Why Choose Cilium’s Gateway API Implementation?
  What Are the Key Features Over Ingress? Migrating to Cilium’s Gateway API Implementation:
  Use the Ingress-to-Gateway Migration Tool Which Path Should You Take First? Why
  Cilium Is a Sensible Default: Preparing for the Future Posted on January 27, 2026
  by Dean Lewis, Senior Technical Marketing Engineer, Isovalent CNCF projects highlighted
  in this post This Member Blog was originally published on the Isovalent blog and
  is republished here with permission. If you’re running Kubernetes, there’s a good
  chance you rely on ingress-nginx to route external traffic to your workloads.'
summary: 'Archival of Ingress-nginx: What Does This Mean for You? What Are Your Options?
  Option 1 – Quickest: Moving to Cilium Ingress Option 2 – Recommended: Upgrading
  to Cilium’s Gateway API Implementation Why Choose Cilium’s Gateway API Implementation?
  What Are the Key Features Over Ingress? Migrating to Cilium’s Gateway API Implementation:
  Use the Ingress-to-Gateway Migration Tool Which Path Should You Take First? Why
  Cilium Is a Sensible Default: Preparing for the Future Posted on January 27, 2026
  by Dean Lewis, Senior Technical Marketing Engineer, Isovalent CNCF projects highlighted
  in this post This Member Blog was originally published on the Isovalent blog and
  is republished here with permission. If you’re running Kubernetes, there’s a good
  chance you rely on ingress-nginx to route external traffic to your workloads. For
  years, ingress-nginx has been the go-to open source ingress controller, valued for
  its reliability and broad community support. Data collected from a recent State
  of Kubernetes Networking Report shows that 50% of respondents use Ingress-nginx
  today. But that’s about to change. The maintainers of ingress-nginx have announced
  that the project is being archived at the start of 2026. This means it will no longer
  receive active maintenance, security patches, or bug fixes. The news, unveiled during
  KubeCon , marks a significant turning point for thousands of Kubernetes users and
  organizations that have built their ingress strategy around it. With ingress-nginx
  entering retirement, platform teams face a choice: keep a critical control-plane
  component without upstream maintenance, or move to an actively supported alternative.
  The Kubernetes community has aligned on the Gateway API as the long-term standard
  for traffic management. That direction shapes your two primary migration paths:
  Move to another ingress controller (such as Cilium Ingress, Traefik, or HAProxy
  Ingress). Adopt the Kubernetes Gateway API , the next-generation standard for ingress
  and traffic management, using a controller like Cilium Gateway API.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/01/27/navigating-the-ingress-nginx-archival-why-now-is-the-time-to-move-to-cilium/
