---
title: 'Scaling the future: How Garanti BBVA manages etcd in massive Red Hat OpenShift
  environments'
date: '2026-06-05T00:00:00+00:00'
tags:
- openshift
source: OpenShift Blog
external_url: https://www.redhat.com/en/blog/scaling-future-how-garanti-bbva-manages-etcd-massive-red-hat-openshift-environments
post_kind: link
draft: false
tldr: 'Scaling the future: How Garanti BBVA manages etcd in massive Red Hat OpenShift
  environments The scale of the challenge The problem: When etcd hits the wall Deep
  dive into optimization Designing a custom solution Real-world results Resources
  Red Hat OpenShift Container Platform | Product Trial About the author Debbie Margulies
  More like this Get the most out of Red Hat Enterprise Linux for Microsoft Azure
  Red Hat OpenShift 4.20: Expanded Oracle Cloud Infrastructure Support Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share At the OpenShift
  Commons Gathering in Amsterdam on March 23—a Day Zero event for KubeCon + CloudNativeCon
  Europe 2026—attendees got a deep look into the engine room of 1 of Turkey''s largest
  private banks. Emirhan Bilge Bulut, an Expert System Engineer at Garanti BBVA, joined
  Gokhan Goksu, a Senior Solution Architect at Red Hat, to discuss the unglamorous
  but essential infrastructure management required to support 30 million customers
  and 1.2 billion daily transactions.'
summary: 'Scaling the future: How Garanti BBVA manages etcd in massive Red Hat OpenShift
  environments The scale of the challenge The problem: When etcd hits the wall Deep
  dive into optimization Designing a custom solution Real-world results Resources
  Red Hat OpenShift Container Platform | Product Trial About the author Debbie Margulies
  More like this Get the most out of Red Hat Enterprise Linux for Microsoft Azure
  Red Hat OpenShift 4.20: Expanded Oracle Cloud Infrastructure Support Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share At the OpenShift
  Commons Gathering in Amsterdam on March 23—a Day Zero event for KubeCon + CloudNativeCon
  Europe 2026—attendees got a deep look into the engine room of 1 of Turkey''s largest
  private banks. Emirhan Bilge Bulut, an Expert System Engineer at Garanti BBVA, joined
  Gokhan Goksu, a Senior Solution Architect at Red Hat, to discuss the unglamorous
  but essential infrastructure management required to support 30 million customers
  and 1.2 billion daily transactions. Figure 1. Emirhan Bilge Bulut, an Expert System
  Engineer at Garanti BBVA, joined Gokhan Goksu, a Solution Architect at Red Hat,
  speaking at the OpenShift Commons Gathering in Amsterdam. Garanti BBVA operates
  at a staggering magnitude. Its infrastructure includes: 60 Red Hat OpenShift clusters,
  with 33 serving production environments. Over 30,000 pods and 3,100 services across
  all clusters. Up to 2 billion transactions processed per day during peak times.
  As organizations scale, they often find that standard tools aren''t enough to manage
  the corresponding growth of their etcd database. In many infrastructures, this database
  is the single critical component that holds all cluster configuration, secrets,
  and metadata. For Garanti BBVA, the challenge manifested as uncontrolled etcd size
  growth. In its non-production environments, which are often more complex due to
  high developer activity, a single cluster might house 40,000 pods and 10,000 microservices.'
---
Open the original post ↗ https://www.redhat.com/en/blog/scaling-future-how-garanti-bbva-manages-etcd-massive-red-hat-openshift-environments
