---
title: ingress-nginx to Envoy Gateway migration on CNCF internal services cluster
date: '2026-04-13T14:01:35+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/04/13/ingress-nginx-to-envoy-gateway-migration-on-cncf-internal-services-cluster/
post_kind: link
draft: false
tldr: 'gateway api and ingress-nginx architectures Configuration for the services
  cluster How we migrated What about certificates? Cross-namespace certificate access
  HTTPRoutes Troubleshooting TLS handshake failures Load balancer health check failures
  Certificate not being served Day 2 operation on certificates 1. Make sure that cert-manager
  supports Gateway API: 2.'
summary: 'gateway api and ingress-nginx architectures Configuration for the services
  cluster How we migrated What about certificates? Cross-namespace certificate access
  HTTPRoutes Troubleshooting TLS handshake failures Load balancer health check failures
  Certificate not being served Day 2 operation on certificates 1. Make sure that cert-manager
  supports Gateway API: 2. Update the ClusterIssuer: 3. Annotate the Gateway for cert-manager
  4. Separate the listeners 5. Remove redundant ReferenceGrants Conclusion Posted
  on April 13, 2026 by Koray Oksay, Kubermatic CNCF projects highlighted in this post
  CNCF hosts a Kubernetes cluster to run some services for internal purposes (namely;
  codimd , GUAC , kcp ). The Kubernetes Project announced the ingress-nginx retirement
  (not to be confused with NGINX or NGINX Ingress Controller ), which also affects
  the above mentioned Cluster. So we started looking into alternatives. After some
  discussions, we decided to continue with gateway-api and its implementation as Envoy
  Gateway. Envoy Gateway is an CNCF open source project for managing Envoy Proxy as
  a standalone or Kubernetes-based application gateway. Gateway API resources are
  used to dynamically provision and configure the managed Envoy Proxies. ingress-nginx
  works with one LoadBalancer service; the ingress controller receives all traffic
  and distributes it based on the Ingress object configuration.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/04/13/ingress-nginx-to-envoy-gateway-migration-on-cncf-internal-services-cluster/
