---
title: Experimenting with Gateway API using kind
date: '2026-01-28T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/01/28/experimenting-gateway-api-with-kind/
post_kind: link
draft: false
tldr: Experimenting with Gateway API using kind Overview Prerequisites Create a kind
  cluster Install cloud-provider-kind Experimenting with Gateway API Deploy a Gateway
  Deploy a demo application Create an HTTPRoute Test your route Troubleshooting Check
  the Gateway status Check the HTTPRoute status Check controller logs Cleanup Remove
  Kubernetes resources Stop cloud-provider-kind Delete the kind cluster Next steps
  A final word of caution This document will guide you through setting up a local
  experimental environment with Gateway API on kind. This setup is designed for learning
  and testing.
summary: 'Experimenting with Gateway API using kind Overview Prerequisites Create
  a kind cluster Install cloud-provider-kind Experimenting with Gateway API Deploy
  a Gateway Deploy a demo application Create an HTTPRoute Test your route Troubleshooting
  Check the Gateway status Check the HTTPRoute status Check controller logs Cleanup
  Remove Kubernetes resources Stop cloud-provider-kind Delete the kind cluster Next
  steps A final word of caution This document will guide you through setting up a
  local experimental environment with Gateway API on kind. This setup is designed
  for learning and testing. It helps you understand Gateway API concepts without production
  complexity. In this guide, you will: Set up a local Kubernetes cluster using kind
  (Kubernetes in Docker) Deploy cloud-provider-kind , which provides both LoadBalancer
  Services and a Gateway API controller Create a Gateway and HTTPRoute to route traffic
  to a demo application Test your Gateway API configuration locally This setup is
  ideal for learning, development, and experimentation with Gateway API concepts.
  Before you begin, ensure you have the following installed on your local machine:
  Docker - Required to run kind and cloud-provider-kind kubectl - The Kubernetes command-line
  tool kind - Kubernetes in Docker curl - Required to test the routes Create a new
  kind cluster by running: kind create cluster kind create cluster This will create
  a single-node Kubernetes cluster running in a Docker container. Next, you need cloud-provider-kind
  , which provides two key components for this setup: A LoadBalancer controller that
  assigns addresses to LoadBalancer-type Services A Gateway API controller that implements
  the Gateway API specification It also automatically installs the Gateway API Custom
  Resource Definitions (CRDs) in your cluster. Run cloud-provider-kind as a Docker
  container on the same host where you created the kind cluster: VERSION = " $( basename
  $( curl -s -L -o /dev/null -w ''%{url_effective}'' https://github. com/kubernetes-sigs/cloud-provider-kind/releases/latest
  )) " docker run -d --name cloud-provider-kind --rm --network host -v /var/run/docker.
  sock:/var/run/docker. sock registry. k8s. io/cloud-provider-kind/cloud-controller-manager:
  ${ VERSION } VERSION = " $( basename $( curl -s -L -o /dev/null -w ''%{url_effective}''
  https://github.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/01/28/experimenting-gateway-api-with-kind/
