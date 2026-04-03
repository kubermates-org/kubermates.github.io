---
title: 'JBoss EAP XP 6.0: Achieving observability with OpenTelemetry'
date: '2026-03-31T00:00:00+00:00'
tags:
- openshift
source: OpenShift Blog
external_url: https://www.redhat.com/en/blog/jboss-eap-xp-60-achieving-observability-opentelemetry
post_kind: link
draft: false
tldr: 'JBoss EAP XP 6.0: Achieving observability with OpenTelemetry OpenTelemetry
  in action Scenario 1: Local environment (Podman + Standalone) Step 1: Infrastructure
  setup (Podman) Step 2: Install and configure JBoss EAP XP 6.0 Step 3: Deploy and
  verify Scenario 2: Setup on Red Hat OpenShift Prerequisites Step 1: Prepare the
  OpenTelemetry collector Step 2: Configure the Helm chart Step 3: Execute deployment
  Step 4: Verify Summary Red Hat OpenShift Container Platform | Product Trial About
  the author Keishi Suzumura More like this [node:rh-smart-meta-title] Streamline
  your work with the new learning drawer in the migration toolkit for virtualization
  Heroes in a Bash Shell | Command Line Heroes The Web Developer And The Presence
  | Compiler: Re:Role Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share The recent article JBoss EAP XP 6 is here announced the release of JBoss EAP
  XP 6.0, which introduced full compliance with MicroProfile 7.0 and a host of new
  features. Among the most significant updates is the enhanced observability provided
  by the support for MicroProfile Telemetry 2.0.'
summary: 'JBoss EAP XP 6.0: Achieving observability with OpenTelemetry OpenTelemetry
  in action Scenario 1: Local environment (Podman + Standalone) Step 1: Infrastructure
  setup (Podman) Step 2: Install and configure JBoss EAP XP 6.0 Step 3: Deploy and
  verify Scenario 2: Setup on Red Hat OpenShift Prerequisites Step 1: Prepare the
  OpenTelemetry collector Step 2: Configure the Helm chart Step 3: Execute deployment
  Step 4: Verify Summary Red Hat OpenShift Container Platform | Product Trial About
  the author Keishi Suzumura More like this [node:rh-smart-meta-title] Streamline
  your work with the new learning drawer in the migration toolkit for virtualization
  Heroes in a Bash Shell | Command Line Heroes The Web Developer And The Presence
  | Compiler: Re:Role Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share The recent article JBoss EAP XP 6 is here announced the release of JBoss EAP
  XP 6.0, which introduced full compliance with MicroProfile 7.0 and a host of new
  features. Among the most significant updates is the enhanced observability provided
  by the support for MicroProfile Telemetry 2.0. In this article, I demonstrate how
  to utilize these observability features to visualize application traces running
  on JBoss EAP XP 6.0, using the official Quickstart application to walk through the
  setup procedures for two scenarios: Local development environment: A setup using
  Podman and the installation manager Production/Cloud environment: Deployment using
  Red Hat OpenShift and Helm charts For this article, I used the opentelemetry-tracing
  application included in the official JBoss EAP Quickstarts. This application is
  configured to automatically collect traces for JAX-RS requests and send them to
  a remote OpenTelemetry collector. opentelemetry-tracing You can clone the code from
  GitHub: $ git clone \ https://github. com/jboss-developer/jboss-eap-quickstarts.
  git $ cd jboss-eap-quickstarts/opentelemetry-tracing $ git clone \ https://github.
  com/jboss-developer/jboss-eap-quickstarts. git $ cd jboss-eap-quickstarts/opentelemetry-tracing
  For the development phase, a robust configuration involves using Podman to run the
  back-end services while running JBoss EAP XP 6.0 on the host machine. First, launch
  Jaeger (the observability back end) and the OpenTelemetry collector so you can create
  a dedicated network to ensure smooth container-to-container communication. Create
  a dedicated network: $ podman network create otel-net $ podman network create otel-net
  Start Jaeger (all-in-one): $ podman run -d --name jaeger \ --network otel-net \
  -e COLLECTOR_OTLP_ENABLED=true \ -p 16686:16686 \ docker. io/jaegertracing/all-in-one:latest
  $ podman run -d --name jaeger \ --network otel-net \ -e COLLECTOR_OTLP_ENABLED=true
  \ -p 16686:16686 \ docker.'
---
Open the original post ↗ https://www.redhat.com/en/blog/jboss-eap-xp-60-achieving-observability-opentelemetry
